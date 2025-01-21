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
class classTouchAcquisitionGroups():
    def __init__(self):
        self.tchSelfPinSelection = []
        self.tchMutXPinSelection = []
        self.tchMutYPinSelection = []
        # defaultValue
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


    def initAcquisitionGroup(self,qtouchComponent, parentMenu, minVal,maxVal,selfChannels,mutualChannels,targetDevice,csdMode,shieldMode):
        """Initialise Acquisition Groups and add to touch Module
        Arguments:
            :qtouchComponent : touchModule
            :parentMenu : parent menu symbol for added menu items
            :minVal : see acquisitionGroupCountMenu.getMin()
            :maxVal : see acquisitionGroupCountMenu.getMax()
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
            :targetDevice : see interface.getDeviceSeries()
            :csdmode : see target_device.getCSDMode(targetDevice)
            :shieldMode : see target_device.getShieldMode(targetDevice)
        Returns:
            :none
        """
        self.maxGroups = maxVal

        for i in range (minVal,maxVal+1):
            if i ==1:
                acquisitionMenu = qtouchComponent.createMenuSymbol("ACQUISITION_MENU", parentMenu)
                acquisitionMenu.setLabel("Acquisition Configuration")
                acquisitionMenu.setVisible(True)
                acquisitionMenu.setEnabled(True)
                self.initacquisitionInstance(qtouchComponent,i,acquisitionMenu,selfChannels,mutualChannels,targetDevice,csdMode,shieldMode)
            else:
                dynamicName = "acquisitionMenu_" +str(i) 
                dynamicId = "ACQUISITION_MENU_" +str(i) 
                vars()[dynamicName] =  qtouchComponent.createMenuSymbol(dynamicId, parentMenu)
                vars()[dynamicName].setLabel("Acquisition Configuration Group"+str(i))
                vars()[dynamicName].setVisible(False)
                vars()[dynamicName].setEnabled(False)
                self.initacquisitionInstance(qtouchComponent,i,vars()[dynamicName],selfChannels,mutualChannels,targetDevice,csdMode,shieldMode)

    #instance
    def initacquisitionInstance(self,qtouchComponent,groupNumber,parentMenu,selfChannels,mutualChannels,targetDevice,csdMode,shieldMode):
        """Initialise Acquisition Instance
        Arguments:
            :qtouchComponent : touchModule
            :groupNumber : index of the group instance
            :parentMenu : parent menu symbol for added menu items
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
            :targetDevice : see interface.getDeviceSeries()
            :csdmode : see target_device.getCSDMode(targetDevice)
            :shieldMode : see target_device.getShieldMode(targetDevice)
        Returns:
            :none
        """
        global touchSenseTechnology
        if int(groupNumber) == 1:
            touchSenseTechnology = qtouchComponent.createKeyValueSetSymbol("SENSE_TECHNOLOGY", parentMenu)
            totalChannelCountSelf = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_SELF",parentMenu)
            totalChannelCountMutl = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_MUTL",parentMenu)
            touchAutoTuneMode = qtouchComponent.createKeyValueSetSymbol("TUNE_MODE_SELECTED", parentMenu)
            touchScanRate = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MEASUREMENT_PERIOD_MS", parentMenu)
            touchAcquisitonFrequency = qtouchComponent.createKeyValueSetSymbol("DEF_SEL_FREQ_INIT", parentMenu)
            if (targetDevice in ["PIC32CZCA80", "PIC32CZCA90","PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01","PIC32CMGC00","PIC32CMSG00"]):
                ptcWakeupTime = qtouchComponent.createIntegerSymbol("DEF_PTC_WAKEUP_EXP", parentMenu)
        else:
            touchSenseTechnology = qtouchComponent.createKeyValueSetSymbol("SENSE_TECHNOLOGY_"+str(groupNumber), parentMenu)
            totalChannelCountSelf = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_SELF_"+str(groupNumber),parentMenu)
            totalChannelCountMutl = qtouchComponent.createIntegerSymbol("MAX_CHANNEL_COUNT_MUTL_"+str(groupNumber),parentMenu)
            touchAutoTuneMode = qtouchComponent.createKeyValueSetSymbol("TUNE_MODE_SELECTED_"+str(groupNumber),parentMenu)
            touchScanRate = qtouchComponent.createIntegerSymbol("DEF_TOUCH_MEASUREMENT_PERIOD_MS_"+str(groupNumber),parentMenu)
            touchAcquisitonFrequency = qtouchComponent.createKeyValueSetSymbol("DEF_SEL_FREQ_INIT_"+str(groupNumber),parentMenu)

        #parameter assignment    
        #touchSenseTechnology
        if(shieldMode != "none"):
            self.setTouchTechnologyDrivenShieldValues(touchSenseTechnology)
        else:
            self.setTouchTechnologyValues(touchSenseTechnology)
        #totalChannelCountSelf
        totalChannelCountSelf.setVisible(True)
        totalChannelCountSelf.setDefaultValue(int(selfChannels))
        totalChannelCountSelf.setLabel("Self-Capacitance Channels")
        #totalChannelCountMutl
        totalChannelCountMutl.setVisible(True)
        totalChannelCountMutl.setDefaultValue(int(mutualChannels))
        totalChannelCountMutl.setLabel("Mutual Capacitance Channels")
        # Select Tuning mode
        self.setAutoTuneModeValues(touchAutoTuneMode,csdMode, targetDevice)
        #Scan Rate (ms)    
        self.setScanRateValues(touchScanRate)    
        #Acquisition Frequency
        self.setAcquisitionFrequencyValues(touchAcquisitonFrequency)
        if (targetDevice in ["PIC32CZCA80", "PIC32CZCA90","PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01","PIC32CMGC00","PIC32CMSG00"]):
            #PTC Wake up component   
            self.setPtcWakeupTime(ptcWakeupTime) 

    #updater
    def updateAcquisitionGroups(self,symbol,event):
        """Handler for number of acquistion groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
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
            grpId = "ACQUISITION_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(False)
            component.getSymbolByID(grpId).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(grpId).setEnabled(True)
                component.getSymbolByID(grpId).setVisible(True)

    #parameter assignment
    def setTouchTechnologyValues(self,touchSenseTechnology):
        """Populate the touchSenseTechnology symbol -  NON DrivenShield
        Arguments:
            :touchSenseTechnology: symbol to be updated
        Returns:
            :none
        """
        touchSenseTechnology.setLabel("Sensor Technology")
        touchSenseTechnology.addKey("SelfCap", "NODE_SELFCAP", "Self Capacitance Sensing")
        touchSenseTechnology.addKey("MutualCap", "NODE_MUTUAL", "Mutual Capacitance Sensing")
        touchSenseTechnology.setDefaultValue(0)
        touchSenseTechnology.setOutputMode("Value")
        touchSenseTechnology.setDisplayMode("Description")
        touchSenseTechnology.setDescription("Selects the sensor technology - Selfcap: Requires one pin per channel; Simple sensor design; Recommended for small number of sensors (less than 12). Mutualcap: Requires one X pin and one Y pin per channel; Can realize X x Y number of sensors in a matrix form; Recommended for large number of sensors (more than 12)")

    def setTouchTechnologyDrivenShieldValues(self,touchSenseTechnology):
        """Populate the touchSenseTechnology symbol for DrivenShield
        Arguments:
            :param :touchSenseTechnology :symbol to be changed
            :csdMode : see target_device.getCSDMode(targetDevice)
        Returns:
            :none
        """
        touchSenseTechnology.setLabel("Sensor Technology")
        touchSenseTechnology.addKey("SelfCap", "NODE_SELFCAP", "Self Capacitance Sensing")
        touchSenseTechnology.addKey("MutualCap", "NODE_MUTUAL", "Mutual Capacitance Sensing")
        touchSenseTechnology.addKey("SelfCapShield", "NODE_SELFCAP_SHIELD", "Self-Capacitance Sensing With Driven Shield")
        touchSenseTechnology.setDefaultValue(0)
        touchSenseTechnology.setOutputMode("Value")
        touchSenseTechnology.setDisplayMode("Description")
        touchSenseTechnology.setDescription("Selects the sensor technology - Selfcap: Requires one pin per channel; Simple sensor design; Recommended for small number of sensors (less than 12). SelfCapShield: Requires one pin per channel with Driven shield options; Simple sensor design; Recommended for small number of sensors (less than 12). Mutualcap: Requires one X pin and one Y pin per channel; Can realize X x Y number of sensors in a matrix form; Recommended for large number of sensors (more than 12)")

    def setAutoTuneModeValues(self,touchAutoTuneMode,csdMode, targetDevice):
        """Populate touchAutoTuneMode symbol
        Arguments:
            :touchAutoTuneMode :symbol to be changed
            :csdMode : see target_device.getCSDMode(targetDevice)
        Returns:
            :none
        """
        touchAutoTuneMode.setLabel("Select the Required Tuning Mode")
        touchAutoTuneMode.addKey("Manual Tuning","CAL_AUTO_TUNE_NONE","Manual tuning is done based on the values defined by user")
        if (targetDevice not in ["PIC32CZCA80", "PIC32CZCA90","PIC32CMGC00","PIC32CMSG00","PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01"]):
            if(csdMode != "NoCSD"):
                touchAutoTuneMode.addKey("Tune CSD","CAL_AUTO_TUNE_CSD","Charge Share Delay - CSD is tuned")
            else:
                touchAutoTuneMode.addKey("Tune Prescaler value","CAL_AUTO_TUNE_PRSC","Clock Prescaler is tuned")
        touchAutoTuneMode.setDefaultValue(0)
        touchAutoTuneMode.setOutputMode("Value")
        touchAutoTuneMode.setDisplayMode("Key")
        touchAutoTuneMode.setDescription("Sets the sensor calibration mode - CAL_AUTO_TUNE_NONE: Manual user setting of Prescaler, Charge share delay & Series resistor. AUTO_TUNE_CSD: QTouch library will use the configured prescaler and series resistor value and adjusts the CSD to ensure full charging.")

    def setScanRateValues(self,touchScanRate):
        """ Populate the touchScanRate symbol
        Arguments:
            :touchScanRate : symbol to be changed
        Returns:
            :none
        """
        touchScanRate.setLabel("Scan Rate (ms)")
        touchScanRate.setDefaultValue(20)
        touchScanRate.setMin(1)
        touchScanRate.setMax(255)
        touchScanRate.setDescription("Defines the timer scan rate in milliseconds to initiate periodic touch measurement on all enabled touch sensors.")

    def setPtcWakeupTime(self,ptcWakeupTime):
        """ Populate the ptcWakeupTime symbol
        Arguments:
            :ptcWakeupTime : symbol to te changed
        Returns:
            :none
        """
        ptcWakeupTime.setLabel("PTC Wake up Time Exponent")
        ptcWakeupTime.setDefaultValue(4)
        ptcWakeupTime.setMin(4)
        ptcWakeupTime.setMax(15)
        ptcWakeupTime.setDescription("The wake-up exponent is passed from the application to the library. The initial value of wakeup exponent that is passed from application is determined on the minimum prescaler and this is further updated automatically inside the library based on changes in Node prescaler values.")

    def setAcquisitionFrequencyValues(self,touchAcquisitonFrequency):
        """Populate the touchAcquisitonFrequency symbol
        Arguments:
            :touchAcquisitonFrequency
        Returns:
            :none
        """
        touchAcquisitonFrequency.setLabel("Acquisition Frequency")
        touchAcquisitonFrequency.addKey("FREQ_0", "FREQ_SEL_0", "No additional clock cycles (Fastest measurement time) ")
        touchAcquisitonFrequency.addKey("FREQ_1", "FREQ_SEL_1", "1 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_2", "FREQ_SEL_2", "2 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_3", "FREQ_SEL_3", "3 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_4", "FREQ_SEL_4", "4 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_5", "FREQ_SEL_5", "5 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_6", "FREQ_SEL_6", "6 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_7", "FREQ_SEL_7", "7 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_8", "FREQ_SEL_8", "8 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_9", "FREQ_SEL_9", "9 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_10", "FREQ_SEL_10", "10 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_11", "FREQ_SEL_11", "11 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_12", "FREQ_SEL_12", "12 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_13", "FREQ_SEL_13", "13 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_14", "FREQ_SEL_14", "14 additional clock cycles ")
        touchAcquisitonFrequency.addKey("FREQ_15", "FREQ_SEL_15", "15 additional clock cycles (Slowest measurement time")
        touchAcquisitonFrequency.addKey("FREQ_16", "FREQ_SEL_SPREAD", "16 different frequencies used")
        touchAcquisitonFrequency.setDefaultValue(0)
        touchAcquisitonFrequency.setOutputMode("Value")
        touchAcquisitonFrequency.setDisplayMode("Value")
        touchAcquisitonFrequency.setDescription(
            "It may be required to change the acquisition frequency if system noise frequency"+
            " is closer to acquisition frequency.In order to vary the acquisition frequency, additional clock cycles"+
            " are added during measurement for FREQ_SEL_0 through FREQ_SEL_15. FREQ_SEL_0 provides the fastest"+
            " measurement time (no additional clock cycles are added) and FREQ_SEL_15 provides the slowest measurement time"+
            " (15 additional clock cycles are added). When FREQ_SEL_SPREAD option is used, all the 16 frequencies are used consecutively in a circular fashion.")