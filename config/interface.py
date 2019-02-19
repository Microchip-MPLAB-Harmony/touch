deviceNode = ATDF.getNode("/avr-tools-device-file/devices")
deviceChild = []
deviceChild = deviceNode.getChildren()
deviceName = deviceChild[0].getAttribute("series")
print(deviceName)

global getDeviceName
getDeviceName = qtouchComponent.createStringSymbol("DEVICE_NAME", touchMenu)
getDeviceName.setDefaultValue(deviceName)
getDeviceName.setVisible(False)