def loadModule():
    qtouchComponent = Module.CreateComponent("lib_qtouch",
                                             "QTouch Library",
                                             "/Libraries/", "config/qtouch.py")
    qtouchComponent.setDisplayType("Peripheral Touch Controller(PTC)")
    qtouchComponent.addCapability("lib_qtouch", "PTC")
    qtouchComponent.addDependency("QTouch_rtc", "TMR", None, False, True)
    qtouchComponent.addDependency("QTouch_sercom", "UART", None, False, False)
