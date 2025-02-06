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
class classTouchKeySourceFiles():
    def __init__(self):
        self.json_data=json_loader_instance.get_data()

    def setKeysFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
        """
        Generates as List of source files required for Keys support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        fileList.append(self.setTouchLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setTouchHeaderFile(configName, qtouchComponent))
        if(useTrustZone == False):
            del fileList[:]
        return fileList

    def setTouchLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates Keys library file (device dependent)
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
        touchLibraryFile.setDestPath("/touch/lib/")
        touchLibraryFile.setEnabled(True)

        architechture=json_loader_instance.get_architecture()
        touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_"+architechture+"_0x0002.X.a")
        touchLibraryFile.setOutputName("qtm_touch_key_"+architechture+"_0x0002.X.a")

        # if (targetDevice in set(["SAME51","SAME53","SAME54","SAMD51","PIC32CXBZ31","WBZ35"])):
        #     touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm4_0x0002.X.a")
        #     touchLibraryFile.setOutputName("qtm_touch_key_cm4_0x0002.X.a")
        # elif (targetDevice in set(["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00"])):
        #     touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm23_0x0002.X.a")
        #     touchLibraryFile.setOutputName("qtm_touch_key_cm23_0x0002.X.a")
        # elif (targetDevice in ["PIC32MZW", "PIC32MZDA"]):
        #     touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_pic32mz_0x0002.X.a")
        #     touchLibraryFile.setOutputName("qtm_touch_key_pic32mz_0x0002.X.a")
        # elif (targetDevice in ["PIC32CZCA80", "PIC32CZCA90"]):
        #     touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_pic32cz_0x0002.X.a")
        #     touchLibraryFile.setOutputName("qtm_touch_key_pic32cz_0x0002.X.a")
        # elif (targetDevice in ["PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01"]):
        #     touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm33_0x0002.X.a")
        #     touchLibraryFile.setOutputName("qtm_touch_key_cm33_0x0002.X.a")
        # else:
        #     touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm0p_0x0002.X.a")
        #     touchLibraryFile.setOutputName("qtm_touch_key_cm0p_0x0002.X.a")
        return touchLibraryFile

    def setTouchHeaderFile(self,configName, qtouchComponent):
        """
        Generates keys api header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KEY_HEADER", None)
        touchHeaderFile.setSourcePath("/src/qtm_touch_key_0x0002_api.h")
        touchHeaderFile.setOutputName("qtm_touch_key_0x0002_api.h")
        touchHeaderFile.setDestPath("/touch/")
        touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchHeaderFile.setType("HEADER")
        touchHeaderFile.setMarkup(False)
        return touchHeaderFile