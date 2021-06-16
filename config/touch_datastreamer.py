"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchDataStreamer():

    def initDataStreamer(self,configName, qtouchComponent, parentLabel):
        """
        Generates as List of source files required for Scroller support
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            fileList: list of file symbols
        """
        enableDataStreamerMenu = qtouchComponent.createBooleanSymbol("ENABLE_DATA_STREAMER", parentLabel)
        enableDataStreamerMenu.setLabel("Enable Data Visualizer")
        enableDataStreamerMenu.setDefaultValue(False)
        enableDataStreamerMenu.setDescription("The Data Visualizer allows touch sensor debug information to be relayed on the USART interface to Data Visualizer software tool. This setting should be enabled for initial sensor tuning and can be disabled later to avoid using USART and additionally save code memory. More information can be found in Microchip Developer Help page.")
        enableDataStreamerMenu.setDependencies(self.enableDataStreamerFtlFiles,["ENABLE_DATA_STREAMER"])

        fileList = []
        fileList.append(self.setDatastreamerHeader(configName, qtouchComponent))
        fileList.append(self.setDatastreamerDb(configName, qtouchComponent))
        fileList.append(self.setDatastreamerDs(configName, qtouchComponent))
        fileList.append(self.setDatastreamerSc(configName, qtouchComponent))
        fileList.append(self.setDatastreamerSource(configName, qtouchComponent))
        return fileList


    # Header File
    def setDatastreamerHeader(self,configName, qtouchComponent):
        """
        Generates Datastreamer.h file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchDataStreamerHeaderFile = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER", None)
        tchDataStreamerHeaderFile.setSourcePath("/src/datastreamer.h")
        tchDataStreamerHeaderFile.setOutputName("datastreamer.h")
        tchDataStreamerHeaderFile.setDestPath("/touch/datastreamer/")
        tchDataStreamerHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tchDataStreamerHeaderFile.setType("HEADER")
        tchDataStreamerHeaderFile.setEnabled(False)
        tchDataStreamerHeaderFile.setMarkup(False)
        return tchDataStreamerHeaderFile

    # Header File2
    def setDatastreamerDb(self,configName, qtouchComponent):
        """
        Generates Datastreamer DB file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchDsHeaderFileDb = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER_db", None)
        tchDsHeaderFileDb.setSourcePath("/templates/03EB00000000000000AA5501.db.ftl")
        tchDsHeaderFileDb.setOutputName("03EB00000000000000AA5501.db")
        tchDsHeaderFileDb.setDestPath("/touch/datastreamer/")
        tchDsHeaderFileDb.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tchDsHeaderFileDb.setType("HEADER")
        tchDsHeaderFileDb.setEnabled(False)
        tchDsHeaderFileDb.setMarkup(True)
        return tchDsHeaderFileDb

    # Header File3
    def setDatastreamerDs(self,configName, qtouchComponent):
        """
        Generates Datastreamer DS file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchDsHeaderFileDs = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER_ds", None)
        tchDsHeaderFileDs.setSourcePath("/templates/03EB00000000000000AA5501.ds.ftl")
        tchDsHeaderFileDs.setOutputName("03EB00000000000000AA5501.ds")
        tchDsHeaderFileDs.setDestPath("/touch/datastreamer/")
        tchDsHeaderFileDs.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tchDsHeaderFileDs.setType("HEADER")
        tchDsHeaderFileDs.setEnabled(False)
        tchDsHeaderFileDs.setMarkup(True)
        return tchDsHeaderFileDs

    # Header File4
    def setDatastreamerSc(self,configName, qtouchComponent):
        """
        Generates Datastreamer SC file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchDsHeaderFileSc = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER_sc", None)
        tchDsHeaderFileSc.setSourcePath("/templates/03EB00000000000000AA5501.sc.ftl")
        tchDsHeaderFileSc.setOutputName("03EB00000000000000AA5501.sc")
        tchDsHeaderFileSc.setDestPath("/touch/datastreamer/")
        tchDsHeaderFileSc.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tchDsHeaderFileSc.setType("HEADER")
        tchDsHeaderFileSc.setEnabled(False)
        tchDsHeaderFileSc.setMarkup(True)
        return tchDsHeaderFileSc

    # Source File
    def setDatastreamerSource(self,configName, qtouchComponent):
        """
        Generates Datastreamer UART C file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tchDataStreamerSourceFile = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_SOURCE", None)
        tchDataStreamerSourceFile.setSourcePath("/templates/datastreamer_UART_sam.c.ftl")
        tchDataStreamerSourceFile.setOutputName("datastreamer_UART_sam.c")
        tchDataStreamerSourceFile.setDestPath("/touch/datastreamer/")
        tchDataStreamerSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tchDataStreamerSourceFile.setType("SOURCE")
        tchDataStreamerSourceFile.setEnabled(False)
        tchDataStreamerSourceFile.setMarkup(True)
        return tchDataStreamerSourceFile


    def enableDataStreamerFtlFiles(self,symbol,event):
        """Enables datastreamer functionality.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component = symbol.getComponent()
        if(event["value"] == True):
            #tchDataStreamerHeaderFile.setEnabled(True)
            component.setDependencyEnabled("Touch_sercom", True)
            component.getSymbolByID("TOUCH_SERCOM_INSTANCE").setVisible(True)
            component.getSymbolByID("TOUCH_DATA_STREAMER_SOURCE").setEnabled(True)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER").setEnabled(True)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_db").setEnabled(True)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_ds").setEnabled(True)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(True)
        else:
            #tchDataStreamerHeaderFile.setEnabled(False)
            component.setDependencyEnabled("Touch_sercom", False)
            component.getSymbolByID("TOUCH_SERCOM_INSTANCE").setVisible(False)
            component.getSymbolByID("TOUCH_DATA_STREAMER_SOURCE").setEnabled(False)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER").setEnabled(False)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_db").setEnabled(False)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_ds").setEnabled(False)
            component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(False)