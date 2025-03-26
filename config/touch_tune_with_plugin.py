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
class classTouchTuneWithPlugin():

    def initTouchTune(self,configName, qtouchComponent, parentLabel):
        """
        Generates as List of source files required for Scroller support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        enableTouchTuneMenu = qtouchComponent.createBooleanSymbol("ENABLE_TOUCH_TUNE_WITH_PLUGIN", parentLabel)
        enableTouchTuneMenu.setLabel("Enable Tuning With Touch Plugin")
        enableTouchTuneMenu.setDefaultValue(False)
        enableTouchTuneMenu.setDescription("The Tuning With Touch Plugin allows touch sensor debug information to be relayed on the USART interface to Tuning With Touch Plugin software tool. This setting should be enabled for initial sensor tuning and can be disabled later to avoid using USART and additionally save code memory. More information can be found in Microchip Developer Help page.")
        enableTouchTuneMenu.setDependencies(self.enableTouchTuneFtlFiles,["ENABLE_TOUCH_TUNE_WITH_PLUGIN"])

        fileList = []
        if json_loader_instance.get_data()["features"]["bidirectionalTune"]==True:
            fileList.append(self.setTouchTuneHeader(configName, qtouchComponent))
            fileList.append(self.setTouchTuneSource(configName, qtouchComponent))
        return fileList


    # Header File
    def setTouchTuneHeader(self,configName, qtouchComponent):
        """
        Generates TouchTune.h file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchTouchTuneHeaderFile = qtouchComponent.createFileSymbol("TOUCH_TUNE_WITH_PLUGIN_HEADER", None)
        tchTouchTuneHeaderFile.setSourcePath("/templates/touchTune.h.ftl")
        tchTouchTuneHeaderFile.setOutputName("touchTune.h")
        tchTouchTuneHeaderFile.setDestPath("/touch/")
        tchTouchTuneHeaderFile.setProjectPath("config/" + configName + "/touch/")
        tchTouchTuneHeaderFile.setType("HEADER")
        tchTouchTuneHeaderFile.setEnabled(False)
        tchTouchTuneHeaderFile.setMarkup(True)
        return tchTouchTuneHeaderFile

    # Source File
    def setTouchTuneSource(self,configName, qtouchComponent):
        """
        Generates TouchTune UART C file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchTouchTuneSourceFile = qtouchComponent.createFileSymbol("TOUCH_TUNE_WITH_PLUGIN_SOURCE", None)
        tchTouchTuneSourceFile.setSourcePath("/templates/touchTune_UART_sam.c.ftl")
        tchTouchTuneSourceFile.setOutputName("touchTune.c")
        tchTouchTuneSourceFile.setDestPath("/touch/")
        tchTouchTuneSourceFile.setProjectPath("config/" + configName + "/touch/")
        tchTouchTuneSourceFile.setType("SOURCE")
        tchTouchTuneSourceFile.setEnabled(False)
        tchTouchTuneSourceFile.setMarkup(True)
        return tchTouchTuneSourceFile


    def enableTouchTuneFtlFiles(self,symbol,event):
        """Enables TouchTune functionality.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component = symbol.getComponent()
        surfaceUtility = symbol.getComponent().getSymbolByID("ENABLE_KRONOCOMM").getValue()
        if(event["value"] == True):
            component.setDependencyEnabled("Touch_sercom_Krono", True)
            component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(True)
            component.getSymbolByID("TOUCH_TUNE_WITH_PLUGIN_SOURCE").setEnabled(True)
            component.getSymbolByID("TOUCH_TUNE_WITH_PLUGIN_HEADER").setEnabled(True)
        else:
            if (surfaceUtility == False):
                component.setDependencyEnabled("Touch_sercom_Krono", False)
                component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(False)
            component.getSymbolByID("TOUCH_TUNE_WITH_PLUGIN_SOURCE").setEnabled(False)
            component.getSymbolByID("TOUCH_TUNE_WITH_PLUGIN_HEADER").setEnabled(False)
