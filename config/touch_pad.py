class classTouchPads():
    def __init__(self):
        self.pinNode = {}
        self.touchPads = {}
        self.touchModule = "PTC"

    def collectPadInfo(self,ATDF):
        self.pads = {}
        self.touchPads = {}
        pinNode = ATDF.getNode("/avr-tools-device-file/pinouts/pinout")

        if pinNode != None:
            pinValues = []
            pinValues = pinNode.getChildren()
            for index in range(0, len(pinValues)):
                self.pads[pinValues[index].getAttribute("pad")] = [pinValues[index].getAttribute("position"), []]

        ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")
        if(ptcPinNode == None):
            ptcPinNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/signals")
            self.touchModule = "ADC0"

        if ptcPinNode != None:
            ptcPinValues = []
            ptcPinValues = ptcPinNode.getChildren()
            for index in range(0, len(ptcPinValues)):
                groups = self.pads[ptcPinValues[index].getAttribute("pad")][1]
                if(ptcPinValues[index].getAttribute("index")==None):
                    groups.append(ptcPinValues[index].getAttribute("group"))
                else:
                    groups.append(ptcPinValues[index].getAttribute("group")+ptcPinValues[index].getAttribute("index"))

        for pad in self.pads:
            groups = self.pads[pad][1]
            if(len(groups) > 0):
                fsetting = self.touchModule+"_"
                for group in groups:
                    fsetting = fsetting + group + "/"
                self.touchPads[pad] = { "index":self.pads[pad][0], "function":fsetting[:len(fsetting)-1] }
        
        print self.touchPads
        print self.pads

    def getTouchPads(self):
        return self.touchPads

    def getPads(self):
        return self.pads

    def getTouchModule(self):
        return self.touchModule

