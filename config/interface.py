"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

"""essential changes for each release must update and review
        : releaseVersion
        : releaseYear
"""
deviceChild = []
deviceName = ""
deviceSeries = "" 
# deviceArchictecture 
# deviceFamily 

def getDeviceName():
    """
    returns the target device name
    Arguments:
        :none
    Returns:
        deviceName (string)
    """
    return deviceName

def getDeviceSeries():
    """
    returns the target device series
    Arguments:
        :none
    Returns:
        deviceSeries (string)
    """
    return deviceSeries

# def getDeviceArchictecture():
#     return deviceArchictecture

# def getDeviceFamily():
#     return deviceFamily


def getTargetDeviceInfo(ATDF,qtouchComponent,touchMenu):
    """
    retrieve target device information from ATDF
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :qtouchComponent : touch module
        :touchMenu : Parent menu for the created symbols
    Returns:
        deviceSeries (string)
    """
    global deviceChild
    global deviceName
    global deviceSeries
    
    releaseVersion = "v3.10.0"
    releaseYear    = "2021"

    devicesNode = ATDF.getNode("/avr-tools-device-file/devices")
    deviceVariant = ATDF.getNode("/avr-tools-device-file/variants").getChildren()


    deviceChild = devicesNode.getChildren()
    deviceName = deviceChild[0].getAttribute("name")
    deviceSeries = deviceChild[0].getAttribute("series")
    # deviceArchictecture = deviceChild[0].getAttribute("architecture")
    # deviceFamily = deviceChild[0].getAttribute("family")


    getDeviceSeries = qtouchComponent.createStringSymbol("DEVICE_NAME", touchMenu)
    getDeviceSeries.setDefaultValue(deviceSeries)
    getDeviceSeries.setVisible(True)

    getDeviceVariant = qtouchComponent.createStringSymbol("DEVICE_VARIANT", touchMenu)
    getDeviceVariant.setDefaultValue(deviceVariant[0].getAttribute("pinout"))
    getDeviceVariant.setVisible(False)

    getDeviceName = qtouchComponent.createStringSymbol("DEVICE_NAME_SPECIFIC", touchMenu)
    getDeviceName.setDefaultValue(deviceName)
    getDeviceName.setVisible(True)

    getreleaseVersion = qtouchComponent.createStringSymbol("REL_VER", touchMenu)
    getreleaseVersion.setDefaultValue(releaseVersion)
    getreleaseVersion.setVisible(False)

    getreleaseYear = qtouchComponent.createStringSymbol("REL_YEAR", touchMenu)
    getreleaseYear.setDefaultValue(releaseYear)
    getreleaseYear.setVisible(False)