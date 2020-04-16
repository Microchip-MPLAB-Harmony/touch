InterruptVector = "PTC" + "_INTERRUPT_ENABLE"
InterruptHandler = "PTC" + "_INTERRUPT_HANDLER"

timer_based_driven_shield_supported_device = ["SAMD21","SAMDA1","SAMHA1","SAME54","SAME53","SAME51","SAMD51","SAMC21","SAMC20","SAML21","SAML22"]
adc_based_touch_acqusition_device = ["SAME54","SAME53","SAME51","SAMD51"]

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
            if (Database.getSymbolValue(remoteID, "RTC_MODE0_MATCHCLR") == False):
                Database.setSymbolValue(remoteID, "RTC_MODE0_MATCHCLR", True)
            if (Database.getSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE") == False):
                Database.setSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE", True)
                Database.setSymbolValue(remoteID, "RTC_MODULE_SELECTION", 0)
        else:
            Database.setSymbolValue(remoteID, "TIMER_PRE_SCALER", 0)
            Database.setSymbolValue(remoteID, "TMR_INTERRUPT_MODE", True)
    if (connectID == "Touch_sercom"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if (Database.getSymbolValue(remoteID, "USART_INTERRUPT_MODE") == True):
            Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", False)

    if (connectID == "Touch_sercom_Krono"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if (Database.getSymbolValue(remoteID, "USART_INTERRUPT_MODE") == False):
            Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", True)


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
    if (connectID == "Touch_sercom_Krono"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE")
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
    elif(event["value"] == True):
        component.getSymbolByID("TOUCH_HOP_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_HOP_HEADER").setEnabled(True)
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
        

def enableScroller(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("TOUCH_SCR_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_SCR_HEADER").setEnabled(True)
    else:
        component.getSymbolByID("TOUCH_SCR_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_SCR_HEADER").setEnabled(False)

def enableGestureFiles(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("TOUCH_GESTURE_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_GESTURE_HEADER").setEnabled(True)
    else:
        component.getSymbolByID("TOUCH_GESTURE_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_GESTURE_HEADER").setEnabled(False)

def enable2DSurfaceFtlFiles(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        #tchKronocommUartHeaderFile.setEnabled(True)
        component.setDependencyEnabled("Touch_sercom_Krono", True)
        component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_SOURCE").setEnabled(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_SOURCE").setEnabled(True)
    else:
        #tchKronocommUartHeaderFile.setEnabled(False)
        component.setDependencyEnabled("Touch_sercom_Krono", False)
        component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_SOURCE").setEnabled(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_SOURCE").setEnabled(False)

autoComponentIDTable = ["rtc"]
autoConnectTable = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"]]

#used for driven shield 
ptcYPads = []
touchChannels = []

################################################################################
#### Component ####
################################################################################
def instantiateComponent(qtouchComponent):
    global autoComponentIDTable
    global autoConnectTable
		
    configName = Variables.get("__CONFIGURATION_NAME")

    touchMenu = qtouchComponent.createMenuSymbol("TOUCH_MENU", None)
    touchMenu.setLabel("Touch Configuration")
    
    touchInfoMenu = qtouchComponent.createMenuSymbol("TOUCH_INFO", None)
    touchInfoMenu.setLabel("Touch Configuration Helper")
    
    touchScriptEvent = qtouchComponent.createStringSymbol("TOUCH_SCRIPT_EVENT", touchInfoMenu)
    touchScriptEvent.setLabel("Script Event ")
    touchScriptEvent.setReadOnly(True)
	
    ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance@[name=\"PTC\"]/parameters/param@[name=\"GCLK_ID\"]")
    ptcFreqencyId= qtouchComponent.createStringSymbol("PTC_CLOCK_FREQ", touchInfoMenu)
    ptcFreqencyId.setLabel("PTC Freqency Id ")
    ptcFreqencyId.setReadOnly(True)
    ptcFreqencyId.setDefaultValue("GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ")
    
    execfile(Module.getPath() +"/config/interface.py")
    execfile(Module.getPath() +"/config/acquisition_"+getDeviceName.getDefaultValue().lower()+".py")
    if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
        execfile(Module.getPath() +"/config/node_E5X.py")
    elif (getDeviceName.getDefaultValue() in ["SAMD20","SAMD21","SAMDA1","SAMHA1"]):
        execfile(Module.getPath() +"/config/node_D2X.py")
    elif (getDeviceName.getDefaultValue() in ["SAML21"]):
        execfile(Module.getPath() +"/config/node_L21.py")
    elif (getDeviceName.getDefaultValue() in ["SAML22"]):
        execfile(Module.getPath() +"/config/node_L22.py")
    elif (getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
        execfile(Module.getPath() +"/config/node_L1x.py")
    elif (getDeviceName.getDefaultValue() in ["SAMD10","SAMD11"]):
        execfile(Module.getPath() +"/config/node_D1X.py")
    elif (getDeviceName.getDefaultValue() in ["PIC32MZW"]):
        execfile(Module.getPath() +"/config/node_pic32mz.py")
        autoComponentIDTable = ["adchs","tmr2"]
        autoConnectTable = [["lib_qtouch", "Touch_timer","tmr2","TMR2_TMR"]]
    else:
        execfile(Module.getPath() +"/config/node_C2X.py")
    
    if (getDeviceName.getDefaultValue() in timer_based_driven_shield_supported_device):
        execfile(Module.getPath() +"/config/drivenshield.py")
        
    execfile(Module.getPath() +"/config/key.py")
    execfile(Module.getPath() +"/config/sensor.py")

    # Enable Scroller 
    enableScrollerMenu = qtouchComponent.createBooleanSymbol("ENABLE_SCROLLER", touchMenu)
    enableScrollerMenu.setLabel("Enable Scroller")
    enableScrollerMenu.setDefaultValue(False)
    execfile(Module.getPath() +"/config/scroller.py")
    enableScrollerMenu.setDependencies(enableScroller,["ENABLE_SCROLLER"])

    # Enable Surface 
    enableSurfaceMenu = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE", touchMenu)
    enableSurfaceMenu.setLabel("Enable Surface")
    enableSurfaceMenu.setDefaultValue(False)
    execfile(Module.getPath() +"/config/surface.py")

    # Enable 4p 
    global fourP
    enable4pMenu = qtouchComponent.createBooleanSymbol("ENABLE_4p", touchMenu)
    enable4pMenu.setLabel("Enable 4p")
    enable4pMenu.setDefaultValue(False)

    # Enable Gesture 
    enableGestureMenu = qtouchComponent.createBooleanSymbol("ENABLE_GESTURE", touchMenu)
    enableGestureMenu.setLabel("Enable Gesture")
    enableGestureMenu.setDefaultValue(False)
    execfile(Module.getPath() +"/config/gesture.py")
    enableGestureMenu.setDependencies(enableGestureFiles,["ENABLE_GESTURE"])

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

    # Enable 2D Surface Visualizer 
    enableSurfaceUtilityMenu = qtouchComponent.createBooleanSymbol("ENABLE_KRONOCOMM", touchMenu)
    enableSurfaceUtilityMenu.setLabel("Enable 2D Surface Utility")
    enableSurfaceUtilityMenu.setDefaultValue(False)
    enableSurfaceUtilityMenu.setDescription("The 2D Surface Utility allows touch sensor debug information to be relayed on the USART interface to 2D Surface Utility software tool. This setting should be enabled for evaluating gestures and touch performance in surface applications. More information can be found in Microchip Developer Help page.")
    enableSurfaceUtilityMenu.setDependencies(enable2DSurfaceFtlFiles,["ENABLE_KRONOCOMM"])
    execfile(Module.getPath() +"/config/Surface_2D_Utility.py")

    qtouchTimerComponent = qtouchComponent.createStringSymbol("TOUCH_TIMER_INSTANCE", None)
    qtouchTimerComponent.setLabel("Timer Component Chosen for Touch middleware")
    qtouchTimerComponent.setReadOnly(True)
    qtouchTimerComponent.setDefaultValue("")
    
    qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_INSTANCE", None)
    qtouchSercomComponent.setLabel("Sercom Component Chosen for Touch middleware")
    qtouchSercomComponent.setReadOnly(True)
    qtouchSercomComponent.setVisible(False)
    qtouchSercomComponent.setDefaultValue("")

    qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_KRONO_INSTANCE", None)
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