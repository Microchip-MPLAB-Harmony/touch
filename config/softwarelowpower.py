################################################################################
#### Component ####
################################################################################
LowPowerSWMenu = qtouchComponent.createMenuSymbol("LOW_POWER_SW_MENU", touchMenu)
LowPowerSWMenu.setLabel("SW Low Power Configuration")

# Enable Software based Low power 
enableSoftwareLowPower = qtouchComponent.createIntegerSymbol("ENABLE_SOFTWARE_LP", LowPowerSWMenu)
enableSoftwareLowPower.setLabel("Enable Software based Low Power")
enableSoftwareLowPower.setDefaultValue(0)
enableSoftwareLowPower.setMin(0)
enableSoftwareLowPower.setMax(1)

#Low-power Node Selection
lowPowerKey = qtouchComponent.createStringSymbol("LOW_POWER_KEYS", LowPowerSWMenu)
lowPowerKey.setLabel("Low-power Keys Selection")
lowPowerKey.setDefaultValue("")
lowPowerKey.setDescription("Series of low-power key numbers separated by ,")

#Low-power Trigger Period
lowPowerTriggerPeriod = qtouchComponent.createIntegerSymbol("LOW_POWER_TRIGGER_PERIOD", LowPowerSWMenu)
lowPowerTriggerPeriod.setLabel("Low-power Trigger Period")
lowPowerTriggerPeriod.setDefaultValue(100)
lowPowerTriggerPeriod.setMin(1)
lowPowerTriggerPeriod.setMax(65535)
lowPowerTriggerPeriod.setDescription("The Lowpower measurement period defines the interval between low-power touch measurement")

#Touch Inactivity Timeout
touchInactivityTime = qtouchComponent.createIntegerSymbol("SW_TCH_INACTIVE_TIME", LowPowerSWMenu)
touchInactivityTime.setLabel("Touch Inactivity Timeout")
touchInactivityTime.setDefaultValue(5000)
touchInactivityTime.setMin(0)
touchInactivityTime.setMax(65535)
touchInactivityTime.setDescription("Waiting time (in millisecond) for the application to switch to low-power measurement after the last touch.")

#Low-power Drift Wakeup Period 
driftPeriod = qtouchComponent.createIntegerSymbol("SW_DRIFT_WAKE_UP_PERIOD", LowPowerSWMenu)
driftPeriod.setLabel("Low-power Drift Wakeup Period ")
driftPeriod.setDefaultValue(2000)
driftPeriod.setMin(0)
driftPeriod.setMax(65535)
driftPeriod.setDescription("During low-power measurement, it is recommended to perfrom periodic active measurement to perform drifting. This parameter defines the measurement interval to perform drifting. It is recommended to configure this parameter more than Lowpower Period.If drift period is not a multiple of Low-power measurement period, then drift will happen at multiples of the Low-power period which is just above the configured drift period. A value of zero means drifting is disabled during low-power measurement.")
