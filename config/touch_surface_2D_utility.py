"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchSurface2DUtility():

    def initSurface2DUtilityInstance(self,configName, qtouchComponent, parentLabel , targetDevice, touchKeyCountMax):
        """Initialise 2D Surface utiilityInstance
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :parentLabel : parent symbol for added menu items
            :targetDevice : see interface.getDeviceSeries()
            :touchKeyCountMax : see target_device.getMutualCount()
        Returns:
            fileList: list of file symbols
        """    
        enableSurfaceUtilityMenu = qtouchComponent.createBooleanSymbol("ENABLE_KRONOCOMM", parentLabel)
        enableSurfaceUtilityMenu.setLabel("Enable 2D Surface Utility")
        enableSurfaceUtilityMenu.setDefaultValue(False)
        enableSurfaceUtilityMenu.setDescription("The 2D Surface Utility allows touch sensor debug information to be relayed on the USART interface to 2D Surface Utility software tool. This setting should be enabled for evaluating gestures and touch performance in surface applications. More information can be found in Microchip Developer Help page.")
        enableSurfaceUtilityMenu.setDependencies(self.enable2DSurfaceFiles,["ENABLE_KRONOCOMM"])

        fileList = []
        fileList.append(self.set2DUartHeaderFile(configName, qtouchComponent))
        fileList.append(self.set2DAdapterHeaderFile(configName, qtouchComponent))
        fileList.append(self.set2DUartSourceFile(configName, qtouchComponent))
        fileList.append(self.set2DAdapterSourceFile(configName, qtouchComponent))
        return fileList

    def set2DUartHeaderFile(self,configName, qtouchComponent):
        """
        Generates 1 touch Surface library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tch2DUartHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_UART_HEADER", None)
        tch2DUartHeaderFile.setSourcePath("/templates/kronocommuart.h.ftl")
        tch2DUartHeaderFile.setOutputName("kronocommuart_sam.h")
        tch2DUartHeaderFile.setDestPath("/touch/datastreamer/")
        tch2DUartHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tch2DUartHeaderFile.setType("HEADER")
        tch2DUartHeaderFile.setEnabled(False)
        tch2DUartHeaderFile.setMarkup(True)
        return tch2DUartHeaderFile

    def set2DAdapterHeaderFile(self,configName, qtouchComponent):
        """
        Generates 1 touch Surface library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tch2DAdapterHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_ADAPTOR_HEADER", None)
        tch2DAdapterHeaderFile.setSourcePath("/templates/kronocommadaptor.h.ftl")
        tch2DAdapterHeaderFile.setOutputName("kronocommadaptor.h")
        tch2DAdapterHeaderFile.setDestPath("/touch/datastreamer/")
        tch2DAdapterHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tch2DAdapterHeaderFile.setType("HEADER")
        tch2DAdapterHeaderFile.setEnabled(False)
        tch2DAdapterHeaderFile.setMarkup(False)
        return tch2DAdapterHeaderFile

    def set2DUartSourceFile(self,configName, qtouchComponent):
        """
        Generates 1 touch Surface library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tch2DUartSourceFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_UART_SOURCE", None)
        tch2DUartSourceFile.setSourcePath("/templates/kronocommuart.c.ftl")
        tch2DUartSourceFile.setOutputName("kronocommuart_sam.c")
        tch2DUartSourceFile.setDestPath("/touch/datastreamer/")
        tch2DUartSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tch2DUartSourceFile.setType("SOURCE")
        tch2DUartSourceFile.setEnabled(False)
        tch2DUartSourceFile.setMarkup(True)
        return tch2DUartSourceFile

    def set2DAdapterSourceFile(self,configName, qtouchComponent):
        """
        Generates 1 touch Surface library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        tch2DAdapterSourceFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_ADAPTOR_SOURCE", None)
        tch2DAdapterSourceFile.setSourcePath("/templates/kronocommadaptor.c.ftl")
        tch2DAdapterSourceFile.setOutputName("kronocommadaptor.c")
        tch2DAdapterSourceFile.setDestPath("/touch/datastreamer/")
        tch2DAdapterSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
        tch2DAdapterSourceFile.setType("SOURCE")
        tch2DAdapterSourceFile.setEnabled(False)
        tch2DAdapterSourceFile.setMarkup(True)
        return tch2DAdapterSourceFile

    def enable2DSurfaceFiles(self,symbol,event):
        """Enables Surface functionality.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component = symbol.getComponent()  
        touchTune = symbol.getComponent().getSymbolByID("ENABLE_TOUCH_TUNE_WITH_PLUGIN").getValue()
        if(event["value"] == True):
            component.setDependencyEnabled("Touch_sercom_Krono", True)
            component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(True)
            component.getSymbolByID("TOUCH_KRONOCOMM_UART_HEADER").setEnabled(True)
            component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_HEADER").setEnabled(True)
            component.getSymbolByID("TOUCH_KRONOCOMM_UART_SOURCE").setEnabled(True)
            component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_SOURCE").setEnabled(True)
        else:
            if (touchTune == False):
                component.setDependencyEnabled("Touch_sercom_Krono", False)
                component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(False)
            component.getSymbolByID("TOUCH_KRONOCOMM_UART_HEADER").setEnabled(False)
            component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_HEADER").setEnabled(False)
            component.getSymbolByID("TOUCH_KRONOCOMM_UART_SOURCE").setEnabled(False)
            component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_SOURCE").setEnabled(False)

