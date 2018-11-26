############################################################################
#### Code Generation ####
############################################################################
# Library File
touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
touchLibraryFile.setSourcePath("/src/libraries/0x0002_qtm_touch_key.X.a")
touchLibraryFile.setOutputName("0x0002_qtm_touch_key.X.a")
touchLibraryFile.setDestPath("/libraries/")
touchLibraryFile.setEnabled(True)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KEY_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_touch_key_0x0002_api.h")
touchHeaderFile.setOutputName("qtm_touch_key_0x0002_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

################################################################################
#### Global Variables ####
################################################################################
touchKeyCountMax = 2


################################################################################
#### Business Logic ####
################################################################################
def setKeyChannelEnableProperty(symbol, event):
    channelId = int(symbol.getID().strip("TOUCH_ENABLE_KEY_"))

    channelCount = int(event["value"])

    if channelId < channelCount:
        symbol.setVisible(True)
        symbol.setValue(True, 1)
    else:
        symbol.setVisible(False)
        symbol.setValue(False, 1)

################################################################################
#### Component ####
################################################################################
keyMenu = qtouchComponent.createMenuSymbol("KEY_MENU", touchMenu)
keyMenu.setLabel("Key Configuration")
keyMenu.setDescription("Configure Keys")

# Touch Channel Enable Count
touchKeyNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_KEY_ENABLE_CNT", keyMenu)
touchKeyNumChannel.setLabel("Number of keys to enable")
touchKeyNumChannel.setDefaultValue(0)
touchKeyNumChannel.setMin(0)
touchKeyNumChannel.setMax(touchKeyCountMax)

for channelID in range(0, touchKeyCountMax):

    touchKeyEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_KEY_" + str(channelID), keyMenu)
    touchKeyEnable.setLabel("Use touch channel " + str(channelID))
    touchKeyEnable.setDependencies(setKeyChannelEnableProperty, ["TOUCH_KEY_ENABLE_CNT"])

    if(channelID>=0):
        touchKeyEnable.setVisible(False)
    else:
        touchKeyEnable.setDefaultValue(True)

    #Sensor Detect Threshold
    touchSym_SENSOR_DET_THRESHOLD_Val = qtouchComponent.createIntegerSymbol("DEF_SENSOR_DET_THRESHOLD" + str(channelID), touchKeyEnable)
    touchSym_SENSOR_DET_THRESHOLD_Val.setLabel("Sensor Detect Threshold")
    touchSym_SENSOR_DET_THRESHOLD_Val.setDefaultValue(20)
    touchSym_SENSOR_DET_THRESHOLD_Val.setMin(0)
    touchSym_SENSOR_DET_THRESHOLD_Val.setMax(255)

    #Sensor Hysteresis
    touchSym_SENSOR_HYST_Val = qtouchComponent.createKeyValueSetSymbol("DEF_SENSOR_HYST" + str(channelID), touchKeyEnable)
    touchSym_SENSOR_HYST_Val.setLabel("Sensor Hysteresis")
    touchSym_SENSOR_HYST_Val.addKey("HYST50", "HYST_50", "50 %")
    touchSym_SENSOR_HYST_Val.addKey("HYST25", "HYST_25", "25 %")
    touchSym_SENSOR_HYST_Val.addKey("HYST125", "HYST_12_5", "12.5 %")
    touchSym_SENSOR_HYST_Val.addKey("HYST625", "HYST_6_25", "6.25 %")
    touchSym_SENSOR_HYST_Val.setDefaultValue(1)
    touchSym_SENSOR_HYST_Val.setOutputMode("Value")
    touchSym_SENSOR_HYST_Val.setDisplayMode("Description")

    #Sensor AKS Setting
    touchSym_NOD_AKS_Val = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_AKS" + str(channelID), touchKeyEnable)
    touchSym_NOD_AKS_Val.setLabel("Sensor AKS")
    touchSym_NOD_AKS_Val.addKey("AKS0", "NO_AKS_GROUP", "No AKS")
    touchSym_NOD_AKS_Val.addKey("AKS1", "AKS_GROUP_1", "AKS Group 1")
    touchSym_NOD_AKS_Val.addKey("AKS2", "AKS_GROUP_2", "AKS Group 2")
    touchSym_NOD_AKS_Val.addKey("AKS3", "AKS_GROUP_3", "AKS Group 3")
    touchSym_NOD_AKS_Val.addKey("AKS4", "AKS_GROUP_4", "AKS Group 4")
    touchSym_NOD_AKS_Val.addKey("AKS5", "AKS_GROUP_5", "AKS Group 5")
    touchSym_NOD_AKS_Val.addKey("AKS6", "AKS_GROUP_6", "AKS Group 6")
    touchSym_NOD_AKS_Val.addKey("AKS7", "AKS_GROUP_7", "AKS Group 7")
    touchSym_NOD_AKS_Val.setDefaultValue(0)
    touchSym_NOD_AKS_Val.setOutputMode("Value")
    touchSym_NOD_AKS_Val.setDisplayMode("Description")




