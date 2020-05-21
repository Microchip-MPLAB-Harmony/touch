################################################################################
#### Global Variables ####
################################################################################
global touchChannelSelf
global touchChannelMutual

getVariant =  ATDF.getNode("/avr-tools-device-file/variants/variant")
getPinout = []
getPinout = getVariant.getAttribute("ordercode")
if ("L10D14" in getPinout):
    touchChannelSelf = 16
    touchChannelMutual = 64
elif ("L10D15" in getPinout):
    touchChannelSelf = 16
    touchChannelMutual = 64
elif ("L10D16" in getPinout):
    touchChannelSelf = 16
    touchChannelMutual = 64
elif ("L10E14" in getPinout):
    touchChannelSelf = 20
    touchChannelMutual = 100
elif ("L10E15" in getPinout):
    touchChannelSelf = 20
    touchChannelMutual = 100
elif ("L10E16" in getPinout):
    touchChannelSelf = 20
    touchChannelMutual = 100
else:
    touchChannelSelf = 16
    touchChannelMutual = 64
def autoTune4pFunc(symbol,event):
    global touchAcq4pLibraryFile
    global touchAcq4pAutoLibraryFile

    if(event["value"] == False):
        touchAcqAutoLibraryFile.setEnabled(True)
        touchAcqLibraryFile.setEnabled(True)
        touchAcq4pAutoLibraryFile.setEnabled(False)
        touchAcq4pLibraryFile.setEnabled(False)
        touch4pHeaderFile.setEnabled(False)
        touchAcqHeaderFile.setEnabled(True)
    else:
        touchAcq4pAutoLibraryFile.setEnabled(True)
        touchAcq4pLibraryFile.setEnabled(True)
        touchAcqAutoLibraryFile.setEnabled(False)
        touchAcqLibraryFile.setEnabled(False)
        touchAcqHeaderFile.setEnabled(False)
        touch4pHeaderFile.setEnabled(True)



global touchAcq4pLibraryFile
global touchAcq4pAutoLibraryFile
global touchAcqHeaderFile
global touch4pHeaderFile

def autoTuneFunc(symbol,event):
    global touchAcqLibraryFile
    global touchAcqAutoLibraryFile

    if(event["value"] == 0):
        touchAcqAutoLibraryFile.setEnabled(False)
        touchAcqLibraryFile.setEnabled(True)
        touchHeaderFile.setEnabled(True)

    else:
        touchAcqAutoLibraryFile.setEnabled(True)
        touchAcqLibraryFile.setEnabled(False)
        touchHeaderFile.setEnabled(True)

global touchAcqLibraryFile
global touchAcqAutoLibraryFile
############################################################################
#### Code Generation ####
############################################################################
# Library File
touchAcqLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_LIB", None)
touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml10_0x0027.X.a")
touchAcqLibraryFile.setOutputName("qtm_acq_saml10_0x0027.X.a")
touchAcqLibraryFile.setDestPath("/touch/lib/")
touchAcqLibraryFile.setEnabled(True)
touchAcqLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])
# Library File
touchAcq4pLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_4P_LIB", None)
touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_saml10_0x0033.X.a")
touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_saml10_0x0033.X.a")
touchAcq4pLibraryFile.setDestPath("/touch/lib/")
touchAcq4pLibraryFile.setEnabled(True)
touchAcq4pLibraryFile.setDependencies(autoTune4pFunc,["ENABLE_4p"])
# Library File
touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB", None)
touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml10_0x0027.X.a")
touchAcqAutoLibraryFile.setOutputName("qtm_acq_saml10_0x0027.X.a")
touchAcqAutoLibraryFile.setDestPath("/touch/lib/")
touchAcqAutoLibraryFile.setEnabled(False)
touchAcqAutoLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])
# Library File
touchAcq4pAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_4P_AUTO_LIB", None)
touchAcq4pAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_saml10_0x0033.X.a")
touchAcq4pAutoLibraryFile.setOutputName("qtm_acq_4p_saml10_0x0033.X.a")
touchAcq4pAutoLibraryFile.setDestPath("/touch/lib/")
touchAcq4pAutoLibraryFile.setEnabled(False)
touchAcq4pAutoLibraryFile.setDependencies(autoTune4pFunc,["ENABLE_4p"])
# Library File
touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm23_0x0005.X.a")
touchBindLibraryFile.setOutputName("qtm_binding_layer_cm23_0x0005.X.a")
touchBindLibraryFile.setDestPath("/touch/lib/")
touchBindLibraryFile.setEnabled(True)

# Header File
touchAcqHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER", None)
touchAcqHeaderFile.setSourcePath("/src/qtm_acq_saml10_0x0027_api.h")
touchAcqHeaderFile.setOutputName("qtm_acq_saml10_0x0027_api.h")
touchAcqHeaderFile.setDestPath("/touch/")
touchAcqHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchAcqHeaderFile.setType("HEADER")
touchAcqHeaderFile.setMarkup(False)
touchAcqHeaderFile.setDependencies(autoTune4pFunc,["ENABLE_4p"])


# Header File
touch4pHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_4P_HEADER", None)
touch4pHeaderFile.setSourcePath("/src/qtm_acq_4p_saml10_0x0033_api.h")
touch4pHeaderFile.setOutputName("qtm_acq_4p_saml10_0x0033_api.h")
touch4pHeaderFile.setDestPath("/touch/")
touch4pHeaderFile.setProjectPath("config/" + configName + "/touch/")
touch4pHeaderFile.setType("HEADER")
touch4pHeaderFile.setMarkup(False)
touch4pHeaderFile.setDependencies(autoTune4pFunc,["ENABLE_4p"])


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
getModuleID.setDefaultValue("0x0027")
getModuleID.setVisible(False)

#Set clock xml for the device
clockXml = qtouchComponent.createStringSymbol("CLOCK_XML", touchMenu)
clockXml.setDefaultValue("l1x_clock_config")
clockXml.setVisible(False)

#Set PTC INTERRUPT HANDLER
Database.setSymbolValue("core", InterruptVector, True)
Database.setSymbolValue("core", InterruptHandler, "PTC_Handler")

#Set PTC PERIPHERAL CLOCK and Choose GCLK AS GCLK1
Database.clearSymbolValue("core", "PTC" + "_CLOCK_ENABLE")
Database.setSymbolValue("core", "PTC" + "_CLOCK_ENABLE", True)
Database.clearSymbolValue("core", "GCLK_ID_19_GENSEL")
Database.setSymbolValue("core", "GCLK_ID_19_GENSEL", 1)

acquisitionMenu = qtouchComponent.createMenuSymbol("ACQUISITION_MENU", touchMenu)
acquisitionMenu.setLabel("Acquisition Configuration")

# Sensing Technology
global touchSenseTechnology
touchSenseTechnology = qtouchComponent.createKeyValueSetSymbol("SENSE_TECHNOLOGY", acquisitionMenu)
touchSenseTechnology.setLabel("Sensor Technology")
touchSenseTechnology.addKey("SelfCap", "NODE_SELFCAP", "Self Capacitance Sensing")
touchSenseTechnology.addKey("MutualCap", "NODE_MUTUAL", "Mutual Capacitance Sensing")
touchSenseTechnology.addKey("SelfCapShield", "NODE_SELFCAP_SHIELD", "Self-Capacitance Sensing With Driven Shield")
touchSenseTechnology.setDefaultValue(0)
touchSenseTechnology.setOutputMode("Value")
touchSenseTechnology.setDisplayMode("Description")
touchSenseTechnology.setDescription("Selects the sensor technology - Selfcap: Requires one pin per channel; Simple sensor design; Recommended for small number of sensors (less than 12). SelfCapShield: Requires one pin per channel with Driven shield options; Simple sensor design; Recommended for small number of sensors (less than 12). Mutualcap: Requires one X pin and one Y pin per channel; Can realize X x Y number of sensors in a matrix form; Recommended for large number of sensors (more than 12)")

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
 
# Enable Driven Shield Plus
drivenShieldMenu = qtouchComponent.createMenuSymbol("DRIVEN_SHIELD", touchMenu)
drivenShieldMenu.setLabel("Driven Shield")

global enableDrivenShieldAdjacent
enableDrivenShieldAdjacent = qtouchComponent.createBooleanSymbol("DS_ADJACENT_SENSE_LINE_AS_SHIELD", drivenShieldMenu)
enableDrivenShieldAdjacent.setLabel("Enable Adjacent Sense Pins as Shield")
enableDrivenShieldAdjacent.setDefaultValue(False)

global enableDrivenShieldDedicated
enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_PIN_ENABLE", drivenShieldMenu)
enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
enableDrivenShieldDedicated.setDefaultValue(False)

global drivenShieldDedicatedPin
drivenShieldDedicatedPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_PIN", enableDrivenShieldDedicated)
drivenShieldDedicatedPin.setLabel("Select Dedicated Driven Shield Pin")
drivenShieldDedicatedPin.setOutputMode("Value")
drivenShieldDedicatedPin.setDefaultValue(0)
drivenShieldDedicatedPin.setDisplayMode("Description")
ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
ptcPinValues = []
ptcPinValues = ptcPinNode.getChildren()
for index in range(0, len(ptcPinValues)):
    if(ptcPinValues[index].getAttribute("group") == "Y"):
        drivenShieldDedicatedPin.addKey(ptcPinValues[index].getAttribute("index"),ptcPinValues[index].getAttribute("group")+"("+ptcPinValues[index].getAttribute("index")+")",ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index")+ "  ("+ ptcPinValues[index].getAttribute("pad")+")")

