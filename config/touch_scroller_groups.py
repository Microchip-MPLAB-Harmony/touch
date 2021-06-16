"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

class classTouchScrollerGroups():
    def __init__(self):
        self.maxGroups = 4

    def getMaxGroups(self):
        """Get maximum acquisition groups
        Arguments:
            :none
        Returns:
            :number of acquistion groups  as (int)
        """
        return int(self.maxGroups)

    def setMaxGroups(self,newMax):
        """Set maximum acquisition groups
        Arguments:
            :newMax - new maximum (int)
        Returns:
            :none
        """
        self.maxGroups = int(newMax)


    def scrollerInstanceInitialise(self,qtouchComponent,groupNumber,parentLabel,selfChannels,mutualChannels):
        """Initialise Scroller Group Instance
        Arguments:
            :qtouchComponent : touchModule
            :groupNumber : index of the group instance
            :parentLabel : parent symbol for added menu items
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
        Returns:
            :none
        """
        if int(groupNumber) == 1:
            touchSCRNum = qtouchComponent.createIntegerSymbol("TOUCH_SCROLLER_ENABLE_CNT", parentLabel)
        else:
            touchSCRNum = qtouchComponent.createIntegerSymbol("TOUCH_SCROLLER_ENABLE_CNT_"+str(groupNumber), parentLabel)
        self.setScrollerEnableCountValues(touchSCRNum,mutualChannels)

        for channelID in range(0, mutualChannels):
            if int(groupNumber) == 1:
                touchScrollerEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_SCROLLER_" + str(channelID), parentLabel)
                touchScrollerEnable.setLabel("Use scroller " + str(channelID))
                touchScrollerEnable.setDefaultValue(False)
                touchScrollerType = qtouchComponent.createKeyValueSetSymbol("DEF_SCR_TYPE" + str(channelID), touchScrollerEnable)
                touchScrollerNum = qtouchComponent.createIntegerSymbol("TOUCH_SCR_SIZE" + str(channelID), touchScrollerEnable)
                touchScrollerNumChannels = qtouchComponent.createIntegerSymbol("TOUCH_SCR_START_KEY"+ str(channelID), touchScrollerEnable)
                touchScrollerResolution = qtouchComponent.createKeyValueSetSymbol("DEF_SCR_RESOLUTION" + str(channelID), touchScrollerEnable)
                touchScrollerDeadband = qtouchComponent.createKeyValueSetSymbol("DEF_SCR_DEADBAND" + str(channelID), touchScrollerEnable)
                touchScrollerPosHysteresis = qtouchComponent.createIntegerSymbol("DEF_SCR_POS_HYS" + str(channelID), touchScrollerEnable)
                touchScrollerContactThreshold = qtouchComponent.createIntegerSymbol("DEF_SCR_CONTACT_THRESHOLD" + str(channelID), touchScrollerEnable)
            else:
                dynamicScrollerEnable = "touchScrollerEnable_" +str(groupNumber) 
                vars()[dynamicScrollerEnable] = qtouchComponent.createBooleanSymbol("GROUP_"+str(groupNumber)+"_TOUCH_ENABLE_SCROLLER_" + str(channelID), parentLabel)
                vars()[dynamicScrollerEnable].setLabel("Use scroller " + str(channelID))
                vars()[dynamicScrollerEnable].setDefaultValue(False)
                touchScrollerType = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_SCR_TYPE" + str(channelID), vars()[dynamicScrollerEnable])
                touchScrollerNum = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"_TOUCH_SCR_SIZE" + str(channelID), vars()[dynamicScrollerEnable])
                touchScrollerNumChannels = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"_TOUCH_SCR_START_KEY"+ str(channelID), vars()[dynamicScrollerEnable])
                touchScrollerResolution = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_SCR_RESOLUTION" + str(channelID), vars()[dynamicScrollerEnable])
                touchScrollerDeadband = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_SCR_DEADBAND" + str(channelID), vars()[dynamicScrollerEnable])
                touchScrollerPosHysteresis = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"_DEF_SCR_POS_HYS" + str(channelID), vars()[dynamicScrollerEnable])
                touchScrollerContactThreshold = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"_DEF_SCR_CONTACT_THRESHOLD" + str(channelID), vars()[dynamicScrollerEnable])

            self.setScrollerTypeValues(touchScrollerType)
            self.setNumSegmentValues(touchScrollerNum,mutualChannels)
            self.setNumChannelsValues(touchScrollerNumChannels,mutualChannels)
            self.setResolutionValues(touchScrollerResolution)
            self.setDeadBandValues(touchScrollerDeadband)
            self.setPositionHysteresisValues(touchScrollerPosHysteresis)
            self.setContactThresholdValues(touchScrollerContactThreshold)


    def initScrollerGroup(self, qtouchComponent, touchMenu, minVal, maxVal, selfChannels, mutualChannels):
        """Initialise Scroller Groups and add to touch Module
        Arguments:
            :qtouchComponent : touchModule
            :parentMenu : parent menu symbol for added menu items
            :minVal : see acquisitionGroupCountMenu.getMin()
            :maxVal : see acquisitionGroupCountMenu.getMax()
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
        Returns:
            :none
        """
        enableScrollerMenu = qtouchComponent.createBooleanSymbol("ENABLE_SCROLLER", touchMenu)
        enableScrollerMenu.setLabel("Enable Scroller")
        enableScrollerMenu.setDefaultValue(False)
        enableScrollerMenu.setVisible(True)

        for i in range (minVal,maxVal+1):
            if i == 1:
                scrollerMenu = qtouchComponent.createMenuSymbol("SCROLLER_MENU", enableScrollerMenu)
                scrollerMenu.setLabel("Scroller Configuration")
                scrollerMenu.setDescription("Configure Scrollers")
                scrollerMenu.setVisible(True)
                scrollerMenu.setEnabled(True)
                self.scrollerInstanceInitialise(qtouchComponent,i,scrollerMenu,selfChannels,mutualChannels)
            else:
                dynamicName = "scrollerMenu_" +str(i) 
                dynamicId = "SCROLLER_MENU_" +str(i) 
                vars()[dynamicName] =  qtouchComponent.createMenuSymbol(dynamicId, enableScrollerMenu)
                vars()[dynamicName].setLabel("Scroller Configuration Group"+str(i))
                vars()[dynamicName].setVisible(True)
                vars()[dynamicName].setEnabled(True)
                self.scrollerInstanceInitialise(qtouchComponent,i,vars()[dynamicName],selfChannels,mutualChannels)
        
        enableScrollerMenu.setDependencies(self.scrollerUpdateEnabled,["ENABLE_SCROLLER"])
        enableScrollerMenu.setValue(False)

    def updateScrollerGroups(self,symbol,event):
        """Handler for number of Scroller groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component= symbol.getComponent()
        currentVal = int(event['symbol'].getValue())
        maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMax()
        minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()
        for x in range(minVal+1,maxVal+1):
            grpId = "SCROLLER_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(False)
            component.getSymbolByID(grpId).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(grpId).setEnabled(True)
                component.getSymbolByID(grpId).setVisible(True)

    def scrollerUpdateEnabled(self,symbol,event):
        """Enables Scroller functionality.
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """
        component= symbol.getComponent()
        scrollerEnabled = event["value"]

        scrollerLibraryFile = component.getSymbolByID("TOUCH_SCR_LIB")
        scrollerHeaderFile = component.getSymbolByID("TOUCH_SCR_HEADER")
        scrollerLibraryFile.setEnabled(scrollerEnabled)
        scrollerHeaderFile.setEnabled(scrollerEnabled)

        maxVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getValue()
        minVal = component.getSymbolByID("NUM_ACQUISITION_GROUPS").getMin()
        for x in range(minVal,maxVal+1):
            if(x == minVal):
                grpId = "SCROLLER_MENU"
            else:
                grpId = "SCROLLER_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(scrollerEnabled)
            component.getSymbolByID(grpId).setVisible(scrollerEnabled)

    def setScrollerEnableCountValues(self,touchSCRNum,mutualChannels):
        """Populate the scroller type symbol 
        Arguments:
            :touchSCRNum : symbol to be populated
            :mutualChannels : see target_device.getMutualCount()
        Returns:
            none
        """
        touchSCRNum.setLabel("Number of slider/wheel to enable")
        touchSCRNum.setDefaultValue(0)
        touchSCRNum.setMin(0)
        touchSCRNum.setMax(mutualChannels)


    def setScrollerTypeValues(self,touchScrollerType):
        """Populate the scroller type symbol 
        Arguments:
            :touchScrollerType : symbol to be populated
        Returns:
            none
        """
        touchScrollerType.setLabel("Choose the scroller type")
        touchScrollerType.addKey("SCROLLER_TYPE_SLIDER","SCROLLER_TYPE_SLIDER","Slider")
        touchScrollerType.addKey("SCROLLER_TYPE_WHEEL","SCROLLER_TYPE_WHEEL","Wheel")
        touchScrollerType.setDefaultValue(0)
        touchScrollerType.setOutputMode("Value")
        touchScrollerType.setDisplayMode("Description")

    def setNumSegmentValues(self,touchScrollerNum,mutualChannels):
        """Populate the scroller number of segments symbol 
        Arguments:
            :touchScrollerNum : symbol to be populated
            :mutualChannels : see target_device.getMutualCount()
        Returns:
            none
        """
        touchScrollerNum.setLabel("Number of buttons or segments that constitute a slider/wheel")
        touchScrollerNum.setDefaultValue(3)
        touchScrollerNum.setMin(2)
        touchScrollerNum.setMax(mutualChannels)
        touchScrollerNum.setDescription("The slider/wheel is made up of multiple buttons. This parameter defines how may buttons or segments constitute a slider/wheel.")

    def setNumChannelsValues(self,touchScrollerNumChannels,mutualChannels):
        """Populate the scroller number of segments symbol 
        Arguments:
            :touchScrollerNumChannels : symbol to be populated
            :mutualChannels : see target_device.getMutualCount()
        Returns:
            none
        """
        touchScrollerNumChannels.setLabel("Starting key number of this scroller")
        touchScrollerNumChannels.setDefaultValue(0)
        touchScrollerNumChannels.setMin(0)
        touchScrollerNumChannels.setMax(mutualChannels)
        touchScrollerNumChannels.setDescription("A scroller is made of multiple buttons. This parameter defines the starting button number of this scroller.")

    def setResolutionValues(self,touchScrollerResolution):
        """Populate the scroller Resolution symbol 
        Arguments:
            :touchScrollerResolution : symbol to be populated
        Returns:
            none
        """
        touchScrollerResolution.setLabel("Scroller Resolution")
        touchScrollerResolution.addKey("SCR_RESOL_2_BIT","SCR_RESOL_2_BIT","2 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_3_BIT","SCR_RESOL_3_BIT","3 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_4_BIT","SCR_RESOL_4_BIT","4 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_5_BIT","SCR_RESOL_5_BIT","5 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_6_BIT","SCR_RESOL_6_BIT","6 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_7_BIT","SCR_RESOL_7_BIT","7 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_8_BIT","SCR_RESOL_8_BIT","8 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_9_BIT","SCR_RESOL_9_BIT","9 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_10_BIT","SCR_RESOL_10_BIT","10 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_11_BIT","SCR_RESOL_11_BIT","11 Bit")
        touchScrollerResolution.addKey("SCR_RESOL_12_BIT","SCR_RESOL_12_BIT","12 Bit")
        touchScrollerResolution.setDefaultValue(6)
        touchScrollerResolution.setOutputMode("Value")
        touchScrollerResolution.setDisplayMode("Description")
        touchScrollerResolution.setDescription("Defines the resolution of slider/wheel in bits. A value of 8 indicates 256 positions. The slider/wheel value will be reported from 0 to 255.")

    def setDeadBandValues(self,touchScrollerDeadband):
        """Populate the scroller Deadband symbol 
        Arguments:
            :touchScrollerDeadband : symbol to be populated
        Returns:
            none
        """
        touchScrollerDeadband.setLabel("Scroller Deadband")
        touchScrollerDeadband.addKey("SCR_DB_NONE", "DB_NONE", "no deadband")
        touchScrollerDeadband.addKey("SCR_DB_1_PERCENT", "SCR_DB_1_PERCENT", "1 Percent")
        touchScrollerDeadband.addKey("SCR_DB_2_PERCENT", "SCR_DB_2_PERCENT", "2 Percent")
        touchScrollerDeadband.addKey("SCR_DB_3_PERCENT", "SCR_DB_3_PERCENT", "3 Percent")
        touchScrollerDeadband.addKey("SCR_DB_4_PERCENT", "SCR_DB_4_PERCENT", "4 Percent")
        touchScrollerDeadband.addKey("SCR_DB_5_PERCENT", "SCR_DB_5_PERCENT", "5 Percent")
        touchScrollerDeadband.addKey("SCR_DB_6_PERCENT", "SCR_DB_6_PERCENT", "6 Percent")
        touchScrollerDeadband.addKey("SCR_DB_7_PERCENT", "SCR_DB_7_PERCENT", "7 Percent")
        touchScrollerDeadband.addKey("SCR_DB_8_PERCENT", "SCR_DB_8_PERCENT", "8 Percent")
        touchScrollerDeadband.addKey("SCR_DB_9_PERCENT", "SCR_DB_9_PERCENT", "9 Percent")
        touchScrollerDeadband.addKey("SCR_DB_10_PERCENT", "SCR_DB_10_PERCENT", "10 Percent")
        touchScrollerDeadband.addKey("SCR_DB_11_PERCENT", "SCR_DB_11_PERCENT", "11 Percent")
        touchScrollerDeadband.addKey("SCR_DB_12_PERCENT", "SCR_DB_12_PERCENT", "12 Percent")
        touchScrollerDeadband.addKey("SCR_DB_13_PERCENT", "SCR_DB_13_PERCENT", "13 Percent")
        touchScrollerDeadband.addKey("SCR_DB_14_PERCENT", "SCR_DB_14_PERCENT", "14 Percent")
        touchScrollerDeadband.addKey("SCR_DB_15_PERCENT", "SCR_DB_15_PERCENT", "15 Percent")
        touchScrollerDeadband.setDefaultValue(10)
        touchScrollerDeadband.setOutputMode("Value")
        touchScrollerDeadband.setDisplayMode("Description")
        touchScrollerDeadband.setDescription("Defines the inactive area on both ends of the slider/wheel where no change in position is reported. If deadband is 10percent,  then inactive area is 10% of slider/wheel length on each end.")


    def setPositionHysteresisValues(self,touchScrollerPosHysteresis):
        """Populate the scroller position Hysteresis symbol 
        Arguments:
            :touchScrollerPosHysteresis : symbol to be populated
        Returns:
            none
        """
        touchScrollerPosHysteresis.setLabel("Scroller Position Hysterisis")
        touchScrollerPosHysteresis.setDefaultValue(8)
        touchScrollerPosHysteresis.setMin(0)
        touchScrollerPosHysteresis.setMax(255)
        touchScrollerPosHysteresis.setDescription("Hysteresis is the number of positions the user has to move back, before the new touch position is reported when the direction of scrolling is changed and during first scroll after touch down.")


    def setContactThresholdValues(self,touchScrollerContactThreshold):
        """Populate the scroller Contact Threshold symbol 
        Arguments:
            :touchScrollerContactThreshold : symbol to be populated
        Returns:
            none
        """
        touchScrollerContactThreshold.setLabel("Scroller Detect threshold")
        touchScrollerContactThreshold.setDefaultValue(20)
        touchScrollerContactThreshold.setMin(0)
        touchScrollerContactThreshold.setMax(65535)
        touchScrollerContactThreshold.setDescription("Defines the threshold for slider/wheel touch delta to detect a user touch. It is recommended to configure the slider/wheel detect threshold to around 50% of minimum slider/wheel touch delta reported when sliding from end to end.")