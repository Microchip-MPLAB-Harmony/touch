def loadModule():

    #mod will have value if PTC peripheral is present in a device variant
    mod = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]")
    for x in ["SAMC21", "SAMC20"]:
        if x in Variables.get("__PROCESSOR"):
            if mod:
                qtouchComponent = Module.CreateComponent("lib_qtouch", "QTouch Library", "/QTouch/", "config/qtouch.py")
                qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                qtouchComponent.addCapability("lib_qtouch", "PTC")
                qtouchComponent.addDependency("QTouch_timer", "TMR", None, False, True)
                qtouchComponent.setDependencyEnabled("QTouch_timer", True)
                qtouchComponent.addDependency("QTouch_sercom", "UART", None, False, False)
                qtouchComponent.setDependencyEnabled("QTouch_sercom", False)
