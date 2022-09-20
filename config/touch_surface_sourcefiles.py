"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchSurfaceFiles():
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
        if (targetDevice in ["SAME51","SAME53","SAME54","SAMD51","PIC32CXBZ31","WBZ35"]):
            surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_cm4_0x0021.X.a")
            surface1TLibraryFile.setOutputName("qtm_surface_cs_cm4_0x0021.X.a")
        elif(targetDevice in ["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00"]):
            surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_cm23_0x0021.X.a")
            surface1TLibraryFile.setOutputName("qtm_surface_cs_cm23_0x0021.X.a")
        elif (targetDevice in ["PIC32MZW", "PIC32MZDA"]):
            surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_pic32mz_0x0021.X.a")
            surface1TLibraryFile.setOutputName("qtm_surface_cs_pic32mz_0x0021.X.a")
        else:
            surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_cm0p_0x0021.X.a")
            surface1TLibraryFile.setOutputName("qtm_surface_cs_cm0p_0x0021.X.a")
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
        if (targetDevice in ["SAME51","SAME53","SAME54","SAMD51","PIC32CXBZ31","WBZ35"]):
            surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_cm4_0x0025.X.a")
            surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_cm4_0x0025.X.a")
        elif(targetDevice in ["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00"]):
            surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_cm23_0x0025.X.a")
            surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_cm23_0x0025.X.a")
        elif (targetDevice in ["PIC32MZW", "PIC32MZDA"]):
            surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_pic32mz_0x0025.X.a")
            surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_pic32mz_0x0025.X.a")
        else:
            surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_cm0p_0x0025.X.a")
            surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_cm0p_0x0025.X.a")
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

