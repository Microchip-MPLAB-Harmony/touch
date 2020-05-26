############################################################################
#### Code Generation ####
############################################################################
global qtouchFilesArray

if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
    # Library File
    touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
    touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm4_0x0002.X.a")
    touchLibraryFile.setOutputName("qtm_touch_key_cm4_0x0002.X.a")
    touchLibraryFile.setDestPath("/touch/lib/")
    touchLibraryFile.setEnabled(True)
elif (getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
    # Library File
    touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
    touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm23_0x0002.X.a")
    touchLibraryFile.setOutputName("qtm_touch_key_cm23_0x0002.X.a")
    touchLibraryFile.setDestPath("/touch/lib/")
    touchLibraryFile.setEnabled(True)
elif (getDeviceName.getDefaultValue() in ["PIC32MZW"]):
    # Library File
    touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
    touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_pic32mz_0x0002.X.a")
    touchLibraryFile.setOutputName("qtm_touch_key_pic32mz_0x0002.X.a")
    touchLibraryFile.setDestPath("/touch/lib/")
    touchLibraryFile.setEnabled(True)
else:
    # Library File
    touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
    touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm0p_0x0002.X.a")
    touchLibraryFile.setOutputName("qtm_touch_key_cm0p_0x0002.X.a")
    touchLibraryFile.setDestPath("/touch/lib/")
    touchLibraryFile.setEnabled(True)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KEY_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_touch_key_0x0002_api.h")
touchHeaderFile.setOutputName("qtm_touch_key_0x0002_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    qtouchFilesArray.append(touchHeaderFile)
    qtouchFilesArray.append(touchLibraryFile)


################################################################################
#### Global Variables ####
################################################################################
touchKeyCountMax = touchChannelCountMax
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
    touchKeyEnable.setDefaultValue(False)

    #Sensor Detect Threshold
    touchSym_SENSOR_DET_THRESHOLD_Val = qtouchComponent.createIntegerSymbol("DEF_SENSOR_DET_THRESHOLD" + str(channelID), touchKeyEnable)
    touchSym_SENSOR_DET_THRESHOLD_Val.setLabel("Sensor Detect Threshold")
    touchSym_SENSOR_DET_THRESHOLD_Val.setDefaultValue(20)
    touchSym_SENSOR_DET_THRESHOLD_Val.setMin(0)
    touchSym_SENSOR_DET_THRESHOLD_Val.setMax(255)
    touchSym_SENSOR_DET_THRESHOLD_Val.setDescription("Configure the sensor's detect threshold. When finger touches sensor, the touch delta increases.Sensor will be reported as touched only if the sensor's touch delta value is more than Sensor Threshold.It is recommended to configure Sensor Threshold as 50~70% of touch delta. User can start with default value and can configure after monitoring touch delta value.")
    
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
    touchSym_SENSOR_HYST_Val.setDescription("Under noisy conditions, the delta value goes up/down over the sensor threshold.During these conditions, the sensor dither in and out of touch.To avoid this, once a sensor goes into detect state, the threshold for the sensor is reduced (by the hysteresis value).Hysteresis values are derived from Sensor Threshold value.")
    
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
    touchSym_NOD_AKS_Val.setDescription("Configures the Adjacent Keys Suppression (AKS).AKS can be used when touching multiple sensors are not allowed in a system or When sensors are physically closer to each other. When sensors are closer to each other, there is a possibility that touching one sensor causes rise in touch delta value on other adjacent sensors. At times the delta raise in other sensors may cross threshold and could report false detection.When such sensors are configured in same AKS group, only the first sensor (which goes in to detect) will be reported as touched.All other sensor's state will be suppressed even if their delta crosses Sensor Threshold.Default: AKS is not used.")



