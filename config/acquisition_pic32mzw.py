################################################################################
#### Global Variables ####
################################################################################
import xml.etree.ElementTree as ET
import os.path
import inspect

global touchChannelSelf
global touchChannelMutual


getVariant =  ATDF.getNode("/avr-tools-device-file/variants/variant")
getPinout = []
getPinout = getVariant.getAttribute("ordercode")
touchChannelSelf = 19
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
touchAcqLibraryFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_LIB", None)
touchAcqLibraryFile.setSourcePath("/src/libraries/hcvd_driver_PIC32MZ1025W104.c")
touchAcqLibraryFile.setOutputName("hcvd_driver_PIC32MZ1025W104.c")
touchAcqLibraryFile.setDestPath("/touch/")
touchAcqLibraryFile.setProjectPath("config/" + configName + "/touch/")
touchAcqLibraryFile.setEnabled(True)
touchAcqLibraryFile.setType("SOURCE")
touchAcqLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])
touchAcqLibraryFile.setMarkup(False)

# Library File
touchAcqAutoLibraryFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_AUTO_LIB", None)
touchAcqAutoLibraryFile.setSourcePath("/src/libraries/hcvd_driver_PIC32MZ1025W104.c")
touchAcqAutoLibraryFile.setOutputName("hcvd_driver_PIC32MZ1025W104.c")
touchAcqAutoLibraryFile.setDestPath("/touch/")
touchAcqAutoLibraryFile.setProjectPath("config/" + configName + "/touch/")
touchAcqAutoLibraryFile.setEnabled(False)
touchAcqAutoLibraryFile.setType("SOURCE")
touchAcqAutoLibraryFile.setDependencies(autoTuneFunc,["TUNE_MODE_SELECTED"])
touchAcqAutoLibraryFile.setMarkup(False)

# Library File
touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_pic32mz_0x0005.X.a")
touchBindLibraryFile.setOutputName("qtm_binding_layer_pic32mz_0x0005.X.a")
touchBindLibraryFile.setDestPath("/touch/lib/")
touchBindLibraryFile.setEnabled(True)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER", None)
touchHeaderFile.setSourcePath("/src/libraries/hcvd_driver_PIC32MZ1025W104.h")
touchHeaderFile.setOutputName("hcvd_driver_PIC32MZ1025W104.h")
touchHeaderFile.setDestPath("/touch/")
touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
touchHeaderFile.setType("HEADER")
touchHeaderFile.setMarkup(False)

# Header File
touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_API_HEADER", None)
touchHeaderFile.setSourcePath("/src/qtm_acq_pic32mzw_0x003e_api.h")
touchHeaderFile.setOutputName("qtm_acq_pic32mzw_0x003e_api.h")
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
getModuleID.setDefaultValue("0x003e")
getModuleID.setVisible(False)

#Set clock xml for the device
clockXml = qtouchComponent.createStringSymbol("CLOCK_XML", touchMenu)
clockXml.setDefaultValue("pic32mzw_clock_config")
clockXml.setVisible(False)

#Set PTC INTERRUPT HANDLER
Database.setSymbolValue("core", InterruptVector, True)
Database.setSymbolValue("core", InterruptHandler, "PTC_Handler")

#Set PTC PERIPHERAL CLOCK and Choose GCLK AS GCLK1
Database.clearSymbolValue("core", "PTC" + "_CLOCK_ENABLE")
Database.setSymbolValue("core", "PTC" + "_CLOCK_ENABLE", True)
Database.clearSymbolValue("core", "GCLK_ID_27_GENSEL")
Database.setSymbolValue("core", "GCLK_ID_27_GENSEL", 1)


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
 
# Enable Driven Shield Plus

dsPins = []
dsPinsTemp = []
dsPinsIndex = []

currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
pinoutXmlPath = os.path.join(currentPath, "../../csp/peripheral/gpio_02467/plugin/pin_xml/pins/MZ_W1_132.xml")
tree = ET.parse(pinoutXmlPath)
root = tree.getroot()
for myPins in root.findall('pins'):
    for myPin in myPins.findall('pin'):
        for myFunction in myPin.findall('function'):
            if myFunction.get("name").startswith("CVDT"):
                tempstring = myPin.get("name")
                index = myFunction.get("name")
                index.replace("CVDT",'')
                dsPinsIndex.append(int(index[4:]))
                dsPinsTemp.append(tempstring)

dsPins = [x for _,x in sorted(zip(dsPinsIndex,dsPinsTemp))]

drivenShieldMenu = qtouchComponent.createMenuSymbol("DRIVEN_SHIELD", touchMenu)
drivenShieldMenu.setLabel("Driven Shield")

#enableDrivenShieldAdjacent = qtouchComponent.createBooleanSymbol("DS_ADJACENT_SENSE_LINE_AS_SHIELD", drivenShieldMenu)
#enableDrivenShieldAdjacent.setLabel("Enable Adjacent Sense Pins as Shield")
#enableDrivenShieldAdjacent.setDefaultValue(False)

enableDrivenShieldDedicated = qtouchComponent.createBooleanSymbol("DS_DEDICATED_PIN_ENABLE", drivenShieldMenu)
enableDrivenShieldDedicated.setLabel("Enable Dedicated Driven Shield Pin")
enableDrivenShieldDedicated.setDefaultValue(False)

drivenShieldDedicatedPin = qtouchComponent.createKeyValueSetSymbol("DS_DEDICATED_PIN", enableDrivenShieldDedicated)
drivenShieldDedicatedPin.setLabel("Select Dedicated Driven Shield Pin")
drivenShieldDedicatedPin.setDefaultValue(0)
drivenShieldDedicatedPin.setDisplayMode("Description")
#drivenShieldDedicatedPin.addKey("--","--","---")
for index in range(0, len(dsPins)):
    drivenShieldDedicatedPin.addKey("X("+str(index)+")",
    str(index),
    "X"+str(index)+"  ("+dsPins[index]+")")
