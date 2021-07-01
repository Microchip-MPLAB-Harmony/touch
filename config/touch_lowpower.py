"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

class classTouchLP():
    def __init__(self):
        self.LOW_POWER_EVENTS_SUPPORTED_DEVICES =  ["SAMD20","SAMD21","SAMDA1","SAMHA1",
                "SAML11","SAML10",
                "SAMC21","SAMC20",
                "PIC32CMLE00","PIC32CMLS00",
                "SAML21","SAML22"]
        self.LOW_POWER_SUPPORTED_DEVICES =  ["SAMD20","SAMD21","SAMDA1","SAMHA1",
            "SAML11","SAML10",
            "SAMC21","SAMC20",
            "PIC32CMLE00","PIC32CMLS00",
            "SAME54","SAME53","SAME51","SAMD51",
            "SAML21","SAML22",
            "SAMD10","SAMD11"]
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []

    def lowPowerEventsSupported(self,targetDevice):
        """
        Checks if the target device supports Low Power events
        Arguments : targetDevice
        Returns : True / False
        """
        if( targetDevice in self.LOW_POWER_EVENTS_SUPPORTED_DEVICES):
            return True
        else:
            return False

    def lowPowerSupported(self,targetDevice):
        """
        Checks if the target device supports Low Power operation
        Arguments : targetDevice
        Returns : True / False
        """
        if( targetDevice in self.LOW_POWER_SUPPORTED_DEVICES):
            return True
        else:
            return False

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def initLowPowerInstance(self,qtouchComponent, parentLabel , targetDevice):
        """
        Creates Low power menu and variables
        Arguments :
            :qtouchComponent : touchModule
            :parentLabel : parent symbol for added menu items
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            none
        """
        LowPowerEvntMenu = qtouchComponent.createMenuSymbol("LOW_POWER_EVENT_MENU", parentLabel)
        LowPowerEvntMenu.setLabel("Low Power Configuration")
        if (self.lowPowerEventsSupported(targetDevice)):
            enableEventLowPower = qtouchComponent.createBooleanSymbol("ENABLE_EVENT_LP", LowPowerEvntMenu)
            enableEventLowPower.setLabel("Event based Low Power")
            enableEventLowPower.setDefaultValue(False)
        
        self.setLowPowerKeyValues(qtouchComponent,LowPowerEvntMenu)
        self.setLowPowerDetThreshold(qtouchComponent,LowPowerEvntMenu)
        self.setLowPowerPeriod(qtouchComponent,LowPowerEvntMenu,targetDevice)
        self.setLowPowerTriggerPeriod(qtouchComponent,LowPowerEvntMenu)
        self.setTouchInactivityTime(qtouchComponent,LowPowerEvntMenu)
        self.setDriftPeriod(qtouchComponent,LowPowerEvntMenu)
        self.setLowPowerKeymask(qtouchComponent,LowPowerEvntMenu)


    def setLowPowerKeyValues(self,qtouchComponent,LowPowerEvntMenu):
        """ Populates the low Power Keys
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
        Returns :
            :none
        """
        lowPowerKey = qtouchComponent.createStringSymbol("LOW_POWER_KEYS", LowPowerEvntMenu)
        lowPowerKey.setLabel("Low-power Keys Selection")
        lowPowerKey.setDefaultValue("")
        lowPowerKey.setDescription("Series of low-power key numbers separated by ,")
        self.addDepSymbol(lowPowerKey, "enablePM", ["LOW_POWER_KEYS"])

    def setLowPowerDetThreshold(self,qtouchComponent,LowPowerEvntMenu):
        """ Populates the low Power Detect threshold
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
        Returns :
            :none
        """
        lowPowerDetThreshold = qtouchComponent.createIntegerSymbol("LOW_POWER_DET_THRESHOLD", LowPowerEvntMenu)
        lowPowerDetThreshold.setLabel("Low-power Detect Threshold")
        lowPowerDetThreshold.setDefaultValue(10)
        lowPowerDetThreshold.setMin(10)
        lowPowerDetThreshold.setMax(255)
        lowPowerDetThreshold.setDescription("Sensor detect threshold for low-power measurement")

    def setLowPowerPeriod(self,qtouchComponent,LowPowerEvntMenu,targetDevice):
        """ Populates the low power Measurement Period
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
            :targetDevice : see interface.getDeviceSeries()
        Returns :
            :none
        """
        lowPowerPeriod = qtouchComponent.createKeyValueSetSymbol("LOW_POWER_PERIOD", LowPowerEvntMenu)
        lowPowerPeriod.setLabel("Low-power Measurement Period")
        if (targetDevice in ["SAMD20","SAMD21","SAMDA1","SAMHA1"]):
            lowPowerPeriod.addKey("NODE_SCAN_4MS", "NODE_SCAN_4MS", "4msec")
            lowPowerPeriod.addKey("NODE_SCAN_8MS", "NODE_SCAN_8MS", "8msec")
            lowPowerPeriod.addKey("NODE_SCAN_16MS", "NODE_SCAN_16MS", "16msec")
            lowPowerPeriod.addKey("NODE_SCAN_32MS", "NODE_SCAN_32MS", "32msec")
            lowPowerPeriod.addKey("NODE_SCAN_64MS", "NODE_SCAN_64MS", "64msec")
            lowPowerPeriod.addKey("NODE_SCAN_128MS", "NODE_SCAN_128MS", "128msec")
            lowPowerPeriod.addKey("NODE_SCAN_256MS", "NODE_SCAN_256MS", "256msec")
            lowPowerPeriod.addKey("NODE_SCAN_512MS", "NODE_SCAN_512MS", "512msec")
        if (targetDevice not in ["SAMD20","SAMD21","SAMDA1","SAMHA1"]):
            lowPowerPeriod.addKey("NODE_SCAN_1024MS", "NODE_SCAN_1024MS", "1024msec")
            lowPowerPeriod.setDefaultValue(3)
        else:
            lowPowerPeriod.setDefaultValue(4)
        lowPowerPeriod.setOutputMode("Value")
        lowPowerPeriod.setDisplayMode("Description")
        lowPowerPeriod.setDescription("The Low-power measurement period determine the interval between low-power touch measurement")

    def setLowPowerTriggerPeriod(self,qtouchComponent,LowPowerEvntMenu):
        """ Populates the low Power Trigger Period
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
        Returns :
            :none
        """
        lowPowerTriggerPeriod = qtouchComponent.createIntegerSymbol("LOW_POWER_TRIGGER_PERIOD", LowPowerEvntMenu)
        lowPowerTriggerPeriod.setLabel("Low-power Trigger Period")
        lowPowerTriggerPeriod.setDefaultValue(100)
        lowPowerTriggerPeriod.setMin(1)
        lowPowerTriggerPeriod.setMax(65535)
        lowPowerTriggerPeriod.setDescription("The Lowpower measurement period defines the interval between low-power touch measurement")

    def setTouchInactivityTime(self,qtouchComponent,LowPowerEvntMenu):
        """ Populates Touch Inactivity Timeout
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
        Returns :
            :none
        """
        touchInactivityTime = qtouchComponent.createIntegerSymbol("TCH_INACTIVE_TIME", LowPowerEvntMenu)
        touchInactivityTime.setLabel("Touch Inactivity Timeout")
        touchInactivityTime.setDefaultValue(5000)
        touchInactivityTime.setMin(0)
        touchInactivityTime.setMax(65535)
        touchInactivityTime.setDescription("Waiting time (in millisecond) for the application to switch to low-power measurement after the last touch.")

    def setDriftPeriod(self,qtouchComponent,LowPowerEvntMenu):
        """ Populates Low Power Drift Wakeup Period 
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
        Returns :
            :none
        """
        driftPeriod = qtouchComponent.createIntegerSymbol("DRIFT_WAKE_UP_PERIOD", LowPowerEvntMenu)
        driftPeriod.setLabel("Low-power Drift Wakeup Period ")
        driftPeriod.setDefaultValue(2000)
        driftPeriod.setMin(0)
        driftPeriod.setMax(65535)
        driftPeriod.setDescription("During low-power measurement, it is recommended to perfrom periodic active measurement to perform drifting. This parameter defines the measurement interval to perform drifting. It is recommended to configure this parameter more than Lowpower Period. A value of zero means drifting is disabled during low-power measurement.")

    def setLowPowerKeymask(self,qtouchComponent,LowPowerEvntMenu):
        """ Creates Low Power Drift key mask symbol, symbol is populated by processSoftwareLP(symbol, event)
        Arguments :
            :qtouchComponent : touchModule
            :LowPowerEvntMenu : parent symbol for added menu items
        Returns :
            :none
        """
        lowPowerKeymask = qtouchComponent.createStringSymbol("LOW_POWER_KEYS_MASK", LowPowerEvntMenu)
        lowPowerKeymask.setLabel("Low-power Keys' mask ")
        lowPowerKeymask.setDefaultValue("")
        lowPowerKeymask.setDescription("low-power mask in hex")
        lowPowerKeymask.setVisible(False)

    def processSoftwareLP(self,symbol, event):
        """Event Handler for Creating low power Keys Mask. 
        Triggered by qtouch.ongenerate. 
        Groups the bits into 8bit masks (lp_mask_of_8)
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        localComponent = symbol.getComponent()
        low_power_mask = localComponent.getSymbolByID("LOW_POWER_KEYS").getValue()
        total_num_channel = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
        lp_mask = []
        low_power_keys = []
        lp_mask_of_8 = []
        
        for i in low_power_mask.split(","):
            low_power_keys.append(i)
        for i in range(total_num_channel):
            if i in low_power_keys:
                lp_mask.append(1)
            else:
                lp_mask.append(0)
        for i in range(1000):
            if len(lp_mask)%8 != 0:
                lp_mask.append(0)
            else:
                break
        for i in range(int(len(lp_mask)/8)):
            sum = 0
            for loop_cnt in range(8):
                index = i*8 + loop_cnt
                if lp_mask[index] == 1:
                    sum = sum + pow(2,loop_cnt)
            lp_mask_of_8.append(hex(sum))
        tempSymbol = localComponent.getSymbolByID("LOW_POWER_KEYS_MASK")
        tempSymbol.setValue(",".join(lp_mask_of_8))