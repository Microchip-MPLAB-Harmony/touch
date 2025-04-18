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
class classTouchGestureSourceFiles():
    def __init__(self):
        self.json_data=json_loader_instance.get_data()

    def setGestureFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
        """
        Generates as List of source files required for gesture support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        fileList.append(self.setGestureLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setGestureHeaderFile(configName, qtouchComponent))
        if(useTrustZone == False):
            del fileList[:]
        return fileList

    def setGestureLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates gesture library file per device
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """

        gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
        gestureLibraryFile.setDestPath("/touch/lib/")
        gestureLibraryFile.setEnabled(False)

        architechture=json_loader_instance.get_architecture()
        gestureLibraryFile.setSourcePath("/src/libraries/qtm_surface_gestures_"+architechture+"_0x0023.X.a")
        gestureLibraryFile.setOutputName("qtm_surface_gestures_"+architechture+"_0x0023.X.a")
        return gestureLibraryFile

    def setGestureHeaderFile(self,configName, qtouchComponent):
        """
        Generates gesture header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        gestureHeaderFile = qtouchComponent.createFileSymbol("TOUCH_GESTURE_HEADER", None)
        gestureHeaderFile.setSourcePath("/src/qtm_gestures_2d_0x0023_api.h")
        gestureHeaderFile.setOutputName("qtm_gestures_2d_0x0023_api.h")
        gestureHeaderFile.setDestPath("/touch/")
        gestureHeaderFile.setProjectPath("config/" + configName + "/touch/")
        gestureHeaderFile.setType("HEADER")
        gestureHeaderFile.setMarkup(False)
        gestureHeaderFile.setEnabled(False)
        return gestureHeaderFile
