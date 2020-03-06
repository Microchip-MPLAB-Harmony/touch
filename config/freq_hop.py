################################################################################
#### Global Variables ####
################################################################################
def freqAutoTuneFunc(symbol,event):
    global freqHopLibraryFile
    global freqHopHeaderFile
    global freqHopAutoLibraryFile
    global freqHopAutoHeaderFile
    hopEnabled = enableFreqHopMenu.getValue()

    if(event["value"] == True):
        freqHopLibraryFile.setEnabled(False)
        freqHopHeaderFile.setEnabled(False)
        freqHopAutoLibraryFile.setEnabled(True)
        freqHopAutoHeaderFile.setEnabled(True)
    elif(hopEnabled == True):
        freqHopLibraryFile.setEnabled(True)
        freqHopHeaderFile.setEnabled(True)
        freqHopAutoLibraryFile.setEnabled(False)
        freqHopAutoHeaderFile.setEnabled(False)
    else:
        freqHopAutoLibraryFile.setEnabled(False)
        freqHopAutoHeaderFile.setEnabled(False)

global freqHopLibraryFile
global freqHopHeaderFile
global freqHopAutoLibraryFile
global freqHopAutoHeaderFile

############################################################################
#### Code Generation ####
############################################################################
if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
    # Library File
    freqHopLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_LIB", None)
    freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_cm4_0x0006.X.a")
    freqHopLibraryFile.setOutputName("qtm_freq_hop_cm4_0x0006.X.a")
    freqHopLibraryFile.setDestPath("/touch/lib/")
    freqHopLibraryFile.setEnabled(False)
    freqHopLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])
    # Library File
    freqHopAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_AUTO_LIB", None)
    freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_autotune_cm4_0x0004.X.a")
    freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_autotune_cm4_0x0004.X.a")
    freqHopAutoLibraryFile.setDestPath("/touch/lib/")
    freqHopAutoLibraryFile.setEnabled(False)
    freqHopAutoLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])
elif(getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
    # Library File
    freqHopLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_LIB", None)
    freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_cm23_0x0006.X.a")
    freqHopLibraryFile.setOutputName("qtm_freq_hop_cm23_0x0006.X.a")
    freqHopLibraryFile.setDestPath("/touch/lib/")
    freqHopLibraryFile.setEnabled(False)
    freqHopLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])
    # Library File
    freqHopAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_AUTO_LIB", None)
    freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_autotune_cm23_0x0004.X.a")
    freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_autotune_cm23_0x0004.X.a")
    freqHopAutoLibraryFile.setDestPath("/touch/lib/")
    freqHopAutoLibraryFile.setEnabled(False)
    freqHopAutoLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])
else:
    # Library File
    freqHopLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_LIB", None)
    freqHopLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_cm0p_0x0006.X.a")
    freqHopLibraryFile.setOutputName("qtm_freq_hop_cm0p_0x0006.X.a")
    freqHopLibraryFile.setDestPath("/touch/lib/")
    freqHopLibraryFile.setEnabled(False)
    freqHopLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])
    # Library File
    freqHopAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_AUTO_LIB", None)
    freqHopAutoLibraryFile.setSourcePath("/src/libraries/qtm_freq_hop_autotune_cm0p_0x0004.X.a")
    freqHopAutoLibraryFile.setOutputName("qtm_freq_hop_autotune_cm0p_0x0004.X.a")
    freqHopAutoLibraryFile.setDestPath("/touch/lib/")
    freqHopAutoLibraryFile.setEnabled(False)
    freqHopAutoLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])

# Header File
freqHopHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HOP_HEADER", None)
freqHopHeaderFile.setSourcePath("/src/qtm_freq_hop_0x0006_api.h")
freqHopHeaderFile.setOutputName("qtm_freq_hop_0x0006_api.h")
freqHopHeaderFile.setDestPath("/touch/")
freqHopHeaderFile.setProjectPath("config/" + configName + "/touch/")
freqHopHeaderFile.setType("HEADER")
freqHopHeaderFile.setMarkup(False)
freqHopHeaderFile.setEnabled(False)
freqHopHeaderFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])

# Header File
freqHopAutoHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HOP_AUTO_HEADER", None)
freqHopAutoHeaderFile.setSourcePath("/src/qtm_freq_hop_auto_0x0004_api.h")
freqHopAutoHeaderFile.setOutputName("qtm_freq_hop_auto_0x0004_api.h")
freqHopAutoHeaderFile.setDestPath("/touch/")
freqHopAutoHeaderFile.setProjectPath("config/" + configName + "/touch/")
freqHopAutoHeaderFile.setType("HEADER")
freqHopAutoHeaderFile.setMarkup(False)
freqHopAutoHeaderFile.setEnabled(False)
freqHopAutoHeaderFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])

################################################################################
#### Global Variables ####
################################################################################
freqHopStepsDefault = 3
freqHopStepsMax = 7

################################################################################
#### Component ####
################################################################################

freqSteps = qtouchComponent.createIntegerSymbol("FREQ_HOP_STEPS", enableFreqHopMenu)
freqSteps.setLabel("Frequency Hop Steps")
freqSteps.setDefaultValue(freqHopStepsDefault)
freqSteps.setMin(3)
freqSteps.setMax(freqHopStepsMax)
freqSteps.setDescription("Defines the number of frequencies used for touch measurement. Noise performance will be good if more number of frequencies are used - but increases response time and RAM usage. If higher number of frequencies needs to be used (to tackle noise), consider enabling frequency auto-tune option.")

for freqID in range(0, freqHopStepsMax):

    #Hop Frequency
    touchSym_HOP_FREQ_Val = qtouchComponent.createKeyValueSetSymbol("HOP_FREQ"+ str(freqID), enableFreqHopMenu)
    touchSym_HOP_FREQ_Val.setLabel("Hop Frequency "+ str(freqID))
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL0", "FREQ_SEL_0", "Frequency 0")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL1", "FREQ_SEL_1", "Frequency 1")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL2", "FREQ_SEL_2", "Frequency 2")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL3", "FREQ_SEL_3", "Frequency 3")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL4", "FREQ_SEL_4", "Frequency 4")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL5", "FREQ_SEL_5", "Frequency 5")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL6", "FREQ_SEL_6", "Frequency 6")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL7", "FREQ_SEL_7", "Frequency 7")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL8", "FREQ_SEL_8", "Frequency 8")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL9", "FREQ_SEL_9", "Frequency 9")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL10", "FREQ_SEL_10", "Frequency 10")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL11", "FREQ_SEL_11", "Frequency 11")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL12", "FREQ_SEL_12", "Frequency 12")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL13", "FREQ_SEL_13", "Frequency 13")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL14", "FREQ_SEL_14", "Frequency 14")
    touchSym_HOP_FREQ_Val.addKey("FREQ_SEL15", "FREQ_SEL_15", "Frequency 15")
    touchSym_HOP_FREQ_Val.setOutputMode("Value")
    touchSym_HOP_FREQ_Val.setDisplayMode("Description")
    touchSym_HOP_FREQ_Val.setDefaultValue(freqID)
    touchSym_HOP_FREQ_Val.setDescription("Sets the Hop Frequencies")

#Frequency Auto Tuning
global enableFreqHopAutoTuneMenu
enableFreqHopAutoTuneMenu = qtouchComponent.createBooleanSymbol("FREQ_AUTOTUNE", enableFreqHopMenu)
enableFreqHopAutoTuneMenu.setLabel("Enable Frequency Auto Tuning")
enableFreqHopAutoTuneMenu.setDefaultValue(False)

#Frequency Auto Tuning - Maximum Variance
touchSym_VARIANCE_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MAX_VARIANCE", enableFreqHopAutoTuneMenu)
touchSym_VARIANCE_Val.setLabel("Maximum Variance")
touchSym_VARIANCE_Val.setDefaultValue(25)
touchSym_VARIANCE_Val.setMin(1)
touchSym_VARIANCE_Val.setMax(255)
touchSym_VARIANCE_Val.setDescription("When frequency auto tune is enabled, the touch measurement frequencies are automatically changed based on noise levels.This parameter sets the threshold for noise level in touch data.If noise level is more than this threshold, then the noisy frequency will be replaced.")

#Frequency Auto Tuning - Tune-in count
touchSym_TUNE_IN_COUNT_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_TUNE_IN_COUNT", enableFreqHopAutoTuneMenu)
touchSym_TUNE_IN_COUNT_Val.setLabel("Maximum Tune-in count")
touchSym_TUNE_IN_COUNT_Val.setDefaultValue(6)
touchSym_TUNE_IN_COUNT_Val.setMin(1)
touchSym_TUNE_IN_COUNT_Val.setMax(255)
touchSym_TUNE_IN_COUNT_Val.setDescription("This parameter acts as an integrator to confirm the noise.The measurement frequency is changed ONLY if noise levels is more than Maximum Variance for Tune In Count measurement cycles. Configuring higher value for Tune in Count might take longer duration to replace a bad frequency. Configuring lower value for Tune in Count might unnecessarily replace frequency.")
