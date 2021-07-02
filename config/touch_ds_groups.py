"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

#import runtime

class classTouchDSGroup():
    def __init__(self, node_inst, targetdevice_inst):
        self.nodeInst = node_inst
        self.targetDeviceInst = targetdevice_inst
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def initDrivenShieldGroup(self,instances,ATDF,qtouchComponent,touchMenu,touchInfoMenu,minGroupCount,maxGroupCount,touchChannelMutual,ptcPininfo,shieldMode):
        """Initialise Driven Shield Groups and add to touch Module
        Arguments:
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :qtouchComponent : touchModule
            :touchMenu : parent menu symbol for added menu items
            :touchInfoMenu : 2nd parent menu for timers
            :minGroupCount : see acquisitionGroupCountMenu.getMin()
            :maxGroupCount : see acquisitionGroupCountMenu.getMax()
            :touchChannelMutual : see self.targetDeviceInst.getMutualCount()
            :targetDevice : see interface.getDeviceSeries()
            :ptcPinValues : see self.targetDeviceInst.setDevicePinValues()
            :shieldMode : see self.targetDeviceInst.getShieldMode()
        Returns:
            :none
        """
        if shieldMode == "hardware":
            drivenShieldMenu = qtouchComponent.createMenuSymbol("DRIVEN_SHIELD", touchMenu)
            drivenShieldMenu.setLabel("Driven Shield")
            enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_PIN_ENABLE", drivenShieldMenu)
            enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
            enableDrivenShieldDedicated.setDefaultValue(False)

            drivenShieldDedicatedPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_PIN", enableDrivenShieldDedicated)
            drivenShieldDedicatedPin.setLabel("Select Dedicated Driven Shield Pin")
            drivenShieldDedicatedPin.setOutputMode("Value")
            drivenShieldDedicatedPin.setDefaultValue(0)
            drivenShieldDedicatedPin.setDisplayMode("Description")

            if instances['interfaceInst'].getDeviceSeries() not in instances['target_deviceInst'].picDevices:
                enableDrivenShieldAdjacent = qtouchComponent.createBooleanSymbol("DS_ADJACENT_SENSE_LINE_AS_SHIELD", drivenShieldMenu)
                enableDrivenShieldAdjacent.setLabel("Enable Adjacent Sense Pins as Shield")
                enableDrivenShieldAdjacent.setDefaultValue(False)

                for index in range(0, len(ptcPininfo)):
                    if(ptcPininfo[index].getAttribute("group") == "Y"):
                        drivenShieldDedicatedPin.addKey(ptcPininfo[index].getAttribute("index"),ptcPininfo[index].getAttribute("group")+"("+ptcPininfo[index].getAttribute("index")+")",ptcPininfo[index].getAttribute("group")+ptcPininfo[index].getAttribute("index")+ "  ("+ ptcPininfo[index].getAttribute("pad")+")")
            else:
                dsPins = ptcPininfo[1]
                for index in range(0, len(dsPins)):
                    drivenShieldDedicatedPin.addKey("X("+str(index)+")",
                    str(index),
                    "X"+str(index)+"  ("+dsPins[index]+")")

        else:

            ptcYPads = []
            for index in range(0, len(ptcPininfo)):
                if(ptcPininfo[index].getAttribute("group") == "Y"):
                    ptcYPads.append(ptcPininfo[index].getAttribute("pad"))
            
            tcInstances = self.getTCTimers(ATDF)
            tccInstances = self.getTCCTimers(ATDF)
            timersSharingPTC = self.getTimersSharingPTC(qtouchComponent,tcInstances,tccInstances,ATDF,ptcYPads)
            timersSharingPTCMUX  = self.getTimersSharingPTCMux(qtouchComponent,tcInstances,tccInstances,ATDF,ptcYPads)


            # --------------
            timerInfo = qtouchComponent.createMenuSymbol("TIMER_INFO", touchInfoMenu)
            timerInfo.setLabel("Timer info")
            drivenShieldPlusApply = qtouchComponent.createStringSymbol("DS_TIMER_APPLY", timerInfo)
            drivenShieldPlusApply.setLabel("Apply Driven Shield Timers ")
            drivenShieldPlusApply.setReadOnly(True)
            self.addDepSymbol(drivenShieldPlusApply, "applyDrivenShieldTimers", ["DS_TIMER_APPLY"])

            enabledrivenShieldMenu = qtouchComponent.createBooleanSymbol("ENABLE_DRIVEN_SHIELD", touchMenu)
            enabledrivenShieldMenu.setLabel("Enable Driven Shield")
            enabledrivenShieldMenu.setDefaultValue(False)
            enabledrivenShieldMenu.setDescription("DS.")
            enabledrivenShieldMenu.setVisible(True)
            enabledrivenShieldMenu.setDependencies(self.drivenShieldUpdateEnabled,["ENABLE_DRIVEN_SHIELD"])

            for groupNum in range (minGroupCount,maxGroupCount+1):
                if groupNum == 1:
                    drivenShieldMenu = qtouchComponent.createMenuSymbol("DRIVEN_SHIELD_MENU", enabledrivenShieldMenu)
                    drivenShieldMenu.setLabel("Driven Shield Configuration")
                    self.initDrivenShieldInstance(instances,
                        ATDF,qtouchComponent,groupNum,drivenShieldMenu,
                        timerInfo,touchMenu,touchChannelMutual,ptcPininfo,
                        tcInstances,tccInstances,timersSharingPTC,timersSharingPTCMUX,shieldMode)
                else:
                    dynamicName = "drivenShieldMenu_"+str(groupNum) 
                    dynamicId = "DRIVEN_SHIELD_MENU_" +str(groupNum) 
                    vars()[dynamicName] = qtouchComponent.createMenuSymbol(dynamicId, enabledrivenShieldMenu)
                    vars()[dynamicName].setLabel("Driven Shield Configuration Group"+str(groupNum))
                    vars()[dynamicName].setVisible(False)
                    vars()[dynamicName].setEnabled(False)
                    self.initDrivenShieldInstance(instances,
                        ATDF,qtouchComponent,groupNum, vars()[dynamicName],timerInfo,
                        touchMenu,touchChannelMutual,ptcPininfo,tcInstances,tccInstances,
                        timersSharingPTC,timersSharingPTCMUX,shieldMode)

    def initDrivenShieldInstance(self,instances,
        ATDF,qtouchComponent,groupNumber,parentLabel, 
        timerInfo, touchMenu, touchChannelMutual, ptcPininfo, 
        tcInstances, tccInstances,timersSharingPTC, timersSharingPTCMUX,
        shieldMode):
        """Initialise Driven Shield Instance
        Arguments:
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :qtouchComponent : touchModule
            :groupNumber : index of the group instance
            :parentLabel : parent symbol for for added menu items
            :timerInfo : perent sysmbol for timer information
            :touchMenu : touchMenu
            :touchChannelMutual : see self.targetDeviceInst.getMutualCount()
            :ptcPininfo : see <self.targetDeviceInst.setDevicePinValues()>
            :tcInstances : see getTCTimers()
            :tccInstances : see getTCCTimers()
            :timersSharingPTC : see getTimersSharingPTC()
            :timersSharingPTCMUX: see getTimersSharingPTCMUX()
            :shieldMode : see self.targetDeviceInst.getShieldMode()
        Returns:
            :none
        """
        if (groupNumber == 1):
            enableDrivenShieldPlus = qtouchComponent.createBooleanSymbol("DS_PLUS_ENABLE", parentLabel)
            enableDrivenShieldPlus.setLabel("Enable Driven Shield Plus")
            enableDrivenShieldPlus.setDefaultValue(False)

            enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_ENABLE", parentLabel)
            enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
            enableDrivenShieldDedicated.setDefaultValue(False)

            drivenShieldDedicatedTimer = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_TIMER", enableDrivenShieldDedicated)
            self.setDSTimers(drivenShieldDedicatedTimer)
            
            drivenShieldDedicatedTimerPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_TIMER_PIN", enableDrivenShieldDedicated)
            self.setDSDedicatedTimerPins(instances,drivenShieldDedicatedTimerPin,ptcPininfo)

            self.setTimerInfoGroup(qtouchComponent,timerInfo,tcInstances,tccInstances,drivenShieldDedicatedTimer,drivenShieldDedicatedTimerPin,ptcPininfo,ATDF)
            if(shieldMode ==  "timer"):
                self.setDSNodesMenu(groupNumber,qtouchComponent,touchMenu,touchChannelMutual,timersSharingPTC, timersSharingPTCMUX)

        else:
            enableDrivenShieldPlus = qtouchComponent.createBooleanSymbol("DS_PLUS_ENABLE_"+str(groupNumber), parentLabel)
            enableDrivenShieldPlus.setLabel("Enable Driven Shield Plus")
            enableDrivenShieldPlus.setDefaultValue(False)
            enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_PIN_ENABLE_"+str(groupNumber), parentLabel)
            enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
            enableDrivenShieldDedicated.setDefaultValue(False)            
            drivenShieldDedicatedTimerPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_PIN_"+str(groupNumber), enableDrivenShieldDedicated)
            self.setDSDedicatedTimerPins(instances,drivenShieldDedicatedTimerPin,ptcPininfo)

    def setDSTimers(self,drivenShieldDedicatedTimer):
        drivenShieldDedicatedTimer.setLabel("Select Dedicated Timer")
        drivenShieldDedicatedTimer.setDefaultValue(0)
        drivenShieldDedicatedTimer.setDisplayMode("Description")
        drivenShieldDedicatedTimer.addKey("---","0","---")

    def setDSDedicatedTimerPins(self,instances,drivenShieldDedicatedPin,ptcPininfo):
        """Populate the driven shield dedicated Table
        Arguments:
            :drivenShieldDedicatedPin : symbol to be populated
            :ptcPininfo : see self.targetDeviceInst.setDevicePinValues() 
        Returns:
            none
        """
        if instances['interfaceInst'].getDeviceSeries() in instances['target_deviceInst'].picDevices:
            drivenShieldDedicatedPin.setLabel("Select Dedicated Driven Shield Pin")
            drivenShieldDedicatedPin.setDisplayMode("Description")
            for index in range(0, len(ptcPininfo)):
                if(ptcPininfo[index].getAttribute("group") == "Y"):
                    drivenShieldDedicatedPin.addKey(
                        ptcPininfo[index].getAttribute("index"),ptcPininfo[index].getAttribute("group")+"("+ptcPininfo[index].getAttribute("index")+")",
                        ptcPininfo[index].getAttribute("group")+ptcPininfo[index].getAttribute("index")+ "  ("+ ptcPininfo[index].getAttribute("pad")+")")

    def setTimerInfoGroup(self,qtouchComponent,timerInfo,tcInstances,tccInstances,drivenShieldDedicatedTimer,drivenShieldDedicatedTimerPin,ptcPininfo,ATDF):
        tindex, pindex = 0, 0
        
        for index in range(0, len(tcInstances)):
            tctimer = tcInstances[index].getAttribute("name")
            drivenShieldDedicatedTimer.addKey(tctimer,str(tindex+1),tctimer)
            tindex+=1
            #create timer info group
            timerMenu = qtouchComponent.createMenuSymbol(tctimer, timerInfo)
            timerMenu.setLabel(tctimer)
            #create signal info
            tcTimerSignal = qtouchComponent.createKeyValueSetSymbol(tctimer+"_SIGNAL", timerMenu)
            tcTimerSignal.setLabel("Signal")
            tcTimerMux = qtouchComponent.createKeyValueSetSymbol(tctimer+"_Mux", timerMenu)
            tcTimerMux.setLabel("Mux")
            tcTimerMuxYpin = qtouchComponent.createKeyValueSetSymbol(tctimer+"_Ypin", timerMenu)
            tcTimerMuxYpin.setLabel("Ypin")

            tcptcSignals = ptcPininfo
            tcSignals = self.getTCTimersSignals(ATDF,tctimer)
            for sindex in range(0, len(tcSignals)):
                tcTimermux = "MUX_"+tcSignals[sindex].getAttribute("pad")+tcSignals[sindex].getAttribute("function")+"_"+tctimer+"_"+tcSignals[sindex].getAttribute("group")+tcSignals[sindex].getAttribute("index")
                tcTimerMux.addKey(tcTimermux, str(sindex), tcTimermux)
                timerPin = tcSignals[sindex].getAttribute("pad")+tcSignals[sindex].getAttribute("function")+"_"+tctimer+"_"+tcSignals[sindex].getAttribute("group")+tcSignals[sindex].getAttribute("index")
                tcTimerSignal.addKey(timerPin, str(sindex), timerPin)
                drivenShieldDedicatedTimerPin.addKey(timerPin,str(pindex+1),timerPin)
                for cnt in range (0, len(tcptcSignals)):
                    if tcptcSignals[cnt].getAttribute("pad") == tcSignals[sindex].getAttribute("pad"):
                        tempstring = "Y("+tcptcSignals[cnt].getAttribute("index")+")"
                        tcTimerMuxYpin.addKey(tempstring, str(sindex) ,tempstring)
                        break
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
        
        for index in range(0, len(tccInstances)):
            tcctimer = tccInstances[index].getAttribute("name")
            drivenShieldDedicatedTimer.addKey(tcctimer,str(tindex+1),tcctimer)
            tindex+=1
            #create timer info group
            timerMenu = qtouchComponent.createMenuSymbol(tcctimer, timerInfo)
            timerMenu.setLabel(tcctimer)
            #create signal info
            tccTimerSignal = qtouchComponent.createKeyValueSetSymbol(tcctimer+"_SIGNAL", timerMenu)
            tccTimerSignal.setLabel("Signal")
            tccTimerMux = qtouchComponent.createKeyValueSetSymbol(tcctimer+"_Mux", timerMenu)
            tccTimerMux.setLabel("Mux")
            tccTimerMuxYpin = qtouchComponent.createKeyValueSetSymbol(tcctimer+"_Ypin", timerMenu)
            tccTimerMuxYpin.setLabel("Ypin")
            tccptcSignals = ptcPininfo
            tccSignals = self.getTCCTimersSignals(ATDF,tcctimer)
            for sindex in range(0, len(tccSignals)):
                tccTimermux = "MUX_"+tccSignals[sindex].getAttribute("pad")+tccSignals[sindex].getAttribute("function")+"_"+tcctimer+"_"+tccSignals[sindex].getAttribute("group")+tccSignals[sindex].getAttribute("index")
                tccTimerMux.addKey(tccTimermux, str(sindex), tccTimermux)
                timerPin = tccSignals[sindex].getAttribute("pad")+tccSignals[sindex].getAttribute("function")+"_"+tcctimer+"_"+tccSignals[sindex].getAttribute("group")+tccSignals[sindex].getAttribute("index")
                tccTimerSignal.addKey(timerPin, str(sindex), timerPin)
                drivenShieldDedicatedTimerPin.addKey(timerPin,str(pindex+1),timerPin)
                for cnt in range (0, len(tccptcSignals)):
                    if tccptcSignals[cnt].getAttribute("pad") == tccSignals[sindex].getAttribute("pad"):
                        tempstring = "Y("+tccptcSignals[cnt].getAttribute("index")+")"
                        tccTimerMuxYpin.addKey(tempstring, str(sindex) ,tempstring)
                        break
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

        

    def getTCTimers(self,ATDF):
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

    def getTCCTimers(self,ATDF):
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

    def getTCTimersSignals(self,ATDF,tcInstance):
        """Retrieve TC signals from each TC peripheral.
        Arguments:
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :tcInstances : see getTCTimers()
        Returns:
            :list of TCTimer signals
        """
        tcSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+ tcInstance +"\"]/signals")
        if (tcSignalNode is not None):
            return tcSignalNode.getChildren()
        else:
            return []

    def getTCCTimersSignals(self,ATDF,tccInstance):
        """Retrieve TC signals from each TC peripheral.
        Arguments:
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :tccInstances : see getTCTimers()
        Returns:
            :list of TCCTimer signals
        """
        tccSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+ tccInstance +"\"]/signals")
        if (tccSignalNode is not None):
            return tccSignalNode.getChildren()
        else:
            return []

    def getTimersSharingPTCMux(self,qtouchComponent,tcInstances,tccInstances,ATDF,ptcYPads):
        """Retrieve a list of strings containing both timer and PTC pin information .
        Arguments:
            :qtouchComponent : touchModule
            :tcInstances : see getTCTimers()
            :tccInstances : see getTCCTimers()
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :ptcYPads : Y Pads extracted from ptcPinValues
        Returns:
            :list of timer and PTC multiplexed pins including pad,function,groupindex
        """
        timersSharingPTCMUX = []

        for indexI in range(0, len(tcInstances)):
            timer = tcInstances[indexI].getAttribute("name")
            tcSignals = self.getTCTimersSignals(ATDF,timer)
            for indexS in range(0, len(tcSignals)):
                qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
                qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
                if tcSignals[indexS].getAttribute("pad") in ptcYPads:
                    string = tcSignals[indexS].getAttribute("pad")+tcSignals[indexS].getAttribute("function")+"_"+timer+"_"+tcSignals[indexS].getAttribute("group")+tcSignals[indexS].getAttribute("index")
                    timersSharingPTCMUX.append(string)
        
        for indexI in range(0, len(tccInstances)):
            timer = tccInstances[indexI].getAttribute("name")
            tcSignals = self.getTCCTimersSignals(ATDF,timer)
            for indexS in range(0, len(tcSignals)):
                qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
                qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
                if tcSignals[indexS].getAttribute("pad") in ptcYPads:
                    string = tcSignals[indexS].getAttribute("pad")+tcSignals[indexS].getAttribute("function")+"_"+timer+"_"+tcSignals[indexS].getAttribute("group")+tcSignals[indexS].getAttribute("index")
                    timersSharingPTCMUX.append(string)

        return timersSharingPTCMUX

    def getTimersSharingPTC(self,qtouchComponent,tcInstances,tccInstances,ATDF,ptcYPads):
        """Retrieve a list of pads multiplexed between timer and PTC.
        Arguments:
            :qtouchComponent : touchModule
            :tcInstances : see getTCTimers()
            :tccInstances : see getTCCTimers()
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :ptcYPads : Y Pads extracted from ptcPinValues
        Returns:
            :list of timer and PTC multiplexed pins by pad
        """
        timersSharingPTC = []
        for indexI in range(0, len(tcInstances)):
            timer = tcInstances[indexI].getAttribute("name")
            tcSignals = self.getTCTimersSignals(ATDF,timer)
            for indexS in range(0, len(tcSignals)):            
                qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
                qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
                if tcSignals[indexS].getAttribute("pad") in ptcYPads:
                    timersSharingPTC.append(timer)
        
        for indexI in range(0, len(tccInstances)):
            timer = tccInstances[indexI].getAttribute("name")
            tcSignals = self.getTCCTimersSignals(ATDF,timer)
            for indexS in range(0, len(tcSignals)):            
                qtouchComponent.addDependency("Drivenshield_"+timer, "TMR", "TMR(Shield)", False, False)
                qtouchComponent.setDependencyEnabled("Drivenshield_"+timer, False)
                if tcSignals[indexS].getAttribute("pad") in ptcYPads:
                    timersSharingPTC.append(timer)

        return timersSharingPTC

    def drivenShieldUpdateEnabled(self,symbol,event):
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
            component.getSymbolByID(grpId).setVisible(currentVal)

    def updateDrivenShieldGroups(self,symbol, event):
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
        
        self.updateDSTimersMenu(symbol,event)

    def updateDSTimersMenu(self,symbol,event):
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
            dstimer = "DS_TIMER_APPLY_" +str(x)
            component.getSymbolByID(dstimer).setEnabled(False)
            component.getSymbolByID(dstimer).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(dstimer).setEnabled(True)
                component.getSymbolByID(dstimer).setVisible(True)

    def updateLumpModeDrivenShield(self,symbol,event,totalChannelCount,lump_symbol):
        """Handler for lump mode support menu click event.  
        Triggered by qtouch.processLump()
        Arguments:
            :symbol : the symbol that triggered the event
            :event : new value of the symbol 
            :totalChannelCount : see self.targetDeviceInst.getMutualCount()
            :lump_feature : lump configuration
        Returns:
            :none
        """
        print("Updating shield lumps")
        component= symbol.getComponent()
        currentVal = int(event['symbol'].getValue())
        enableDrivenShieldAdjacent = component.getSymbolByID("DS_ADJACENT_SENSE_LINE_AS_SHIELD").getValue()
        enableDrivenShieldDedicated = component.getSymbolByID("DS_DEDICATED_PIN_ENABLE").getValue()
        drivenShieldDedicatedPin = component.getSymbolByID("DS_DEDICATED_PIN")
        
#        tchSelfPinSelection = self.nodeInst.getTchSelfPinSelection()
#        tchMutXPinSelection = self.nodeInst.getTchMutXPinSelection()

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
                            value = self.nodeInst.tchSelfPinSelection[int(a)].getValue()
                            input0.append(self.nodeInst.tchSelfPinSelection[int(a)].getKeyValue(value))
                        if (i < totalChannelCount-LUMP_NUM):
                            for j in range(0,(totalChannelCount-LUMP_NUM)):
                                value1 = self.nodeInst.tchSelfPinSelection[int(i)].getValue()
                                if ((self.nodeInst.tchSelfPinSelection[int(i)].getKeyValue(value1)) != input0[j]):
                                    shieldPins.append(input0[j])
                        else:
                            LUMP_NODE_VAL = self.nodeInst.tchSelfPinSelection[int(i)].getValue()
                            LUMP_NODE_INDI = self.nodeInst.tchSelfPinSelection[int(i)].getKeyValue(LUMP_NODE_VAL).split("|")
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
                                shildY = self.nodeInst.tchSelfPinSelection[int(j)].getValue()
                                shieldY = self.nodeInst.tchSelfPinSelection[int(j)].getKeyValue(shildY)
                                shieldPins.append(shieldY)
                                print ("Adjacent Shield pins = "+ str(shieldPins))
                if(shieldPins != []):
                    drivenPin = "|".join(shieldPins)
                    print ("Drive pins = "+ str(drivenPin))
                else:
                    drivenPin = "X_NONE"
                    print ("Drive pins = NONE")
                self.nodeInst.tchMutXPinSelection[int(i)].setKeyValue(str(i),drivenPin)
                self.nodeInst.tchMutXPinSelection[int(i)].setValue(int(i))

#        self.nodeInst.setTchSelfPinSelection(tchSelfPinSelection)
#        self.nodeInst.setTchMutXPinSelection(tchMutXPinSelection)
    
    def setDSNodesMenu(self,groupNumber,qtouchComponent,touchMenu,touchChannelMutual,timersSharingPTC, timersSharingPTCMUX):
        """Populate the driven shield settings in the nodes group menus 
        Arguments:
            :groupNumber : index of the group instance
            :qtouchComponent : touchModule
            :touchMenu : touchMenu
            :touchChannelMutual : see self.targetDeviceInst.getMutualCount() 
            :timersSharingPTC : see getTimersSharingPTC()
            :timersSharingPTCMUX: see getTimersSharingPTCMUX()
        Returns:
            none
        """
        
        nodesMenuArray =[]
        if groupNumber == 1:
            for idx in range (0 ,touchChannelMutual-1):
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

