"""
Copyright (C) [2023], Microchip Technology Inc., and its subsidiaries. All rights reserved.

The software and documentation is provided by microchip and its contributors
"as is" and any express, implied or statutory warranties, including, but not
limited to, the implied warranties of merchantability, fitness for a particular
purpose and non-infringement of third party intellectual property rights are
disclaimed to the fullest extent permitted by law. In no event shall microchip
or its contributors be liable for any direct, indirect, incidental, special,
exemplary, or consequential damages (including, but not limited to, procurement
of substitute goods or services; loss of use, data, or profits; or business
interruption) however caused and on any theory of liability, whether in contract,
strict liability, or tort (including negligence or otherwise) arising in any way
out of the use of the software and documentation, even if advised of the
possibility of such damage.

Except as expressly permitted hereunder and subject to the applicable license terms
for any third-party software incorporated in the software and any applicable open
source software license terms, no license or other rights, whether express or
implied, are granted under any patent or other intellectual property rights of
Microchip or any third party.
"""
class classTouchPads():
    def __init__(self):
        self.pinNode = {}
        self.touchPads = {}
        self.touchModule = "PTC"

    def collectPadInfo(self,ATDF):
        self.pads = {}
        self.touchPads = {}
        #pinNode = ATDF.getNode("/avr-tools-device-file/pinouts/pinout")
        pinOuts = ATDF.getNode("/avr-tools-device-file/pinouts")
        pinNode = pinOuts.getChildren()[len(pinOuts.getChildren())-1]
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

