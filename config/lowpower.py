global low_power_events_supported

def enablePM(symbol,event):
	pmComponentID = ["pm"]
	supcComponentID = ["supc"]
	if(lowPowerKey.getValue()!= ""):
		Database.activateComponents(pmComponentID)
		if (getDeviceName.getDefaultValue() in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
			Database.activateComponents(supcComponentID)
	else:
		if(getDeviceName.getDefaultValue() in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
			Database.deactivateComponents(supcComponentID)
		if(getDeviceName.getDefaultValue() not in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
			Database.deactivateComponents(pmComponentID)

################################################################################
#### Component ####
################################################################################
LowPowerEvntMenu = qtouchComponent.createMenuSymbol("LOW_POWER_EVENT_MENU", touchMenu)
LowPowerEvntMenu.setLabel("Low Power Configuration")

# Enable Event based Low power 
if (getDeviceName.getDefaultValue() in low_power_events_supported):
	enableEventLowPower = qtouchComponent.createBooleanSymbol("ENABLE_EVENT_LP", LowPowerEvntMenu)
	enableEventLowPower.setLabel("Event based Low Power")
	enableEventLowPower.setDefaultValue(False)

#Low-power Node Selection
global lowPowerKey
lowPowerKey = qtouchComponent.createStringSymbol("LOW_POWER_KEYS", LowPowerEvntMenu)
lowPowerKey.setLabel("Low-power Keys Selection")
lowPowerKey.setDefaultValue("")
lowPowerKey.setDescription("Series of low-power key numbers separated by ,")
lowPowerKey.setDependencies(enablePM,["LOW_POWER_KEYS"])

#Low-power Detect Threshold
lowPowerDetThreshold = qtouchComponent.createIntegerSymbol("LOW_POWER_DET_THRESHOLD", LowPowerEvntMenu)
lowPowerDetThreshold.setLabel("Low-power Detect Threshold")
lowPowerDetThreshold.setDefaultValue(10)
lowPowerDetThreshold.setMin(10)
lowPowerDetThreshold.setMax(255)
lowPowerDetThreshold.setDescription("Sensor detect threshold for low-power measurement")

#Low-power Measurement Period
lowPowerPeriod = qtouchComponent.createKeyValueSetSymbol("LOW_POWER_PERIOD", LowPowerEvntMenu)
lowPowerPeriod.setLabel("Low-power Measurement Period")
lowPowerPeriod.addKey("NODE_SCAN_8MS", "NODE_SCAN_8MS", "8msec")
lowPowerPeriod.addKey("NODE_SCAN_16MS", "NODE_SCAN_16MS", "16msec")
lowPowerPeriod.addKey("NODE_SCAN_32MS", "NODE_SCAN_32MS", "32msec")
lowPowerPeriod.addKey("NODE_SCAN_64MS", "NODE_SCAN_64MS", "64msec")
lowPowerPeriod.addKey("NODE_SCAN_128MS", "NODE_SCAN_128MS", "128msec")
lowPowerPeriod.addKey("NODE_SCAN_256MS", "NODE_SCAN_256MS", "256msec")
lowPowerPeriod.addKey("NODE_SCAN_512MS", "NODE_SCAN_512MS", "512msec")
lowPowerPeriod.addKey("NODE_SCAN_1024MS", "NODE_SCAN_1024MS", "1024msec")
lowPowerPeriod.setDefaultValue(3)
lowPowerPeriod.setOutputMode("Value")
lowPowerPeriod.setDisplayMode("Description")
lowPowerPeriod.setDescription("The Low-power measurement period determine the interval between low-power touch measurement")

#Low-power Trigger Period
lowPowerTriggerPeriod = qtouchComponent.createIntegerSymbol("LOW_POWER_TRIGGER_PERIOD", LowPowerEvntMenu)
lowPowerTriggerPeriod.setLabel("Low-power Trigger Period")
lowPowerTriggerPeriod.setDefaultValue(100)
lowPowerTriggerPeriod.setMin(1)
lowPowerTriggerPeriod.setMax(65535)
lowPowerTriggerPeriod.setDescription("The Lowpower measurement period defines the interval between low-power touch measurement")

#Touch Inactivity Timeout
touchInactivityTime = qtouchComponent.createIntegerSymbol("TCH_INACTIVE_TIME", LowPowerEvntMenu)
touchInactivityTime.setLabel("Touch Inactivity Timeout")
touchInactivityTime.setDefaultValue(5000)
touchInactivityTime.setMin(0)
touchInactivityTime.setMax(65535)
touchInactivityTime.setDescription("Waiting time (in millisecond) for the application to switch to low-power measurement after the last touch.")

#Low-power Drift Wakeup Period 
driftPeriod = qtouchComponent.createIntegerSymbol("DRIFT_WAKE_UP_PERIOD", LowPowerEvntMenu)
driftPeriod.setLabel("Low-power Drift Wakeup Period ")
driftPeriod.setDefaultValue(2000)
driftPeriod.setMin(0)
driftPeriod.setMax(65535)
driftPeriod.setDescription("During low-power measurement, it is recommended to perfrom periodic active measurement to perform drifting. This parameter defines the measurement interval to perform drifting. It is recommended to configure this parameter more than Lowpower Period. A value of zero means drifting is disabled during low-power measurement.")

lowPowerKeymask = qtouchComponent.createStringSymbol("LOW_POWER_KEYS_MASK", LowPowerEvntMenu)
lowPowerKeymask.setLabel("Low-power Keys' mask ")
lowPowerKeymask.setDefaultValue("")
lowPowerKeymask.setDescription("low-power mask in hex")
lowPowerKeymask.setVisible(False)