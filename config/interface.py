#essential changes for each release
releaseVersion = "v3.7.0"
releaseYear    = "2020"


deviceNode = ATDF.getNode("/avr-tools-device-file/devices")
deviceVariant = ATDF.getNode("/avr-tools-device-file/variants").getChildren()

deviceChild = []
deviceChild = deviceNode.getChildren()
deviceName = deviceChild[0].getAttribute("series")
print(deviceName)
print(deviceVariant[0].getAttribute("pinout"))

global getDeviceName
getDeviceName = qtouchComponent.createStringSymbol("DEVICE_NAME", touchMenu)
getDeviceName.setDefaultValue(deviceName)
getDeviceName.setVisible(False)

getDeviceVariant = qtouchComponent.createStringSymbol("DEVICE_VARIANT", touchMenu)
getDeviceVariant.setDefaultValue(deviceVariant[0].getAttribute("pinout"))
getDeviceVariant.setVisible(False)

getreleaseVersion = qtouchComponent.createStringSymbol("REL_VER", touchMenu)
getreleaseVersion.setDefaultValue(releaseVersion)
getreleaseVersion.setVisible(False)

getreleaseYear = qtouchComponent.createStringSymbol("REL_YEAR", touchMenu)
getreleaseYear.setDefaultValue(releaseYear)
getreleaseYear.setVisible(False)