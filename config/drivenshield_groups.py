"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
import target_device
import node_groups
global Database

#group
def initDrivenShieldGroup(ATDF,qtouchComponent,touchMenu,touchInfoMenu,minGroupCount,maxGroupCount,touchChannelMutual,ptcPininfo,shieldMode):    
    """Initialise Driven Shield Groups and add to touch Module
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :qtouchComponent : touchModule
        :touchMenu : parent menu symbol for added menu items
        :touchInfoMenu : 2nd parent menu for timers
        :minGroupCount : see acquisitionGroupCountMenu.getMin()
        :maxGroupCount : see acquisitionGroupCountMenu.getMax()
        :touchChannelMutual : see target_device.getMutualCount()
        :targetDevice : see interface.getDeviceSeries()
        :ptcPinValues : see target_device.setDevicePinValues()
        :shieldMode : see target_device.getShieldMode()
    Returns:
        :none
    """
    ptcYPads = []
    for index in range(0, len(ptcPininfo)):
        if(ptcPininfo[index].getAttribute("group") == "Y"):
            ptcYPads.append(ptcPininfo[index].getAttribute("pad"))
    
    tcSignals =[]
    tcInstances = getTCTimers(ATDF)
    if(tcInstances is not None):
        tcSignals = getTCTimersSignals(ATDF,tcInstances)
    tccSignals =[]
    tccInstances = getTCCTimers(ATDF)
    if(tccInstances is not None):    
        tccSignals = getTCCTimersSignals(ATDF,tccInstances)

    timersSharingPTC = []
    timersSharingPTCMUX = []
    timersSharingPTC = getTimersSharingPTC(qtouchComponent,tcInstances,tcSignals,timersSharingPTC,ptcYPads)
    timersSharingPTCMUX = getTimersSharingPTCMUX(qtouchComponent,tcInstances,tcSignals,timersSharingPTCMUX,ptcYPads)
    # --------------

    timerInfo = qtouchComponent.createMenuSymbol("TIMER_INFO", touchInfoMenu)
    timerInfo.setLabel("Timer info")

    enabledrivenShieldMenu = qtouchComponent.createBooleanSymbol("ENABLE_DRIVEN_SHIELD", touchMenu)
    enabledrivenShieldMenu.setLabel("Enable Driven Shield")
    enabledrivenShieldMenu.setDefaultValue(False)
    enabledrivenShieldMenu.setDescription("DS.")
    enabledrivenShieldMenu.setVisible(True)
    enabledrivenShieldMenu.setEnabled(False)
    enabledrivenShieldMenu.setDependencies(drivenShieldUpdateEnabled,["ENABLE_DRIVEN_SHIELD"])

    for groupNum in range (minGroupCount,maxGroupCount+1):
        if groupNum == 1:
            drivenShieldMenu = qtouchComponent.createMenuSymbol("DRIVEN_SHIELD_MENU", enabledrivenShieldMenu)
            drivenShieldMenu.setLabel("Driven Shield Configuration")
            drivenShieldMenu.setVisible(False)
            drivenShieldMenu.setEnabled(False)
            initDrivenShieldInstance(
                ATDF,qtouchComponent,groupNum,drivenShieldMenu,
                timerInfo,touchMenu,touchChannelMutual,ptcPininfo,
                tcInstances,tccInstances,timersSharingPTC,timersSharingPTCMUX,tcSignals,tccSignals,shieldMode)
        else:
            dynamicName = "drivenShieldMenu_"+str(groupNum) 
            dynamicId = "DRIVEN_SHIELD_MENU_" +str(groupNum) 
            vars()[dynamicName] = qtouchComponent.createMenuSymbol(dynamicId, enabledrivenShieldMenu)
            vars()[dynamicName].setLabel("Driven Shield Configuration Group"+str(groupNum))
            vars()[dynamicName].setVisible(False)
            vars()[dynamicName].setEnabled(False)
            initDrivenShieldInstance(
                ATDF,qtouchComponent,groupNum, vars()[dynamicName],timerInfo,
                touchMenu,touchChannelMutual,ptcPininfo,tcInstances,tccInstances,
                timersSharingPTC,timersSharingPTCMUX,tcSignals,tccSignals,shieldMode)
    
def initDrivenShieldInstance(
    ATDF,qtouchComponent,groupNumber,parentLabel, 
    timerInfo, touchMenu, touchChannelMutual, ptcPininfo, 
    tcInstances, tccInstances,timersSharingPTC, timersSharingPTCMUX,
    tcSignals,tccSignals,shieldMode):
    """Initialise Driven Shield Instance
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :qtouchComponent : touchModule
        :groupNumber : index of the group instance
        :parentLabel : parent symbol for for added menu items
        :timerInfo : perent sysmbol for timer information
        :touchMenu : touchMenu
        :touchChannelMutual : see target_device.getMutualCount()
        :ptcPininfo : see <target_device.setDevicePinValues()>
        :tcInstances : see getTCTimers()
        :tccInstances : see getTCCTimers()
        :timersSharingPTC : see getTimersSharingPTC()
        :timersSharingPTCMUX: see getTimersSharingPTCMUX()
        :tcSignals : see getTCTimersSignals()
        :tccSignals : see= getTCCTimersSignals()
        :shieldMode : see target_device.getShieldMode()
    Returns:
        :none
    """
    if (groupNumber == 1):
        if(shieldMode == "hardware"):
            enableDrivenShieldAdjacent = qtouchComponent.createBooleanSymbol("DS_ADJACENT_SENSE_LINE_AS_SHIELD", parentLabel)
            enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_PIN_ENABLE", parentLabel)
            drivenShieldDedicatedPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_PIN", enableDrivenShieldDedicated)
            enableDrivenShieldAdjacent.setLabel("Enable Adjacent Sense Pins as Shield")
            enableDrivenShieldAdjacent.setDefaultValue(False)
            enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
            enableDrivenShieldDedicated.setDefaultValue(False)
            setDSDedicatedPins(drivenShieldDedicatedPin,ptcPininfo)
    else:
        if(shieldMode == "hardware"):
            enableDrivenShieldAdjacent = qtouchComponent.createBooleanSymbol("DS_ADJACENT_SENSE_LINE_AS_SHIELD_"+str(groupNumber), parentLabel)
            enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_PIN_ENABLE_"+str(groupNumber), parentLabel)
            drivenShieldDedicatedPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_PIN_"+str(groupNumber), enableDrivenShieldDedicated)
            enableDrivenShieldAdjacent.setLabel("Enable Adjacent Sense Pins as Shield")
            enableDrivenShieldAdjacent.setDefaultValue(False)
            enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
            enableDrivenShieldDedicated.setDefaultValue(False)
            setDSDedicatedPins(drivenShieldDedicatedPin,ptcPininfo)


def setDSDedicatedPins(drivenShieldDedicatedPin,ptcPininfo):
    """Populate the driven shield dedicated Table
    Arguments:
        :drivenShieldDedicatedPin : symbol to be populated
        :ptcPininfo : see target_device.setDevicePinValues() 
    Returns:
        none
    """
    drivenShieldDedicatedPin.setLabel("Select Dedicated Driven Shield Pin")
    drivenShieldDedicatedPin.setDisplayMode("Description")
    for index in range(0, len(ptcPininfo)):
        if(ptcPininfo[index].getAttribute("group") == "Y"):
            drivenShieldDedicatedPin.addKey(
                ptcPininfo[index].getAttribute("index"),ptcPininfo[index].getAttribute("group")+"("+ptcPininfo[index].getAttribute("index")+")",
                ptcPininfo[index].getAttribute("group")+ptcPininfo[index].getAttribute("index")+ "  ("+ ptcPininfo[index].getAttribute("pad")+")")

def getTCTimers(ATDF):
    """Retrieve TC timers from device ATDF
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
    Returns:
        :list of TCTimer
    """
    tcInstancesNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]")
    if (tcInstancesNode is not None):
        return tcInstancesNode.getChildren()
    else:
        return []

def getTCCTimers(ATDF):
    """Retrieve TCC timers from device ATDF
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
    Returns:
        :list of TCCTimer
    """
    tccInstancesNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]")
    if (tccInstancesNode is not None):
        return tccInstancesNode.getChildren()
    else:
        return []

def getTCTimersSignals(ATDF,tcInstances):
    """Retrieve TC signals from each TC peripheral.
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :tcInstances : see getTCTimers()
    Returns:
        :list of TCTimer signals
    """
    for indexI in range(0, len(tcInstances)):
        tcSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+ tcInstances[indexI].getAttribute("name") +"\"]/signals")
        if (tcSignalNode is not None):
            return tcSignalNode.getChildren()
        else:
            return []

def getTCCTimersSignals(ATDF,tccInstances):
    """Retrieve TC signals from each TC peripheral.
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :tccInstances : see getTCTimers()
    Returns:
        :list of TCCTimer signals
    """
    for indexI in range(0, len(tccInstances)):
        tccSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+ tccInstances[indexI].getAttribute("name") +"\"]/signals")
        if (tccSignalNode is not None):
            return tccSignalNode.getChildren()
        else:
            return []

def getTimersSharingPTCMUX(qtouchComponent,tcInstances,tcSignals,timersSharingPTCMUX,ptcYPads):
    """Retrieve a list of strings containing both timer and PTC pin information .
    Arguments:
        :qtouchComponent : touchModule
        :tcInstances : see getTCTimers()
        :tcSignals : see getTCTimersSignals()
        :timersSharingPTCMUX : see getTimersSharingPTCMUX()
        :ptcYPads : Y Pads extracted from ptcPinValues
    Returns:
        :list of timer and PTC multiplexed pins including pad,function,groupindex
    """
    for indexI in range(0, len(tcInstances)):
        for indexS in range(0, len(tcSignals)):
            timer = tcInstances[indexI].getAttribute("name")
            qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
            qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
            if tcSignals[indexS].getAttribute("pad") in ptcYPads:
                string = tcSignals[indexS].getAttribute("pad")+tcSignals[indexS].getAttribute("function")+"_"+timer+"_"+tcSignals[indexS].getAttribute("group")+tcSignals[indexS].getAttribute("index")
                timersSharingPTCMUX.append(string)
        return timersSharingPTCMUX

def getTimersSharingPTC(qtouchComponent,tcInstances,tcSignals,timersSharingPTC,ptcYPads):
    """Retrieve a list of pads multiplexed between timer and PTC.
    Arguments:
        :qtouchComponent : touchModule
        :tcInstances : see getTCTimers()
        :tcSignals : see getTCTimersSignals()
        :timersSharingPTCMUX : see getTimersSharingPTCMUX()
        :ptcYPads : Y Pads extracted from ptcPinValues
    Returns:
        :list of timer and PTC multiplexed pins by pad
    """
    for indexI in range(0, len(tcInstances)):
        for indexS in range(0, len(tcSignals)):
            timer = tcInstances[indexI].getAttribute("name")
            qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
            qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
            if tcSignals[indexS].getAttribute("pad") in ptcYPads:
                timersSharingPTC.append(timer)
    return timersSharingPTC

def drivenShieldUpdateEnabled(symbol,event):
    """Enables Driven Shield functionality.
    Arguments:
        :symbol : the symbol that triggered the callback
        :event : the new value. 
    Returns:
        :none
    """
    component= symbol.getComponent()
    currentVal = bool(event['symbol'].getValue())
    maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getValue()
    minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()
    for x in range(minVal,maxVal+1):
        if(x == minVal):
            grpId = "DRIVEN_SHIELD_MENU"
        else:
            grpId = "DRIVEN_SHIELD_MENU_" +str(x)
        component.getSymbolByID(grpId).setEnabled(currentVal)
        component.getSymbolByID(grpId).setVisible(currentVal)


#updater
def updateDrivenShieldGroups(symbol, event):
    """Handler for number of driven shield groups being used. 
    Triggered by qtouch.updateGroupsCounts(symbol,event)
    Arguments:
        :symbol : the symbol that triggered the callback
        :event : the new value. 
    Returns:
        :none
    """
    component= symbol.getComponent()
    currentVal = int(event['symbol'].getValue())
    maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMax()
    minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()   
    for x in range(minVal+1,maxVal+1):
        grpId = "DRIVEN_SHIELD_MENU_" +str(x)
        component.getSymbolByID(grpId).setEnabled(False)
        component.getSymbolByID(grpId).setVisible(False)
        if(currentVal >= x):
            component.getSymbolByID(grpId).setEnabled(True)
            component.getSymbolByID(grpId).setVisible(True)
    
    updateDSTimersMenu(symbol,event)

def updateDSTimersMenu(symbol,event):
    """Updates Driven shield timers. Triggered by updateDrivenShieldGroups.
    Arguments:
        :symbol : the symbol that triggered the callback
        :event : the new value. 
    Returns:
        :none
    """
    component= symbol.getComponent()
    currentVal = int(event['symbol'].getValue())
    maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMax()
    minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()
    for x in range(minVal+1,maxVal+1):
        # dsDedicatedTimer = "DS_DEDICATED_ENABLE_" +str(x)
        dsTimer = "DS_TIMER_APPLY_" +str(x)
        component.getSymbolByID(dsTimer).setEnabled(False)
        component.getSymbolByID(dsTimer).setVisible(False)
        if(currentVal >= x):
            component.getSymbolByID(dsTimer).setEnabled(True)
            component.getSymbolByID(dsTimer).setVisible(True)

def updateLumpModeDrivenShield(symbol,event,totalChannelCount,lump_symbol):
    """Handler for lump mode support menu click event.  
    Triggered by qtouch.processLump()
    Arguments:
        :symbol : the symbol that triggered the event
        :event : new value of the symbol 
        :totalChannelCount : see target_device.getMutualCount()
        :lump_feature : lump configuration
    Returns:
        :none
    """
    print("Updating shield lumps")
    component= symbol.getComponent()
    currentVal = int(event['symbol'].getValue())
    enableDrivenShieldAdjacent = component.getSymbolByID("DS_ADJACENT_SENSE_LINE_AS_SHIELD")
    enableDrivenShieldDedicated = component.getSymbolByID("DS_DEDICATED_PIN_ENABLE")
    drivenShieldDedicatedPin = component.getSymbolByID("DS_DEDICATED_PIN").getValue()
    
    tchSelfPinSelection = node_groups.getTchSelfPinSelection()
    tchMutXPinSelection = node_groups.getTchMutXPinSelection()

    for i in range(0,totalChannelCount):
        if((enableDrivenShieldAdjacent == True) or (enableDrivenShieldDedicated == True)):
            print("TRUE TRUE")
            shieldPins = []
            if (enableDrivenShieldDedicated == True):
                shieldY = drivenShieldDedicatedPin.getValue()
                shieldY = drivenShieldDedicatedPin.getKeyValue(shieldY)
                shieldPins.append(shieldY)
                print ("Dedicated Shield pins = "+ str(shieldPins))

            if (enableDrivenShieldAdjacent == True):
                lump_feature = lump_symbol.getValue()
                if (lump_feature != ""):
                    LUMP_INDI = lump_feature.split(";")
                    LUMP_NUM = len(LUMP_INDI)
                    input0 =[]
                    for a in range(0,(totalChannelCount-LUMP_NUM)):
                        value = tchSelfPinSelection[int(a)].getValue()
                        input0.append(tchSelfPinSelection[int(a)].getKeyValue(value))
                    if (i < totalChannelCount-LUMP_NUM):
                        for j in range(0,(totalChannelCount-LUMP_NUM)):
                            value1 = tchSelfPinSelection[int(i)].getValue()
                            if ((tchSelfPinSelection[int(i)].getKeyValue(value1)) != input0[j]):
                                shieldPins.append(input0[j])
                    else:
                        LUMP_NODE_VAL = tchSelfPinSelection[int(i)].getValue()
                        LUMP_NODE_INDI = tchSelfPinSelection[int(i)].getKeyValue(LUMP_NODE_VAL).split("|")
                        LUMP_NODE_SIZE = len(LUMP_NODE_INDI)
                        for j in range(0,(totalChannelCount-LUMP_NUM)):
                            par = 0
                            for y in range(0,LUMP_NODE_SIZE):
                                if (LUMP_NODE_INDI[y] == input0[j]):
                                    par = 1
                            if par == 0:
                                shieldPins.append(input0[j])
                else:
                    for j in range(0,totalChannelCount):
                        if (i != j):
                            shildY = tchSelfPinSelection[int(j)].getValue()
                            shieldY = tchSelfPinSelection[int(j)].getKeyValue(shildY)
                            shieldPins.append(shieldY)
                            print ("Adjacent Shield pins = "+ str(shieldPins))
            if(shieldPins != []):
                drivenPin = "|".join(shieldPins)
                print ("Drive pins = "+ str(drivenPin))
            else:
                drivenPin = "X_NONE"
                print ("Drive pins = NONE")
            tchMutXPinSelection[int(i)].setKeyValue(str(i),drivenPin)
            tchMutXPinSelection[int(i)].setValue(int(i))

    node_groups.setTchSelfPinSelection(tchSelfPinSelection)
    node_groups.setTchMutXPinSelection(tchMutXPinSelection)
'''    

def setDSNodesMenu(ATDF,groupNumber,qtouchComponent,touchMenu,touchChannelMutual,ptcPinValues,tcInstances,tccInstances,timersSharingPTC, timersSharingPTCMUX):
    """Populate the driven shield settings in the nodes group menus 
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :groupNumber : index of the group instance
        :qtouchComponent : touchModule
        :touchMenu : touchMenu
        :touchChannelMutual : see target_device.getMutualCount() 
        :ptcPinValues : see target_device.setDevicePinValues()
        :tcInstances : see getTCTimers()
        :tccInstances : see getTCCTimers()
        :timersSharingPTC : see getTimersSharingPTC()
        :timersSharingPTCMUX: see getTimersSharingPTCMUX()
    Returns:
        none
    """
    nodesMenuArray =[]
    if groupNumber == 1:
        for idx in range (0 ,touchChannelMutual):
            nodesMenuArray.append(touchMenu.getComponent().getSymbolByID("TOUCH_ENABLE_CH_"+str(idx)))
        
        for channelID in range(0, len(nodesMenuArray)):
            dsAdjacentTimerPinValue = qtouchComponent.createKeyValueSetSymbol("DSPLUS_TIMER_PIN"  + str(channelID), nodesMenuArray[channelID])
            dsAdjacentTimerPinValue.setLabel("Selected DS TC/TCC")
            dsAdjacentTimerPinValue.setDisplayMode("Description")
            dsAdjacentTimerPinValue.setDescription("The Timer or Timer counter assigned for Driven shield +")
            dsAdjacentTimerPinValue.addKey("---", "-1", "---")        
            for tIndex in range(0, len(timersSharingPTC)):
                dsAdjacentTimerPinValue.addKey(timersSharingPTC[tIndex], str(tIndex), timersSharingPTC[tIndex])
            
            dsAdjacentTimerPinMuxValue = qtouchComponent.createKeyValueSetSymbol("DSPLUS_TIMER_PINMUX"  + str(channelID), nodesMenuArray[channelID])
            dsAdjacentTimerPinMuxValue.setLabel("DS PIN MUX")
            dsAdjacentTimerPinMuxValue.setDisplayMode("Description")
            dsAdjacentTimerPinMuxValue.setDescription("Pin MUX for the selected Y line and the timer")
            dsAdjacentTimerPinMuxValue.addKey("---", "-1", "---")
            for tIndex in range(0, len(timersSharingPTCMUX)):
                dsAdjacentTimerPinMuxValue.addKey(timersSharingPTCMUX[tIndex], str(tIndex), timersSharingPTCMUX[tIndex])
    else:
        for idx in range (0 ,touchChannelMutual):
            nodesMenuArray.append(touchMenu.getComponent().getSymbolByID("GROUP_"+str(groupNumber)+"_TOUCH_ENABLE_CH_"+str(idx)))

        for channelID in range(0, len(nodesMenuArray)):
            dsAdjacentTimerPinValue = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DSPLUS_TIMER_PIN"  + str(channelID), nodesMenuArray[channelID])
            dsAdjacentTimerPinValue.setLabel("Selected DS TC/TCC")
            dsAdjacentTimerPinValue.setDisplayMode("Description")
            dsAdjacentTimerPinValue.setDescription("The Timer or Timer counter assigned for Driven shield +")
            dsAdjacentTimerPinValue.addKey("---", "-1", "---")        
            for tIndex in range(0, len(timersSharingPTC)):
                dsAdjacentTimerPinValue.addKey(timersSharingPTC[tIndex], str(tIndex), timersSharingPTC[tIndex])

            dsAdjacentTimerPinMuxValue = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DSPLUS_TIMER_PINMUX"  + str(channelID), nodesMenuArray[channelID])
            dsAdjacentTimerPinMuxValue.setLabel("DS PIN MUX")
            dsAdjacentTimerPinMuxValue.setDisplayMode("Description")
            dsAdjacentTimerPinMuxValue.setDescription("Pin MUX for the selected Y line and the timer")
            dsAdjacentTimerPinMuxValue.addKey("---", "-1", "---")
            for tIndex in range(0, len(timersSharingPTCMUX)):
                dsAdjacentTimerPinMuxValue.addKey(timersSharingPTCMUX[tIndex], str(tIndex), timersSharingPTCMUX[tIndex])

   


def applyDrivenShieldTimers(symbol, event):
    """apply driven shield timers. Triggered by Driven shield plus application.
    Arguments:
        :symbol : the symbol that triggered the callback
        :event : the new value. 
    Returns:
        :none
    """    
    print("---------Entering apply DSTimers----------")
    global Database
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
    print("---------Leaving apply DSTimers----------")






'''