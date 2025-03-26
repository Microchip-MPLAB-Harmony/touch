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

"""essential changes for each release must update and review
        : releaseVersion
        : releaseYear
"""
from json_loader import json_loader_instance
class classTouchInterface():
    def __init__(self):
        # self.deviceChild = []
        self.deviceName = ""
        self.deviceSeries = "" 
        self.deviceVariant= ""

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
        releaseVersion = "v3.18.0"
        releaseYear    = "2025"

        # self.deviceChild = devicesNode.getChildren()
        self.deviceName = json_loader_instance.get_deviceName()
        self.deviceSeries = json_loader_instance.get_deviceSeries()
        self.deviceVariant = json_loader_instance.get_deviceVariant()

        getDeviceSeries = qtouchComponent.createStringSymbol("DEVICE_NAME", touchMenu)
        getDeviceSeries.setDefaultValue(self.deviceSeries)
        getDeviceSeries.setVisible(True)

        getDeviceVariant = qtouchComponent.createStringSymbol("DEVICE_VARIANT", touchMenu)
        getDeviceVariant.setDefaultValue(self.deviceVariant)
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