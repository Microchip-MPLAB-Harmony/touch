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
from json_loader import json_loader_instance

class classTouchSurface():
    def __init__(self, node_inst):
        self.nodeInst = node_inst
        self.json_data=json_loader_instance.get_data()
        # self.surface_rearrangement_macro = set(["SAML10","SAML1xE","SAML11","PIC32CMLE00","PIC32CMLS00","SAME54","SAME53","SAME51","SAMD51"])

    def initSurfaceInstance(self,qtouchComponent, parentLabel , targetDevice, touchKeyCountMax):
        """Initialise Surface Instance
        Arguments:
            :qtouchComponent : touchModule
            :parentLabel : parent symbol for added menu items
            :targetDevice : see interface.getDeviceSeries()
            :touchKeyCountMax : see target_device.getMutualCount()
        Returns:
            :none
        """    
        enableSurfaceMenu = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE", parentLabel)
        enableSurfaceMenu.setLabel("Enable Surface")
        enableSurfaceMenu.setDefaultValue(False)
        enableSurfaceMenu.setDependencies(self.surfaceUpdateEnabled,["ENABLE_SURFACE"])

        surfaceMenu = qtouchComponent.createMenuSymbol("SURFACE_MENU", enableSurfaceMenu)
        surfaceMenu.setLabel("Surface Configuration")
        surfaceMenu.setDescription("Configure Surface")
        surfaceMenu.setVisible(False)

        if self.json_data["features"]["xy_multiplex"] == True:
            touchChSurafceX = qtouchComponent.createStringSymbol("TOUCH_CH_SURFACE_X_LINES", surfaceMenu)
            touchChSurafceX.setVisible(True)
            touchChSurafceY = qtouchComponent.createStringSymbol("TOUCH_CH_SURFACE_Y_LINES", surfaceMenu)
            touchChSurafceY.setVisible(True)

        orientationKey = qtouchComponent.createIntegerSymbol("SURFACE_ORIENTATION", surfaceMenu)
        self.setOrientationKeyValues(orientationKey)
        enableSurface1T = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE1T", surfaceMenu)
        self.setEnableSurface1TValues(enableSurface1T)
        enableSurface2T = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE2T", surfaceMenu)
        self.setEnableSurface2TValues(enableSurface2T)
        horiStartKey = qtouchComponent.createIntegerSymbol("HORI_START_KEY", surfaceMenu)
        self.setHoriStartKeyValues(horiStartKey, touchKeyCountMax)
        horiNumKey = qtouchComponent.createIntegerSymbol("HORI_NUM_KEY", surfaceMenu)
        self.setHoriNumKeyValues(horiNumKey)
        vertStartKey = qtouchComponent.createIntegerSymbol("VERT_START_KEY", surfaceMenu)
        self.setVertStartKeyValues(vertStartKey, touchKeyCountMax)
        vertNumKey = qtouchComponent.createIntegerSymbol("VERT_NUM_KEY", surfaceMenu)
        self.setVertNumKeyValues(vertNumKey)
        positionResol = qtouchComponent.createKeyValueSetSymbol("DEF_POS_RESOLUTION", surfaceMenu)
        self.setPositionResolValues(positionResol)
        deadbandPercent = qtouchComponent.createKeyValueSetSymbol("DEF_DEADBAND_PERCENT", surfaceMenu)
        self.setDeadbandPercentValues(deadbandPercent)
        medianFilter = qtouchComponent.createIntegerSymbol("ENABLE_MED_FILTER", surfaceMenu)
        self.setMedianFilterValues(medianFilter)
        iirFilter = qtouchComponent.createIntegerSymbol("ENABLE_IIR_FILTER", surfaceMenu)
        self.setIIRFilterValues(iirFilter)
        posHysterisis = qtouchComponent.createIntegerSymbol("DEF_POS_HYS", surfaceMenu)
        self.setPositionHysteresisValues(posHysterisis)
        contactMinThreshold = qtouchComponent.createIntegerSymbol("DEF_CONTACT_THRESHOLD", surfaceMenu)
        self.setContactMinThresholdValues(contactMinThreshold)

    def surfaceUpdateEnabled(self,symbol,event):
        """Enables Surface functionality.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component = symbol.getComponent()
        if (component.getSymbolByID("ENABLE_SURFACE").getValue() == True):
            component.getSymbolByID("SURFACE_MENU").setEnabled(True)
            component.getSymbolByID("SURFACE_MENU").setVisible(True)
        else:
            component.getSymbolByID("SURFACE_MENU").setEnabled(False)
            component.getSymbolByID("SURFACE_MENU").setVisible(False)

        if component.getSymbolValue("TOUCH_PRE_GENERATE"):
            component.setSymbolValue("TOUCH_PRE_GENERATE", False)
        component.setSymbolValue("TOUCH_PRE_GENERATE", True)

    def setOrientationKeyValues(self,orientationKey):
        orientationKey.setLabel("Set Orientation of Surface")
        orientationKey.setDefaultValue(0)


    def setEnableSurface1TValues(self,enableSurface1T): 
        """Populate the 1 touch surface enable symbol 
        Arguments:
            :enableSurface1T : symbol to be populated
        Returns:
            none
        """
        enableSurface1T.setLabel("Enable Surface 1T")
        enableSurface1T.setDefaultValue(False)
        enableSurface1T.setDependencies(self.enableSurfaceFiles,["ENABLE_SURFACE1T"])

    def setEnableSurface2TValues(self,enableSurface2T):
        """Populate the 2 touch surface enable symbol 
        Arguments:
            :enableSurface2T : symbol to be populated
        Returns:
            none
        """
        enableSurface2T.setLabel("Enable Surface 2T")
        enableSurface2T.setDefaultValue(False)
        enableSurface2T.setDependencies(self.enableSurfaceFiles,["ENABLE_SURFACE2T"])

    def setHoriStartKeyValues(self,horiStartKey, touchKeyCountMax):
        """Populate the Horizontal start key symbol 
        Arguments:
            :horiStartKey : symbol to be populated
            :touchKeyCountMax : see target_device.getMutualCount()
        Returns:
            none
        """
        horiStartKey.setLabel("Horizontal Start Key")
        horiStartKey.setDefaultValue(0)
        horiStartKey.setMin(0)
        horiStartKey.setMax(touchKeyCountMax)
        horiStartKey.setDescription("Start key of horizontal axis.")

    def setHoriNumKeyValues(self,horiNumKey):
        """Populate the Horizontal number of keys symbol 
        Arguments:
            :horiNumKey : symbol to be populated
        Returns:
            none
        """
        horiNumKey.setLabel("Horizontal Number of Channel")
        horiNumKey.setDefaultValue(2)
        horiNumKey.setMin(0)
        horiNumKey.setMax(255)
        horiNumKey.setDescription("Number of Channels forming horizontal axis.")

    def setVertStartKeyValues(self,vertStartKey, touchKeyCountMax): 
        """Populate the Vertical start key symbol 
        Arguments:
            :horiStartKey : symbol to be populated
            :touchKeyCountMax : see target_device.getMutualCount()
        Returns:
            none
        """
        vertStartKey.setLabel("Vertical Start Key")
        vertStartKey.setDefaultValue(2)
        vertStartKey.setMin(0)
        vertStartKey.setMax(touchKeyCountMax)
        vertStartKey.setDescription("Start key of Vertical axis.")

    def setVertNumKeyValues(self,vertNumKey): 
        """Populate the Vertical number of keys symbol 
        Arguments:
            :horiNumKey : symbol to be populated
        Returns:
            none
        """
        vertNumKey.setLabel("Vertical Number of Channel")
        vertNumKey.setDefaultValue(2)
        vertNumKey.setMin(0)
        vertNumKey.setMax(255)
        vertNumKey.setDescription("Number of Channels forming Vertical axis.")


    def setPositionResolValues(self,positionResol):
        """Populate the Position Resolution symbol 
        Arguments:
            :positionResol : symbol to be populated
        Returns:
            none
        """
        positionResol.setLabel("Position Resolution ")
        positionResol.addKey("RESOL_2_BIT","RESOL_2_BIT","2 Bit")
        positionResol.addKey("RESOL_3_BIT","RESOL_3_BIT","3 Bit")
        positionResol.addKey("RESOL_4_BIT","RESOL_4_BIT","4 Bit")
        positionResol.addKey("RESOL_5_BIT","RESOL_5_BIT","5 Bit")
        positionResol.addKey("RESOL_6_BIT","RESOL_6_BIT","6 Bit")
        positionResol.addKey("RESOL_7_BIT","RESOL_7_BIT","7 Bit")
        positionResol.addKey("RESOL_8_BIT","RESOL_8_BIT","8 Bit")
        positionResol.addKey("RESOL_9_BIT","RESOL_9_BIT","9 Bit")
        positionResol.addKey("RESOL_10_BIT","RESOL_10_BIT","10 Bit")
        positionResol.addKey("RESOL_11_BIT","RESOL_11_BIT","11 Bit")
        positionResol.addKey("RESOL_12_BIT","RESOL_12_BIT","12 Bit")
        positionResol.setDefaultValue(6)
        positionResol.setOutputMode("Value")
        positionResol.setDisplayMode("Key")
        positionResol.setDescription("Full scale position resolution reported for the axis. Options are RESOL_2_BIT - RESOL_12_BIT")

    #Surface Deadband
    def setDeadbandPercentValues(self,deadbandPercent):
        """Populate the deadband percentage symbol 
        Arguments:
            :deadbandPercent : symbol to be populated
        Returns:
            none
        """
        deadbandPercent.setLabel("Deadband Percentage")
        deadbandPercent.addKey("DB_NONE", "DB_NONE", "no deadband")
        deadbandPercent.addKey("DB_1_PERCENT", "DB_1_PERCENT", "1 Percent")
        deadbandPercent.addKey("DB_2_PERCENT", "DB_2_PERCENT", "2 Percent")
        deadbandPercent.addKey("DB_3_PERCENT", "DB_3_PERCENT", "3 Percent")
        deadbandPercent.addKey("DB_4_PERCENT", "DB_4_PERCENT", "4 Percent")
        deadbandPercent.addKey("DB_5_PERCENT", "DB_5_PERCENT", "5 Percent")
        deadbandPercent.addKey("DB_6_PERCENT", "DB_6_PERCENT", "6 Percent")
        deadbandPercent.addKey("DB_7_PERCENT", "DB_7_PERCENT", "7 Percent")
        deadbandPercent.addKey("DB_8_PERCENT", "DB_8_PERCENT", "8 Percent")
        deadbandPercent.addKey("DB_9_PERCENT", "DB_9_PERCENT", "9 Percent")
        deadbandPercent.addKey("DB_10_PERCENT", "DB_10_PERCENT", "10 Percent")
        deadbandPercent.addKey("DB_11_PERCENT", "DB_11_PERCENT", "11 Percent")
        deadbandPercent.addKey("DB_12_PERCENT", "DB_12_PERCENT", "12 Percent")
        deadbandPercent.addKey("DB_13_PERCENT", "DB_13_PERCENT", "13 Percent")
        deadbandPercent.addKey("DB_14_PERCENT", "DB_14_PERCENT", "14 Percent")
        deadbandPercent.addKey("DB_15_PERCENT", "DB_15_PERCENT", "15 Percent")
        deadbandPercent.setDefaultValue(1)
        deadbandPercent.setOutputMode("Value")
        deadbandPercent.setDisplayMode("Key")
        deadbandPercent.setDescription("Size of the edge correction deadbands as a percentage of the full scale range. Options are DB_1_PERCENT - DB_15_PERCENT")

    #median filter
    def setMedianFilterValues(self,medianFilter): 
        """Populate the Median Filter Enable symbol 
        Arguments:
            :medianFilter : symbol to be populated
        Returns:
            none
        """
        medianFilter.setLabel("Median Filter")
        medianFilter.setMin(0)
        medianFilter.setMax(1)
        medianFilter.setDefaultValue(1)
        medianFilter.setDescription("Enable or Disable Median Filter. Enable- 1, Disable - 0")

    #iir filter
    def setIIRFilterValues(self,iirFilter):
        """Populate the iir filter symbol 
        Arguments:
            :iirFilter : symbol to be populated
        Returns:
            none
        """
        iirFilter.setLabel("IIR Filter")
        iirFilter.setMin(0)
        iirFilter.setMax(3)
        iirFilter.setDefaultValue(3)
        iirFilter.setDescription("Configure IIR filter. 0 - None, 1 - 25%, 2 - 50%, 3 - 75%")

    #Position Hysterisis
    def setPositionHysteresisValues(self,posHysterisis):
        """Populate the position hysteresis symbol 
        Arguments:
            :posHysterisis : symbol to be populated
        Returns:
            none
        """
        posHysterisis.setLabel("Surface Position Hysterisis")
        posHysterisis.setDefaultValue(3)
        posHysterisis.setMin(0)
        posHysterisis.setMax(255)
        posHysterisis.setDescription("The minimum travel distance to be reported after contact or direction change. Applicable to Horizontal and Vertical directions")

    #Contact min threshold
    def setContactMinThresholdValues(self,contactMinThreshold):
        """Populate the minimum contact threshold symbol 
        Arguments:
            :contactMinThreshold : symbol to be populated
        Returns:
            none
        """
        contactMinThreshold.setLabel("Surface Detect threshold")
        contactMinThreshold.setDefaultValue(60)
        contactMinThreshold.setMin(0)
        contactMinThreshold.setMax(65535)
        contactMinThreshold.setDescription("The minimum contact size measurement for persistent contact tracking. Contact size is the sum of neighbouring keys' touch deltas forming the touch contact.")

    def enableSurfaceFiles(self,symbol,event):
        """Enables / disables surface source files. For both 1 touch and 2 touch.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component = symbol.getComponent()
        if(component.getSymbolByID("ENABLE_SURFACE1T").getValue() == True):
            component.getSymbolByID("TOUCH_SURFACE1T_LIB").setEnabled(True)
            component.getSymbolByID("TOUCH_SURFACE1T_HEADER").setEnabled(True)
            component.getSymbolByID("TOUCH_SURFACE2T_LIB").setEnabled(False)
            component.getSymbolByID("TOUCH_SURFACE2T_HEADER").setEnabled(False)
        else:
            component.getSymbolByID("TOUCH_SURFACE1T_LIB").setEnabled(False)
            component.getSymbolByID("TOUCH_SURFACE1T_HEADER").setEnabled(False)

        if(component.getSymbolByID("ENABLE_SURFACE2T").getValue() == True):
            component.getSymbolByID("TOUCH_SURFACE2T_LIB").setEnabled(True)
            component.getSymbolByID("TOUCH_SURFACE2T_HEADER").setEnabled(True)
            component.getSymbolByID("TOUCH_SURFACE1T_LIB").setEnabled(False)
            component.getSymbolByID("TOUCH_SURFACE1T_HEADER").setEnabled(False)
        else:
            component.getSymbolByID("TOUCH_SURFACE2T_LIB").setEnabled(False)
            component.getSymbolByID("TOUCH_SURFACE2T_HEADER").setEnabled(False)

    def getSurfaceRearrangeRequired(self,targetDevice):
        """Determines whether surface rearrangement is required( device dependent)
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :True / False
        """

        return self.json_data["features"]["xy_multiplex"]
        
    def updateLumpModeSurface(self,symbol,touchSenseTechnology,totalChannelCount):
        """Handler for lump mode support menu click event.  
        Triggered by qtouch.processLump()
        Arguments:
            :symbol : the symbol that triggered the event
            :touchSenseTechnology : acuisition metho( SelfCap, MutualCap) 
            :totalChannelCount : see target_device.getMutualCount()
        Returns:
            :none
        """
        component = symbol.getComponent()
        surfaceEnabled = component.getSymbolByID("ENABLE_SURFACE").getValue()

        lumpConfigXSym = component.getSymbolByID("FTL_X_INFO")
        lumpConfigYSym = component.getSymbolByID("FTL_Y_INFO")
        xconfig = lumpConfigXSym.getValue().split(",")
        yconfig = lumpConfigYSym.getValue().split(",")

        if (touchSenseTechnology == "MutualCap") and (surfaceEnabled == True):
            MUTL_SURFACE_X = []
            MUTL_SURFACE_Y = []
            HORI_START_KEY = component.getSymbolByID("HORI_START_KEY").getValue()
            HORI_NUM_KEY = component.getSymbolByID("HORI_NUM_KEY").getValue()
            VERT_START_KEY = component.getSymbolByID("VERT_START_KEY").getValue()
            VERT_NUM_KEY = component.getSymbolByID("VERT_NUM_KEY").getValue()

            for i in range(HORI_START_KEY,(HORI_START_KEY+HORI_NUM_KEY)):
                MUTL_SURFACE_X.append(xconfig[int(i)])
            MUTL_SURFACE_X = "|".join(MUTL_SURFACE_X)
            for j in range(VERT_START_KEY,(VERT_START_KEY+VERT_NUM_KEY)):
                MUTL_SURFACE_Y.append(yconfig[int(j)])
            MUTL_SURFACE_Y = "|".join(MUTL_SURFACE_Y)
            for i in range(VERT_START_KEY,(VERT_START_KEY+VERT_NUM_KEY)):
                xconfig[int(i)] = MUTL_SURFACE_X
            for i in range(HORI_START_KEY,(HORI_START_KEY+HORI_NUM_KEY)):
                yconfig[int(i)] = MUTL_SURFACE_Y
            lumpConfigXSym.setValue(",".join(xconfig))
            lumpConfigYSym.setValue(",".join(yconfig))

    def surface_rearrange(self,symbol,event):
        """Handler for rarranging the surface sensor structure
        Triggered by qtouch.ongenerate. 
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        localComponent = symbol.getComponent()
        touchSenseTechnology = localComponent.getSymbolByID("SENSE_TECHNOLOGY").getValue()
        surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
        targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()

        lumpConfigXSym = localComponent.getSymbolByID("FTL_X_INFO")
        lumpConfigYSym = localComponent.getSymbolByID("FTL_Y_INFO")
        xconfig = lumpConfigXSym.getValue().split(",")
        yconfig = lumpConfigYSym.getValue().split(",")

        if self.getSurfaceRearrangeRequired(targetDevice) and (touchSenseTechnology == 1) and (surfaceEnabled == True):
            hor_y_surface = []
            hor_x_surface = []
            ver_y_surface = []
            ver_x_surface = []
            HORI_START_KEY1 = localComponent.getSymbolByID("HORI_START_KEY").getValue()
            HORI_NUM_KEY1 = localComponent.getSymbolByID("HORI_NUM_KEY").getValue()
            VERT_START_KEY1 = localComponent.getSymbolByID("VERT_START_KEY").getValue()
            VERT_NUM_KEY1 = localComponent.getSymbolByID("VERT_NUM_KEY").getValue()

            # swap X and Y for horizontal channels
            for i in range(HORI_START_KEY1,(HORI_START_KEY1+HORI_NUM_KEY1)):
                temp = yconfig[i]
                temp = temp.replace('Y','X')
                hor_x_surface.append(temp)

                temp = xconfig[i]
                temp = temp.replace('X','Y')
                hor_y_surface.append(temp)

            # no swap for vertical channels
            for j in range(VERT_START_KEY1,(VERT_START_KEY1+VERT_NUM_KEY1)):
                ver_x_surface.append(xconfig[j])
                ver_y_surface.append(yconfig[j])

            for i in range(HORI_NUM_KEY1):
                xconfig[i+HORI_START_KEY1] = hor_x_surface[i]
                yconfig[i+HORI_START_KEY1] = hor_y_surface[i]

            for i in range(VERT_NUM_KEY1):
                xconfig[i+VERT_START_KEY1] = ver_x_surface[i]
                yconfig[i+VERT_START_KEY1] = ver_y_surface[i]

            lumpConfigXSym.setValue(",".join(xconfig))
            lumpConfigYSym.setValue(",".join(yconfig))
