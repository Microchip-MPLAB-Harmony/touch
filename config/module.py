"""
Copyright (C) [2023], Microchip Technology Inc., and its subsidiaries. All rights reserved.

The software and documentation is provided by microchip and its contributors
"as is" and any express, implied or statutory warranties, including, but not
limited to, the implied warranties of merchantability, fitness for a particular
purpose and non-infringement of third party intellectual property rights are
disclaimed to the fullest extent permitted by law. In no event shall microchip
or its contributors be liable for any direct, indirect, incidental, special,
exemplary, or consequential damages (including, but not limited to, procurement
of substitute goods or services; loss of use, data, or profits; or business
interruption) however caused and on any theory of liability, whether in contract,
strict liability, or tort (including negligence or otherwise) arising in any way
out of the use of the software and documentation, even if advised of the
possibility of such damage.

Except as expressly permitted hereunder and subject to the applicable license terms
for any third-party software incorporated in the software and any applicable open
source software license terms, no license or other rights, whether express or
implied, are granted under any patent or other intellectual property rights of
Microchip or any third party.
"""
"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

import os
import re
import sys
import json
import inspect

def list_files_in_directory(directory_path):
    try:
        # List all files and directories in the specified directory
        files_and_directories = os.listdir(directory_path)

        # Filter out directories and non-json files, only keep .json files
        json_files = [f for f in files_and_directories if os.path.isfile(os.path.join(directory_path, f)) and f.lower().endswith('.json')]

        return json_files
    except FileNotFoundError:
        return []
    except PermissionError:
        return []

def match_data(data, array):
    pattern = re.compile(data)
    return any(pattern.search(item) for item in array)

def loadModule():
    #mod will have value if PTC peripheral is present in a device variant
    mod = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]")
    deviceNode = ATDF.getNode("/avr-tools-device-file/devices")
    mod_adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]")

    deviceVariant = ATDF.getNode("/avr-tools-device-file/variants").getChildren()

    parent_dir=os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))
    json_folder=os.path.join(parent_dir,"json")
    files = list_files_in_directory(json_folder)
    
    deviceChild = deviceNode.getChildren()
    deviceName = deviceChild[0].getAttribute("name")
    deviceVariant=deviceVariant[0].getAttribute("pinout")
    deviceSeries=str(deviceChild[0].getAttribute("series"))
    if deviceSeries == "PIC32MZ":
        deviceSeries = deviceChild[0].getAttribute("family")
    architecture=str(deviceChild[0].getAttribute("architecture"))

    if mod_adc:
        mod_id=mod_adc.getAttribute("id")
        mod_version=mod_adc.getAttribute("version")
        print("ADC-Mod",mod_adc.getAttribute("id"))
    if mod:
        mod_id=mod.getAttribute("id")
        mod_version=mod.getAttribute("version")
        print("PTC-Mod",mod.getAttribute("id"))
    is_supported_device=match_data(deviceSeries,files)
    
    if(is_supported_device==True):
        # json_loader_path="C:/Users/i78387/.mcc/HarmonyContent/touch/config"
        sys.path.append(parent_dir)
        from json_loader import json_loader_instance
        data_from_json = json_loader_instance.load_json(json_folder,deviceSeries,deviceVariant,deviceName,mod_id,mod_version,architecture)
    
        #common
        if data_from_json != None:
            core=data_from_json["features"]["core"]
            qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
        else:
            print("Version not found for this module_id")

        qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
        qtouchComponent.setDependencyEnabled("Touch_timer", True)
        qtouchComponent.addDependency("SW_Timer", "SYS_TIME", None, True, True)
        qtouchComponent.setDependencyEnabled("SW_Timer", False)
        qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
        qtouchComponent.setDependencyEnabled("Touch_sercom", False)
        qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
        qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)

        if core=="PTC" and mod:
            qtouchComponentAcquistion = Module.CreateComponent("ptc","PTC","/Touch/","config/ptc_based_acq_engine.py")
            qtouchComponentAcquistion.addCapability("ptc_Acq_Engine", "Acq_Engine")
            qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
            qtouchComponent.setDependencyEnabled("PTC",True)
            qtouchComponent.addDependency("lib_acquire","Acq_Engine",None,False,True)
            qtouchComponent.setDependencyEnabled("lib_acquire", True)
            qtouchComponent.addCapability("lib_qtouch", "TouchData")
        elif core=="ADC":
            qtouchComponentAcquistion = Module.CreateComponent("ptc","PTC","/Touch/","config/ptc_based_acq_engine.py")
            qtouchComponentAcquistion.addCapability("ptc_Acq_Engine", "Acq_Engine")
            qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
            qtouchComponent.addCapability("lib_qtouch", "TouchData")
            qtouchComponent.addDependency("lib_acquire","Acq_Engine",None,False,True)
            qtouchComponent.setDependencyEnabled("lib_acquire", True)
            qtouchComponentAcquistion.addDependency("lib_acquire","ADC",None,False,True)
            qtouchComponentAcquistion.setDependencyEnabled("lib_acquire", True)
        elif core=="CVD":
            qtouchComponent.setDisplayType("HCVD")
            qtouchComponent.addDependency("Acq_Engine", "ADC", None, False, True)
            qtouchComponent.setDependencyEnabled("Acq_Engine", True)
    else:
        print(deviceSeries+" - Device is not supported")

    