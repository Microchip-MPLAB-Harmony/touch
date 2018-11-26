################################################################################
#### Global Variables ####
################################################################################
freqHopStepsDefault = 3
freqHopStepsMax = 7


################################################################################
#### Business Logic ####
################################################################################
def setFreqHopEnableProperty(symbol, event):
    channelId = int(symbol.getID().strip("HOP_FREQ"))

    channelCount = int(event["value"])

    print channelCount, channelId
    if channelId < channelCount:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
        
def enableFreqHopAutoTuneParameters(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("DEF_TOUCH_MAX_VARIANCE").setVisible(True)
        component.getSymbolByID("DEF_TOUCH_TUNE_IN_COUNT").setVisible(True)
    else:
        component.getSymbolByID("DEF_TOUCH_MAX_VARIANCE").setVisible(False)
        component.getSymbolByID("DEF_TOUCH_TUNE_IN_COUNT").setVisible(False)

################################################################################
#### Component ####
################################################################################

freqSteps = qtouchComponent.createIntegerSymbol("FREQ_HOP_STEPS", enableFreqHopMenu)
freqSteps.setLabel("Frequency Hop Steps")
freqSteps.setDefaultValue(freqHopStepsDefault)
freqSteps.setMin(3)
freqSteps.setMax(freqHopStepsMax)
freqSteps.setVisible(False)

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
    touchSym_HOP_FREQ_Val.setVisible(False)
    touchSym_HOP_FREQ_Val.setDependencies(setFreqHopEnableProperty, ["FREQ_HOP_STEPS"])

    if(freqID>=freqHopStepsDefault):
        touchSym_HOP_FREQ_Val.setVisible(False)

#Frequency Auto Tuning
enableFreqHopAutoTuneMenu = qtouchComponent.createBooleanSymbol("FREQ_AUTOTUNE", enableFreqHopMenu)
enableFreqHopAutoTuneMenu.setLabel("Enable Frequency Auto Tuning")
enableFreqHopAutoTuneMenu.setVisible(False)
enableFreqHopAutoTuneMenu.setDependencies(enableFreqHopAutoTuneParameters,["FREQ_AUTOTUNE"])

#Frequency Auto Tuning - Maximum Variance
touchSym_VARIANCE_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MAX_VARIANCE", enableFreqHopAutoTuneMenu)
touchSym_VARIANCE_Val.setLabel("Maximum Variance")
touchSym_VARIANCE_Val.setDefaultValue(25)
touchSym_VARIANCE_Val.setMin(1)
touchSym_VARIANCE_Val.setMax(255)
touchSym_VARIANCE_Val.setVisible(False)

#Frequency Auto Tuning - Tune-in count
touchSym_TUNE_IN_COUNT_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_TUNE_IN_COUNT", enableFreqHopAutoTuneMenu)
touchSym_TUNE_IN_COUNT_Val.setLabel("Maximum Tune-in count")
touchSym_TUNE_IN_COUNT_Val.setDefaultValue(6)
touchSym_TUNE_IN_COUNT_Val.setMin(1)
touchSym_TUNE_IN_COUNT_Val.setMax(255)
touchSym_TUNE_IN_COUNT_Val.setVisible(False)


