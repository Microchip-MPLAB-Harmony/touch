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
class classTouchSurfaceFiles():
    def __init__(self):
        self.json_data=json_loader_instance.get_data()

    def setSurfaceFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
        """
        Generates as List of source files required for Surface support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        fileList.append(self.setSurface1TLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setSurface2TLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setSurface1THeaderFile(configName, qtouchComponent))
        fileList.append(self.setSurface2THeaderFile(configName, qtouchComponent))
        if(useTrustZone == False):
            del fileList[:]
        return fileList

    def setSurface1TLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates 1 touch Surface library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        surface1TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE1T_LIB", None)
        surface1TLibraryFile.setDestPath("/touch/lib/")
        surface1TLibraryFile.setEnabled(False)

        architechture=json_loader_instance.get_architecture()
        surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_"+architechture+"_0x0021.X.a")
        surface1TLibraryFile.setOutputName("qtm_surface_cs_"+architechture+"_0x0021.X.a")
        return surface1TLibraryFile


    def setSurface2TLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates 2 touch Surface library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        surface2TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE2T_LIB", None)
        surface2TLibraryFile.setDestPath("/touch/lib/")
        surface2TLibraryFile.setEnabled(False)
        architechture=json_loader_instance.get_architecture()
        surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_"+architechture+"_0x0025.X.a")
        surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_"+architechture+"_0x0025.X.a")
        return surface2TLibraryFile

    def setSurface1THeaderFile(self,configName, qtouchComponent):
        """
        Generates 1 touch Surface Header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        surface1THeaderFile = qtouchComponent.createFileSymbol("TOUCH_SURFACE1T_HEADER", None)
        surface1THeaderFile.setSourcePath("/src/qtm_surface_cs_0x0021_api.h")
        surface1THeaderFile.setOutputName("qtm_surface_cs_0x0021_api.h")
        surface1THeaderFile.setDestPath("/touch/")
        surface1THeaderFile.setProjectPath("config/" + configName + "/touch/")
        surface1THeaderFile.setType("HEADER")
        surface1THeaderFile.setMarkup(False)
        surface1THeaderFile.setEnabled(False)
        return surface1THeaderFile

    def setSurface2THeaderFile(self,configName, qtouchComponent):
        """
        Generates 2 touch Surface Header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        surface2THeaderFile = qtouchComponent.createFileSymbol("TOUCH_SURFACE2T_HEADER", None)
        surface2THeaderFile.setSourcePath("/src/qtm_surface_cs2t_0x0025_api.h")
        surface2THeaderFile.setOutputName("qtm_surface_cs2t_0x0025_api.h")
        surface2THeaderFile.setDestPath("/touch/")
        surface2THeaderFile.setProjectPath("config/" + configName + "/touch/")
        surface2THeaderFile.setType("HEADER")
        surface2THeaderFile.setMarkup(False)
        surface2THeaderFile.setEnabled(False)
        return surface2THeaderFile

