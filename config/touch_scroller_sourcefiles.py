"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchScrollerSourceFiles():

    def setScrollerFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
        """
        Generates as List of source files required for Scroller support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        fileList.append(self.setScrollerLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setScrollerHeaderFile(configName, qtouchComponent))
        if(useTrustZone == False):
            del fileList[:]
        return fileList

    def setScrollerLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates Scroller library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        if (targetDevice in ["SAME51","SAME53","SAME54","SAMD51","PIC32CXBZ31","WBZ35"]):
            scrollerLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SCR_LIB", None)
            scrollerLibraryFile.setSourcePath("/src/libraries/qtm_scroller_cm4_0x000b.X.a")
            scrollerLibraryFile.setOutputName("qtm_scroller_cm4_0x000b.X.a")
            scrollerLibraryFile.setDestPath("/touch/lib/")
            scrollerLibraryFile.setEnabled(False)
        elif (targetDevice in ["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00"]):
            scrollerLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SCR_LIB", None)
            scrollerLibraryFile.setSourcePath("/src/libraries/qtm_scroller_cm23_0x000b.X.a")
            scrollerLibraryFile.setOutputName("qtm_scroller_cm23_0x000b.X.a")
            scrollerLibraryFile.setDestPath("/touch/lib/")
            scrollerLibraryFile.setEnabled(False)
        elif (targetDevice in ["PIC32MZW", "PIC32MZDA"]):
            scrollerLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SCR_LIB", None)
            scrollerLibraryFile.setSourcePath("/src/libraries/qtm_scroller_pic32mz_0x000b.X.a")
            scrollerLibraryFile.setOutputName("qtm_scroller_pic32mz_0x000b.X.a")
            scrollerLibraryFile.setDestPath("/touch/lib/")
            scrollerLibraryFile.setEnabled(False)
        else:
            scrollerLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SCR_LIB", None)
            scrollerLibraryFile.setSourcePath("/src/libraries/qtm_scroller_cm0p_0x000b.X.a")
            scrollerLibraryFile.setOutputName("qtm_scroller_cm0p_0x000b.X.a")
            scrollerLibraryFile.setDestPath("/touch/lib/")
            scrollerLibraryFile.setEnabled(False)
        return scrollerLibraryFile

    def setScrollerHeaderFile(self,configName, qtouchComponent):
        """
        Generates Scroller header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        scrollerHeaderFile = qtouchComponent.createFileSymbol("TOUCH_SCR_HEADER", None)
        scrollerHeaderFile.setSourcePath("/src/qtm_scroller_0x000b_api.h")
        scrollerHeaderFile.setOutputName("qtm_scroller_0x000b_api.h")
        scrollerHeaderFile.setDestPath("/touch/")
        scrollerHeaderFile.setProjectPath("config/" + configName + "/touch/")
        scrollerHeaderFile.setType("HEADER")
        scrollerHeaderFile.setEnabled(False)
        scrollerHeaderFile.setMarkup(False)
        return scrollerHeaderFile
