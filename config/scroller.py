############################################################################
#### Code Generation ####
############################################################################
# Library File
scrollerLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SCR_LIB", None)
scrollerLibraryFile.setSourcePath("/src/libraries/0x000b_qtm_scroller.X.a")
scrollerLibraryFile.setOutputName("0x000b_qtm_scroller.X.a")
scrollerLibraryFile.setDestPath("/touch/lib/")
scrollerLibraryFile.setEnabled(True)

# Header File
scrollerHeaderFile = qtouchComponent.createFileSymbol("TOUCH_SCR_HEADER", None)
scrollerHeaderFile.setSourcePath("/src/qtm_scroller_0x000b_api.h")
scrollerHeaderFile.setOutputName("qtm_scroller_0x000b_api.h")
scrollerHeaderFile.setDestPath("/touch/")
scrollerHeaderFile.setProjectPath("config/" + configName + "/touch/")
scrollerHeaderFile.setType("HEADER")
scrollerHeaderFile.setMarkup(False)

################################################################################
#### Global Variables ####
################################################################################
touchScrollerCountMax = touchChannelCountMax
################################################################################
#### Components ####
################################################################################

scrollerMenu = qtouchComponent.createMenuSymbol("SCROLLER_MENU", touchMenu)
scrollerMenu.setLabel("Slider/Wheel Configuration")
scrollerMenu.setDescription("Configure Scrollers - Sliders and Wheels")

touchSCRNum = qtouchComponent.createIntegerSymbol("TOUCH_SCROLLER_ENABLE_CNT", scrollerMenu)
touchSCRNum.setLabel("Number of slider/wheel to enable")
touchSCRNum.setDefaultValue(0)
touchSCRNum.setMin(0)
touchSCRNum.setMax(touchScrollerCountMax)

for channelID in range(0, touchScrollerCountMax):

    touchScrollerEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_SCROLLER_" + str(channelID), scrollerMenu)
    touchScrollerEnable.setLabel("Use scroller " + str(channelID))
    touchScrollerEnable.setDefaultValue(False)
    
    touchScrollerType = qtouchComponent.createKeyValueSetSymbol("DEF_SCR_TYPE" + str(channelID), touchScrollerEnable)
    touchScrollerType.setLabel("Choose the scroller type")
    touchScrollerType.addKey("SCROLLER_TYPE_SLIDER","SCROLLER_TYPE_SLIDER","Slider")
    touchScrollerType.addKey("SCROLLER_TYPE_WHEEL","SCROLLER_TYPE_WHEEL","Wheel")
    touchScrollerType.setDefaultValue(0)
    touchScrollerType.setOutputMode("Value")
    touchScrollerType.setDisplayMode("Description")
    
    touchScrollerNum = qtouchComponent.createIntegerSymbol("TOUCH_SCR_SIZE" + str(channelID), touchScrollerEnable)
    touchScrollerNum.setLabel("Number of buttons or segments that constitute a slider/wheel")
    touchScrollerNum.setDefaultValue(3)
    touchScrollerNum.setMin(2)
    touchScrollerNum.setMax(touchKeyCountMax)
    touchScrollerNum.setDescription("The slider/wheel is made up of multiple buttons. This parameter defines how may buttons or segments constitute a slider/wheel.")
    
    touchScrollerNumChannels = qtouchComponent.createIntegerSymbol("TOUCH_SCR_START_KEY"+ str(channelID), touchScrollerEnable)
    touchScrollerNumChannels.setLabel("Starting key number of this scroller")
    touchScrollerNumChannels.setDefaultValue(0)
    touchScrollerNumChannels.setMin(0)
    touchScrollerNumChannels.setMax(touchKeyCountMax)
    touchScrollerNumChannels.setDescription("A scroller is made of multiple buttons. This parameter defines the starting button number of this scroller.")

    #Scroller Resolution
    touchSym_SCR_RESOLUTION_Val = qtouchComponent.createKeyValueSetSymbol("DEF_SCR_RESOLUTION" + str(channelID), touchScrollerEnable)
    touchSym_SCR_RESOLUTION_Val.setLabel("Scroller Resolution")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_2_BIT","RESOL_2_BIT","2 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_3_BIT","RESOL_3_BIT","3 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_4_BIT","RESOL_4_BIT","4 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_5_BIT","RESOL_5_BIT","5 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_6_BIT","RESOL_6_BIT","6 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_7_BIT","RESOL_7_BIT","7 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_8_BIT","RESOL_8_BIT","8 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_9_BIT","RESOL_9_BIT","9 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_10_BIT","RESOL_10_BIT","10 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_11_BIT","RESOL_11_BIT","11 bit")
    touchSym_SCR_RESOLUTION_Val.addKey("RESOL_12_BIT","RESOL_12_BIT","12 bit")
    touchSym_SCR_RESOLUTION_Val.setDefaultValue(6)
    touchSym_SCR_RESOLUTION_Val.setOutputMode("Value")
    touchSym_SCR_RESOLUTION_Val.setDisplayMode("Description")
    touchSym_SCR_RESOLUTION_Val.setDescription("Defines the resolution of slider/wheel in bits. A value of 8 indicates 256 positions. The slider/wheel value will be reported from 0 to 255.")

    #Scroller Deadband
    touchSym_SCR_DEADBAND_Val = qtouchComponent.createKeyValueSetSymbol("DEF_SCR_DEADBAND" + str(channelID), touchScrollerEnable)
    touchSym_SCR_DEADBAND_Val.setLabel("Scroller Deadband")
    touchSym_SCR_DEADBAND_Val.addKey("DB_NONE", "DB_NONE", "no deadband")
    touchSym_SCR_DEADBAND_Val.addKey("DB_1_PERCENT", "DB_1_PERCENT", "1percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_2_PERCENT", "DB_2_PERCENT", "2percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_3_PERCENT", "DB_3_PERCENT", "3percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_4_PERCENT", "DB_4_PERCENT", "4percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_5_PERCENT", "DB_5_PERCENT", "5percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_6_PERCENT", "DB_6_PERCENT", "6percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_7_PERCENT", "DB_7_PERCENT", "7percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_8_PERCENT", "DB_8_PERCENT", "8percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_9_PERCENT", "DB_9_PERCENT", "9percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_10_PERCENT", "DB_10_PERCENT", "10percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_11_PERCENT", "DB_11_PERCENT", "11percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_12_PERCENT", "DB_12_PERCENT", "12percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_13_PERCENT", "DB_13_PERCENT", "13percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_14_PERCENT", "DB_14_PERCENT", "14percent")
    touchSym_SCR_DEADBAND_Val.addKey("DB_15_PERCENT", "DB_15_PERCENT", "15percent")
    touchSym_SCR_DEADBAND_Val.setDefaultValue(10)
    touchSym_SCR_DEADBAND_Val.setOutputMode("Value")
    touchSym_SCR_DEADBAND_Val.setDisplayMode("Description")
    touchSym_SCR_DEADBAND_Val.setDescription("Defines the inactive area on both ends of the slider/wheel where no change in position is reported. If deadband is 10percent,  then inactive area is 10% of slider/wheel length on each end.")

    #Position Hysterisis
    touchSym_SCR_POS_HYST_Val = qtouchComponent.createIntegerSymbol("DEF_SCR_POS_HYS" + str(channelID), touchScrollerEnable)
    touchSym_SCR_POS_HYST_Val.setLabel("Scroller Position Hysterisis")
    touchSym_SCR_POS_HYST_Val.setDefaultValue(8)
    touchSym_SCR_POS_HYST_Val.setMin(0)
    touchSym_SCR_POS_HYST_Val.setMax(255)
    touchSym_SCR_POS_HYST_Val.setDescription("Hysteresis is the number of positions the user has to move back, before the new touch position is reported when the direction of scrolling is changed and during first scroll after touch down.")

    #Contact min threshold
    touchSym_SCR_THRESHOLD_Val = qtouchComponent.createIntegerSymbol("DEF_SCR_CONTACT_THRESHOLD" + str(channelID), touchScrollerEnable)
    touchSym_SCR_THRESHOLD_Val.setLabel("Scroller Detect threshold")
    touchSym_SCR_THRESHOLD_Val.setDefaultValue(20)
    touchSym_SCR_THRESHOLD_Val.setMin(0)
    touchSym_SCR_THRESHOLD_Val.setMax(65535)
    touchSym_SCR_THRESHOLD_Val.setDescription("Defines the threshold for slider/wheel touch delta to detect a user touch. It is recommended to configure the slider/wheel detect threshold to around 50% of minimum slider/wheel touch delta reported when sliding from end to end.")

