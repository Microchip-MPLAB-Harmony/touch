import json
import os
import copy


class classJsonLoader:
    def __init__(self):
        self._series_loaded_data = None
        self._version_loaded_data=None
        self._device_series=None
        self._device_variant=None
        self._device_name=None
        self._architecture=None
        self._architectureDict={
            "CORTEX-M0PLUS":"cm0p",
            "CORTEX-M23":"cm23",
            "CORTEX-M33":"cm33",
            "CORTEX-M4":"cm4",
            "CORTEX-M7":"pic32cz",
            "MIPS":"pic32mz"
        }

    def merge_dicts(self,dict1, dict2):
        """Recursively merge two dictionaries."""
        result = copy.deepcopy(dict1)  # Create a deep copy of dict1
        for key in dict2:
            if key in result:
                if isinstance(result[key], dict) and isinstance(dict2[key], dict):
                    result[key] = self.merge_dicts(result[key], dict2[key])
                else:
                    result[key] = dict2[key]
            else:
                result[key] = dict2[key]
        return result

    def load_json(self,json_dir,deviceSeries,deviceVariant,deviceName,mod_id,mod_version,architecture):

        PIC32CMJH00_V1=[
            "PIC32CM2532JH00032",
            "PIC32CM2532JH00048",
            "PIC32CM2532JH00064",
            "PIC32CM2532JH00100",
            "PIC32CM5164JH00032",
            "PIC32CM5164JH00048",
            "PIC32CM5164JH00064",
            "PIC32CM5164JH00100",
        ]

        PIC32CMJH00_V2=["PIC32CM3204JH00032",
            "PIC32CM3204JH00048",
            "PIC32CM3204JH00064",
            "PIC32CM6408JH00032",
            "PIC32CM6408JH00048",
            "PIC32CM6408JH00064"]

        if deviceName in PIC32CMJH00_V1:
            deviceSeries="PIC32CMJH00_V1"
        elif deviceName in PIC32CMJH00_V2:
            deviceSeries="PIC32CMJH00_V2"

        print("Loading JSON for:", deviceSeries)
        file_path = os.path.join(json_dir, deviceSeries + ".json")
        version_path = os.path.join(json_dir,"versions.json")

        # Read the JSON file
        with open(file_path, "r") as file:
            self._series_loaded_data = json.load(file)

        # if self._series_loaded_data["features"]["core"]=="ADC":
        #     mod_id=mod_adc_id
        #     mod_version=mod_adc_version

        # with open(version_path, "r") as file:
        #     version_data=json.load(file)
        #     if mod_version in version_data[self._series_loaded_data["features"]["core"]][mod_id]:
        #         self._version_loaded_data = version_data[self._series_loaded_data["features"]["core"]][mod_id][mod_version]
        #     else:
        #         self._version_loaded_data=None

        #check
        core=self._series_loaded_data["features"]["core"]
        if core!="CVD":
            with open(version_path, "r") as file:
                version_data=json.load(file)
                if mod_version in version_data[core][mod_id]:
                    self._version_loaded_data = version_data[core][mod_id][mod_version]
                    self._series_loaded_data = self.merge_dicts(self._series_loaded_data, self._version_loaded_data)
                else:
                    self._version_loaded_data=None

        if self._version_loaded_data==None and core!="CVD":
            return None

        self._architecture=self._architectureDict[architecture]

        self._device_series=deviceSeries

        self._device_name=deviceName

        self._device_variant=deviceVariant

        return self._series_loaded_data

    def get_data(self):
        return self._series_loaded_data

    def get_deviceSeries(self):
        return self._device_series

    def get_deviceName(self):
        return self._device_name

    def get_deviceVariant(self):
        return self._device_variant

    # def get_version_data(self):
    #     return self._version_loaded_data

    def get_architecture(self):
        return self._architecture

json_loader_instance = classJsonLoader()
