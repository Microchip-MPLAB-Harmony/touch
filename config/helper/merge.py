import json
import sys
import os
import inspect

def merge_json_files(file1,core,mod_id,mod_version):
    try:
        with open("../json"+'/'+file1, 'r') as f1, open("../json"+'/'+"versions.json", 'r') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)[core][mod_id][mod_version]

        # Merge the two dictionaries
        merged_data = data1
        merged_data["version_data"] = data2

        with open("output.json", 'w') as f_out:
            json.dump(merged_data, f_out, indent=4)

        print(f"Successfully merged {file1} and 'version.json' into output.json ")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python merge_json.py <file1.json> <core> <module_id> <module_version> ")
    else:
        file1 = sys.argv[1]
        core=sys.argv[2]
        mod_id=sys.argv[3]
        mod_version=sys.argv[4]
        merge_json_files(file1,core,mod_id,mod_version)
