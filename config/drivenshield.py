#driven shield support

global timer_based_driven_shield_supported_device
global adc_based_touch_acqusition_device

def applyDrivenShieldTimers(symbol, event):
    
    component = symbol.getComponent()
    toRemove = []
    toAdd = []
    toConnect = []
    tIndex = 0
    
    toremove = []
    toadd = []

    applyTimers = symbol.getValue().split(">")
    if len(applyTimers[0].strip("]["))!=0:
        toremove = applyTimers[0].strip("][").split(", ")
    if len(applyTimers[1].strip("]["))!=0:
        toadd = applyTimers[1].strip("][").split(", ")
    
    for timer in toremove:
        toRemove.append(timer.lower())
        component.setDependencyEnabled("Drivenshield_"+timer, False)
    for timer in toadd:
        toAdd.append(timer.lower())
        if "TCC" not in timer:
            toConnect.append(["lib_qtouch", "Drivenshield_"+timer,timer.lower(), timer+"_TMR"])
        component.setDependencyEnabled("Drivenshield_"+timer, True)
    
    if len(toRemove)!=0:
        Database.deactivateComponents(toRemove)
    if len(toAdd)!=0:
        Database.activateComponents(toAdd)
        if len(toConnect)!=0:
            Database.connectDependencies(toConnect)
        sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
        sevent.setValue("dstimer")
        sevent.setValue("")
           
        
def enableDrivenShield(symbol,event):
    global drivenShieldHeadFile
    global drivenShieldSourceFile
    dsPlusEnabled = enableDrivenShieldPlus.getValue()
    dsEnabled = enableDrivenShieldDedicated.getValue()
    if((dsPlusEnabled == True) or (dsEnabled == True)):
        drivenShieldHeadFile.setEnabled(True)
        drivenShieldSourceFile.setEnabled(True)
    else:
        drivenShieldHeadFile.setEnabled(False)
        drivenShieldSourceFile.setEnabled(False)
global drivenShieldHeadFile
global drivenShieldSourceFile
#collect timers and timer sharing ptc pads   

timersSharingPTC = []
timersSharingPTCMUX = []
tcInstancesNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]")
tcInstances = []
tcInstances = tcInstancesNode.getChildren()
for indexI in range(0, len(tcInstances)):
    tcSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+ tcInstances[indexI].getAttribute("name") +"\"]/signals")
    tcSignals = []
    tcSignals = tcSignalNode.getChildren()
    for indexS in range(0, len(tcSignals)):
        timer = tcInstances[indexI].getAttribute("name")
        qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
        qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
        if tcSignals[indexS].getAttribute("pad") in ptcYPads:
            timersSharingPTC.append(timer)
            string = tcSignals[indexS].getAttribute("pad")+tcSignals[indexS].getAttribute("function")+"_"+timer+"_"+tcSignals[indexS].getAttribute("group")+tcSignals[indexS].getAttribute("index")
            timersSharingPTCMUX.append(string)
        
tccInstancesNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]")
tccInstances = []
tccInstances = tccInstancesNode.getChildren()
for indexI in range(0, len(tccInstances)):
    tccSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+ tccInstances[indexI].getAttribute("name") +"\"]/signals")
    tccSignals = []
    tccSignals = tccSignalNode.getChildren()
    for indexS in range(0, len(tccSignals)):
        if tccSignals[indexS].getAttribute("pad") in ptcYPads:
            timer = tccInstances[indexI].getAttribute("name")
            timersSharingPTC.append(timer)
            string = tccSignals[indexS].getAttribute("pad")+tccSignals[indexS].getAttribute("function")+"_"+timer+"_"+tccSignals[indexS].getAttribute("group")+tccSignals[indexS].getAttribute("index")
            timersSharingPTCMUX.append(string)
            qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
            qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
        
drivenShieldHeadFile = qtouchComponent.createFileSymbol("HEADER_DRIVENSHIELD", None)
drivenShieldHeadFile.setSourcePath("/templates/driven_shield.h.ftl")
drivenShieldHeadFile.setOutputName("driven_shield.h")
drivenShieldHeadFile.setDestPath("/touch/")
drivenShieldHeadFile.setProjectPath("config/" + configName + "/touch/")
drivenShieldHeadFile.setType("HEADER")
drivenShieldHeadFile.setMarkup(True)
drivenShieldHeadFile.setDependencies(enableDrivenShield,["DS_DEDICATED_ENABLE"])
drivenShieldHeadFile.setDependencies(enableDrivenShield,["DS_PLUS_ENABLE"])

drivenShieldSourceFile = qtouchComponent.createFileSymbol("SOURCE_DRIVENSHIELD", None)
drivenShieldSourceFile.setSourcePath("/templates/driven_shield.c.ftl")
drivenShieldSourceFile.setOutputName("driven_shield.c")
drivenShieldSourceFile.setDestPath("/touch/")
drivenShieldSourceFile.setProjectPath("config/" + configName + "/touch/")
drivenShieldSourceFile.setType("SOURCE")
drivenShieldSourceFile.setMarkup(True)
drivenShieldSourceFile.setDependencies(enableDrivenShield,["DS_DEDICATED_ENABLE"])
drivenShieldSourceFile.setDependencies(enableDrivenShield,["DS_PLUS_ENABLE"])

if (getDeviceName.getDefaultValue() in timer_based_driven_shield_supported_device):
    # Enable Driven Shield SW
    #populate node menu for Driven Shield Plus
    for channelID in range(0, len(touchChannels)):
        touchSym_DS_ADJACENT_TIMER_PIN_Val = qtouchComponent.createKeyValueSetSymbol("DSPLUS_TIMER_PIN"  + str(channelID), touchChannels[channelID])
        touchSym_DS_ADJACENT_TIMER_PIN_Val.setLabel("Selected DS TC/TCC")
        touchSym_DS_ADJACENT_TIMER_PIN_Val.setDisplayMode("Description")
        touchSym_DS_ADJACENT_TIMER_PIN_Val.setDescription("The Timer or Timer counter assigned for Driven shield +")
        touchSym_DS_ADJACENT_TIMER_PIN_Val.addKey("---", "-1", "---")
        
        for tIndex in range(0, len(timersSharingPTC)):
                touchSym_DS_ADJACENT_TIMER_PIN_Val.addKey(timersSharingPTC[tIndex], str(tIndex), timersSharingPTC[tIndex])
        
        touchSym_DS_ADJACENT_TIMER_PIN_MUX_Val = qtouchComponent.createKeyValueSetSymbol("DSPLUS_TIMER_PINMUX"  + str(channelID), touchChannels[channelID])
        touchSym_DS_ADJACENT_TIMER_PIN_MUX_Val.setLabel("DS PIN MUX")
        touchSym_DS_ADJACENT_TIMER_PIN_MUX_Val.setDisplayMode("Description")
        touchSym_DS_ADJACENT_TIMER_PIN_MUX_Val.setDescription("Pin MUX for the selected Y line and the timer")
        touchSym_DS_ADJACENT_TIMER_PIN_MUX_Val.addKey("---", "-1", "---")
        for tIndex in range(0, len(timersSharingPTCMUX)):
                touchSym_DS_ADJACENT_TIMER_PIN_MUX_Val.addKey(timersSharingPTCMUX[tIndex], str(tIndex), timersSharingPTCMUX[tIndex])

    #populate main menu for Driven Shield
    drivenShieldMenu = qtouchComponent.createMenuSymbol("DRIVEN_SHIELD", touchMenu)
    drivenShieldMenu.setLabel("Driven Shield")
    
    global enableDrivenShieldPlus
    enableDrivenShieldPlus = qtouchComponent.createBooleanSymbol("DS_PLUS_ENABLE", drivenShieldMenu)
    enableDrivenShieldPlus.setLabel("Enable Driven Shield Plus")
    enableDrivenShieldPlus.setDefaultValue(False)
    
    global enableDrivenShieldDedicated
    enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_ENABLE", drivenShieldMenu)
    enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
    enableDrivenShieldDedicated.setDefaultValue(False)
    
    drivenShieldDedicatedTimer = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_TIMER", enableDrivenShieldDedicated)
    drivenShieldDedicatedTimer.setLabel("Select Dedicated Timer")
    drivenShieldDedicatedTimer.setDefaultValue(0)
    drivenShieldDedicatedTimer.setDisplayMode("Description")
    #drivenShieldDedicatedTimer.setDependencies(updateDedicatedDSTimer,["DS_DEDICATED_TIMER"])
    drivenShieldDedicatedTimer.addKey("---","0","---")
    
    drivenShieldDedicatedTimerPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_TIMER_PIN", enableDrivenShieldDedicated)
    drivenShieldDedicatedTimerPin.setLabel("Select Dedicated Timer Pin")
    drivenShieldDedicatedTimerPin.setDefaultValue(0)
    drivenShieldDedicatedTimerPin.setDisplayMode("Description")
    drivenShieldDedicatedTimerPin.addKey("---","0","---")
    
    timerInfo = qtouchComponent.createMenuSymbol("TIMER_INFO", touchInfoMenu)
    timerInfo.setLabel("Timer info")
    
    drivenShieldPlusApply = qtouchComponent.createStringSymbol("DS_TIMER_APPLY", timerInfo)
    drivenShieldPlusApply.setLabel("Apply Driven Shield Timers ")
    drivenShieldPlusApply.setReadOnly(True)
    drivenShieldPlusApply.setDependencies(applyDrivenShieldTimers,["DS_TIMER_APPLY"])
        
    #tcInstancesNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]")
    #tcInstances = []
    #tcInstances = tcInstancesNode.getChildren()
    tindex, pindex = 0, 0
    for index in range(0, len(tcInstances)):
        tctimer = tcInstances[index].getAttribute("name")
        drivenShieldDedicatedTimer.addKey(tctimer,str(tindex+1),tctimer)
        tindex+=1
        #create timer info group
        timerMenu = qtouchComponent.createMenuSymbol(tctimer, timerInfo)
        timerMenu.setLabel(tctimer)
        #create signal info
        timerSignal = qtouchComponent.createKeyValueSetSymbol(tctimer+"_SIGNAL", timerMenu)
        timerSignal.setLabel("Signal")
        timerMux = qtouchComponent.createKeyValueSetSymbol(tctimer+"_Mux", timerMenu)
        timerMux.setLabel("Mux")
        timerMuxYpin = qtouchComponent.createKeyValueSetSymbol(tctimer+"_Ypin", timerMenu)
        timerMuxYpin.setLabel("Ypin")
    
        tcSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+ tctimer +"\"]/signals")
        if getDeviceName.getDefaultValue() in adc_based_touch_acqusition_device:
          tcptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/signals")
        else:
          tcptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/parameters")
        tcptcSignals = []
        tcptcSignals = tcptcPinNode.getChildren()
        tcSignals = []
        tcSignals = tcSignalNode.getChildren()
        timerPins = []
        for sindex in range(0, len(tcSignals)):
            timermux = "MUX_"+tcSignals[sindex].getAttribute("pad")+tcSignals[sindex].getAttribute("function")+"_"+tctimer+"_"+tcSignals[sindex].getAttribute("group")+tcSignals[sindex].getAttribute("index")
            timerMux.addKey(timermux, str(sindex), timermux)
            timerPin = tcSignals[sindex].getAttribute("pad")+tcSignals[sindex].getAttribute("function")+"_"+tctimer+"_"+tcSignals[sindex].getAttribute("group")+tcSignals[sindex].getAttribute("index")
            timerSignal.addKey(timerPin, str(sindex), timerPin)
            drivenShieldDedicatedTimerPin.addKey(timerPin,str(pindex+1),timerPin)
            for cnt in range (0, len(tcptcSignals)):
                if tcptcSignals[cnt].getAttribute("pad") == tcSignals[sindex].getAttribute("pad"):
                    tempstring = "Y("+tcptcSignals[cnt].getAttribute("index")+")"
                    timerMuxYpin.addKey(tempstring, str(sindex) ,tempstring)
                    break;
            pindex+= 1
        
        timerClock = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+ tctimer +"\"]/parameters/param@[name=\"GCLK_ID\"]")
        clockIndex = qtouchComponent.createStringSymbol(tctimer+"_CLOCK_INDEX", timerMenu)
        clockIndex.setLabel("Clock Index ")
        clockIndex.setReadOnly(True)
        clockIndex.setDefaultValue("GCLK_ID_"+timerClock.getAttribute("value")+"_GENSEL")
        
        timertUser = ATDF.getNode("/avr-tools-device-file/devices/device/events/users/user@[name=\""+ tctimer +"_EVU\"]")
        eventUser = qtouchComponent.createStringSymbol(tctimer+"_EVENT_USER", timerMenu)
        eventUser.setLabel("Event User ")
        eventUser.setReadOnly(True)
        eventUser.setDefaultValue("EVSYS_USER_"+timertUser.getAttribute("index"))
            
    #tccInstancesNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]")
    #tccInstances = []
    #tccInstances = tccInstancesNode.getChildren()
    for index in range(0, len(tccInstances)):
        tcctimer = tccInstances[index].getAttribute("name")
        drivenShieldDedicatedTimer.addKey(tcctimer,str(tindex+1),tcctimer)
        tindex+=1
        #create timer info group
        timerMenu = qtouchComponent.createMenuSymbol(tcctimer, timerInfo)
        timerMenu.setLabel(tcctimer)
        #create signal info
        timerSignal = qtouchComponent.createKeyValueSetSymbol(tcctimer+"_SIGNAL", timerMenu)
        timerSignal.setLabel("Signal")
        
        tccSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+ tcctimer +"\"]/signals")
        tccSignals = []
        tccSignals = tccSignalNode.getChildren()
        timerPins = []
        for sindex in range(0, len(tccSignals)):
            timerPin = tccSignals[sindex].getAttribute("pad")+"("+tccSignals[sindex].getAttribute("group")+"/"+tccSignals[sindex].getAttribute("index")+")"
            timerSignal.addKey(timerPin, str(sindex), timerPin)
            drivenShieldDedicatedTimerPin.addKey(timerPin,str(pindex+1),timerPin)
            pindex+= 1

        timerClock = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+ tcctimer +"\"]/parameters/param@[name=\"GCLK_ID\"]")
        clockIndex = qtouchComponent.createStringSymbol(tcctimer+"_CLOCK_INDEX", timerMenu)
        clockIndex.setLabel("Clock Index ")
        clockIndex.setReadOnly(True)
        clockIndex.setDefaultValue("GCLK_ID_"+timerClock.getAttribute("value")+"_GENSEL")
        
        timertUser = ATDF.getNode("/avr-tools-device-file/devices/device/events/users/user@[name=\""+ tcctimer +"_EV_0\"]")
        eventUser = qtouchComponent.createStringSymbol(tcctimer+"_EVENT_USER", timerMenu)
        eventUser.setLabel("Event User ")
        eventUser.setReadOnly(True)
        eventUser.setDefaultValue("EVSYS_USER_"+timertUser.getAttribute("index"))