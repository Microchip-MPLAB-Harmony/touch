"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchCustAddition():
    def __init__(self):
        self.dmaChannel = ""
        self.currentOcmp = ""
        self.currentTmr = ""
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []

    def setCurrentDmaChannel(self, chnum):
        self.dmaChannel = str(chnum)

    def getCurrentDmaChannel(self):
        return self.dmaChannel

    def setCurrentOCMPChannel(self, chnum):
        self.currentOcmp = str(chnum)

    def getCurrentOCMPChannel(self):
        return self.currentOcmp

    def setCurrentTMRChannel(self, chnum):
        self.currentTmr = str(chnum)

    def getCurrentTMRChannel(self):
        return self.currentTmr

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def collectPinsWithOCCapability(self,Database):
        packagePinCount = Database.getSymbolValue("core", "PPS_PIN_COUNT")
        #print packagePinCount
        component = Database.getComponentByID("core")
        symbol = component.getSymbolByID("SYS_PORT_PPS_OUTPUT_PIN_" + str(0))
        pins = []
        pins[:] = symbol.getValues()
        keys = []
        symbol = component.getSymbolByID("SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(0))
        for j in range(symbol.getKeyCount()):
            keys.append(str(symbol.getKey(j)))
        return pins, keys


    def initCustomMenu(self,ATDF,targetDevice,qtouchComponent,parentMenu,Database):
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
        additionalMenu = qtouchComponent.createMenuSymbol("ADDITIONAL_COFIG", parentMenu)
        additionalMenu.setLabel("Additional Configuration")
        additionalMenu.setVisible(True)
        additionalMenu.setEnabled(True)

        touchDMA = qtouchComponent.createKeyValueSetSymbol("TOUCH_PIC32MZDA_DMA", additionalMenu)
        touchDMA.setLabel("Select DMA")
        touchDMA.setDisplayMode("Description")
        self.addDepSymbol(touchDMA, "onPic32mzdaChange", ["TOUCH_PIC32MZDA_DMA"])

        numdmachannel = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
        for i in range(int(numdmachannel)):
            touchDMA.addKey("DMAC_CHANNEL_"+str(i), str(i), "DMA_CHANNEL_"+str(i))
            if self.dmaChannel == "":
                if Database.getSymbolValue("core", "DMAC_CHAN"+str(i)+"_ENBL") != True:
                    self.dmaChannel = str(i)
                    setSym = "DMAC_CHAN"+str(i)+"_ENBL"
                    Database.setSymbolValue("core",setSym, True)
                    setSym = "DMAC_REQUEST_"+str(i)+"_SOURCE"
                    Database.setSymbolValue("core",setSym, "ADC_DC1")
        touchDMA.setDefaultValue(int(self.dmaChannel))

        touchEnableDs = qtouchComponent.createBooleanSymbol("TOUCH_DRIVEN_SHIELD_ENABLE", additionalMenu)
        touchEnableDs.setLabel("Enable Driven Shield")
        touchEnableDs.setDefaultValue(False)
        self.addDepSymbol(touchEnableDs, "onPic32mzdaChange", ["TOUCH_DRIVEN_SHIELD_ENABLE"])

        touchOcmpList = qtouchComponent.createKeyValueSetSymbol("TOUCH_DS_COMP", additionalMenu)
        touchOcmpList.setLabel("Select OCMP")
        touchOcmpList.setVisible(False)
        touchOcmpList.setDisplayMode("Description")
        self.addDepSymbol(touchOcmpList, "onPic32mzdaChange", ["TOUCH_DS_COMP"])

        touchTmrList = qtouchComponent.createKeyValueSetSymbol("TOUCH_DS_TMR", additionalMenu)
        touchTmrList.setLabel("Select TMR")
        touchTmrList.setVisible(False)
        touchTmrList.setDisplayMode("Description")
        self.addDepSymbol(touchTmrList, "onPic32mzdaChange", ["TOUCH_DS_TMR"])
        touchTmrList.addKey("TMR2","tmr2","Timer 2")
        touchTmrList.addKey("TMR3","tmr3","Timer 3")

        ocmpList = []
        ocmp = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"OCMP\"]")
        instances = ocmp.getChildren()
        for inst in instances:
            ocmpList.append(inst.getAttribute("name"))
        for ocmp in ocmpList:
            touchOcmpList.addKey(ocmp,ocmp,ocmp)

        touchOcmpPins = qtouchComponent.createKeyValueSetSymbol("TOUCH_DS_COMP_PIN", additionalMenu)
        touchOcmpPins.setLabel("Select OC Pin Option")
        touchOcmpPins.setDefaultValue(0)
        touchOcmpPins.setDisplayMode("Description")
        touchOcmpPins.addKey("---","0","---")

        reMappablePins , remappableKeys = self.collectPinsWithOCCapability(Database)

        for pin in reMappablePins:
            touchOcmpPins.addKey(pin,pin,pin)

        # for pin in remappableKeys:
        #     if "OC" in pin:
        #         touchOcmpPins.addKey(pin,pin,pin)


        print "reMappablePins", "remappableKeys", reMappablePins, remappableKeys