"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchNodeGroups():
    def __init__(self):
        self.tchSelfPinSelection = []
        self.tchMutXPinSelection = []
        self.tchMutYPinSelection = []
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []
        # defaultValue
        self.maxGroups = 4

    def getTchSelfPinSelection(self):
        """Get self capacitance pins
        Arguments:
            : none
        Returns:
            : list of self capacitance pins
        """
        return self.tchSelfPinSelection

    def setTchSelfPinSelection(self,newTchSelfPinSelection):
        """Set self capacitance pins
        Arguments:
            : list of self capacitance pins
        Returns:
            : none
        """
        self.tchSelfPinSelection = newTchSelfPinSelection



    def getTchMutXPinSelection(self):
        """Get mutual capacitance x pins
        Arguments:
            : none
        Returns:
            : list of mutual capacitance x pins
        """
        return self.tchMutXPinSelection

    def setTchMutXPinSelection(self,newTchMutXPinSelection):
        """Set mutual capacitance x pins
        Arguments:
            : list of mutual capacitance x pins
        Returns:
            : none
        """
        self.tchMutXPinSelection = newTchMutXPinSelection

    def getTchMutYPinSelection(self):
        """Get mutual capacitance y pins
        Arguments:
            : none
        Returns:
            : list of mutual capacitance y pins
        """
        return self.tchMutYPinSelection

    def setTchMutYPinSelection(self,newTchMutYPinSelection):
        """Set mutual capacitance y pins
        Arguments:
            : list of mutual capacitance y pins
        Returns:
            : none
        """
        self.tchMutYPinSelection = newTchMutYPinSelection

    def getMaxGroups(self):
        """Get maximum node groups
        Arguments:
            :none
        Returns:
            :number of node groups  as (int)
        """
        return int(self.maxGroups)

    def setMaxGroups(self,newMax):
        """Set maximum node groups
        Arguments:
            :newMax - new maximum (int)
        Returns:
            :none
        """
        self.maxGroups = int(newMax)

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def initNodeGroupInstance(self,instances,qtouchComponent,groupNumber,parentLabel,selfChannels,mutualChannels,ptcPinValues,csdMode,rSelMode):
        """Initialise Node Group Instance
        Arguments:
            :qtouchComponent : touchModule
            :groupNumber : index of the group instance
            :parentLabel : parent symbol for added menu items
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
            :ptcPinValues : see target_device.setDevicePinValues()
            :csdmode : see target_device.getCSDMode(targetDevice)
            :rSelMode: see target_device.getRSelMode(targetDevice)
        Returns:
            :none
        """
        touchNodeNumChannel = 0
        print ("node group instances ", instances)

        if int(groupNumber) == 1:
            touchNodeNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_CHAN_ENABLE_CNT", parentLabel)
        else:
            touchNodeNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_CHAN_ENABLE_CNT"+str(groupNumber), parentLabel)
        
        if touchNodeNumChannel != 0:
            touchNodeNumChannel.setLabel("Number of nodes to enable")
            touchNodeNumChannel.setDefaultValue(0)
            touchNodeNumChannel.setMin(0)
            touchNodeNumChannel.setMax(mutualChannels)
        
        for channelID in range(0, mutualChannels):
            if int(groupNumber) == 1:
                touchChEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_CH_" + str(channelID), parentLabel)
                touchChEnable.setLabel("Use touch channel " + str(channelID))
                self.tchSelfPinSelection.append(qtouchComponent.createKeyValueSetSymbol("SELFCAP-INPUT_"+ str(channelID), touchChEnable))
                self.tchMutXPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-X-INPUT_"+ str(channelID), touchChEnable))
                self.tchMutYPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-Y-INPUT_"+ str(channelID), touchChEnable))
                self.addDepSymbol(self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1], "updatePinsSettings", ["SELFCAP-INPUT_"+ str(channelID)])
                self.addDepSymbol(self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1], "updatePinsSettings", ["MUTL-X-INPUT_"+ str(channelID)])
                self.addDepSymbol(self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1], "updatePinsSettings", ["MUTL-Y-INPUT_"+ str(channelID)])

                if(csdMode!="NoCSD"):
                    #Charge Share Delay
                    touchChargeShareDelay = qtouchComponent.createIntegerSymbol("DEF_TOUCH_CHARGE_SHARE_DELAY" + str(channelID), touchChEnable)
                #Series Resistor
                touchSeriesResistor = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_SERIES_RESISTOR" + str(channelID), touchChEnable)
                #PTC Clock Prescaler
                touchPTCPrescaler = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_PTC_PRESCALER" + str(channelID), touchChEnable)
                #Analog Gain
                touchAnalogGain = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_GAIN_ANA" + str(channelID), touchChEnable)
                #Digital Filter Gain - Accumulated sum is scaled to Digital Gain
                touchDigitalFilterGain = qtouchComponent.createKeyValueSetSymbol("DEF_DIGI_FILT_GAIN"  + str(channelID), touchChEnable)
                #Digital Filter Oversampling - Number of samples for each measurement
                touchDigitalFilterOversampling = qtouchComponent.createKeyValueSetSymbol("DEF_DIGI_FILT_OVERSAMPLING" + str(channelID), touchChEnable)
            else:
                dynamicTouchChEnable = "touchChEnable_" +str(groupNumber) 
                vars()[dynamicTouchChEnable] = qtouchComponent.createBooleanSymbol("GROUP_"+str(groupNumber)+"_TOUCH_ENABLE_CH_" + str(channelID), parentLabel)
                vars()[dynamicTouchChEnable].setLabel("Use touch channel " + str(channelID))
                self.tchSelfPinSelection.append(qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_SELFCAP-INPUT_"+ str(channelID), vars()[dynamicTouchChEnable]))
                self.tchMutXPinSelection.append(qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_MUTL-X-INPUT_"+ str(channelID), vars()[dynamicTouchChEnable]))
                self.tchMutYPinSelection.append(qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_MUTL-Y-INPUT_"+ str(channelID), vars()[dynamicTouchChEnable]))
                self.addDepSymbol(self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1], "updatePinsSettings", ["GROUP_"+str(groupNumber)+"_SELFCAP-INPUT_"+ str(channelID)])
                self.addDepSymbol(self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1], "updatePinsSettings", ["GROUP_"+str(groupNumber)+"_MUTL-X-INPUT_"+ str(channelID)])
                self.addDepSymbol(self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1], "updatePinsSettings", ["GROUP_"+str(groupNumber)+"_MUTL-Y-INPUT_"+ str(channelID)])

                #Charge Share Delay
                if(csdMode!="NoCSD"):
                    touchChargeShareDelay = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"_DEF_TOUCH_CHARGE_SHARE_DELAY" + str(channelID), vars()[dynamicTouchChEnable])
                #Series Resistor
                touchSeriesResistor = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_NOD_SERIES_RESISTOR" + str(channelID), vars()[dynamicTouchChEnable])
                #PTC Clock Prescaler
                touchPTCPrescaler = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_NOD_PTC_PRESCALER" + str(channelID), vars()[dynamicTouchChEnable])
                #Analog Gain
                touchAnalogGain = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_NOD_GAIN_ANA" + str(channelID), vars()[dynamicTouchChEnable])
                #Digital Filter Gain - Accumulated sum is scaled to Digital Gain
                touchDigitalFilterGain = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_DIGI_FILT_GAIN"  + str(channelID), vars()[dynamicTouchChEnable])
                #Digital Filter Oversampling - Number of samples for each measurement
                touchDigitalFilterOversampling = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_DIGI_FILT_OVERSAMPLING" + str(channelID), vars()[dynamicTouchChEnable])

            self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1].setLabel("Select Y Pin for Channel "+ str(channelID))
            self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1].setOutputMode("Value")
            self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1].setDisplayMode("Description")
            self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1].setLabel("Select X Pin for Channel "+ str(channelID))
            self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1].setOutputMode("Value")
            self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1].setDisplayMode("Description")
            self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1].setLabel("Select Y Pin for Channel "+ str(channelID))
            self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1].setOutputMode("Value")
            self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1].setDisplayMode("Description")
            
            if(csdMode!="NoCSD"):
                self.setCSDValues(touchChargeShareDelay,csdMode)

            if(rSelMode == "e5x"):
                self.setSeriesRValuesE5x(touchSeriesResistor)
            elif(rSelMode == "l22"):
                self.setSeriesRValuesL22(touchSeriesResistor)
            else:
                self.setSeriesRValues(touchSeriesResistor)

            #PTC Clock Prescaler
            self.setPTCPresscalerValues(touchPTCPrescaler)
            #Analog Gain
            self.setAnalogGainValues(touchAnalogGain)
            #Digital Filter Gain - Accumulated sum is scaled to Digital Gain
            self.setDigitalFilterGainValues(touchDigitalFilterGain)
            #Digital Filter Oversampling - Number of samples for each measurement
            self.setDigitalFilterOversamplingValues(touchDigitalFilterOversampling)
            # X and Y assignment

            if instances['interfaceInst'].getDeviceSeries() in instances['target_deviceInst'].picDevices:
                if instances['interfaceInst'].getDeviceSeries() == "PIC32MZW":
                    cvdRPins = ptcPinValues[0]
                    cvdTPins = ptcPinValues[1]
                    for index in range(0, len(cvdRPins)):
                        self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1].addKey(str(index+1),
                        "Y("+str(index+1)+")",
                        "Y"+str(index+1)+"  ("+cvdRPins[index]+")")
                    for index in range(0, len(cvdTPins)):
                        self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1].addKey(str(index),
                        "X("+str(index)+")",
                        "X"+str(index)+"  ("+cvdTPins[index]+")")
                else:
                    cvdRPins = ptcPinValues[0]
                    cvdTPins = ptcPinValues[1]
                    offset = 0
                    for index in range(0, len(cvdRPins)):
                        anNumber = cvdRPins[index].split("AN")[1]
                        anNumber = int(anNumber)
                        text = "  ("+cvdRPins[index].split("_")[0]+")"
                        if (anNumber <= 4) or (anNumber >= 41 and anNumber <= 45):
                            continue
                        else:
                            self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1].addKey("Y("+str(anNumber)+")",
                            "Y("+str(anNumber)+")",
                            "Y"+str(anNumber)+text)
                            self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1].addKey("Y("+str(anNumber)+")",
                            "Y("+str(anNumber)+")",
                            "Y"+str(anNumber)+text)
                    for index in range(0, len(cvdTPins)):
                        self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1].addKey("X("+str(anNumber)+")",
                        "Y("+str(anNumber)+")",
                        "X"+str(anNumber)+text)
            else:
                for index in range(0, len(ptcPinValues)):
                    if(ptcPinValues[index].getAttribute("group") == "Y"):
                        self.tchSelfPinSelection[len(self.tchSelfPinSelection)-1].addKey(
                            ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
                            ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")

                        self.tchMutYPinSelection[len(self.tchMutYPinSelection)-1].addKey(
                            ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
                            ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")

                    if(ptcPinValues[index].getAttribute("group") == "X"):        
                        self.tchMutXPinSelection[len(self.tchMutXPinSelection)-1].addKey(
                            ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
                            ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")


    def initNodeGroup(self,instances,qtouchComponent, touchMenu, minVal,maxVal,selfChannels,mutualChannels, ptcPinValues,csdMode,rSelMode):
        """Initialise Node Groups and add to touch Module
        Arguments:
            :qtouchComponent : touchModule
            :touchMenu : parent menu symbol for added menu items
            :minVal : see acquisitionGroupCountMenu.getMin()
            :maxVal : see acquisitionGroupCountMenu.getMax()
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
            :ptcPinValues : see target_device.setDevicePinValues()
            :csdmode : see target_device.getCSDMode(targetDevice)
            :rSelMode : see target_device.getRSelMode(targetDevice)
        Returns:
            :none
        """
        self.maxGroups = maxVal

        for groupNum in range (minVal,maxVal+1):
            if groupNum ==1:
                nodeMenu = qtouchComponent.createMenuSymbol("NODE_MENU", touchMenu)
                nodeMenu.setLabel("Node Configuration")
                nodeMenu.setDescription("Configure Nodes")
                nodeMenu.setVisible(True)
                nodeMenu.setEnabled(True)
                self.initNodeGroupInstance(instances,qtouchComponent,groupNum,nodeMenu,selfChannels,mutualChannels,ptcPinValues,csdMode,rSelMode)
            else:
                dynamicNodeMenu = "nodeMenu_" +str(groupNum) 
                dynamicId = "NODE_MENU_" +str(groupNum) 
                vars()[dynamicNodeMenu] =  qtouchComponent.createMenuSymbol(dynamicId, touchMenu)
                vars()[dynamicNodeMenu].setLabel("Node Configuration Group"+str(groupNum))
                vars()[dynamicNodeMenu].setVisible(False)
                vars()[dynamicNodeMenu].setEnabled(False)
                self.initNodeGroupInstance(instances,qtouchComponent,groupNum,vars()[dynamicNodeMenu],selfChannels,mutualChannels,ptcPinValues,csdMode,rSelMode)

    def updateNodeGroups(self,symbol,event):
        """Handler for number of Node groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
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
            grpId = "NODE_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(False)
            component.getSymbolByID(grpId).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(grpId).setEnabled(True)
                component.getSymbolByID(grpId).setVisible(True)

    def setCSDValues(self,touchChargeShareDelay,csdMode):
        """Populate the charge share delay symbol 
        Arguments:
            :touchChargeShareDelay : symbol to be populated
            :csdMode : see target_device.getCSDMode(targetDevice)
        Returns:
            none
        """
        touchChargeShareDelay.setLabel("Additional Charge Share Delay")
        touchChargeShareDelay.setDefaultValue(0)
        touchChargeShareDelay.setMin(0)
        touchChargeShareDelay.setDescription("Increase in Charge Share Delay increases sensor charging time and so the touch measurement time. It indicates the number of additional cycles that are inserted within a touch measurement cycle.")
        
        if(csdMode == "8bitCSD"):
            touchChargeShareDelay.setMax(63)
        elif(csdMode == "16bitCSD"):
            touchChargeShareDelay.setMax(255)
        else:
            touchChargeShareDelay.setMax(255)


    def setSeriesRValues(self,touchSeriesResistor):
        """Populate the series resistor symbol 
        Arguments:
            :touchSeriesResistor : symbol to be populated
        Returns:
            none
        """
        touchSeriesResistor.setLabel("Series Resistor")
        touchSeriesResistor.addKey("RES0", "RSEL_VAL_0", "No resistor")
        touchSeriesResistor.addKey("RES20", "RSEL_VAL_20", "20 k")
        touchSeriesResistor.addKey("RES50", "RSEL_VAL_50", "50 k")
        touchSeriesResistor.addKey("RES100", "RSEL_VAL_100", "100 k")
        touchSeriesResistor.setDefaultValue(0)
        touchSeriesResistor.setOutputMode("Value")
        touchSeriesResistor.setDisplayMode("Description")
        touchSeriesResistor.setDescription("Selection for internal series resistor.Higher series resistor provides higher noise immunity and requires long time for charging. This could affect response time. So, series resistor should be selected optimally.")

    def setSeriesRValuesE5x(self,touchSeriesResistor):
        """Populate the series resistor symbol for d5x,e5x devices
        Arguments:
            :touchSeriesResistor : symbol to be populated
        Returns:
            none
        """
        touchSeriesResistor.setLabel("Series Resistor")
        touchSeriesResistor.addKey("RES0", "RSEL_VAL_0", "No resistor")
        touchSeriesResistor.addKey("RES3", "RSEL_VAL_3", "3")
        touchSeriesResistor.addKey("RES6", "RSEL_VAL_6", "6 k")
        touchSeriesResistor.addKey("RES20", "RSEL_VAL_20", "20 k")
        touchSeriesResistor.addKey("RES50", "RSEL_VAL_50", "50 k")
        touchSeriesResistor.addKey("RES75", "RSEL_VAL_75", "75 k")
        touchSeriesResistor.addKey("RES100", "RSEL_VAL_100", "100 k")
        touchSeriesResistor.addKey("RES200", "RSEL_VAL_200", "200 k")
        touchSeriesResistor.setDefaultValue(0)
        touchSeriesResistor.setOutputMode("Value")
        touchSeriesResistor.setDisplayMode("Description")
        touchSeriesResistor.setDescription("Selection for internal series resistor.Higher series resistor provides higher noise immunity and requires long time for charging. This could affect response time. So, series resistor should be selected optimally.")

    def setSeriesRValuesL22(self,touchSeriesResistor):
        """Populate the series resistor symbol for l22 devices
        Arguments:
            :touchSeriesResistor : symbol to be populated
        Returns:
            none
        """
        touchSeriesResistor.setLabel("Series Resistor")
        touchSeriesResistor.addKey("RES0", "RSEL_VAL_0", "No resistor")
        touchSeriesResistor.addKey("RES20", "RSEL_VAL_20", "20 k")
        touchSeriesResistor.addKey("RES50", "RSEL_VAL_50", "50 k")
        touchSeriesResistor.addKey("RES75", "RSEL_VAL_75", "75 k")
        touchSeriesResistor.addKey("RES100", "RSEL_VAL_100", "100 k")
        touchSeriesResistor.addKey("RES200", "RSEL_VAL_200", "200 k")
        touchSeriesResistor.setDefaultValue(0)
        touchSeriesResistor.setOutputMode("Value")
        touchSeriesResistor.setDisplayMode("Description")
        touchSeriesResistor.setDescription("Selection for internal series resistor.Higher series resistor provides higher noise immunity and requires long time for charging. This could affect response time. So, series resistor should be selected optimally.")

    def setPTCPresscalerValues(self,touchPTCPrescaler):
        """Populate the ptc prescaler symbol
        Arguments:
            :touchPTCPrescaler : symbol to be populated
        Returns:
            none
        """
        touchPTCPrescaler.setLabel("PTC Clock Prescaler")
        touchPTCPrescaler.addKey("PRESC4", "PRSC_DIV_SEL_4", "4")
        touchPTCPrescaler.addKey("PRESC8", "PRSC_DIV_SEL_8", "8")
        touchPTCPrescaler.addKey("PRESC16", "PRSC_DIV_SEL_16", "16")
        touchPTCPrescaler.addKey("PRESC32", "PRSC_DIV_SEL_32", "32")
        touchPTCPrescaler.setDefaultValue(0)
        touchPTCPrescaler.setOutputMode("Value")
        touchPTCPrescaler.setDisplayMode("Description")
        touchPTCPrescaler.setDescription("The PTC clock is prescaled by PTC and then used for touch measurement.The PTC prescaling factor is defined by this parameter. It is recommended to configure this parameter such that the clock after the prescaler is less than or equal to 1MHz.")

    def setAnalogGainValues(self,touchAnalogGain):
        """Populate the analog gain symbol
        Arguments:
            :touchPTCPrescaler : symbol to be populated
        Returns:
            none
        """
        touchAnalogGain.setLabel("Analog Gain")
        touchAnalogGain.addKey("ANA_GAIN1", "GAIN_1", "1")
        touchAnalogGain.addKey("ANA_GAIN2", "GAIN_2", "2")
        touchAnalogGain.addKey("ANA_GAIN4", "GAIN_4", "4")
        touchAnalogGain.addKey("ANA_GAIN8", "GAIN_8", "8")
        touchAnalogGain.addKey("ANA_GAIN16", "GAIN_16", "16")
        touchAnalogGain.setDefaultValue(0)
        touchAnalogGain.setOutputMode("Value")
        touchAnalogGain.setDisplayMode("Description")
        touchAnalogGain.setDescription("Gain setting for touch delta value.Higher gain setting increases touch delta as well as noise.So, optimum gain setting should be used.Gain should be tuned such that the touch delta is between 40~60 counts.")
            
    def setDigitalFilterGainValues(self,touchDigitalFilterGain):
        """Populate the digital gain symbol
        Arguments:
            :touchPTCPrescaler : symbol to be populated
        Returns:
            none
        """
        touchDigitalFilterGain.setLabel("Digital Filter Gain")
        touchDigitalFilterGain.addKey("GAIN1", "GAIN_1", "1")
        touchDigitalFilterGain.addKey("GAIN2", "GAIN_2", "2")
        touchDigitalFilterGain.addKey("GAIN4", "GAIN_4", "4")
        touchDigitalFilterGain.addKey("GAIN8", "GAIN_8", "8")
        touchDigitalFilterGain.addKey("GAIN16", "GAIN_16", "16")
        touchDigitalFilterGain.setDefaultValue(0)
        touchDigitalFilterGain.setOutputMode("Value")
        touchDigitalFilterGain.setDisplayMode("Description")
        touchDigitalFilterGain.setDescription("Gain setting for touch delta value. Higher gain setting increases touch delta as well as noise. So, optimum gain setting should be used.Gain should be tuned such that the touch delta is between 40~60 counts. ")
            
    def setDigitalFilterOversamplingValues(self,touchDigitalFilterOversampling):
        """Populate the digital oversampling symbol
        Arguments:
            :touchPTCPrescaler : symbol to be populated
        Returns:
            none
        """
        touchDigitalFilterOversampling.setLabel("Digital Filter Oversampling")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE1", "FILTER_LEVEL_1", "1 sample")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE2", "FILTER_LEVEL_2", "2 samples")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE4", "FILTER_LEVEL_4", "4 samples")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE8", "FILTER_LEVEL_8", "8 samples")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE16", "FILTER_LEVEL_16", "16 samples")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE32", "FILTER_LEVEL_32", "32 samples")
        touchDigitalFilterOversampling.addKey("DF_OVERSAMPLE64", "FILTER_LEVEL_64", "64 samples")
        touchDigitalFilterOversampling.setDefaultValue(4)
        touchDigitalFilterOversampling.setOutputMode("Value")
        touchDigitalFilterOversampling.setDisplayMode("Description")
        touchDigitalFilterOversampling.setDescription("Defines the number of samples taken for each measurement.Higher filter level settings, for each measurements more number of samples taken which helps to average out the noise.Higher filter level settings takes long time to do a touch measurement which affects response time.So, start with default value and increase depends on noise levels.")

    def updateLumpMode(self,lump_symbol,touchtech):
        """Handler for number of lump mode support. Triggered by qtouch.processLump(symbol, event)
        Arguments:
            :symbol : the symbol that triggered the callback
            touchtech : see node_groups.setTouchTechnologyValues()
        Returns:
            :none
        """
        print(touchtech)
        lump_feature = lump_symbol.getValue()
        if (lump_feature != ""):
            lump_items = str(lump_feature).split(";")
            num_of_lumps = len(lump_items)
            for lmp in range(0,num_of_lumps):
                lump_x = []
                lump_y = []

                lump_split = str(lump_items[lmp]).split(":")
                
                lump_node = lump_split[0]
                lump_node_array = str(lump_split[1]).split(",")
                if ((touchtech == "SelfCap") or (touchtech == "SelfCapShield")):
                    for item in lump_node_array:
                        val = self.tchSelfPinSelection[int(item)].getValue()
                        yCh = self.tchSelfPinSelection[int(item)].getKeyValue(val)
                        if yCh not in lump_y:
                            lump_y.append(yCh)
                    lumpy = "|".join(lump_y)
                    key1 = self.tchMutXPinSelection[int(lump_node)].getKey(0)
                    self.tchSelfPinSelection[int(lump_node)].setKeyValue(str(key1),lumpy)
                    self.tchSelfPinSelection[int(lump_node)].setValue(0)
                elif (touchtech == "MutualCap"):
                    for item in lump_node_array:
                        val1 = self.tchMutXPinSelection[int(item)].getValue()
                        val2 = self.tchMutYPinSelection[int(item)].getValue()
                        xCh = self.tchMutXPinSelection[int(item)].getKeyValue(val1)
                        yCh = self.tchMutYPinSelection[int(item)].getKeyValue(val2)
                        if xCh not in lump_x:
                            lump_x.append(xCh)
                        if yCh not in lump_y:
                            lump_y.append(yCh)
                    lumpx = "|".join(lump_x)
                    key1 = self.tchMutXPinSelection[int(lump_node)].getKey(0)
                    self.tchMutXPinSelection[int(lump_node)].setKeyValue(str(key1),lumpx)
                    self.tchMutXPinSelection[int(lump_node)].setValue(0)
                    lumpy = "|".join(lump_y)
                    key2 = self.tchMutYPinSelection[int(lump_node)].getKey(0)
                    self.tchMutYPinSelection[int(lump_node)].setKeyValue(str(key2),lumpy)
                    self.tchMutYPinSelection[int(lump_node)].setValue(0)
        else:
            print("NOT LUMPING NODES")