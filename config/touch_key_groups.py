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

class classTouchKeyGroups():
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

    def initKeysGroupInstance(self,qtouchComponent,groupNumber,parentLabel,selfChannels,mutualChannels):
        """Initialise Key Groups Instance
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
            touchKeyNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_KEY_ENABLE_CNT", parentLabel)
        else:
            touchKeyNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_KEY_ENABLE_CNT_"+str(groupNumber), parentLabel)
        
        if touchKeyNumChannel != 0:
            touchKeyNumChannel.setLabel("Number of keys to enable")
            touchKeyNumChannel.setDefaultValue(0)
            touchKeyNumChannel.setMin(0)
            touchKeyNumChannel.setMax(mutualChannels)

            for channelID in range(0, mutualChannels):
                if int(groupNumber) == 1:
                    touchKeyEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_KEY_" + str(channelID), parentLabel)
                    touchKeyEnable.setLabel("Use touch channel " + str(channelID))
                    touchKeyEnable.setDefaultValue(False)
                    #Sensor Detect Threshold
                    touchKeyDetectThreshold = qtouchComponent.createIntegerSymbol("DEF_SENSOR_DET_THRESHOLD" + str(channelID), touchKeyEnable)
                    #Sensor Hysteresis
                    touchKeyHysteresis = qtouchComponent.createKeyValueSetSymbol("DEF_SENSOR_HYST" + str(channelID), touchKeyEnable)
                    #Sensor AKS Setting
                    touchKeyAKS = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_AKS" + str(channelID), touchKeyEnable)
                else:
                    dynamicTouchKeyEnable = "touchKeyEnable_" +str(groupNumber) 
                    vars()[dynamicTouchKeyEnable] = qtouchComponent.createBooleanSymbol("GROUP_"+str(groupNumber)+"_TOUCH_ENABLE_KEY_" + str(channelID), parentLabel)
                    vars()[dynamicTouchKeyEnable].setLabel("Use touch channel " + str(channelID))
                    #Sensor Detect Threshold
                    touchKeyDetectThreshold = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"_DEF_SENSOR_DET_THRESHOLD" + str(channelID), vars()[dynamicTouchKeyEnable])
                    #Sensor Hysteresis
                    touchKeyHysteresis = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_SENSOR_HYST" + str(channelID), vars()[dynamicTouchKeyEnable])
                    #Sensor AKS Setting
                    touchKeyAKS = qtouchComponent.createKeyValueSetSymbol("GROUP_"+str(groupNumber)+"_DEF_NOD_AKS" + str(channelID), vars()[dynamicTouchKeyEnable])
                
                #parameter assignment
                self.setThresholdValues(touchKeyDetectThreshold)
                self.setHysteresisValues(touchKeyHysteresis)
                self.setAKSValues(touchKeyAKS)

    #group
    def initKeyGroup(self,qtouchComponent, touchMenu, minVal,maxVal,selfChannels,mutualChannels):
        """Initialise Key Groups and add to touch Module
        Arguments:
            :qtouchComponent : touchModule
            :touchMenu : parent menu symbol for added menu items
            :minVal : see acquisitionGroupCountMenu.getMin()
            :maxVal : see acquisitionGroupCountMenu.getMax()
            :selfChannels : see target_device.getSelfCount()
            :mutualChannels : see target_device.getMutualCount()
        Returns:
            :none
        """
        self.maxGroups = maxVal

        for groupNum in range (minVal,maxVal+1):
            if groupNum ==1:
                keyMenu = qtouchComponent.createMenuSymbol("KEY_MENU", touchMenu)
                keyMenu.setLabel("Key Configuration")
                keyMenu.setDescription("Configure Keys")
                keyMenu.setVisible(True)
                keyMenu.setEnabled(True)
                self.initKeysGroupInstance(qtouchComponent,groupNum,keyMenu,selfChannels,mutualChannels)
            else:
                dynamicName = "keyMenu_" +str(groupNum) 
                dynamicId = "KEY_MENU_" +str(groupNum) 
                vars()[dynamicName] =  qtouchComponent.createMenuSymbol(dynamicId, touchMenu)
                vars()[dynamicName].setLabel("keys Configuration Group"+str(groupNum))
                vars()[dynamicName].setVisible(False)
                vars()[dynamicName].setEnabled(False)
                self.initKeysGroupInstance(qtouchComponent,groupNum,vars()[dynamicName],selfChannels,mutualChannels)

    #updater
    def updateKeyGroups(self,symbol,event):
        """Handler for number of Node groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
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
            grpId = "KEY_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(False)
            component.getSymbolByID(grpId).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(grpId).setEnabled(True)
                component.getSymbolByID(grpId).setVisible(True)

    #parameter assignment
    def setThresholdValues(self,touchKeyDetectThreshold):
        """Populate the key detect threshold symbol
        Arguments:
            :touchKeyDetectThreshold : symbol to be populated
        Returns:
            none
        """
        touchKeyDetectThreshold.setLabel("Sensor Detect Threshold")
        touchKeyDetectThreshold.setDefaultValue(20)
        touchKeyDetectThreshold.setMin(0)
        touchKeyDetectThreshold.setMax(255)
        touchKeyDetectThreshold.setDescription("Configure the sensor's detect threshold. When finger touches sensor, the touch delta increases.Sensor will be reported as touched only if the sensor's touch delta value is more than Sensor Threshold.It is recommended to configure Sensor Threshold as 50~70% of touch delta. User can start with default value and can configure after monitoring touch delta value.")

    def setHysteresisValues(self,touchKeyHysteresis):
        """Populate the key hysteresis symbol
        Arguments:
            :touchKeyHysteresis : symbol to be populated
        Returns:
            none
        """
        touchKeyHysteresis.setLabel("Sensor Hysteresis")
        touchKeyHysteresis.addKey("HYST50", "HYST_50", "50 %")
        touchKeyHysteresis.addKey("HYST25", "HYST_25", "25 %")
        touchKeyHysteresis.addKey("HYST125", "HYST_12_5", "12.5 %")
        touchKeyHysteresis.addKey("HYST625", "HYST_6_25", "6.25 %")
        touchKeyHysteresis.setDefaultValue(1)
        touchKeyHysteresis.setOutputMode("Value")
        touchKeyHysteresis.setDisplayMode("Description")
        touchKeyHysteresis.setDescription("Under noisy conditions, the delta value goes up/down over the sensor threshold.During these conditions, the sensor dither in and out of touch.To avoid this, once a sensor goes into detect state, the threshold for the sensor is reduced (by the hysteresis value).Hysteresis values are derived from Sensor Threshold value.")

    def setAKSValues(self,touchKeyAKS):
        """Populate the key AKS symbol
        Arguments:
            :touchKeyAKS : symbol to be populated
        Returns:
            none
        """
        touchKeyAKS.setLabel("Sensor AKS")
        touchKeyAKS.addKey("AKS0", "NO_AKS_GROUP", "No AKS")
        touchKeyAKS.addKey("AKS1", "AKS_GROUP_1", "AKS Group 1")
        touchKeyAKS.addKey("AKS2", "AKS_GROUP_2", "AKS Group 2")
        touchKeyAKS.addKey("AKS3", "AKS_GROUP_3", "AKS Group 3")
        touchKeyAKS.addKey("AKS4", "AKS_GROUP_4", "AKS Group 4")
        touchKeyAKS.addKey("AKS5", "AKS_GROUP_5", "AKS Group 5")
        touchKeyAKS.addKey("AKS6", "AKS_GROUP_6", "AKS Group 6")
        touchKeyAKS.addKey("AKS7", "AKS_GROUP_7", "AKS Group 7")
        touchKeyAKS.setDefaultValue(0)
        touchKeyAKS.setOutputMode("Value")
        touchKeyAKS.setDisplayMode("Description")
        touchKeyAKS.setDescription("Configures the Adjacent Keys Suppression (AKS).AKS can be used when touching multiple sensors are not allowed in a system or When sensors are physically closer to each other. When sensors are closer to each other, there is a possibility that touching one sensor causes rise in touch delta value on other adjacent sensors. At times the delta raise in other sensors may cross threshold and could report false detection.When such sensors are configured in same AKS group, only the first sensor (which goes in to detect) will be reported as touched.All other sensor's state will be suppressed even if their delta crosses Sensor Threshold.Default: AKS is not used.")
