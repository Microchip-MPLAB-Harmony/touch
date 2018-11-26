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

#Away from Touch Recal Integration Count
touchSym_ANTI_TCH_DET_INT_Val = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DET_INT", sensorMenu)
touchSym_ANTI_TCH_DET_INT_Val.setLabel("Away from Touch Recal Intergration Count")
touchSym_ANTI_TCH_DET_INT_Val.setDefaultValue(5)
touchSym_ANTI_TCH_DET_INT_Val.setMin(0)
touchSym_ANTI_TCH_DET_INT_Val.setMax(255)

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

#Touch Drift Rate
touchSym_TCH_DRIFT_RATE_Val = qtouchComponent.createIntegerSymbol("DEF_TCH_DRIFT_RATE", sensorMenu)
touchSym_TCH_DRIFT_RATE_Val.setLabel("Touch Drift Rate")
touchSym_TCH_DRIFT_RATE_Val.setDefaultValue(20)
touchSym_TCH_DRIFT_RATE_Val.setMin(0)
touchSym_TCH_DRIFT_RATE_Val.setMax(255)

#Away from Touch Drift Rate
touchSym_ANTI_TCH_DRIFT_RATE_Val = qtouchComponent.createIntegerSymbol("DEF_ANTI_TCH_DRIFT_RATE", sensorMenu)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setLabel("Away from Touch Drift Rate")
touchSym_ANTI_TCH_DRIFT_RATE_Val.setDefaultValue(5)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setMin(0)
touchSym_ANTI_TCH_DRIFT_RATE_Val.setMax(255)

#Drift Hold Time
touchSym_DRIFT_HOLD_TIME_Val = qtouchComponent.createIntegerSymbol("DEF_DRIFT_HOLD_TIME", sensorMenu)
touchSym_DRIFT_HOLD_TIME_Val.setLabel("Drift Hold Time")
touchSym_DRIFT_HOLD_TIME_Val.setDefaultValue(20)
touchSym_DRIFT_HOLD_TIME_Val.setMin(0)
touchSym_DRIFT_HOLD_TIME_Val.setMax(255)

#Reburst mode
touchSym_REBURST_MODE_Val = qtouchComponent.createKeyValueSetSymbol("DEF_REBURST_MODE", sensorMenu)
touchSym_REBURST_MODE_Val.setLabel("Re-burst mode")
touchSym_REBURST_MODE_Val.addKey("REBURST0", "REBURST_NONE", "Disable reburst")
touchSym_REBURST_MODE_Val.addKey("REBURST1", "REBURST_UNRESOLVED", "Reburst sensors only in process of calibration / filter in / filter out and AKS groups")
touchSym_REBURST_MODE_Val.addKey("REBURST2", "REBURST_ALL", "Reburst all active sensors")
touchSym_REBURST_MODE_Val.setDefaultValue(1)
touchSym_REBURST_MODE_Val.setOutputMode("Value")
touchSym_REBURST_MODE_Val.setDisplayMode("Description")
    
#Max ON Duration
touchSym_MAX_ON_DURATION_Val = qtouchComponent.createIntegerSymbol("DEF_MAX_ON_DURATION", sensorMenu)
touchSym_MAX_ON_DURATION_Val.setLabel("Max ON Duration")
touchSym_MAX_ON_DURATION_Val.setDefaultValue(0)
touchSym_MAX_ON_DURATION_Val.setMin(0)
touchSym_MAX_ON_DURATION_Val.setMax(255)


