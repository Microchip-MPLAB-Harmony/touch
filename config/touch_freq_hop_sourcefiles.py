"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchFreqSourceFiles():

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
        if (targetDevice in set(["SAME51","SAME53","SAME54","SAMD51"])):    
            freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_cm4_0x0006.X.a")
            freqHopLibraryFile.setOutputName("qtm_freq_hop_cm4_0x0006.X.a")
        elif(targetDevice in set(["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"])):
            freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_cm23_0x0006.X.a")
            freqHopLibraryFile.setOutputName("qtm_freq_hop_cm23_0x0006.X.a")
        elif (targetDevice in set(["PIC32MZW", "PIC32MZDA"])):
            freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_pic32mz_0x0006.X.a")
            freqHopLibraryFile.setOutputName("qtm_freq_hop_pic32mz_0x0006.X.a")
        else:
            freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_cm0p_0x0006.X.a")
            freqHopLibraryFile.setOutputName("qtm_freq_hop_cm0p_0x0006.X.a")
        return "TOUCH_HOP_LIB"

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
    
        if (targetDevice in set(["SAME51","SAME53","SAME54","SAMD51"])):    
            freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_auto_cm4_0x0004.X.a")
            freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_auto_cm4_0x0004.X.a")
        elif(targetDevice in set(["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"])):
            freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_auto_cm23_0x0004.X.a")
            freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_auto_cm23_0x0004.X.a")
        elif (targetDevice in set(["PIC32MZW", "PIC32MZDA"])):
            freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_auto_pic32mz_0x0004.X.a")
            freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_auto_pic32mz_0x0004.X.a")
        else:
            freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_auto_cm0p_0x0004.X.a")
            freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_auto_cm0p_0x0004.X.a")
        return "TOUCH_HOP_AUTO_LIB"

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
        return "TOUCH_HOP_HEADER"

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
        return "TOUCH_HOP_AUTO_HEADER"
