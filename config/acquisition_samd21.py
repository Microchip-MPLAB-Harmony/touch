################################################################################
#### Global Variables ####
################################################################################
global touchChannelSelf
global touchChannelMutual
try:
    ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/parameters")
    ptcPinValues = []
    ptcPinValues = ptcPinNode.getChildren()
    touchChannelSelf = ptcPinValues[6].getAttribute("value")
    touchChannelMutual = ptcPinValues[7].getAttribute("value")
except:
    getVariant =  ATDF.getNode("/avr-tools-device-file/devices/device")
    getPinout = []
    getPinout = getVariant.getAttribute("name")
    if ("D21J15" in getPinout):
        touchChannelSelf = 16
        touchChannelMutual = 60
    elif ("D21J16" in getPinout):
        touchChannelSelf = 16
        touchChannelMutual = 130
    elif ("D21J17" in getPinout):
        touchChannelSelf = 16
        touchChannelMutual = 256
    elif ("D21J18" in getPinout):
        touchChannelSelf = 16
        touchChannelMutual = 256
    elif ("D21G15" in getPinout):
        touchChannelSelf = 10
        touchChannelMutual = 60
    elif ("D21G16" in getPinout):
        touchChannelSelf = 10
        touchChannelMutual = 120
    elif ("D21G17" in getPinout):
        touchChannelSelf = 10
        touchChannelMutual = 120
    elif ("D21G18" in getPinout):
        touchChannelSelf = 10
        touchChannelMutual = 120
    elif ("D21E15" in getPinout):
        touchChannelSelf = 6
        touchChannelMutual = 60
    elif ("D21E16" in getPinout):
        touchChannelSelf = 6
        touchChannelMutual = 60
    elif ("D21E17" in getPinout):
        touchChannelSelf = 6
        touchChannelMutual = 60
    elif ("D21E18" in getPinout):
        touchChannelSelf = 6
        touchChannelMutual = 60
    else:
        touchChannelSelf = 16
        touchChannelMutual = 256


def autoTuneFunc(symbol,event):
    global touchAcqLibraryFile
    global touchAcqAutoLibraryFile

    if(event["value"] == 0):
        touchAcqAutoLibraryFile.setEnabled(False)
        touchAcqLibraryFile.setEnabled(True)
    else:
        touchAcqAutoLibraryFile.setEnabled(True)
        touchAcqLibraryFile.setEnabled(False)


global touchAcqLibraryFile
global touchAcqAutoLibraryFile

############################################################################
#### Code Generation ####
############################################################################
# Library File
touchAcqLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_LIB", None)
touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
touchAcqLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
touchAcqLibraryFile.setDestPath("/touch/lib/")
touchAcqLibraryFile.setEnabled(True)
touchAcqLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])

# Library File
touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB", None)
touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
touchAcqAutoLibraryFile.setDestPath("/touch/lib/")
touchAcqAutoLibraryFile.setEnabled(False)
touchAcqAutoLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])

# Library File
touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm0p_0x0005.X.a")
touchBindLibraryFile.setOutputName("qtm_binding_layer_cm0p_0x0005.X.a")
touchBindLibraryFile.setDestPath("/touch/lib/")
touchBindLibraryFile.setEnabled(True)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_acq_samd21_0x0024_api.h")
touchHeaderFile.setOutputName("qtm_acq_samd21_0x0024_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_BIND_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_binding_layer_0x0005_api.h")
touchHeaderFile.setOutputName("qtm_binding_layer_0x0005_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_COMMON_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_common_components_api.h")
touchHeaderFile.setOutputName("qtm_common_components_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

################################################################################
#### Component ####
################################################################################

#Set acquisition module id for the device
getModuleID = qtouchComponent.createStringSymbol("MODULE_ID", touchMenu)
getModuleID.setDefaultValue("0x0024")
getModuleID.setVisible(False)

#Set clock xml for the device
clockXml = qtouchComponent.createStringSymbol("CLOCK_XML", touchMenu)
clockXml.setDefaultValue("d21_clock_config")
clockXml.setVisible(False)

#Set PTC INTERRUPT HANDLER
Database.setSymbolValue("core", InterruptVector, True)
Database.setSymbolValue("core", InterruptHandler, "PTC_Handler")

#Set PTC PERIPHERAL CLOCK
Database.clearSymbolValue("core", "PTC" + "_CLOCK_ENABLE")
Database.setSymbolValue("core", "PTC" + "_CLOCK_ENABLE", True)


#Set Peripheral clocks
Database.setSymbolValue("core", "GCLK_ID_4_GENSEL", 1)
Database.setSymbolValue("core", "GCLK_ID_34_GENSEL", 2)

#Database.setSymbolValue("nvmctrl", "NVM_RWS", 2)

acquisitionMenu = qtouchComponent.createMenuSymbol("ACQUISITION_MENU", touchMenu)
acquisitionMenu.setLabel("Acquisition Configuration")

# Sensing Technology
global touchSenseTechnology
touchSenseTechnology = qtouchComponent.createKeyValueSetSymbol("SENSE_TECHNOLOGY", acquisitionMenu)
touchSenseTechnology.setLabel("Sensor Technology")
touchSenseTechnology.addKey("SelfCap", "NODE_SELFCAP", "Self Capacitance Sensing")
touchSenseTechnology.addKey("MutualCap", "NODE_MUTUAL", "Mutual Capacitance Sensing")
touchSenseTechnology.setDefaultValue(0)
touchSenseTechnology.setOutputMode("Value")
touchSenseTechnology.setDisplayMode("Description")
touchSenseTechnology.setDescription("Selects the sensor technology - Selfcap: Requires one pin per channel; Simple sensor design; Recommended for small number of sensors (less than 12). Mutualcap: Requires one X pin and one Y pin per channel; Can realize X x Y number of sensors in a matrix form; Recommended for large number of sensors (more than 12)")

totalChannelCountSelf = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_SELF",acquisitionMenu)
totalChannelCountSelf.setVisible(True)
totalChannelCountSelf.setDefaultValue(int(touchChannelSelf))

totalChannelCountMutl = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_MUTL",acquisitionMenu)
totalChannelCountMutl.setVisible(True)
totalChannelCountMutl.setDefaultValue(int(touchChannelMutual))

# Select Tuning mode
touchAutoTuneMode = qtouchComponent.createKeyValueSetSymbol("TUNE_MODE_SELECTED", acquisitionMenu)
touchAutoTuneMode.setLabel("Select the Required Tuning Mode")
touchAutoTuneMode.addKey("Manual Tuning","CAL_AUTO_TUNE_NONE","Manual tuning is done based on the values defined by user")
touchAutoTuneMode.addKey("Tune Resistor value","CAL_AUTO_TUNE_RSEL","Series Resistor is tuned")
touchAutoTuneMode.addKey("Tune Prescaler","CAL_AUTO_TUNE_PRSC","Pre-scaler is tuned")
touchAutoTuneMode.setDefaultValue(0)
touchAutoTuneMode.setOutputMode("Value")
touchAutoTuneMode.setDisplayMode("Key")
touchAutoTuneMode.setDescription("Sets the sensor calibration mode - CAL_AUTO_TUNE_NONE: Manual user setting of Prescaler, & Series resistor. CAL_AUTO_TUNE_PRSC: QTouch library will use the configured series resistor value and adjusts the prescaler to ensure full charging.")

#Scan Rate (ms)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MEASUREMENT_PERIOD_MS", acquisitionMenu)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setLabel("Scan Rate (ms)")
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setDefaultValue(20)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setMin(1)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setMax(255)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setDescription("Defines the timer scan rate in milliseconds to initiate periodic touch measurement on all enabled touch sensors.")

#PTC Interrupt Priority
touchSym_PTC_INTERRUPT_PRIORITY_Val = qtouchComponent.createIntegerSymbol("DEF_PTC_INTERRUPT_PRIORITY", acquisitionMenu)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setLabel("PTC Interrupt Priority")
touchSym_PTC_INTERRUPT_PRIORITY_Val.setDefaultValue(3)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setMin(0)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setMax(3)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setDescription("Defines the interrupt priority for the PTC. Set low priority to PTC interrupt for applications having interrupt time constraints.")

#Acquisition Frequency
touchSym_SEL_FREQ_INIT_Val = qtouchComponent.createKeyValueSetSymbol("DEF_SEL_FREQ_INIT", acquisitionMenu)
touchSym_SEL_FREQ_INIT_Val.setLabel("Acquisition Frequency")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_0", "FREQ_SEL_0", "No additional clock cycles (Fastest measurement time) ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_1", "FREQ_SEL_1", "1 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_2", "FREQ_SEL_2", "2 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_3", "FREQ_SEL_3", "3 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_4", "FREQ_SEL_4", "4 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_5", "FREQ_SEL_5", "5 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_6", "FREQ_SEL_6", "6 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_7", "FREQ_SEL_7", "7 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_8", "FREQ_SEL_8", "8 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_9", "FREQ_SEL_9", "9 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_10", "FREQ_SEL_10", "10 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_11", "FREQ_SEL_11", "11 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_12", "FREQ_SEL_12", "12 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_13", "FREQ_SEL_13", "13 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_14", "FREQ_SEL_14", "14 additional clock cycles ")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_15", "FREQ_SEL_15", "15 additional clock cycles (Slowest measurement time")
touchSym_SEL_FREQ_INIT_Val.addKey("FREQ_16", "FREQ_SEL_SPREAD", "16 different frequencies used")
touchSym_SEL_FREQ_INIT_Val.setDefaultValue(0)
touchSym_SEL_FREQ_INIT_Val.setOutputMode("Value")
touchSym_SEL_FREQ_INIT_Val.setDisplayMode("Value")
touchSym_SEL_FREQ_INIT_Val.setDescription("It may be required to change the acquisition frequency if system noise frequency is closer to acquisition frequency.In order to vary the acquisition frequency, additional clock cycles are added during measurement for FREQ_SEL_0 through FREQ_SEL_15. FREQ_SEL_0 provides the fastest measurement time (no additional clock cycles are added) and FREQ_SEL_15 provides the slowest measurement time (15 additional clock cycles are added). When FREQ_SEL_SPREAD option is used, all the 16 frequencies are used consecutively in a circular fashion.")