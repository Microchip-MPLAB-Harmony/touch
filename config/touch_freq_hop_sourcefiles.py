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
class classTouchFreqSourceFiles():
    def __init__(self):
        self.json_data=json_loader_instance.get_data()

    def setFreqHopFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
        """
        Generates as List of source files required for frequency hop support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        # freqHopLibraryFile
        fileList.append(self.setfreqHopLibraryFile(configName, qtouchComponent, targetDevice))
        # freqHopAutoLibraryFile
        fileList.append(self.setfreqHopAutoLibraryFile(configName, qtouchComponent, targetDevice))
        # freqHopHeaderFile
        fileList.append(self.setfreqHopHeaderFile(configName, qtouchComponent))
        # freqHopAutoHeaderFile
        fileList.append(self.setfreqHopAutoHeaderFile(configName, qtouchComponent))

        if(useTrustZone == False):
            del fileList[:]

        return fileList

    # freqHopLibraryFile
    def setfreqHopLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates frequency hop library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        freqHopLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_LIB", None)
        freqHopLibraryFile.setDestPath("/touch/lib/")
        freqHopLibraryFile.setEnabled(True)

        architechture=json_loader_instance.get_architecture()
        freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_"+architechture+"_0x0006.X.a")
        freqHopLibraryFile.setOutputName("qtm_freq_hop_"+architechture+"_0x0006.X.a")
        
        return freqHopLibraryFile

    # freqHopAutoLibraryFile
    def setfreqHopAutoLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates frequency hop auto library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        freqHopAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_AUTO_LIB", None)
        freqHopAutoLibraryFile.setDestPath("/touch/lib/")
        freqHopAutoLibraryFile.setEnabled(True)     

        architechture=json_loader_instance.get_architecture()
        freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_auto_"+architechture+"_0x0004.X.a")
        freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_auto_"+architechture+"_0x0004.X.a")

        return freqHopAutoLibraryFile

    # freqHopHeaderFile
    def setfreqHopHeaderFile(self,configName, qtouchComponent):
        """
        Generates frequency hop header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        freqHopHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HOP_HEADER", None)
        freqHopHeaderFile.setSourcePath("/src/qtm_freq_hop_0x0006_api.h")
        freqHopHeaderFile.setOutputName("qtm_freq_hop_0x0006_api.h")
        freqHopHeaderFile.setDestPath("/touch/")
        freqHopHeaderFile.setProjectPath("config/" + configName + "/touch/")
        freqHopHeaderFile.setType("HEADER")
        freqHopHeaderFile.setMarkup(False)
        freqHopHeaderFile.setEnabled(True)
        return freqHopHeaderFile

    # freqHopAutoHeaderFile
    def setfreqHopAutoHeaderFile(self,configName, qtouchComponent):
        """
        Generates frequency hop auto header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        freqHopAutoHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HOP_AUTO_HEADER", None)
        freqHopAutoHeaderFile.setSourcePath("/src/qtm_freq_hop_auto_0x0004_api.h")
        freqHopAutoHeaderFile.setOutputName("qtm_freq_hop_auto_0x0004_api.h")
        freqHopAutoHeaderFile.setDestPath("/touch/")
        freqHopAutoHeaderFile.setProjectPath("config/" + configName + "/touch/")
        freqHopAutoHeaderFile.setType("HEADER")
        freqHopAutoHeaderFile.setMarkup(False)
        freqHopAutoHeaderFile.setEnabled(True)
        return freqHopAutoHeaderFile
