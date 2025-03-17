import json
import os
import inspect
import sys

def check_mandatory(json_data, mandatory_properties, errors):
    def check_properties(data, properties, path, errors):
        for prop in properties:
            if isinstance(prop, dict):
                for key, sub_props in prop.items():
                    if key not in data:
                        errors.append(f"Error: '{path + key}' property must be provided.")
                    else:
                        check_properties(data[key], sub_props, path + key + ".", errors)
            else:
                if prop not in data:
                    errors.append(f"Error: '{path + prop}' property must be provided.")
                elif path + prop == "clock_config.settings":
                    if not isinstance(data[prop], list):
                        errors.append(f"Error: '{path + prop}' should be an array.")
                    else:
                        for i, item in enumerate(data[prop]):
                            if not isinstance(item, dict):
                                errors.append(f"Error: '{path + prop}[{i}]' should be an object.")
                            else:
                                required_keys = {"symbol", "value", "componentId", "name"}
                                item_keys = set(item.keys())
                                missing_keys = required_keys - item_keys
                                extra_keys = item_keys - required_keys
                                if missing_keys:
                                    errors.append(f"Error: '{path + prop}[{i}]' is missing properties: {', '.join(missing_keys)}.")
                                if extra_keys:
                                    errors.append(f"Error: '{path + prop}[{i}]' has extra properties: {', '.join(extra_keys)}.")

    check_properties(json_data, mandatory_properties, "", errors)

def check_conditional(data, condition_key, condition_values, required_key, required_subkeys, errors):
    # Helper function to get nested value
    def get_nested_value(d, keys):
        for key in keys:
            if isinstance(d, dict) and key in d:
                d = d[key]
            else:
                return None
        return d

    # Extract the condition value
    condition_value_actual = get_nested_value(data, condition_key)

    # Check if the condition is met
    if condition_value_actual in condition_values:
        # Split the required key to handle nested properties
        required_data = get_nested_value(data, required_key.split('.'))

        # Check if the required key is present
        if required_data is None:
            errors.append(f"Error: '{required_key}' property must be provided when '{'.'.join(condition_key)}' is in '{condition_values}'.")
        else:
            # Check if the required subkeys are present
            for subkey in required_subkeys:
                if subkey not in required_data:
                    errors.append(f"Error: '{required_key}' property must include '{subkey}' value.")
    else:
        # Check if the required key should not be present
        required_data = get_nested_value(data, required_key.split('.'))

        if required_data is not None:
            errors.append(f"Error: '{required_key}' property should not be provided when '{'.'.join(condition_key)}' is not in '{condition_values}'.")

def check_auto_tune(tune_array, errors):
    allowed_values = {"CAL_AUTO_TUNE_NONE", "CAL_AUTO_TUNE_PRSC", "CAL_AUTO_TUNE_CSD"}

    if not all(value in allowed_values for value in tune_array):
        errors.append(f"Error: Please check auto tune list values. Allowed values 'CAL_AUTO_TUNE_NONE, CAL_AUTO_TUNE_PRSC, CAL_AUTO_TUNE_CSD' ")

def validate_json(data):
    errors = []

    mandatory_properties = [
        {"features": ["core", "module_id", "self", "mutual", "hardware_shield", "timer_shield", "csd", "scroller", "surface", "gesture", "frequency_hop", "frequency_hop_auto", "low_power_software", "low_power_event", "lump_mode", "boost_mode", "wake_up", "ptc_prescaler", "trust_zone"]},
        {"acquisition": [{"tune_mode": ["component_values", "default_index"]}, {"measurement_period": ["min", "max", "default"]}]},
        {"node": [
            {"analog_gain": ["component_values", "default_index"]},
            {"digital_gain": ["component_values", "default_index"]},
            {"filter_level": ["component_values", "default_index"]},
            {"versions": ["manual", "auto"]}
        ]},
        {"clock_config": ["settings", "descriptions"]},
    ]

    # Check if the data contains top-level keys that need to be iterated
    if "features" not in data:
        # Iterate over the top-level keys in the JSON data
        for key, nested_data in data.items():
            # Validate JSON
            check_mandatory(nested_data, mandatory_properties, errors)

            # List of conditions and required properties
            conditions = [
                (('features', 'ptc_prescaler'), [True], 'node.ptc_prescaler', ["component_values", "default_index"]),
                (('features', 'csd'), [True], 'node.csd', ['min', 'max', 'default']),
                (('features', 'core'), ["PTC", "ADC"], 'acquisition.interrupt_priority', ['min', 'max', 'default']),
                (('features', 'low_power_event'), [True], 'acquisition.event_system_low_power', ["component_values", "default_index"]),
                (('features', 'wake_up'), [True], 'acquisition.wake_up', ['min', 'max', 'default']),
                (('features', 'trust_zone'), [True], "acquisition.trust_zone.nvicid", []),
                (('features', 'boost_mode'), [True], "acquisition.boost_mode.module_id", [])
            ]

            # Iterate over the conditions and call the check_property function
            for condition in conditions:
                check_conditional(nested_data, *condition, errors)

            # Check 'list_values'
            # auto_tune
            if "acquisition" in nested_data and "tune_mode" in nested_data["acquisition"]:
                check_auto_tune(nested_data["acquisition"]["tune_mode"]["component_values"], errors)
    else:
        # Direct validation
        check_mandatory(data, mandatory_properties, errors)

        # List of conditions and required properties
        conditions = [
            (('features', 'ptc_prescaler'), [True], 'node.ptc_prescaler', ["component_values", "default_index"]),
            (('features', 'csd'), [True], 'node.csd', ['min', 'max', 'default']),
            (('features', 'core'), ["PTC", "ADC"], 'acquisition.interrupt_priority', ['min', 'max', 'default']),
            (('features', 'low_power_event'), [True], 'acquisition.event_system_low_power', ["component_values", "default_index"]),
            (('features', 'wake_up'), [True], 'acquisition.wake_up', ['min', 'max', 'default']),
            (('features', 'trust_zone'), [True], "acquisition.trust_zone.nvicid", []),
            (('features', 'boost_mode'), [True], "acquisition.boost_mode.module_id", [])
        ]

        # Iterate over the conditions and call the check_property function
        for condition in conditions:
            check_conditional(data, *condition, errors)

        # Check 'list_values'
        # auto_tune
        if "acquisition" in data and "tune_mode" in data["acquisition"]:
            check_auto_tune(data["acquisition"]["tune_mode"]["component_values"], errors)

    return errors

def main():
    # Get the parent directory of the current script (helper folder)
    parent_dir = os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))

    # Get the config directory
    config_dir = os.path.dirname(parent_dir)

    # Get the json folder inside the config directory
    json_folder = os.path.join(config_dir, "json")

    # Iterate over all JSON files in the folder
    for file_name in os.listdir(json_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(json_folder, file_name)
            try:
                # Validate the JSON data
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    errors = validate_json(data)

                # Print the validation results
                if errors:
                    print(file_name + " - JSON file format is invalid. Please fix all below error.")
                    for error in errors:
                        print(error)
                else:
                    print(file_name + " - JSON file is valid.")

            except FileNotFoundError:
                print(file_name + "json file was not found.")

            except Exception as e:
                print(file_name + " has some errors in file. Please fix the below errors")
                print(e)

if __name__ == "__main__":
    main()
