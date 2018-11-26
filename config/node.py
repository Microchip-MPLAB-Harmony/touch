################################################################################
#### Global Variables ####
################################################################################
touchChannelCountMax = 2
################################################################################
#### Business Logic ####
################################################################################
def setNodeChannelEnableProperty(symbol, event):
    channelId = int(symbol.getID().strip("TOUCH_ENABLE_CH_"))
    channelCount = int(event["value"])
    #Log.writeInfoMessage(str(channelCount))
    if channelId < channelCount:
        symbol.setVisible(True)
        symbol.setValue(True,1)
    else:
        symbol.setVisible(False)
        symbol.setValue(False,1)

def selfcapFunc(mySymbol, event):
    symObj=event["symbol"]
    Log.writeInfoMessage(symObj.getSelectedKey())
    index = int(mySymbol.getID().split("_")[1])
    Log.writeInfoMessage(str(index))
    if (symObj.getSelectedKey() == "SelfCap"):
        mySymbol.setVisible(True)
    else:
        mySymbol.setVisible(False)

def mutlFunc(mySymbol, event):
    symObj=event["symbol"]
    Log.writeInfoMessage(symObj.getSelectedKey())
    index = int(mySymbol.getID().split("_")[1])
    Log.writeInfoMessage(str(index))
    if (symObj.getSelectedKey() == "MutualCap"):
        mySymbol.setVisible(True)
    else:
        mySymbol.setVisible(False)

def getChannelCount(symbol,event):
    numChann = int(event["value"])
################################################################################
#### Component ####
################################################################################
nodeMenu = qtouchComponent.createMenuSymbol("NODE_MENU", touchMenu)
nodeMenu.setLabel("Node Configuration")

# Touch Channel Enable Count
touchNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_CHAN_ENABLE_CNT", nodeMenu)
touchNumChannel.setLabel("Number of Channels to enable")
touchNumChannel.setDefaultValue(0)
touchNumChannel.setMin(0)
touchNumChannel.setMax(touchChannelCountMax)
touchNumChannel.setDependencies(getChannelCount,["TOUCH_CHAN_ENABLE_CNT"])

tchSelfPinSelection = []
tchMutXPinSelection = []
tchMutYPinSelection = []

for channelID in range(0,int(touchChannelCountMax)):

    touchChEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_CH_" + str(channelID), nodeMenu)
    touchChEnable.setLabel("Use touch channel " + str(channelID))
    touchChEnable.setVisible(False)
    touchChEnable.setDependencies(setNodeChannelEnableProperty, ["TOUCH_CHAN_ENABLE_CNT"])

    tchSelfPinSelection.append(qtouchComponent.createKeyValueSetSymbol("SELFCAP-INPUT_"+ str(channelID), touchChEnable))
    tchSelfPinSelection[channelID].setLabel("Select Y Pin for Channel "+ str(channelID))
    tchSelfPinSelection[channelID].setDefaultValue(0)
    tchSelfPinSelection[channelID].setOutputMode("Key")
    tchSelfPinSelection[channelID].setDisplayMode("Description")
    tchSelfPinSelection[channelID].setVisible(True)
    tchSelfPinSelection[channelID].setDependencies(selfcapFunc, ["SENSE_TECHNOLOGY"])
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "Y"):
            tchSelfPinSelection[channelID].addKey(ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
        ptcPinValues[index].getAttribute("index"),
        ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")

    tchMutXPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-X-INPUT_"+ str(channelID), touchChEnable))
    tchMutXPinSelection[channelID].setLabel("Select X Pin for Channel "+ str(channelID))
    tchMutXPinSelection[channelID].setDefaultValue(0)
    tchMutXPinSelection[channelID].setOutputMode("Key")
    tchMutXPinSelection[channelID].setDisplayMode("Description")
    tchMutXPinSelection[channelID].setVisible(False)
    tchMutXPinSelection[channelID].setDependencies(mutlFunc, ["SENSE_TECHNOLOGY"])
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "X"):        
            tchMutXPinSelection[channelID].addKey(ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
        ptcPinValues[index].getAttribute("index"),
        ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")

    tchMutYPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-Y-INPUT_"+ str(channelID), touchChEnable))
    tchMutYPinSelection[channelID].setLabel("Select Y Pin for Channel "+ str(channelID))
    tchMutYPinSelection[channelID].setDefaultValue(0)
    tchMutYPinSelection[channelID].setOutputMode("Key")
    tchMutYPinSelection[channelID].setDisplayMode("Description")
    tchMutYPinSelection[channelID].setVisible(False)
    tchMutYPinSelection[channelID].setDependencies(mutlFunc, ["SENSE_TECHNOLOGY"])
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "Y"):        
            tchMutYPinSelection[channelID].addKey(ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
        ptcPinValues[index].getAttribute("index"),
        ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")   

    #Charge Share Delay
    touchSym_CSD_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_CHARGE_SHARE_DELAY" + str(channelID), touchChEnable)
    touchSym_CSD_Val.setLabel("Additional Charge Share Delay")
    touchSym_CSD_Val.setDefaultValue(0)
    touchSym_CSD_Val.setMin(0)
    touchSym_CSD_Val.setMax(255)

    #Series Resistor
    touchSym_SERIES_RESISTOR_Val = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_SERIES_RESISTOR" + str(channelID), touchChEnable)
    touchSym_SERIES_RESISTOR_Val.setLabel("Series Resistor")
    touchSym_SERIES_RESISTOR_Val.addKey("RES0", "RSEL_VAL_0", "No resistor")
    touchSym_SERIES_RESISTOR_Val.addKey("RES20", "RSEL_VAL_20", "20 k")
    touchSym_SERIES_RESISTOR_Val.addKey("RES50", "RSEL_VAL_50", "50 k")
    touchSym_SERIES_RESISTOR_Val.addKey("RES100", "RSEL_VAL_100", "100 k")
    touchSym_SERIES_RESISTOR_Val.setDefaultValue(0)
    touchSym_SERIES_RESISTOR_Val.setOutputMode("Value")
    touchSym_SERIES_RESISTOR_Val.setDisplayMode("Description")

    #PTC Clock Prescaler
    touchSym_PTC_PRESCALER_Val = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_PTC_PRESCALER" + str(channelID), touchChEnable)
    touchSym_PTC_PRESCALER_Val.setLabel("PTC Clock Prescaler")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC0", "PRSC_DIV_SEL_1", "No prescaler")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC2", "PRSC_DIV_SEL_2", "2")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC4", "PRSC_DIV_SEL_4", "4")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC8", "PRSC_DIV_SEL_8", "8")
    touchSym_PTC_PRESCALER_Val.setDefaultValue(1)
    touchSym_PTC_PRESCALER_Val.setOutputMode("Value")
    touchSym_PTC_PRESCALER_Val.setDisplayMode("Description")

    #Analog Gain
    touchSym_ANALOG_GAIN_Val = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_GAIN_ANA" + str(channelID), touchChEnable)
    touchSym_ANALOG_GAIN_Val.setLabel("Analog Gain")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN1", "GAIN_1", "1")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN2", "GAIN_2", "2")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN4", "GAIN_4", "4")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN8", "GAIN_8", "8")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN16", "GAIN_16", "16")
    touchSym_ANALOG_GAIN_Val.setDefaultValue(0)
    touchSym_ANALOG_GAIN_Val.setOutputMode("Value")
    touchSym_ANALOG_GAIN_Val.setDisplayMode("Description")

    #Digital Filter Gain - Accumulated sum is scaled to Digital Gain
    touchSym_DIGI_FILT_GAIN_Val = qtouchComponent.createKeyValueSetSymbol("DEF_DIGI_FILT_GAIN"  + str(channelID), touchChEnable)
    touchSym_DIGI_FILT_GAIN_Val.setLabel("Digital Filter Gain")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN1", "GAIN_1", "1")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN2", "GAIN_2", "2")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN4", "GAIN_4", "4")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN8", "GAIN_8", "8")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN16", "GAIN_16", "16")
    touchSym_DIGI_FILT_GAIN_Val.setDefaultValue(0)
    touchSym_DIGI_FILT_GAIN_Val.setOutputMode("Value")
    touchSym_DIGI_FILT_GAIN_Val.setDisplayMode("Description")

    #Digital Filter Oversampling - Number of samples for each measurement
    touchSym_DIGI_FILT_OVERSAMPLING_Val = qtouchComponent.createKeyValueSetSymbol("DEF_DIGI_FILT_OVERSAMPLING" + str(channelID), touchChEnable)
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setLabel("Digital Filter Oversampling")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE1", "FILTER_LEVEL_1", "1 sample")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE2", "FILTER_LEVEL_2", "2 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE4", "FILTER_LEVEL_4", "4 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE8", "FILTER_LEVEL_8", "8 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE16", "FILTER_LEVEL_16", "16 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE32", "FILTER_LEVEL_32", "32 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE64", "FILTER_LEVEL_64", "64 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setDefaultValue(4)
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setOutputMode("Value")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setDisplayMode("Description")