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

def check_conditional(data, condition_key, condition_value, required_key, required_subkeys, errors):
    # Extract the condition value
    condition_value_actual = data.get(condition_key[0], {}).get(condition_key[1])

    # Check if the condition is met
    if condition_value_actual == condition_value:
        # Split the required key to handle nested properties
        required_key_parts = required_key.split('.')
        required_data = data
        for part in required_key_parts:
            if part in required_data:
                required_data = required_data[part]
            else:
                required_data = None
                break

        # Check if the required key is present
        if required_data is None:
            errors.append(f"Error: '{required_key}' property must be provided when '{condition_key[1]}' is '{condition_value}'.")
        else:
            # Check if the required subkeys are present
            for subkey in required_subkeys:
                if subkey not in required_data:
                    errors.append(f"Error: '{required_key}' property must include '{subkey}' value.")
    else:
        # Check if the required key should not be present
        required_key_parts = required_key.split('.')
        required_data = data
        for part in required_key_parts:
            if part in required_data:
                required_data = required_data[part]
            else:
                required_data = None
                break

        if required_data is not None:
            errors.append(f"Error: '{required_key}' property should not be provided when '{condition_key[1]}' is not '{condition_value}'.")


#function for autotune_list
def check_auto_tune(tune_array,errors):
    allowed_values={"CAL_AUTO_TUNE_NONE","CAL_AUTO_TUNE_PRSC","CAL_AUTO_TUNE_CSD"}

    if not all(value in allowed_values for value in tune_array):
        errors.append(f"Error: Please check auto tune list values. Allowed values 'CAL_AUTO_TUNE_NONE,CAL_AUTO_TUNE_PRSC,CAL_AUTO_TUNE_CSD' ")

def validate_json(data):
    errors = []

    mandatory_properties = [
        {"features":["core","module_id","self","mutual","scroller","surface","gesture","frequency_hop","frequency_hop_auto","low_power_software","low_power_event","lump_mode","boost_mode"]},

        {"acquisition":[{"tune_mode":["component_values","default_index"]},{"measurement_period":["min","max","default"]},{"interrupt_priority":["min","max","default"]}]},
        
        {"node":[{"series_resistor":["component_values","default_index"]},
        {"analog_gain":["component_values","default_index"]},
        {"digital_gain":["component_values","default_index"]},
        {"filter_level":["component_values","default_index"]},
        {"ptc_clock_range":["min","max"]},{"versions":["manual","auto"]}]},

        {"clock_config":["settings","descriptions"]},

        {"version_data":["hardware_shield","timer_shield","csd","ptc_clock_range","series_resistor"]}
    ]

    # Validate JSON
    check_mandatory(data, mandatory_properties,errors)

    # List of conditions and required properties
    conditions = [
        (('features', 'ptc_precaler'), True, 'node.ptc_prescaler', ["component_values","default_index"]),
        (('version_data','csd'),True,'node.csd',['min','max','default']),
        (('features','low_power_event'),True,'acquisition.event_system_low_power',["component_values","default_index"]),
        (('features','wake_up'),True,'acquisition.wake_up',['min','max','default']),
        (('version_data','timer_shield'),True,"driven_shield",[]),
        (('features','trust_zone'),True,"acquisition.trust_zone.nvicid",[]),
        (('features','boost_mode'),True,"acquisition.boost_mode.module_id",[])
    ]

    #validate nested properties of driven_shield only required
    if "driven_shield" in data and data["version_data"]["timer_shield"]==True:
        check_mandatory(data, [{"driven_shield":[{"core":[{"clock":["tc","tcc"]},"dma"]},
        {"timer":["tc","tcc"]},{"evsys":["module","user","timer"]}]}],errors)

    # Iterate over the conditions and call the check_property function
    for condition in conditions:
        check_conditional(data, *condition, errors)

    # Check 'list_values'
    # auto_tune
    if "acquisition" in data and "tune_mode" in data["acquisition"]:
        check_auto_tune(data["acquisition"]["tune_mode"]["component_values"],errors)

    return errors

def main():
    # Load the JSON file
    # parent_dir=os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))
    # json_folder=os.path.join(parent_dir,"json")

    try:
        # Validate the JSON data
        with open('output.json', 'r') as file:
            data = json.load(file)
            errors = validate_json(data)

        # Print the validation results
        if errors:
            print("Output.json - JSON file format is invalid. Please fix all below error.")
            for error in errors:
                print(error)
        else:
            print("Output.json - JSON file is valid.")
    
    except FileNotFoundError:
        print(" file was not found.")

    # except Exception as e:
    #     print(sys.argv[1]+" has some errors in file. Please fix the below errors")
    #     print(e)

if __name__ == "__main__":
    main()
