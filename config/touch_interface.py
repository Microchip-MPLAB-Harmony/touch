"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

"""essential changes for each release must update and review
        : releaseVersion
        : releaseYear
"""
class classTouchInterface():
    def __init__(self):
        self.deviceChild = []
        self.deviceName = ""
        self.deviceSeries = "" 

    def getDeviceName(self):
        """
        returns the target device name
        Arguments:
            :none
        Returns:
            self.deviceName (string)
        """
        return self.deviceName

    def getDeviceSeries(self):
        """
        returns the target device series
        Arguments:
            :none
        Returns:
            self.deviceSeries (string)
        """
        return self.deviceSeries

    # def getDeviceArchictecture():
    #     return deviceArchictecture

    # def getDeviceFamily():
    #     return deviceFamily

    def getTargetDeviceInfo(self,ATDF,qtouchComponent,touchMenu):
        """
        retrieve target device information from ATDF
        Arguments:
            :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
            :qtouchComponent : touch module
            :touchMenu : Parent menu for the created symbols
        Returns:
            self.deviceSeries (string)
        """
        releaseVersion = "v3.11.2"
        releaseYear    = "2022"

        devicesNode = ATDF.getNode("/avr-tools-device-file/devices")
        deviceVariant = ATDF.getNode("/avr-tools-device-file/variants").getChildren()


        self.deviceChild = devicesNode.getChildren()
        self.deviceName = self.deviceChild[0].getAttribute("name")
        self.deviceSeries = self.deviceChild[0].getAttribute("series")
        if self.deviceSeries == "PIC32CMLS60":
            self.deviceSeries = "PIC32CMLS00"
        if self.deviceSeries == "PIC32MZ":
            self.deviceSeries = self.deviceChild[0].getAttribute("family")

        # deviceArchictecture = self.deviceChild[0].getAttribute("architecture")
        # deviceFamily = self.deviceChild[0].getAttribute("family")


        getDeviceSeries = qtouchComponent.createStringSymbol("DEVICE_NAME", touchMenu)
        getDeviceSeries.setDefaultValue(self.deviceSeries)
        getDeviceSeries.setVisible(True)

        getDeviceVariant = qtouchComponent.createStringSymbol("DEVICE_VARIANT", touchMenu)
        getDeviceVariant.setDefaultValue(deviceVariant[0].getAttribute("pinout"))
        getDeviceVariant.setVisible(False)

        getDeviceName = qtouchComponent.createStringSymbol("DEVICE_NAME_SPECIFIC", touchMenu)
        getDeviceName.setDefaultValue(self.deviceName)
        getDeviceName.setVisible(True)

        getreleaseVersion = qtouchComponent.createStringSymbol("REL_VER", touchMenu)
        getreleaseVersion.setDefaultValue(releaseVersion)
        getreleaseVersion.setVisible(False)

        getreleaseYear = qtouchComponent.createStringSymbol("REL_YEAR", touchMenu)
        getreleaseYear.setDefaultValue(releaseYear)
        getreleaseYear.setVisible(False)