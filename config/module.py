"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

supportedDevices = ["PIC32MZ","SAMC21","SAMC20", "SAME51","SAME53","SAME54","SAMD51","SAMD20","SAMD21","SAML21","SAML22","SAML10","SAML11","SAMD10","SAMD11","SAMDA1","SAMHA1","PIC32CM"]
#The following devices which have X,Y signals listed under ADC0 instead of PTC are listed as special devices.
ADCDevices = ["SAME51","SAME53","SAME54","SAMD51"]
#notSupportedVariants = ["ATSAMC21J18A"]
notSupportedVariants = []
PIC32Devices = ["PIC32MZ"]

def loadModule():
    #mod will have value if PTC peripheral is present in a device variant
    mod = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]")
    deviceNode = ATDF.getNode("/avr-tools-device-file/devices")
    deviceChild = deviceNode.getChildren()
    deviceName = deviceChild[0].getAttribute("family")
    for x in supportedDevices:
        if x in Variables.get("__PROCESSOR"):
            if Variables.get("__PROCESSOR") not in notSupportedVariants:
                if mod:
                    qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
                    qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                    qtouchComponent.addCapability("lib_qtouch", "PTC")
                    qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                    qtouchComponent.setDependencyEnabled("Touch_timer", True)
                    qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom", False)
                    qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)
                elif x in ADCDevices:
                    qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
                    qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                    qtouchComponent.addCapability("lib_qtouch", "PTC")
                    qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                    qtouchComponent.setDependencyEnabled("Touch_timer", True)
                    qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom", False)
                    qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)
                elif x in PIC32Devices and deviceName == "PIC32MZW":
                    qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
                    qtouchComponent.setDisplayType("HCVD")
                    qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                    qtouchComponent.setDependencyEnabled("Touch_timer", True)
                    qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom", False)
                    qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)
