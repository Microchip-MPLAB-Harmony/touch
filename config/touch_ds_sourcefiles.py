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
class classTouchDSFiles():

    def setDrivenShieldFiles(self,configName, qtouchComponent,useTrustZone):
        """
        Generates as List of source files required for Driven shield support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            fileList: list of file symbols
        """
        # freqHopHeaderFile
        fileList = []
        fileList.append(self.setDrivenShieldHeaderFile(configName, qtouchComponent))
        # freqHopAutoHeaderFile
        fileList.append(self.setDrivenShieldSourceile(configName, qtouchComponent))
        if(useTrustZone ==  False):
            del fileList[:]
        return fileList

    def setDrivenShieldHeaderFile(self,configName, qtouchComponent):
        """
        Generates Driven shield header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        drivenShieldHeadFile = qtouchComponent.createFileSymbol("HEADER_DRIVENSHIELD", None)
        drivenShieldHeadFile.setSourcePath("/templates/driven_shield.h.ftl")
        drivenShieldHeadFile.setOutputName("driven_shield.h")
        drivenShieldHeadFile.setDestPath("/touch/")
        drivenShieldHeadFile.setProjectPath("config/" + configName + "/touch/")
        drivenShieldHeadFile.setType("HEADER")
        drivenShieldHeadFile.setMarkup(True)
        drivenShieldHeadFile.setEnabled(False)
        drivenShieldHeadFile.setDependencies(self.enableDrivenShieldFiles,["DS_DEDICATED_ENABLE"])
        drivenShieldHeadFile.setDependencies(self.enableDrivenShieldFiles,["DS_PLUS_ENABLE"])
        return drivenShieldHeadFile

    def setDrivenShieldSourceile(self,configName, qtouchComponent):
        """
        Generates Driven shield source file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        drivenShieldSourceFile = qtouchComponent.createFileSymbol("SOURCE_DRIVENSHIELD", None)
        drivenShieldSourceFile.setSourcePath("/templates/driven_shield.c.ftl")
        drivenShieldSourceFile.setOutputName("driven_shield.c")
        drivenShieldSourceFile.setDestPath("/touch/")
        drivenShieldSourceFile.setProjectPath("config/" + configName + "/touch/")
        drivenShieldSourceFile.setType("SOURCE")
        drivenShieldSourceFile.setMarkup(True)
        drivenShieldSourceFile.setEnabled(False)
        drivenShieldSourceFile.setDependencies(self.enableDrivenShieldFiles,["DS_DEDICATED_ENABLE"])
        drivenShieldSourceFile.setDependencies(self.enableDrivenShieldFiles,["DS_PLUS_ENABLE"])
        return drivenShieldSourceFile

    def enableDrivenShieldFiles(self,symbol,event):
        """Handler for enabling source / header files.
        Arguments:
            :symbol : the symbol that triggered the event
            :event : new value of the symbol 
        Returns:
            :none
        """
        localComponent= symbol.getComponent()
        enableSourceFiles = bool(event['symbol'].getValue())
        localComponent.getSymbolByID("HEADER_DRIVENSHIELD").setEnabled(enableSourceFiles)
        localComponent.getSymbolByID("SOURCE_DRIVENSHIELD").setEnabled(enableSourceFiles)