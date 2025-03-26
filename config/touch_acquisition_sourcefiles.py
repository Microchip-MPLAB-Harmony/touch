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
from json_loader import json_loader_instance
class classTouchAcquisitionSourceFiles():
    def __init__(self):
        self.json_data=json_loader_instance.get_data()

    def setAcquisitionFiles(self,configName, qtouchComponent, targetDevice, useTrustZone):
        """
        Generates as List of source files required for Acquisition
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        # touchAcqLibraryFile
        fileList.append(self.setAcquisitionLibraryFileN(configName, qtouchComponent, targetDevice))
        # touchAcqAutoLibraryFile
        fileList.append(self.setAutoAcquisitionLibraryFileN(configName, qtouchComponent, targetDevice))
        # touchBindLibraryFile
        fileList.append(self.setBindLibraryFile(configName, qtouchComponent, targetDevice))
        # touchAcqHeaderFile
        fileList.append(self.setAcqHeaderFileN(configName, qtouchComponent, targetDevice))
        # touchBindHeaderFile
        fileList.append(self.setBindHeaderFile(configName, qtouchComponent, targetDevice))
        # touchCommonHeaderFile
        fileList.append(self.setCommonHeaderFile(configName, qtouchComponent, targetDevice))

        if(useTrustZone == False):
            del fileList[:]

        return fileList


    def setBindHeaderFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates binding layer header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        touchBindHeaderFile = qtouchComponent.createFileSymbol("TOUCH_BIND_HEADER", None)
        touchBindHeaderFile.setDestPath("/touch/")
        touchBindHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchBindHeaderFile.setType("HEADER")
        touchBindHeaderFile.setMarkup(False)
        touchBindHeaderFile.setEnabled(False)
        touchBindHeaderFile.setSourcePath("/src/qtm_binding_layer_0x0005_api.h")
        touchBindHeaderFile.setOutputName("qtm_binding_layer_0x0005_api.h")
        return touchBindHeaderFile

    def setCommonHeaderFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates common components api header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        touchCommonHeaderFile = qtouchComponent.createFileSymbol("TOUCH_COMMON_HEADER", None)
        touchCommonHeaderFile.setSourcePath("/src/qtm_common_components_api.h")
        touchCommonHeaderFile.setOutputName("qtm_common_components_api.h")
        touchCommonHeaderFile.setDestPath("/touch/")
        touchCommonHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchCommonHeaderFile.setType("HEADER")
        touchCommonHeaderFile.setMarkup(False)
        return touchCommonHeaderFile

    def setAcquisitionLibraryFileN(self,configName, qtouchComponent, targetDevice):
        """
        Generates acquisition library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        file_names=self.json_data["acquisition"]["file_names"]["library_files"]

        if (self.json_data["features"]["core"]=="CVD"):
            for i, value in enumerate(file_names):
            # Create a new file symbol for each file name
                touchAcqLibraryFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_LIB"+str(i+1), None)   
                touchAcqLibraryFile.setDestPath("/touch/")
                touchAcqLibraryFile.setProjectPath("config/" + configName + "/touch/")
                touchAcqLibraryFile.setSourcePath("/src/libraries/"+value)
                touchAcqLibraryFile.setOutputName(value)
                touchAcqLibraryFile.setEnabled(True)
                touchAcqLibraryFile.setDependencies(self.enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])
        else:
            for i, value in enumerate(file_names):
            # Create a new file symbol for each file name
                touchAcqLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_LIB"+str(i+1), None)   
                touchAcqLibraryFile.setDestPath("/touch/lib/")
                touchAcqLibraryFile.setSourcePath("/src/libraries/"+value)
                touchAcqLibraryFile.setOutputName(value)
                touchAcqLibraryFile.setEnabled(True)
                touchAcqLibraryFile.setDependencies(self.enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])
        return touchAcqLibraryFile

    def setAutoAcquisitionLibraryFileN(self,configName, qtouchComponent, targetDevice):
        """
        Generates auto acquisition library file per device
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symboltempvar
        """
        file_names=self.json_data["acquisition"]["file_names"]["library_files"]

        if (self.json_data["features"]["core"]=="CVD"):
            for i, value in enumerate(file_names):
                touchAcqAutoLibraryFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_AUTO_LIB"+str(i+1), None)
                touchAcqAutoLibraryFile.setDestPath("/touch/")
                touchAcqAutoLibraryFile.setProjectPath("config/" + configName + "/touch/")
                touchAcqAutoLibraryFile.setSourcePath("/src/libraries/"+value)
                touchAcqAutoLibraryFile.setOutputName(value)
        else:
            for i, value in enumerate(file_names):
                touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB"+str(i+1), None)
                touchAcqAutoLibraryFile.setDestPath("/touch/lib/")
                touchAcqAutoLibraryFile.setSourcePath("/src/libraries/"+value)
                touchAcqAutoLibraryFile.setOutputName(value)
        touchAcqAutoLibraryFile.setEnabled(False)
        touchAcqAutoLibraryFile.setDependencies(self.enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])
        return touchAcqAutoLibraryFile

    def setBindLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates binding layer library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
        touchBindLibraryFile.setDestPath("/touch/lib/")
        touchBindLibraryFile.setEnabled(False)

        architechture=json_loader_instance.get_architecture()
        touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_"+architechture+"_0x0005.X.a")
        print("bind","qtm_binding_layer_"+architechture+"_0x0005.X.a")
        touchBindLibraryFile.setOutputName("qtm_binding_layer_"+architechture+"_0x0005.X.a")

        return touchBindLibraryFile

    def setAcqHeaderFileN(self,configName, qtouchComponent, targetDevice):
        """
        Generates acquisition api header file per device
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """

        file_names=self.json_data["acquisition"]["file_names"]["header_files"]

        for i, value in enumerate(file_names):
            # Create a new file symbol for each file name
            acqHeaderFileN = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER" + str(i+1), None)
            acqHeaderFileN.setDestPath("/touch/")
            acqHeaderFileN.setProjectPath("config/" + configName + "/touch/")
            acqHeaderFileN.setType("HEADER")
            acqHeaderFileN.setMarkup(True)
            acqHeaderFileN.setSourcePath("/src/"+value)  
            if ".ftl" in value:
                value=value.replace(".ftl","")
            acqHeaderFileN.setOutputName(value)
            
        return acqHeaderFileN

    def enableAutoTuneFunctionality(self,symbol,event):
        """Handler for auto tune library selection.
        Arguments:
            :symbol : the symbol that triggered the event
            :event : new value of the symbol 
        Returns:
            :none
        """
        library_list=self.json_data["acquisition"]["file_names"]["library_files"]
        localcomponent = symbol.getComponent()
        for i in range(len(library_list)):
            touchAcqLibraryFile = localcomponent.getSymbolByID("TOUCH_ACQ_LIB"+str(i+1))
            touchAcqAutoLibraryFile = localcomponent.getSymbolByID("TOUCH_ACQ_AUTO_LIB"+str(i+1))

            if(event["value"] == 0):
                touchAcqAutoLibraryFile.setEnabled(False)
                touchAcqLibraryFile.setEnabled(True)
            else:
                touchAcqAutoLibraryFile.setEnabled(True)
                touchAcqLibraryFile.setEnabled(False)