################################################################################
#### Global Variables ####
################################################################################
def freqAutoTuneFunc(symbol,event):
    global freqHopLibraryFile
    global freqHopHeaderFile
    global freqHopAutoLibraryFile
    global freqHopAutoHeaderFile

    if(event["value"] == True):
        freqHopLibraryFile.setEnabled(False)
        freqHopHeaderFile.setEnabled(False)
        freqHopAutoLibraryFile.setEnabled(True)
        freqHopAutoHeaderFile.setEnabled(True)
    else:
        freqHopLibraryFile.setEnabled(True)
        freqHopHeaderFile.setEnabled(True)
        freqHopAutoLibraryFile.setEnabled(False)
        freqHopAutoHeaderFile.setEnabled(False)

global freqHopLibraryFile
global freqHopHeaderFile
global freqHopAutoLibraryFile
global freqHopAutoHeaderFile

############################################################################
#### Code Generation ####
############################################################################
# Library File
freqHopLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_LIB", None)
freqHopLibraryFile.setSourcePath("/src/libraries/0x0006_qtm_freq_hop.X.a")
freqHopLibraryFile.setOutputName("0x0006_qtm_freq_hop.X.a")
freqHopLibraryFile.setDestPath("/qtouch/lib/")
freqHopLibraryFile.setEnabled(True)
freqHopLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])

# Header File
freqHopHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HOP_HEADER", None)
freqHopHeaderFile.setSourcePath("/src/qtm_freq_hop_0x0006_api.h")
freqHopHeaderFile.setOutputName("qtm_freq_hop_0x0006_api.h")
freqHopHeaderFile.setDestPath("/qtouch/")
freqHopHeaderFile.setProjectPath("config/" + configName + "/qtouch/")
freqHopHeaderFile.setType("HEADER")
freqHopHeaderFile.setMarkup(False)
freqHopHeaderFile.setEnabled(True)
freqHopHeaderFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])

# Library File
freqHopAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_HOP_AUTO_LIB", None)
freqHopAutoLibraryFile.setSourcePath("/src/libraries/0x0004_qtm_freq_hop_autotune.X.a")
freqHopAutoLibraryFile.setOutputName("0x0004_qtm_freq_hop_autotune.X.a")
freqHopAutoLibraryFile.setDestPath("/qtouch/lib/")
freqHopAutoLibraryFile.setEnabled(False)
freqHopAutoLibraryFile.setDependencies(freqAutoTuneFunc,["FREQ_AUTOTUNE"])

# Header File
freqHopAutoHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HOP_AUTO_HEADER", None)
freqHopAutoHeaderFile.setSourcePath("/src/qtm_freq_hop_auto_0x0004_api.h")
freqHopAutoHeaderFile.setOutputName("qtm_freq_hop_auto_0x0004_api.h")
freqHopAutoHeaderFile.setDestPath("/qtouch/")
freqHopAutoHeaderFile.setProjectPath("config/" + configName + "/qtouch/")
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


#Frequency Auto Tuning
enableFreqHopAutoTuneMenu = qtouchComponent.createBooleanSymbol("FREQ_AUTOTUNE", enableFreqHopMenu)
enableFreqHopAutoTuneMenu.setLabel("Enable Frequency Auto Tuning")

#Frequency Auto Tuning - Maximum Variance
touchSym_VARIANCE_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MAX_VARIANCE", enableFreqHopAutoTuneMenu)
touchSym_VARIANCE_Val.setLabel("Maximum Variance")
touchSym_VARIANCE_Val.setDefaultValue(25)
touchSym_VARIANCE_Val.setMin(1)
touchSym_VARIANCE_Val.setMax(255)

#Frequency Auto Tuning - Tune-in count
touchSym_TUNE_IN_COUNT_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_TUNE_IN_COUNT", enableFreqHopAutoTuneMenu)
touchSym_TUNE_IN_COUNT_Val.setLabel("Maximum Tune-in count")
touchSym_TUNE_IN_COUNT_Val.setDefaultValue(6)
touchSym_TUNE_IN_COUNT_Val.setMin(1)
touchSym_TUNE_IN_COUNT_Val.setMax(255)


