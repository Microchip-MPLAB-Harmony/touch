################################################################################
#### Component ####
################################################################################
sensorMenu = qtouchComponent.createMenuSymbol("SENSOR_MENU", touchMenu)
sensorMenu.setLabel("Sensor Configuration")

#Detect Integration
touchSym_DETECT_INT_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_DET_INT", sensorMenu)
touchSym_DETECT_INT_Val.setLabel("Detect Integration")
touchSym_DETECT_INT_Val.setDefaultValue(4)
touchSym_DETECT_INT_Val.setMin(0)
touchSym_DETECT_INT_Val.setMax(255)
touchSym_DETECT_INT_Val.setDescription("'Detect Integration' defines the number of additional touchmeasurements to be performed to confirm a touch detection. Value of 0 will not do additional measurements Default: 4 measurements Note: For surface and gesture projects, change the value of Detect Integration to 1")

#Away from Touch Recal Integration Count
touchSym_ANTI_TCH_DET_INT_Val = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DET_INT", sensorMenu)
touchSym_ANTI_TCH_DET_INT_Val.setLabel("Away from Touch Recal Intergration Count")
touchSym_ANTI_TCH_DET_INT_Val.setDefaultValue(5)
touchSym_ANTI_TCH_DET_INT_Val.setMin(0)
touchSym_ANTI_TCH_DET_INT_Val.setMax(255)
touchSym_ANTI_TCH_DET_INT_Val.setDescription("'Away from Touch Recal Integration Count' defines the counter for additional measurements to confirm away from touch signal to initiate Away from touch re-calibration. Value of 0 will disable away from Touch Recal integration")

#Away from Touch Recal Threshold
touchSym_ANTI_TCH_RECAL_THRSHLD_Val = qtouchComponent.createKeyValueSetSymbol("DEF_ANTI_TCH_RECAL_THRSHLD", sensorMenu)
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.setLabel("Away from Touch Recal Threshold")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.addKey("RECAL100", "RECAL_100", "100 percent of Touch threshold")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.addKey("RECAL50", "RECAL_50", "50 percent of Touch threshold")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.addKey("RECAL25", "RECAL_25", "25 percent of Touch threshold")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.addKey("RECAL125", "RECAL_12_5", "12.5 percent of Touch threshold")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.addKey("RECAL625", "RECAL_6_25", "6.25 percent of Touch threshold")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.setDefaultValue(0)
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.setOutputMode("Value")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.setDisplayMode("Description")
touchSym_ANTI_TCH_RECAL_THRSHLD_Val.setDescription("If the touch delta is more than 'Away from Touch Recal Threshold' on negative side, then sensor is recalibrated.")

#Touch Drift Rate
touchSym_TCH_DRIFT_RATE_Val = qtouchComponent.createIntegerSymbol("DEF_TCH_DRIFT_RATE", sensorMenu)
touchSym_TCH_DRIFT_RATE_Val.setLabel("Touch Drift Rate")
touchSym_TCH_DRIFT_RATE_Val.setDefaultValue(20)
touchSym_TCH_DRIFT_RATE_Val.setMin(0)
touchSym_TCH_DRIFT_RATE_Val.setMax(255)
touchSym_TCH_DRIFT_RATE_Val.setDescription("When signal value is greater than reference, this value defines the rate at which sensor reference value should be adjusted towards change in signal value. 'Touch Drift Rate' value is scaled by 200msec. If 'Touch Drift Rate' is 10, then drift period is 10x200msec = 2seconds. Every two seconds, reference value will be incremented by '1' till it is equal to signal value.Value of 0 will disable Towards touch  drift rate Default: 20 (4 seconds)")

#Away from Touch Drift Rate
touchSym_ANTI_TCH_DRIFT_RATE_Val = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DRIFT_RATE", sensorMenu)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setLabel("Away from Touch Drift Rate")
touchSym_ANTI_TCH_DRIFT_RATE_Val.setDefaultValue(5)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setMin(0)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setMax(255)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setDescription("When signal value is smaller than reference, this value defines the rate at which sensor reference value should be adjusted towards change in signal value.'Away from Touch Drift Rate' value is scaled by 200msec. If 'Away from Touch Drift Rate' is 10, then drift period is 10x200msec = 2seconds. Every two seconds, reference value will be decremented by '1' till it is equal to signal value. Value of 0 will disable Away from touch  drift rate Default: 5")

#Drift Hold Time
touchSym_DRIFT_HOLD_TIME_Val = qtouchComponent.createIntegerSymbol("DEF_DRIFT_HOLD_TIME", sensorMenu)
touchSym_DRIFT_HOLD_TIME_Val.setLabel("Drift Hold Time")
touchSym_DRIFT_HOLD_TIME_Val.setDefaultValue(20)
touchSym_DRIFT_HOLD_TIME_Val.setMin(0)
touchSym_DRIFT_HOLD_TIME_Val.setMax(255)
touchSym_DRIFT_HOLD_TIME_Val.setDescription("When a sensor is in detect, the drifting on all other sensors are stopped. When the finger is removed from the sensor the drifting is started. 'Drift hold time' defines the amount of time the drifting needs to be paused after removing the finger. This value is scaled by 200msec. Value of 0 will disable the Drift Hold time Feature Default: 20 (4 seconds)")

#Reburst mode
touchSym_REBURST_MODE_Val = qtouchComponent.createKeyValueSetSymbol("DEF_REBURST_MODE", sensorMenu)
touchSym_REBURST_MODE_Val.setLabel("Re-burst mode")
touchSym_REBURST_MODE_Val.addKey("REBURST0", "REBURST_NONE", "Disable reburst")
touchSym_REBURST_MODE_Val.addKey("REBURST1", "REBURST_UNRESOLVED", "Reburst sensors only in process of calibration / filter in / filter out and AKS groups")
touchSym_REBURST_MODE_Val.addKey("REBURST2", "REBURST_ALL", "Reburst all active sensors")
touchSym_REBURST_MODE_Val.setDefaultValue(1)
touchSym_REBURST_MODE_Val.setOutputMode("Value")
touchSym_REBURST_MODE_Val.setDisplayMode("Description")
touchSym_REBURST_MODE_Val.setDescription("Under various conditions (like Calibration, Detect Integration, Recalibration), additional touch measurements needs to be performed in order to confirm an activity.This parameter defines how the rebursting (additional touch measurements) happens. It is recommended to use default value in order to get faster response time.Default: Reburst sensors only in process of calibration / filter in / filter out and AKS groups")
   
#Max ON Duration
touchSym_MAX_ON_DURATION_Val = qtouchComponent.createIntegerSymbol("DEF_MAX_ON_DURATION", sensorMenu)
touchSym_MAX_ON_DURATION_Val.setLabel("Max ON Duration")
touchSym_MAX_ON_DURATION_Val.setDefaultValue(0)
touchSym_MAX_ON_DURATION_Val.setMin(0)
touchSym_MAX_ON_DURATION_Val.setMax(255)
touchSym_MAX_ON_DURATION_Val.setDescription("Defines the maximum sensor ON time. For a system, if prolonged touch is not valid, then 'Max-on-duration (MOD)' can be configured. If a sensor is in detect for more than MOD, then the sensor is calibrated. If MOD is configured as zero, then MOD is infinite. Otherwise, this value is scaled by 200msec. Value of 0 will disable Max on duration(infinite time) Default: 0 ")


