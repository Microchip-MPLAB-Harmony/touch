InterruptVector = "PTC" + "_INTERRUPT_ENABLE"
InterruptHandler = "PTC" + "_INTERRUPT_HANDLER"

def onAttachmentConnected(source,target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if (connectID == "Touch_timer"):
        plibUsed = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if targetID == "RTC_TMR":
            Database.setSymbolValue(remoteID, "RTC_MODE0_MATCHCLR", True, 1)
            Database.setSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE", True, 2)        
    
    if (connectID == "Touch_sercom"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", False, 1)


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if (connectID == "Touch_timer"):
        plibUsed = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE")
        plibUsed.clearValue()
    
    if (connectID == "Touch_sercom"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE")
        plibUsed.clearValue()

def enableHopFiles(symbol,event):
    component = symbol.getComponent()
    hopAutoEnabled = enableFreqHopAutoTuneMenu.getValue()
    print(hopAutoEnabled)
    if(event["value"] == True) and (hopAutoEnabled == True):
        component.getSymbolByID("TOUCH_HOP_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_HOP_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_HOP_AUTO_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_HOP_AUTO_HEADER").setEnabled(True)
    else:
        component.getSymbolByID("TOUCH_HOP_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_HOP_HEADER").setEnabled(False)

def enableDataStreamerFtlFiles(symbol,event):
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
        
autoComponentIDTable = ["rtc"]
autoConnectTable = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"]]

################################################################################
#### Component ####
################################################################################
def instantiateComponent(qtouchComponent):

    configName = Variables.get("__CONFIGURATION_NAME")

    #SET PTC INTERRUPT HANDLER
    Database.setSymbolValue("core", InterruptVector, True, 2)
    Database.setSymbolValue("core", InterruptHandler, "PTC_Handler", 2)
    
    #SET PTC PERIPHERAL CLOCK AND CHOOSE GCLK AS GCLK1
    Database.clearSymbolValue("core", "PTC" + "_CLOCK_ENABLE")
    Database.setSymbolValue("core", "PTC" + "_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", "GCLK_ID_37_GENSEL")
    Database.setSymbolValue("core", "GCLK_ID_37_GENSEL", 1, 2)
    
    #SET GCLK FOR PTC - GCLK1 AT 4MHZ
    Database.clearSymbolValue("core", "GCLK_INST_NUM1")
    Database.setSymbolValue("core", "GCLK_INST_NUM1", True, 2)
    Database.clearSymbolValue("core", "GCLK_1_DIV")
    Database.setSymbolValue("core", "GCLK_1_DIV", 12, 2)
    
    touchMenu = qtouchComponent.createMenuSymbol("TOUCH_MENU", None)
    touchMenu.setLabel("Touch Configuration")
    
    execfile(Module.getPath() +"/config/interface.py")
    if(getDeviceName.getDefaultValue() == "SAMC20"):
        execfile(Module.getPath() +"/config/acquisition_samc20.py")
    else:
        execfile(Module.getPath() +"/config/acquisition_samc21.py")
    execfile(Module.getPath() +"/config/node.py")
    execfile(Module.getPath() +"/config/key.py")
    execfile(Module.getPath() +"/config/sensor.py")
    
    global enableFreqHopMenu
    # Enable Frequency Hop  
    enableFreqHopMenu = qtouchComponent.createBooleanSymbol("ENABLE_FREQ_HOP", touchMenu)
    enableFreqHopMenu.setLabel("Enable Frequency Hop")
    enableFreqHopMenu.setDefaultValue(False)
    enableFreqHopMenu.setDescription("Frequency Hop is a mechanism used in touch measurement to avoid noisy signal value. In Frequency Hop, more than one bursting frequency (user configurable) is used. Refer QTouch Modular Library Userguide for more details on Frequency Hop.")
    execfile(Module.getPath() +"/config/freq_hop.py")
    enableFreqHopMenu.setDependencies(enableHopFiles,["ENABLE_FREQ_HOP"])

    # Enable Datastreamer  
    enableDataStreamerMenu = qtouchComponent.createBooleanSymbol("ENABLE_DATA_STREAMER", touchMenu)
    enableDataStreamerMenu.setLabel("Enable Data Visualizer")
    enableDataStreamerMenu.setDefaultValue(False)
    enableDataStreamerMenu.setDescription("The Data Visualizer allows touch sensor debug information to be relayed on the USART interface to Data Visualizer software tool. This setting should be enabled for initial sensor tuning and can be disabled later to avoid using USART and additionally save code memory. More information can be found in Microchip Developer Help page.")
    enableDataStreamerMenu.setDependencies(enableDataStreamerFtlFiles,["ENABLE_DATA_STREAMER"])
    execfile(Module.getPath() +"/config/datastreamer.py")
    
    qtouchTimerComponent = qtouchComponent.createStringSymbol("TOUCH_TIMER_INSTANCE", None)
    qtouchTimerComponent.setLabel("Timer Component Chosen for Touch middleware")
    qtouchTimerComponent.setReadOnly(True)
    qtouchTimerComponent.setDefaultValue("")
    
    qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_INSTANCE", None)
    qtouchSercomComponent.setLabel("Sercom Component Chosen for Touch middleware")
    qtouchSercomComponent.setReadOnly(True)
    qtouchSercomComponent.setVisible(False)
    qtouchSercomComponent.setDefaultValue("")
    
############################################################################
#### Code Generation ####
############################################################################
    #configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER", None)
    touchHeaderFile.setSourcePath("/templates/touch.h.ftl")
    touchHeaderFile.setOutputName("touch.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(True)
	
    # Header File
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER1", None)
    touchHeaderFile.setSourcePath("/templates/touch_api_ptc.h.ftl")
    touchHeaderFile.setOutputName("touch_api_ptc.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(True)
	
    # Source File
    touchSourceFile = qtouchComponent.createFileSymbol("TOUCH_SOURCE", None)
    touchSourceFile.setSourcePath("/templates/touch.c.ftl")
    touchSourceFile.setOutputName("touch.c")
    touchSourceFile.setDestPath("/touch/")
    touchSourceFile.setProjectPath("config/" + configName +"/touch/")
    touchSourceFile.setType("SOURCE")
    touchSourceFile.setMarkup(True)

        #System Initialization
    ptcSystemInitFile = qtouchComponent.createFileSymbol("PTC_SYS_INIT", None)
    ptcSystemInitFile.setType("STRING")
    ptcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
    ptcSystemInitFile.setSourcePath("../touch/templates/system/initialization.c.ftl")
    ptcSystemInitFile.setMarkup(True)

    # System Definition
    ptcSystemDefFile = qtouchComponent.createFileSymbol("PTC_SYS_DEF", None)
    ptcSystemDefFile.setType("STRING")
    ptcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ptcSystemDefFile.setSourcePath("../touch/templates/system/definitions.h.ftl")
    ptcSystemDefFile.setMarkup(True)

    qtouchComponent.addPlugin("../touch/plugin/ptc_manager_c21.jar")

def finalizeComponent(qtouchComponent):
    res = Database.activateComponents(autoComponentIDTable)
    res = Database.connectDependencies(autoConnectTable)