"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchFreqGroups():
    def __init__(self):
        self.maxGroups = 4
        self.freqHopStepsMax = 7
        self.freqHopStepsDefault = 3
    def getMaxGroups(self):
        """Get maximum acquisition groups
        Arguments:
            :none
        Returns:
            :number of acquistion groups  as (int)
        """
        return int(self.maxGroups)

    def setMaxGroups(self,newMax):
        """Set maximum acquisition groups
        Arguments:
            :newMax - new maximum (int)
        Returns:
            :none
        """
        self.maxGroups = int(newMax)

    #instance
    def initFreqHopGroupInstance(self,qtouchComponent,groupNumber,parentLabel):
        """Initialise frequency hop Group Instance
        Arguments:
            :qtouchComponent : touchModule
            :groupNumber : index of the group instance
            :parentLabel : parent symbol for added menu items
        Returns:
            :none
        """


        if int(groupNumber) == 1:
            freqSteps = qtouchComponent.createIntegerSymbol("FREQ_HOP_STEPS", parentLabel)
            freqSteps.setDependencies(self.freqHopStepCountUpdate,["FREQ_HOP_STEPS"])
            enableFreqHopAutoTuneMenu = qtouchComponent.createBooleanSymbol("FREQ_AUTOTUNE", parentLabel)
            enableFreqHopAutoTuneMenu.setDependencies(self.freqHopUpdateEnabled,["FREQ_AUTOTUNE"])
            maxVariance = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MAX_VARIANCE", enableFreqHopAutoTuneMenu)
            tuneInCount = qtouchComponent.createIntegerSymbol("DEF_TOUCH_TUNE_IN_COUNT", enableFreqHopAutoTuneMenu)
        else:
            freqSteps = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"FREQ_HOP_STEPS", parentLabel)
            freqSteps.setDependencies(self.freqHopStepCountUpdate,["GROUP_"+str(groupNumber)+"FREQ_HOP_STEPS"])
            enableFreqHopAutoTuneMenu = qtouchComponent.createBooleanSymbol("GROUP_"+str(groupNumber)+"FREQ_AUTOTUNE", parentLabel)
            enableFreqHopAutoTuneMenu.setDependencies(self.freqHopUpdateEnabled,["GROUP_"+str(groupNumber)+"FREQ_AUTOTUNE"])
            maxVariance = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"DEF_TOUCH_MAX_VARIANCE", enableFreqHopAutoTuneMenu)
            tuneInCount = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"DEF_TOUCH_TUNE_IN_COUNT", enableFreqHopAutoTuneMenu)

        #parameter assignment
        enableFreqHopAutoTuneMenu.setLabel("Enable Frequency Auto Tuning")
        enableFreqHopAutoTuneMenu.setDefaultValue(False)
        
        self.setFreqHopValues(qtouchComponent,self.freqHopStepsDefault,self.freqHopStepsMax,groupNumber,parentLabel)
        self.setFreqStepsValues(freqSteps,self.freqHopStepsDefault,self.freqHopStepsMax)
        self.setMaxVarianceValues(maxVariance)
        self.setTuneInCountValues(tuneInCount)

    #group
    def initFreqHopGroup(self,qtouchComponent, parentMenu, minVal, maxVal, targetDevice):
        """Initialise Frequency Hop Groups and add to touch Module
        Arguments:
            :qtouchComponent : touchModule
            :parentMenu : parent menu symbol for added menu items
            :minVal : see acquisitionGroupCountMenu.getMin()
            :maxVal : see acquisitionGroupCountMenu.getMax()
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :none
        """
        global maxGroups
        maxGroups = maxVal
        enableFreqHopMenu = qtouchComponent.createBooleanSymbol("ENABLE_FREQ_HOP",  parentMenu)
        enableFreqHopMenu.setLabel("Enable Frequency Hop")
        enableFreqHopMenu.setDefaultValue(True)
        enableFreqHopMenu.setDescription("Frequency Hop is a mechanism used in touch measurement to avoid noisy signal value. In Frequency Hop, more than one bursting frequency (user configurable) is used. Refer QTouch Modular Library Userguide for more details on Frequency Hop.")
        enableFreqHopMenu.setVisible(True)
        enableFreqHopMenu.setEnabled(True)
        enableFreqHopMenu.setDependencies(self.freqHopUpdateEnabled,["ENABLE_FREQ_HOP"])

        for groupNum in range (minVal,maxVal+1):
            if groupNum ==1:
                freqHopcfg = qtouchComponent.createMenuSymbol("FREQ_HOP_MENU", enableFreqHopMenu)
                freqHopcfg.setLabel("Frequency Hop Configuration")
                freqHopcfg.setDescription("Frequency Hop is a mechanism used in touch measurement to avoid noisy signal value. In Frequency Hop, more than one bursting frequency (user configurable) is used. Refer QTouch Modular Library Userguide for more details on Frequency Hop.")
                freqHopcfg.setVisible(True)
                freqHopcfg.setEnabled(True)
                self.initFreqHopGroupInstance(qtouchComponent,groupNum,freqHopcfg)
            else:
                dynamicName = "freqHopcfg_" +str(groupNum) 
                dynamicId = "FREQ_HOP_MENU_" +str(groupNum) 
                vars()[dynamicName] = qtouchComponent.createMenuSymbol(dynamicId, enableFreqHopMenu)
                vars()[dynamicName].setLabel("Frequency Hop Configuration Group"+str(groupNum))
                vars()[dynamicName].setDescription("Frequency Hop is a mechanism used in touch measurement to avoid noisy signal value. In Frequency Hop, more than one bursting frequency (user configurable) is used. Refer QTouch Modular Library Userguide for more details on Frequency Hop.")
                vars()[dynamicName].setVisible(False)
                vars()[dynamicName].setEnabled(False)
                self.initFreqHopGroupInstance(qtouchComponent,groupNum,vars()[dynamicName])

    def updateFreqHopGroups(self,symbol,event):
        """Handler for number of frequency hop groups being used. 
        Triggered by qtouch.updateGroupsCounts(symbol,event)
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component= symbol.getComponent()
        currentVal = int(event['symbol'].getValue())
        maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMax()
        minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()
        for x in range(minVal+1,maxVal+1):
            grpId = "FREQ_HOP_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(False)
            component.getSymbolByID(grpId).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(grpId).setEnabled(True)
                component.getSymbolByID(grpId).setVisible(True)


    def setSourceFilesEnabledStatus(self,fHopEnabled,autoTuneEnabled,symbol):
        """Enables frequency hop Autotune functionality. Also Enables/Disables freqHop and AutoFreqHop files and Libraries.
        Arguments:
            :fHopEnabled : Boolean Flag
            :autoTuneEnabled :Boolean Flag
            :symbol : symbol received by freqHopUpdateEnabled()
        Returns:
            :none
        """    
        print("setSourceFilesEnabledStatus AUTOTUNE STATUS UPDATE : " + str(autoTuneEnabled))
        print("setSourceFilesEnabledStatus AUTOTUNE ENABLE STATUS UPDATE : " + str(fHopEnabled))
        
        component= symbol.getComponent()
        freqHopLibraryFile  = component.getSymbolByID("TOUCH_HOP_LIB")
        freqHopAutoLibraryFile = component.getSymbolByID("TOUCH_HOP_AUTO_LIB")
        freqHopHeaderFile = component.getSymbolByID("TOUCH_HOP_HEADER")
        freqHopAutoHeaderFile = component.getSymbolByID("TOUCH_HOP_AUTO_HEADER")
        
        if(fHopEnabled == True):
            freqHopLibraryFile.setEnabled(not autoTuneEnabled)
            freqHopHeaderFile.setEnabled(not autoTuneEnabled)
            freqHopAutoLibraryFile.setEnabled(autoTuneEnabled)
            freqHopAutoHeaderFile.setEnabled(autoTuneEnabled)
        else:
            freqHopLibraryFile.setEnabled(False)
            freqHopHeaderFile.setEnabled(False)
            freqHopAutoLibraryFile.setEnabled(False)
            freqHopAutoHeaderFile.setEnabled(False)

    def freqHopStepCountUpdate(self, symbol, event):
        component= symbol.getComponent()
        steps = int(symbol.getValue())

        for freqID in range(0, self.freqHopStepsMax):
            symbol = component.getSymbolByID("HOP_FREQ"+ str(freqID))
            symbol.setVisible(True)
            
            if freqID >= steps:
                symbol.setVisible(False)

    def freqHopUpdateEnabled(self,symbol,event):
        """Enables frequency hop functionality. Also Enables/Disables associated source files and Libraries.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component= symbol.getComponent()
        maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getValue()
        minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()

        fHopEnabled = component.getSymbolByID("ENABLE_FREQ_HOP").getValue()
        autoTuneEnabled = component.getSymbolByID("FREQ_AUTOTUNE").getValue()

        self.setSourceFilesEnabledStatus(fHopEnabled,autoTuneEnabled,symbol)

        for x in range(minVal,maxVal+1):
            if(x == minVal):
                fhMenu = "FREQ_HOP_MENU"
            else:
                fhMenu = "FREQ_HOP_MENU_" +str(x) 
            
            component.getSymbolByID(fhMenu).setEnabled(fHopEnabled)
            component.getSymbolByID(fhMenu).setVisible(fHopEnabled)

    #parameter assignment
    def setFreqStepsValues(self,freqSteps, stepsDefault,stepsMax):
        """Populate the frequency hop steps symbol 
        Arguments:
            :freqSteps : symbol to be populated
            :stepsDefault : default value
            :stepsMax : Maximum Value
        Returns:
            none
        """
        freqSteps.setLabel("Frequency Hop Steps")
        freqSteps.setDefaultValue(stepsDefault)
        freqSteps.setMin(3)
        freqSteps.setMax(stepsMax)
        freqSteps.setDescription("Defines the number of frequencies used for touch measurement. Noise performance will be good if more number of frequencies are used - but increases response time and RAM usage. If higher number of frequencies needs to be used (to tackle noise), consider enabling frequency auto-tune option.")

    def setFreqHopValues(self,qtouchComponent,steps,maxSteps,groupNumber,parentLabel):
        """Populate the frequency hop Values symbol 
        Arguments:
            :qtouchComponent : touchModule
            :steps : the number of steps to add
            :groupNumber : index of the frequency hop group
            :parentLabel : parent  symbol for added menu items
        Returns:
            none
        """
        for freqID in range(0, maxSteps):
            if(groupNumber ==1):
                freqHopValues = qtouchComponent.createKeyValueSetSymbol("HOP_FREQ"+ str(freqID), parentLabel)
            else:
                freqHopValues = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_HOP_FREQ"+ str(freqID), parentLabel)
            
            freqHopValues.setLabel("Hop Frequency "+ str(freqID)) 
            freqHopValues.addKey("FREQ_SEL0", "FREQ_SEL_0", "Frequency 0")
            freqHopValues.addKey("FREQ_SEL1", "FREQ_SEL_1", "Frequency 1")
            freqHopValues.addKey("FREQ_SEL2", "FREQ_SEL_2", "Frequency 2")
            freqHopValues.addKey("FREQ_SEL3", "FREQ_SEL_3", "Frequency 3")
            freqHopValues.addKey("FREQ_SEL4", "FREQ_SEL_4", "Frequency 4")
            freqHopValues.addKey("FREQ_SEL5", "FREQ_SEL_5", "Frequency 5")
            freqHopValues.addKey("FREQ_SEL6", "FREQ_SEL_6", "Frequency 6")
            freqHopValues.addKey("FREQ_SEL7", "FREQ_SEL_7", "Frequency 7")
            freqHopValues.addKey("FREQ_SEL8", "FREQ_SEL_8", "Frequency 8")
            freqHopValues.addKey("FREQ_SEL9", "FREQ_SEL_9", "Frequency 9")
            freqHopValues.addKey("FREQ_SEL10", "FREQ_SEL_10", "Frequency 10")
            freqHopValues.addKey("FREQ_SEL11", "FREQ_SEL_11", "Frequency 11")
            freqHopValues.addKey("FREQ_SEL12", "FREQ_SEL_12", "Frequency 12")
            freqHopValues.addKey("FREQ_SEL13", "FREQ_SEL_13", "Frequency 13")
            freqHopValues.addKey("FREQ_SEL14", "FREQ_SEL_14", "Frequency 14")
            freqHopValues.addKey("FREQ_SEL15", "FREQ_SEL_15", "Frequency 15")
            freqHopValues.setOutputMode("Value")
            freqHopValues.setDisplayMode("Description")
            freqHopValues.setDefaultValue(freqID)
            freqHopValues.setDescription("Sets the Hop Frequencies")
            
            if freqID >= steps:
                freqHopValues.setVisible(False)

    def setMaxVarianceValues(self,maxVariance):
        """Populate the maximum variance symbol 
        Arguments:
            :maxVariance : symbol to be updated
        Returns:
            none
        """
        maxVariance.setLabel("Maximum Variance")
        maxVariance.setDefaultValue(25)
        maxVariance.setMin(1)
        maxVariance.setMax(255)
        maxVariance.setDescription("When frequency auto tune is enabled, the touch measurement frequencies are automatically changed based on noise levels.This parameter sets the threshold for noise level in touch data.If noise level is more than this threshold, then the noisy frequency will be replaced.")

    def setTuneInCountValues(self,tuneInCount):
        """Populate the tune in count symbol 
        Arguments:
            :tuneInCount : symbol to be updated
        Returns:
            none
        """
        tuneInCount.setLabel("Maximum Tune-in count")
        tuneInCount.setDefaultValue(6)
        tuneInCount.setMin(1)
        tuneInCount.setMax(255)
        tuneInCount.setDescription("This parameter acts as an integrator to confirm the noise.The measurement frequency is changed ONLY if noise levels is more than Maximum Variance for Tune In Count measurement cycles. Configuring higher value for Tune in Count might take longer duration to replace a bad frequency. Configuring lower value for Tune in Count might unnecessarily replace frequency.")