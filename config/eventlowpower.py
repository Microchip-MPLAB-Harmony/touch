################################################################################
#### Component ####
################################################################################
LowPowerEvntMenu = qtouchComponent.createMenuSymbol("LOW_POWER_EVENT_MENU", touchMenu)
LowPowerEvntMenu.setLabel("Event Low Power Configuration")

# Enable Event based Low power 
enableEventLowPower = qtouchComponent.createIntegerSymbol("ENABLE_EVENT_LP", LowPowerEvntMenu)
enableEventLowPower.setLabel("Enable Event based Low Power")
enableEventLowPower.setMin(0)
enableEventLowPower.setMax(1)
enableEventLowPower.setDefaultValue(0)

#Low-power Node Selection
lowPowerNode = qtouchComponent.createIntegerSymbol("LOW_POWER_NODE", LowPowerEvntMenu)
lowPowerNode.setLabel("Low-power Node Selection")
lowPowerNode.setDefaultValue(0)
lowPowerNode.setMin(0)
lowPowerNode.setMax(255)
lowPowerNode.setDescription("Low-power measurement node number")

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
