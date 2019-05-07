################################################################################
#### Global Variables ####
################################################################################

touchChannelSelf = 32
touchChannelMutual = 256


def autoTuneFunc(symbol,event):
    global touchAcqLibraryFile
    global touchAcqAutoLibraryFile

    if(event["value"] == "CAL_AUTO_TUNE_NONE"):
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
touchAcqLibraryFile.setSourcePath("/src/libraries/0x000f_qtm_same51_acq.X.a")
touchAcqLibraryFile.setOutputName("0x000f_qtm_same51_acq.X.a")
touchAcqLibraryFile.setDestPath("/touch/lib/")
touchAcqLibraryFile.setEnabled(True)
touchAcqLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])

# Library File
touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB", None)
touchAcqAutoLibraryFile.setSourcePath("/src/libraries/0x000f_qtm_same51_acq.X.a")
touchAcqAutoLibraryFile.setOutputName("0x000f_qtm_same51_acq.X.a")
touchAcqAutoLibraryFile.setDestPath("/touch/lib/")
touchAcqAutoLibraryFile.setEnabled(False)
touchAcqAutoLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])

# Library File
touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
touchBindLibraryFile.setSourcePath("/src/libraries/0x0005_qtm_binding_layer_cm4.X.a")
touchBindLibraryFile.setOutputName("0x0005_qtm_binding_layer_cm4.X.a")
touchBindLibraryFile.setDestPath("/touch/lib/")
touchBindLibraryFile.setEnabled(True)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_acq_same54_0x000f_api.h")
touchHeaderFile.setOutputName("qtm_acq_same54_0x000f_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

# Header File
touchHeaderFile1 = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER1", None)
touchHeaderFile1.setSourcePath("/src/qtm_acq_same51_0x000f_api.h")
touchHeaderFile1.setOutputName("qtm_acq_same51_0x000f_api.h")
touchHeaderFile1.setDestPath("/touch/")
touchHeaderFile1.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile1.setType("HEADER")
touchHeaderFile1.setMarkup(False)


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
getModuleID.setDefaultValue("0x000f")
getModuleID.setVisible(False)

#Set PTC/ADC0 INTERRUPT HANDLER
Database.setSymbolValue("core", "NVIC_119_0_ENABLE", True)
Database.setSymbolValue("core", "NVIC_119_0_HANDLER", "ADC0_1_Handler")

#Configure DFLL - closed mode
# Database.setSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE", True) 
# Database.setSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE", 1)
# Database.setSymbolValue("core", "CONFIG_CLOCK_DFLL_ONDEMAND", 0) 
# Database.setSymbolValue("core", "CONFIG_CLOCK_DFLL_COARSE", 10)
# Database.setSymbolValue("core", "CONFIG_CLOCK_DFLL_FINE", 10)
# Database.setSymbolValue("core", "CONFIG_CLOCK_DFLL_MUL", 1464)
# Database.setSymbolValue("core", "GCLK_ID_0_GENSEL", 3) 
# Database.setSymbolValue("core", "GCLK_ID_0_CHEN", True)

# #Set GCLK FOR CPU, PTC - GCLK1(DFLL) AT 8MHZ, GCLK0(DFLL) AT 48MHz
# # Database.clearSymbolValue("core", "GCLK_0_SRC")
# # Database.setSymbolValue("core", "GCLK_0_SRC", 6) 
# # Database.clearSymbolValue("core", "GCLK_0_DIV")
# # Database.setSymbolValue("core", "GCLK_0_DIV", 1)
# # Database.setSymbolValue("core", "GCLK_INST_NUM1", True)
# # Database.clearSymbolValue("core", "GCLK_1_SRC")
# # Database.setSymbolValue("core", "GCLK_1_SRC", 5)
# # Database.clearSymbolValue("core", "GCLK_1_DIV") 
# # Database.setSymbolValue("core", "GCLK_1_DIV", 6)

# Database.setSymbolValue("core", "GCLK_INST_NUM3", True)
# Database.setSymbolValue("core", "GCLK_3_SRC", 4) 
# Database.setSymbolValue("core", "GCLK_INST_NUM4", True)
# Database.setSymbolValue("core", "GCLK_4_SRC", 6)
# Database.setSymbolValue("core", "GCLK_4_DIV", 6) 

#Set ADC0 PERIPHERAL CLOCK and Choose GCLK AS GCLK1
Database.clearSymbolValue("core", "ADC0_CLOCK_ENABLE")
Database.setSymbolValue("core", "GCLK_ID_40_CHEN", True)
Database.setSymbolValue("core", "ADC0_CLOCK_ENABLE", True)
Database.clearSymbolValue("core", "GCLK_ID_40_GENSEL")
Database.setSymbolValue("core", "GCLK_ID_40_GENSEL", 4)

acquisitionMenu = qtouchComponent.createMenuSymbol("ACQUISITION_MENU", touchMenu)
acquisitionMenu.setLabel("Acquisition Configuration")

# Sensing Technology
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
touchAutoTuneMode.addKey("Tune CSD","CAL_AUTO_TUNE_CSD","Charge Share Delay - CSD is tuned")
touchAutoTuneMode.setDefaultValue(0)
touchAutoTuneMode.setOutputMode("Value")
touchAutoTuneMode.setDisplayMode("Key")
touchAutoTuneMode.setDescription("Sets the sensor calibration mode - CAL_AUTO_TUNE_NONE: Manual user setting of Prescaler, Charge share delay & Series resistor. AUTO_TUNE_CSD: QTouch library will use the configured prescaler and series resistor value and adjusts the CSD to ensure full charging.")

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
touchSym_PTC_INTERRUPT_PRIORITY_Val.setDefaultValue(2)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setMin(0)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setMax(2)
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
 