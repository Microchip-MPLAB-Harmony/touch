"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
maxGroups = 4 # defaultValue

def getMaxGroups():
    """Get maximum sensor groups
    Arguments:
        :none
    Returns:
        :number of sensor groups  as (int)
    """
    global maxGroups
    return int(maxGroups)

def setMaxGroups(newMax):
    """Set maximum sensor groups
    Arguments:
        :newMax - new maximum (int)
    Returns:
        :none
    """
    global maxGroups
    maxGroups = int(newMax)

#instance
def initSensorsGroupInstance(qtouchComponent,groupNumber,parentLabel):
    """Initialise Sensor Group Instance
    Arguments:
        :qtouchComponent : touchModule
        :groupNumber : index of the group instance
        :parentLabel : parent symbol for added menu items
    Returns:
        :none
    """
    if int(groupNumber) == 1:
        DetectIntegration = qtouchComponent.createIntegerSymbol("DEF_TOUCH_DET_INT", parentLabel)
        AntiTouchDetectIntegration = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DET_INT", parentLabel)
        AntiTouchRecalThreshold = qtouchComponent.createKeyValueSetSymbol("DEF_ANTI_TCH_RECAL_THRSHLD", parentLabel)
        DriftRate = qtouchComponent.createIntegerSymbol("DEF_TCH_DRIFT_RATE", parentLabel)
        AntiTouchDriftRate = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DRIFT_RATE", parentLabel)
        DriftHoldTime = qtouchComponent.createIntegerSymbol("DEF_DRIFT_HOLD_TIME", parentLabel)
        ReburstMode = qtouchComponent.createKeyValueSetSymbol("DEF_REBURST_MODE", parentLabel)
        MaxOnDuration = qtouchComponent.createIntegerSymbol("DEF_MAX_ON_DURATION", parentLabel)
    else:
        DetectIntegration = qtouchComponent.createIntegerSymbol("DEF_TOUCH_DET_INT_"+str(groupNumber), parentLabel)
        AntiTouchDetectIntegration = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DET_INT_"+str(groupNumber), parentLabel)
        AntiTouchRecalThreshold = qtouchComponent.createKeyValueSetSymbol("DEF_ANTI_TCH_RECAL_THRSHLD_"+str(groupNumber), parentLabel)
        DriftRate = qtouchComponent.createIntegerSymbol("DEF_TCH_DRIFT_RATE_"+str(groupNumber), parentLabel)
        AntiTouchDriftRate = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DRIFT_RATE_"+str(groupNumber), parentLabel)
        DriftHoldTime = qtouchComponent.createIntegerSymbol("DEF_DRIFT_HOLD_TIME_"+str(groupNumber), parentLabel)
        ReburstMode = qtouchComponent.createKeyValueSetSymbol("DEF_REBURST_MODE_"+str(groupNumber), parentLabel)
        MaxOnDuration = qtouchComponent.createIntegerSymbol("DEF_MAX_ON_DURATION_"+str(groupNumber), parentLabel)
    #parameter assignment
    setDetectIntegrationValues(DetectIntegration)
    setAntiTouchDetectIntegrationValues(AntiTouchDetectIntegration)
    setAntiTouchRecalThresholdValues(AntiTouchRecalThreshold)
    setDriftRateValues(DriftRate)
    setAntiTouchDriftRateVlues(AntiTouchDriftRate)
    setDriftHoldTimeValues(DriftHoldTime)
    setReburstModeValues(ReburstMode)
    setMaxOnDurationValues(MaxOnDuration)

#group
def initSensorGroup(qtouchComponent, touchMenu, minVal,maxVal):
    """Initialise Sensor Groups and add to touch Module
    Arguments:
        :qtouchComponent : touchModule
        :touchMenu : parent menu symbol for added menu items
        :minVal : see acquisitionGroupCountMenu.getMin()
        :maxVal : see acquisitionGroupCountMenu.getMax()
    Returns:
        :none
    """
    global maxGroups
    maxGroups = maxVal

    for i in range (minVal,maxVal+1):
        if i ==1:
            sensorMenu = qtouchComponent.createMenuSymbol("SENSOR_MENU", touchMenu)
            sensorMenu.setLabel("Sensor Configuration")
            sensorMenu.setDescription("Configure Sensors")
            sensorMenu.setVisible(True)
            sensorMenu.setEnabled(True)
            initSensorsGroupInstance(qtouchComponent,i,sensorMenu)
        else:
            dynamicName = "sensorMenu_" +str(i) 
            dynamicId = "SENSOR_MENU_" +str(i) 
            vars()[dynamicName] =  qtouchComponent.createMenuSymbol(dynamicId, touchMenu)
            vars()[dynamicName].setLabel("Sensor Configuration Group"+str(i))
            vars()[dynamicName].setVisible(False)
            vars()[dynamicName].setEnabled(False)
            initSensorsGroupInstance(qtouchComponent,i,vars()[dynamicName])

#updater
def updateSensorGroups(symbol,event):
    """Handler for number of Sensor groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
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
        grpId = "SENSOR_MENU_" +str(x)
        component.getSymbolByID(grpId).setEnabled(False)
        component.getSymbolByID(grpId).setVisible(False)
        if(currentVal >= x):
            component.getSymbolByID(grpId).setEnabled(True)
            component.getSymbolByID(grpId).setVisible(True)

#parameter assignment
def setDetectIntegrationValues(DetectIntegration):
    """Populate the Detect Integration symbol 
    Arguments:
        :DetectIntegration : symbol to be populated
    Returns:
        none
    """
    DetectIntegration.setLabel("Detect Integration")
    DetectIntegration.setDefaultValue(4)
    DetectIntegration.setMin(0)
    DetectIntegration.setMax(255)
    DetectIntegration.setDescription("'Detect Integration' defines the number of additional touchmeasurements to be performed to confirm a touch detection. Value of 0 will not do additional measurements Default: 4 measurements Note: For surface and gesture projects, change the value of Detect Integration to 1")

def setAntiTouchDetectIntegrationValues(AntiTouchDetectIntegration):
    """Populate the Anti touch Detect Integration symbol 
    Arguments:
        :AntiTouchDetectIntegration : symbol to be populated
    Returns:
        none
    """
    AntiTouchDetectIntegration.setLabel("Away from Touch Recal Intergration Count")
    AntiTouchDetectIntegration.setDefaultValue(5)
    AntiTouchDetectIntegration.setMin(0)
    AntiTouchDetectIntegration.setMax(255)
    AntiTouchDetectIntegration.setDescription("'Away from Touch Recal Integration Count' defines the counter for additional measurements to confirm away from touch signal to initiate Away from touch re-calibration. Value of 0 will disable away from Touch Recal integration")

def setAntiTouchRecalThresholdValues(AntiTouchRecalThreshold):
    """Populate the Anti touch Recalibration threshold symbol 
    Arguments:
        :AntiTouchRecalThreshold : symbol to be populated
    Returns:
        none
    """
    AntiTouchRecalThreshold.setLabel("Away from Touch Recal Threshold")
    AntiTouchRecalThreshold.addKey("RECAL100", "RECAL_100", "100 percent of Touch threshold")
    AntiTouchRecalThreshold.addKey("RECAL50", "RECAL_50", "50 percent of Touch threshold")
    AntiTouchRecalThreshold.addKey("RECAL25", "RECAL_25", "25 percent of Touch threshold")
    AntiTouchRecalThreshold.addKey("RECAL125", "RECAL_12_5", "12.5 percent of Touch threshold")
    AntiTouchRecalThreshold.addKey("RECAL625", "RECAL_6_25", "6.25 percent of Touch threshold")
    AntiTouchRecalThreshold.setDefaultValue(0)
    AntiTouchRecalThreshold.setOutputMode("Value")
    AntiTouchRecalThreshold.setDisplayMode("Description")
    AntiTouchRecalThreshold.setDescription("If the touch delta is more than 'Away from Touch Recal Threshold' on negative side, then sensor is recalibrated.")

def setDriftRateValues(DriftRate):
    """Populate the drift rate symbol 
    Arguments:
        :DriftRate : symbol to be populated
    Returns:
        none
    """
    DriftRate.setLabel("Touch Drift Rate")
    DriftRate.setDefaultValue(20)
    DriftRate.setMin(0)
    DriftRate.setMax(255)
    DriftRate.setDescription("When signal value is greater than reference, this value defines the rate at which sensor reference value should be adjusted towards change in signal value. 'Touch Drift Rate' value is scaled by 200msec. If 'Touch Drift Rate' is 10, then drift period is 10x200msec = 2seconds. Every two seconds, reference value will be incremented by '1' till it is equal to signal value.Value of 0 will disable Towards touch  drift rate Default: 20 (4 seconds)")

def setAntiTouchDriftRateVlues(AntiTouchDriftRate):
    """Populate the ant touch drift rate symbol 
    Arguments:
        :AntiTouchDriftRate : symbol to be populated
    Returns:
        none
    """
    AntiTouchDriftRate.setLabel("Away from Touch Drift Rate")
    AntiTouchDriftRate.setDefaultValue(5)
    AntiTouchDriftRate.setMin(0)
    AntiTouchDriftRate.setMax(255)
    AntiTouchDriftRate.setDescription("When signal value is smaller than reference, this value defines the rate at which sensor reference value should be adjusted towards change in signal value.'Away from Touch Drift Rate' value is scaled by 200msec. If 'Away from Touch Drift Rate' is 10, then drift period is 10x200msec = 2seconds. Every two seconds, reference value will be decremented by '1' till it is equal to signal value. Value of 0 will disable Away from touch  drift rate Default: 5")

def setDriftHoldTimeValues(DriftHoldTime):
    """Populate the drift hold time  symbol 
    Arguments:
        :DriftHoldTime : symbol to be populated
    Returns:
        none
    """
    DriftHoldTime.setLabel("Drift Hold Time")
    DriftHoldTime.setDefaultValue(20)
    DriftHoldTime.setMin(0)
    DriftHoldTime.setMax(255)
    DriftHoldTime.setDescription("When a sensor is in detect, the drifting on all other sensors are stopped. When the finger is removed from the sensor the drifting is started. 'Drift hold time' defines the amount of time the drifting needs to be paused after removing the finger. This value is scaled by 200msec. Value of 0 will disable the Drift Hold time Feature Default: 20 (4 seconds)")

def setReburstModeValues(ReburstMode):
    """Populate the Reburst Mode symbol 
    Arguments:
        :ReburstMode : symbol to be populated
    Returns:
        none
    """
    ReburstMode.setLabel("Re-burst mode")
    ReburstMode.addKey("REBURST0", "REBURST_NONE", "Disable reburst")
    ReburstMode.addKey("REBURST1", "REBURST_UNRESOLVED", "Reburst sensors only in process of calibration / filter in / filter out and AKS groups")
    ReburstMode.addKey("REBURST2", "REBURST_ALL", "Reburst all active sensors")
    ReburstMode.setDefaultValue(1)
    ReburstMode.setOutputMode("Value")
    ReburstMode.setDisplayMode("Description")
    ReburstMode.setDescription("Under various conditions (like Calibration, Detect Integration, Recalibration), additional touch measurements needs to be performed in order to confirm an activity.This parameter defines how the rebursting (additional touch measurements) happens. It is recommended to use default value in order to get faster response time.Default: Reburst sensors only in process of calibration / filter in / filter out and AKS groups")

def setMaxOnDurationValues(MaxOnDuration):
    """Populate the max on duration symbol 
    Arguments:
        :MaxOnDuration : symbol to be populated
    Returns:
        none
    """
    MaxOnDuration.setLabel("Max ON Duration")
    MaxOnDuration.setDefaultValue(0)
    MaxOnDuration.setMin(0)
    MaxOnDuration.setMax(255)
    MaxOnDuration.setDescription("Defines the maximum sensor ON time. For a system, if prolonged touch is not valid, then 'Max-on-duration (MOD)' can be configured. If a sensor is in detect for more than MOD, then the sensor is calibrated. If MOD is configured as zero, then MOD is infinite. Otherwise, this value is scaled by 200msec. Value of 0 will disable Max on duration(infinite time) Default: 0 ")
