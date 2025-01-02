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
"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

supportedDevices = ["PIC32CZ","PIC32CX","WBZ3","WBZ6","PIC32MZ","SAMC21","SAMC20", "SAME51","SAME53","SAME54","SAMD51","SAMD20","SAMD21","SAML21","SAML22","SAML10","SAML11","SAML1xE","SAMD10","SAMD11","SAMDA1","SAMHA1","PIC32CM","PIC32CK"]
#The following devices which have X,Y signals listed under ADC0 instead of PTC are listed as special devices.
ADCDevices = ["SAME51","SAME53","SAME54","SAMD51"]
#notSupportedVariants = ["ATSAMC21J18A"]
notSupportedVariants = []
PIC32Devices = ["PIC32MZ", "PIC32MZW","PIC32CX","WBZ3","WBZ6"]
PIC32DeviceVariant = ["PIC32MZW", "PIC32MZDA","PIC32CX","WBZ3","WBZ6"]



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
                    qtouchComponentAcquistion = Module.CreateComponent("ptc","PTC","/Touch/","config/ptc_based_acq_engine.py")
                    qtouchComponentAcquistion.addCapability("ptc_Acq_Engine", "Acq_Engine")
                    qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                    qtouchComponent.setDependencyEnabled("PTC",True)
                    qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                    qtouchComponent.setDependencyEnabled("Touch_timer", True)
                    qtouchComponent.addDependency("SW_Timer", "SYS_TIME", None, True, True)
                    qtouchComponent.setDependencyEnabled("SW_Timer", False)
                    qtouchComponent.addDependency("lib_acquire","Acq_Engine",None,False,True)
                    qtouchComponent.setDependencyEnabled("lib_acquire", True)
                    qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom", False)
                    qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)
                    qtouchComponent.addCapability("lib_qtouch", "TouchData")
                elif x in ADCDevices:
                    qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
                    qtouchComponentAcquistion = Module.CreateComponent("ptc","PTC","/Touch/","config/ptc_based_acq_engine.py")
                    qtouchComponentAcquistion.addCapability("ptc_Acq_Engine", "Acq_Engine")
                    qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                    qtouchComponent.addCapability("lib_qtouch", "TouchData")
                    qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                    qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                    qtouchComponent.addDependency("SW_Timer", "SYS_TIME", None, True, True)
                    qtouchComponent.setDependencyEnabled("SW_Timer", False)
                    qtouchComponent.addDependency("lib_acquire","Acq_Engine",None,False,True)
                    qtouchComponent.setDependencyEnabled("lib_acquire", True)
                    qtouchComponentAcquistion.addDependency("lib_acquire","ADC",None,False,True)
                    qtouchComponentAcquistion.setDependencyEnabled("lib_acquire", True)
                    qtouchComponent.setDependencyEnabled("Touch_timer", True)
                    qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom", False)
                    qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)
                elif (x in PIC32Devices) and (deviceName in PIC32DeviceVariant):
                    qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
                    qtouchComponent.setDisplayType("HCVD")
                    qtouchComponent.addDependency("Acq_Engine", "ADC", None, False, True)
                    qtouchComponent.setDependencyEnabled("Acq_Engine", True)
                    qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                    qtouchComponent.setDependencyEnabled("Touch_timer", True)
                    qtouchComponent.addDependency("SW_Timer", "SYS_TIME", None, True, True)
                    qtouchComponent.setDependencyEnabled("SW_Timer", False)
                    qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom", False)
                    qtouchComponent.addDependency("Touch_sercom_Krono", "UART", None, False, False)
                    qtouchComponent.setDependencyEnabled("Touch_sercom_Krono", False)
