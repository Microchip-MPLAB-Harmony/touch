"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
maxGroups = 4 # defaultValue

def getMaxGroups():
    """Get maximum acquisition groups
    Arguments:
        :none
    Returns:
        :number of acquistion groups  as (int)
    """
    global maxGroups
    return int(maxGroups)

def setMaxGroups(newMax):
    """Set maximum acquisition groups
    Arguments:
        :newMax - new maximum (int)
    Returns:
        :none
    """
    global maxGroups
    maxGroups = int(newMax)


def initAcquisitionGroup(qtouchComponent, parentMenu, minVal,maxVal,selfChannels,mutualChannels,targetDevice,csdMode,shieldMode):
    """Initialise Acquisition Groups and add to touch Module
    Arguments:
        :qtouchComponent : touchModule
        :parentMenu : parent menu symbol for added menu items
        :minVal : see acquisitionGroupCountMenu.getMin()
        :maxVal : see acquisitionGroupCountMenu.getMax()
        :selfChannels : see target_device.getSelfCount()
        :mutualChannels : see target_device.getMutualCount()
        :targetDevice : see interface.getDeviceSeries()
        :csdmode : see target_device.getCSDMode(targetDevice)
        :shieldMode : see target_device.getShieldMode(targetDevice)
    Returns:
        :none
    """
    global maxGroups
    maxGroups = maxVal

    for i in range (minVal,maxVal+1):
        if i ==1:
            acquisitionMenu = qtouchComponent.createMenuSymbol("ACQUISITION_MENU", parentMenu)
            acquisitionMenu.setLabel("Acquisition Configuration")
            acquisitionMenu.setVisible(True)
            acquisitionMenu.setEnabled(True)
            initacquisitionInstance(qtouchComponent,i,acquisitionMenu,selfChannels,mutualChannels,targetDevice,csdMode,shieldMode)
        else:
            dynamicName = "acquisitionMenu_" +str(i) 
            dynamicId = "ACQUISITION_MENU_" +str(i) 
            vars()[dynamicName] =  qtouchComponent.createMenuSymbol(dynamicId, parentMenu)
            vars()[dynamicName].setLabel("Acquisition Configuration Group"+str(i))
            vars()[dynamicName].setVisible(False)
            vars()[dynamicName].setEnabled(False)
            initacquisitionInstance(qtouchComponent,i,vars()[dynamicName],selfChannels,mutualChannels,targetDevice,csdMode,shieldMode)

#instance
def initacquisitionInstance(qtouchComponent,groupNumber,parentMenu,selfChannels,mutualChannels,targetDevice,csdMode,shieldMode):
    """Initialise Acquisition Instance
    Arguments:
        :qtouchComponent : touchModule
        :groupNumber : index of the group instance
        :parentMenu : parent menu symbol for added menu items
        :selfChannels : see target_device.getSelfCount()
        :mutualChannels : see target_device.getMutualCount()
        :targetDevice : see interface.getDeviceSeries()
        :csdmode : see target_device.getCSDMode(targetDevice)
        :shieldMode : see target_device.getShieldMode(targetDevice)
    Returns:
        :none
    """
    global touchSenseTechnology    
    if int(groupNumber) == 1:
        touchSenseTechnology = qtouchComponent.createKeyValueSetSymbol("SENSE_TECHNOLOGY", parentMenu)
        totalChannelCountSelf = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_SELF",parentMenu)
        totalChannelCountMutl = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_MUTL",parentMenu)
        touchAutoTuneMode = qtouchComponent.createKeyValueSetSymbol("TUNE_MODE_SELECTED", parentMenu)
        touchScanRate = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MEASUREMENT_PERIOD_MS", parentMenu)
        touchAcquisitonFrequency = qtouchComponent.createKeyValueSetSymbol("DEF_SEL_FREQ_INIT", parentMenu)
    else:
        touchSenseTechnology = qtouchComponent.createKeyValueSetSymbol("SENSE_TECHNOLOGY_"+str(groupNumber), parentMenu)
        totalChannelCountSelf = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_SELF_"+str(groupNumber),parentMenu)
        totalChannelCountMutl = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_MUTL_"+str(groupNumber),parentMenu)
        touchAutoTuneMode = qtouchComponent.createKeyValueSetSymbol("TUNE_MODE_SELECTED_"+str(groupNumber),parentMenu)
        touchScanRate = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MEASUREMENT_PERIOD_MS_"+str(groupNumber),parentMenu)
        touchAcquisitonFrequency = qtouchComponent.createKeyValueSetSymbol("DEF_SEL_FREQ_INIT_"+str(groupNumber),parentMenu)
    #parameter assignment    
    #touchSenseTechnology
    if(shieldMode == "hardware"):
        setTouchTechnologyDrivenShieldValues(touchSenseTechnology)
    else:
        setTouchTechnologyValues(touchSenseTechnology)
    #totalChannelCountSelf
    totalChannelCountSelf.setVisible(True)
    totalChannelCountSelf.setDefaultValue(int(selfChannels))
    totalChannelCountSelf.setLabel("Self Capacitance Channels")
    #totalChannelCountMutl
    totalChannelCountMutl.setVisible(True)
    totalChannelCountMutl.setDefaultValue(int(mutualChannels))
    totalChannelCountMutl.setLabel("Mutual Capacitance Channels")
    # Select Tuning mode
    setAutoTuneModeValues(touchAutoTuneMode,csdMode)
    #Scan Rate (ms)    
    setScanRateValues(touchScanRate)    
    #Acquisition Frequency
    setAcquisitionFrequencyValues(touchAcquisitonFrequency)

#updater
def updateAcquisitionGroups(symbol,event):
    """Handler for number of acquistion groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
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
        grpId = "ACQUISITION_MENU_" +str(x)
        component.getSymbolByID(grpId).setEnabled(False)
        component.getSymbolByID(grpId).setVisible(False)
        if(currentVal >= x):
            component.getSymbolByID(grpId).setEnabled(True)
            component.getSymbolByID(grpId).setVisible(True)

#parameter assignment
def setTouchTechnologyValues(touchSenseTechnology):
    """Populate the touchSenseTechnology symbol -  NON DrivenShield
    Arguments:
        :touchSenseTechnology: symbol to be updated
    Returns:
        :none
    """
    touchSenseTechnology.setLabel("Sensor Technology")
    touchSenseTechnology.addKey("SelfCap", "NODE_SELFCAP", "Self Capacitance Sensing")
    touchSenseTechnology.addKey("MutualCap", "NODE_MUTUAL", "Mutual Capacitance Sensing")
    touchSenseTechnology.setDefaultValue(0)
    touchSenseTechnology.setOutputMode("Value")
    touchSenseTechnology.setDisplayMode("Description")
    touchSenseTechnology.setDescription("Selects the sensor technology - Selfcap: Requires one pin per channel; Simple sensor design; Recommended for small number of sensors (less than 12). Mutualcap: Requires one X pin and one Y pin per channel; Can realize X x Y number of sensors in a matrix form; Recommended for large number of sensors (more than 12)")

def setTouchTechnologyDrivenShieldValues(touchSenseTechnology):
    """Populate the touchSenseTechnology symbol for DrivenShield
    Arguments:
        :param :touchSenseTechnology :symbol to be changed
        :csdMode : see target_device.getCSDMode(targetDevice)
    Returns:
        :none
    """
    touchSenseTechnology.setLabel("Sensor Technology")
    touchSenseTechnology.addKey("SelfCap", "NODE_SELFCAP", "Self Capacitance Sensing")
    touchSenseTechnology.addKey("MutualCap", "NODE_MUTUAL", "Mutual Capacitance Sensing")
    touchSenseTechnology.addKey("SelfCapShield", "NODE_SELFCAP_SHIELD", "Self-Capacitance Sensing With Driven Shield")
    touchSenseTechnology.setDefaultValue(0)
    touchSenseTechnology.setOutputMode("Value")
    touchSenseTechnology.setDisplayMode("Description")
    touchSenseTechnology.setDescription("Selects the sensor technology - Selfcap: Requires one pin per channel; Simple sensor design; Recommended for small number of sensors (less than 12). SelfCapShield: Requires one pin per channel with Driven shield options; Simple sensor design; Recommended for small number of sensors (less than 12). Mutualcap: Requires one X pin and one Y pin per channel; Can realize X x Y number of sensors in a matrix form; Recommended for large number of sensors (more than 12)")

def setAutoTuneModeValues(touchAutoTuneMode,csdMode):
    """Populate touchAutoTuneMode symbol
    Arguments:
        :touchAutoTuneMode :symbol to be changed
        :csdMode : see target_device.getCSDMode(targetDevice)
    Returns:
        :none
    """
    touchAutoTuneMode.setLabel("Select the Required Tuning Mode")
    touchAutoTuneMode.addKey("Manual Tuning","CAL_AUTO_TUNE_NONE","Manual tuning is done based on the values defined by user")
    touchAutoTuneMode.addKey("Tune Resistor value","CAL_AUTO_TUNE_RSEL","Series Resistor is tuned")
    if(csdMode != "NoCSD"):
        touchAutoTuneMode.addKey("Tune CSD","CAL_AUTO_TUNE_CSD","Charge Share Delay - CSD is tuned")
    touchAutoTuneMode.setDefaultValue(0)
    touchAutoTuneMode.setOutputMode("Value")
    touchAutoTuneMode.setDisplayMode("Key")
    touchAutoTuneMode.setDescription("Sets the sensor calibration mode - CAL_AUTO_TUNE_NONE: Manual user setting of Prescaler, Charge share delay & Series resistor. AUTO_TUNE_CSD: QTouch library will use the configured prescaler and series resistor value and adjusts the CSD to ensure full charging.")

def setScanRateValues(touchScanRate):
    """ Populate the touchScanRate symbol
    Arguments:
        :touchScanRate : symbol to tbe changed
    Returns:
        :none
    """
    touchScanRate.setLabel("Scan Rate (ms)")
    touchScanRate.setDefaultValue(20)
    touchScanRate.setMin(1)
    touchScanRate.setMax(255)
    touchScanRate.setDescription("Defines the timer scan rate in milliseconds to initiate periodic touch measurement on all enabled touch sensors.")

def setAcquisitionFrequencyValues(touchAcquisitonFrequency):
    """Populate the touchAcquisitonFrequency symbol
    Arguments:
        :touchAcquisitonFrequency
    Returns:
        :none
    """
    touchAcquisitonFrequency.setLabel("Acquisition Frequency")
    touchAcquisitonFrequency.addKey("FREQ_0", "FREQ_SEL_0", "No additional clock cycles (Fastest measurement time) ")
    touchAcquisitonFrequency.addKey("FREQ_1", "FREQ_SEL_1", "1 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_2", "FREQ_SEL_2", "2 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_3", "FREQ_SEL_3", "3 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_4", "FREQ_SEL_4", "4 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_5", "FREQ_SEL_5", "5 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_6", "FREQ_SEL_6", "6 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_7", "FREQ_SEL_7", "7 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_8", "FREQ_SEL_8", "8 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_9", "FREQ_SEL_9", "9 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_10", "FREQ_SEL_10", "10 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_11", "FREQ_SEL_11", "11 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_12", "FREQ_SEL_12", "12 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_13", "FREQ_SEL_13", "13 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_14", "FREQ_SEL_14", "14 additional clock cycles ")
    touchAcquisitonFrequency.addKey("FREQ_15", "FREQ_SEL_15", "15 additional clock cycles (Slowest measurement time")
    touchAcquisitonFrequency.addKey("FREQ_16", "FREQ_SEL_SPREAD", "16 different frequencies used")
    touchAcquisitonFrequency.setDefaultValue(0)
    touchAcquisitonFrequency.setOutputMode("Value")
    touchAcquisitonFrequency.setDisplayMode("Value")
    touchAcquisitonFrequency.setDescription(
        "It may be required to change the acquisition frequency if system noise frequency"+
        " is closer to acquisition frequency.In order to vary the acquisition frequency, additional clock cycles"+
        " are added during measurement for FREQ_SEL_0 through FREQ_SEL_15. FREQ_SEL_0 provides the fastest"+
        " measurement time (no additional clock cycles are added) and FREQ_SEL_15 provides the slowest measurement time"+
        " (15 additional clock cycles are added). When FREQ_SEL_SPREAD option is used, all the 16 frequencies are used consecutively in a circular fashion.")