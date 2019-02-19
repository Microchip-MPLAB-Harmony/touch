def loadModule():

    #mod will have value if PTC peripheral is present in a device variant
    mod = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]")
    for x in ["SAMC21", "SAMC20"]:
        if x in Variables.get("__PROCESSOR"):
            if mod:
                qtouchComponent = Module.CreateComponent("lib_qtouch", "Touch Library", "/Touch/", "config/qtouch.py")
                qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
                qtouchComponent.addCapability("lib_qtouch", "PTC")
                qtouchComponent.addDependency("Touch_timer", "TMR", None, False, True)
                qtouchComponent.setDependencyEnabled("Touch_timer", True)
                qtouchComponent.addDependency("Touch_sercom", "UART", None, False, False)
                qtouchComponent.setDependencyEnabled("Touch_sercom", False)
