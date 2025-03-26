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
class classTouchBoostModeFiles():

    def __init__(self):
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []
        self.json_data=json_loader_instance.get_data()

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def setBoostModeFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
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
        fileList.append(self.setBoostModeLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setBoostModeHeaderFile(configName, qtouchComponent, targetDevice))

        if(useTrustZone == False):
            del fileList[:]

        return fileList

    def setBoostModeLibraryFile(self,configName, qtouchComponent, targetDevice):
        touchAcq4pLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_4P_LIB", None)
        touchAcq4pLibraryFile.setDestPath("/touch/lib/")
        touchAcq4pLibraryFile.setEnabled(False)
        self.addDepSymbol(touchAcq4pLibraryFile, "libChangeBoostMode", ["ENABLE_BOOST"])

        files_names=self.json_data["acquisition"]["boost_mode"]["library_files"]
        # device_family=json_loader_instance.get_deviceSeries().lower()
        for i,value in enumerate(files_names):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/"+value)
            touchAcq4pLibraryFile.setOutputName(value)
        return touchAcq4pLibraryFile

    def setBoostModeHeaderFile(self,configName, qtouchComponent, targetDevice):
        touchAcq4pHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_4P_HEADER", None)
        touchAcq4pHeaderFile.setDestPath("/touch/")
        touchAcq4pHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchAcq4pHeaderFile.setType("HEADER")
        touchAcq4pHeaderFile.setMarkup(False)
        touchAcq4pHeaderFile.setEnabled(False)
        self.addDepSymbol(touchAcq4pHeaderFile, "libChangeBoostMode", ["ENABLE_BOOST"])
        files_names=self.json_data["acquisition"]["boost_mode"]["header_files"]
        for i,value in enumerate(files_names):
            touchAcq4pHeaderFile.setSourcePath("/src/"+value)
            touchAcq4pHeaderFile.setOutputName(value)
        return touchAcq4pHeaderFile


