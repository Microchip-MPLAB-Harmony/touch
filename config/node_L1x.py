################################################################################
#### Global Variables ####
################################################################################
touchChannelCountMax =totalChannelCountMutl.getValue()

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

global tchSelfPinSelection
global tchMutXPinSelection
global tchMutYPinSelection
tchSelfPinSelection = []
tchMutXPinSelection = []
tchMutYPinSelection = []

for channelID in range(0, touchChannelCountMax):

    touchChEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_CH_" + str(channelID), nodeMenu)
    touchChEnable.setLabel("Use touch channel " + str(channelID))

    tchSelfPinSelection.append(qtouchComponent.createKeyValueSetSymbol("SELFCAP-INPUT_"+ str(channelID), touchChEnable))
    tchSelfPinSelection[channelID].setLabel("Select Y Pin for Channel "+ str(channelID))
    tchSelfPinSelection[channelID].setDefaultValue(0)
    tchSelfPinSelection[channelID].setOutputMode("Value")
    tchSelfPinSelection[channelID].setDisplayMode("Description")
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "Y"):
            tchSelfPinSelection[channelID].addKey(
            ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
        ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")
    tchSelfPinSelection[channelID].setDependencies(getPinValue,["SELFCAP-INPUT_"+ str(channelID)])

    tchMutXPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-X-INPUT_"+ str(channelID), touchChEnable))
    tchMutXPinSelection[channelID].setLabel("Select X Pin for Channel "+ str(channelID))
    tchMutXPinSelection[channelID].setDefaultValue(0)
    tchMutXPinSelection[channelID].setOutputMode("Value")
    tchMutXPinSelection[channelID].setDisplayMode("Description")
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "X"):        
            tchMutXPinSelection[channelID].addKey(ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
        ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")
    tchMutXPinSelection[channelID].setDependencies(getPinValue,["MUTL-X-INPUT_"+ str(channelID)])

    tchMutYPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-Y-INPUT_"+ str(channelID), touchChEnable))
    tchMutYPinSelection[channelID].setLabel("Select Y Pin for Channel "+ str(channelID))
    tchMutYPinSelection[channelID].setDefaultValue(0)
    tchMutYPinSelection[channelID].setOutputMode("Value")
    tchMutYPinSelection[channelID].setDisplayMode("Description")
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "Y"):        
            tchMutYPinSelection[channelID].addKey(ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",
        ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")   
    tchMutYPinSelection[channelID].setDependencies(getPinValue,["MUTL-Y-INPUT_"+ str(channelID)])		

    #Charge Share Delay
    touchSym_CSD_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_CHARGE_SHARE_DELAY" + str(channelID), touchChEnable)
    touchSym_CSD_Val.setLabel("Additional Charge Share Delay")
    touchSym_CSD_Val.setDefaultValue(0)
    touchSym_CSD_Val.setMin(0)
    touchSym_CSD_Val.setMax(255)
    touchSym_CSD_Val.setDescription("Increase in Charge Share Delay increases sensor charging time and so the touch measurement time. It indicates the number of additional cycles that are inserted within a touch measurement cycle.")

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
    touchSym_SERIES_RESISTOR_Val.setDescription("Selection for internal series resistor.Higher series resistor provides higher noise immunity and requires long time for charging. This could affect response time. So, series resistor should be selected optimally.")

    #PTC Clock Prescaler
    touchSym_PTC_PRESCALER_Val = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_PTC_PRESCALER" + str(channelID), touchChEnable)
    touchSym_PTC_PRESCALER_Val.setLabel("PTC Clock Prescaler")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC4", "PRSC_DIV_SEL_4", "4")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC8", "PRSC_DIV_SEL_8", "8")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC16", "PRSC_DIV_SEL_16", "16")
    touchSym_PTC_PRESCALER_Val.addKey("PRESC32", "PRSC_DIV_SEL_32", "32")
    touchSym_PTC_PRESCALER_Val.setDefaultValue(0)
    touchSym_PTC_PRESCALER_Val.setOutputMode("Value")
    touchSym_PTC_PRESCALER_Val.setDisplayMode("Description")
    touchSym_PTC_PRESCALER_Val.setDescription("The PTC clock is prescaled by PTC and then used for touch measurement.The PTC prescaling factor is defined by this parameter. It is recommended to configure this parameter such that the clock after the prescaler is less than or equal to 1MHz")
    
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
    touchSym_ANALOG_GAIN_Val.setDescription("Gain setting for touch delta value.Higher gain setting increases touch delta as well as noise.So, optimum gain setting should be used.Gain should be tuned such that the touch delta is between 40~60 counts.")
	
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
    touchSym_DIGI_FILT_GAIN_Val.setDescription("Gain setting for touch delta value. Higher gain setting increases touch delta as well as noise. So, optimum gain setting should be used.Gain should be tuned such that the touch delta is between 40~60 counts. ")
	
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
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setDescription("Defines the number of samples taken for each measurement.Higher filter level settings, for each measurements more number of samples taken which helps to average out the noise.Higher filter level settings takes long time to do a touch measurement which affects response time.So, start with default value and increase depends on noise levels.")