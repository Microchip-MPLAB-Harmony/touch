import json
import os


class classJsonLoader:
    def __init__(self):
        self._last_loaded_data = None
        self._version_loaded_data=None
        self._device_name=None
        self._architecture=None
        self._architectureDict={
            "CORTEX-M0PLUS":"cm0p",
            "CORTEX-M23":"cm23",
            "CORTEX-M4":"cm4",
            "MIPS":"pic32mz"
        }

    def load_json(self,json_dir,file_name,mod_id,mod_version,architecture):

        print("Loading JSON for:", file_name)
        file_path = os.path.join(json_dir, file_name + ".json")
        version_path = os.path.join(json_dir,"versions.json")

        # Read the JSON file
        with open(file_path, "r") as file:
            self._last_loaded_data = json.load(file)

        with open(version_path, "r") as file:
            version_data=json.load(file)
            self._version_loaded_data = version_data[self._last_loaded_data["features"]["core"]][mod_id]["3.2.0"]

        self._architecture=self._architectureDict[architecture]

        self._device_name=file_name

        return self._last_loaded_data

    def get_data(self):
        return self._last_loaded_data

    def get_deviceName(self):
        return self._device_name

    def get_version_data(self):
        return self._version_loaded_data

    def get_architecture(self):
        return self._architecture

json_loader_instance = classJsonLoader()
