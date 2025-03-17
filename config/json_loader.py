import json
import os
import copy


class classJsonLoader:
    def __init__(self):
        self._series_loaded_data = None
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

    def load_json(self,json_dir,deviceSeries,deviceVariant,deviceName,mod_id,mod_version,architecture):

        print("Loading JSON for:", deviceSeries)
        file_path = os.path.join(json_dir, deviceSeries + ".json")

        # Read the JSON file
        with open(file_path, "r") as file:
            json_all_data = json.load(file)

        mod_id_version=str(mod_id)+"_"+str(mod_version)
        if mod_id==None and mod_version==None: #CVD
            self._series_loaded_data=json_all_data
        elif mod_id_version in json_all_data: #PTC , ADC
            print("mod",mod_id_version)
            self._series_loaded_data=json_all_data[mod_id_version]
        else:
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

    def get_architecture(self):
        return self._architecture

json_loader_instance = classJsonLoader()
