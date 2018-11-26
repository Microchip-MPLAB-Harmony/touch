################################################################################
#### Global Variables ####
################################################################################
global touchAutoTuneMode
global touchAcqLibraryFile
global touchAcqAutoLibraryFile

def autoTuneFunc(symbol,event):
	if(event["value"] == True):
	    touchAutoTuneMode.setVisible(True)
	    touchAcqAutoLibraryFile.setEnabled(True)
	    touchAcqLibraryFile.setEnabled(False)
	else:
	    touchAutoTuneMode.setVisible(False)
	    touchAcqAutoLibraryFile.setEnabled(False)
	    touchAcqLibraryFile.setEnabled(True)
		
############################################################################
#### Code Generation ####
############################################################################
# Library File
touchAcqLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_LIB", None)
touchAcqLibraryFile.setSourcePath("/src/libraries/0x0020_qtm_samc21_acq.X.a")
touchAcqLibraryFile.setOutputName("0x0020_qtm_samc21_acq.X.a")
touchAcqLibraryFile.setDestPath("/libraries/")
touchAcqLibraryFile.setEnabled(True)
touchAcqLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE"])

# Library File
touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB", None)
touchAcqAutoLibraryFile.setSourcePath("/src/libraries/0x0020_qtm_samc21_acq_auto.X.a")
touchAcqAutoLibraryFile.setOutputName("0x0020_qtm_samc21_acq_auto.X.a")
touchAcqAutoLibraryFile.setDestPath("/libraries/")
touchAcqAutoLibraryFile.setEnabled(True)
touchAcqAutoLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE"])

# Library File
touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
touchBindLibraryFile.setSourcePath("/src/libraries/0x0005_qtm_binding_layer.X.a")
touchBindLibraryFile.setOutputName("0x0005_qtm_binding_layer.X.a")
touchBindLibraryFile.setDestPath("/libraries/")
touchBindLibraryFile.setEnabled(True)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_acq_samc21_0x0020_api.h")
touchHeaderFile.setOutputName("qtm_acq_samc21_0x0020_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_BIND_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_binding_layer_0x0005_api.h")
touchHeaderFile.setOutputName("qtm_binding_layer_0x0005_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_COMMON_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_common_components_api.h")
touchHeaderFile.setOutputName("qtm_common_components_api.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

################################################################################
#### Component ####
################################################################################

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

# Tune Mode
touchAutoTune = qtouchComponent.createBooleanSymbol("TUNE_MODE", acquisitionMenu)
touchAutoTune.setLabel("Is Sensor Auto Tuning Required?")
touchAutoTune.setDefaultValue(False)

# Select Tuning mode
touchAutoTuneMode = qtouchComponent.createKeyValueSetSymbol("TUNE_MODE_SELECTED", acquisitionMenu)
touchAutoTuneMode.setLabel("Select the Required Tuning Mode")
touchAutoTuneMode.addKey("Tune Resistor value","CAL_AUTO_TUNE_RSEL","Series Resistor is tuned")
touchAutoTuneMode.addKey("Tune CSD","CAL_AUTO_TUNE_CSD","Charge Share Delay - CSD is tuned")
touchAutoTuneMode.setDefaultValue(1)
touchAutoTuneMode.setOutputMode("Value")
touchAutoTuneMode.setDisplayMode("Description")
touchAutoTuneMode.setVisible(False)
touchAutoTuneMode.setDependencies(autoTuneFunc,["TUNE_MODE"])

#Scan Rate (ms)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MEASUREMENT_PERIOD_MS", acquisitionMenu)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setLabel("Scan Rate (ms)")
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setDefaultValue(20)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setMin(1)
touchSym_TOUCH_MEASUREMENT_PERIOD_MS_Val.setMax(255)

#PTC Interrupt Priority
touchSym_PTC_INTERRUPT_PRIORITY_Val = qtouchComponent.createIntegerSymbol("DEF_PTC_INTERRUPT_PRIORITY", acquisitionMenu)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setLabel("PTC Interrupt Priority")
touchSym_PTC_INTERRUPT_PRIORITY_Val.setDefaultValue(2)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setMin(0)
touchSym_PTC_INTERRUPT_PRIORITY_Val.setMax(2)

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
touchSym_SEL_FREQ_INIT_Val.setDisplayMode("Description")

