#essential changes for each release
releaseVersion = "v3.4.0"
releaseYear    = "2019"


deviceNode = ATDF.getNode("/avr-tools-device-file/devices")
deviceChild = []
deviceChild = deviceNode.getChildren()
deviceName = deviceChild[0].getAttribute("series")
print(deviceName)

global getDeviceName
getDeviceName = qtouchComponent.createStringSymbol("DEVICE_NAME", touchMenu)
getDeviceName.setDefaultValue(deviceName)
getDeviceName.setVisible(False)

getreleaseVersion = qtouchComponent.createStringSymbol("REL_VER", touchMenu)
getreleaseVersion.setDefaultValue(releaseVersion)
getreleaseVersion.setVisible(False)

getreleaseYear = qtouchComponent.createStringSymbol("REL_YEAR", touchMenu)
getreleaseYear.setDefaultValue(releaseYear)
getreleaseYear.setVisible(False)