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
import touch_boost_mode_sourcefiles
from json_loader import json_loader_instance

class classTouchBoostModeGroups():
    def __init__(self):
        self.maxGroups = 4 # defaultValue
        # self.boost_mode_support = set(["SAML10","SAML1xE","SAML11","PIC32CMLE00","PIC32CMLS00","PIC32CZCA80","PIC32CZCA90","PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01"])
        # self.boost_mode_remove_support_temporarily = set(["PIC32CZCA80","PIC32CZCA90"])
        self.bostModeSourceInstance = touch_boost_mode_sourcefiles.classTouchBoostModeFiles()
        self.json_data=json_loader_instance.get_data()

    def getDepDetails(self):
        return self.bostModeSourceInstance.getDepDetails()

    def initBoostModeGroup(self,configName, qtouchComponent, parentMenu, minVal, maxVal, targetDevice,useTrustZone):
        """
        Creates boost mode menu and variables
        Arguments :
            :configName : see Variables.get("__CONFIGURATION_NAME") ref: https://confluence.microchip.com/display/MH/MHC+Python+Interface
            :qtouchComponent : touchModule
            :parentMenu : parent symbol for added menu items
            :minVal : see acquisitionGroupCountMenu.getMin()
            :maxVal : see acquisitionGroupCountMenu.getMax()
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            none
        """
        for groupNum in range (minVal,maxVal+1):
            if groupNum ==1:
                boostMenu = qtouchComponent.createMenuSymbol("Boost_MENU", parentMenu)
                boostMenu.setLabel("Boost Mode Configuration")
                boostMenu.setVisible(True)
                self.initBoostModeInstance(qtouchComponent,groupNum,boostMenu)
            else:
                dynamicName = "boostMenu_" +str(groupNum) 
                dynamicId = "BOOST_MENU_" +str(groupNum) 
                vars()[dynamicName] = qtouchComponent.createMenuSymbol(dynamicId, parentMenu)
                vars()[dynamicName].setLabel("Boost Mode Configuration Group"+str(groupNum))
                vars()[dynamicName].setVisible(True)
                self.initBoostModeInstance(qtouchComponent,groupNum,vars()[dynamicName])
        
        self.bostModeSourceInstance.setBoostModeFiles(configName, qtouchComponent, targetDevice, useTrustZone)

    def initBoostModeInstance(self,qtouchComponent,groupNumber,parentLabel):
        """Initialise boost mode groups Instance
        Arguments:
            :qtouchComponent : touchModule
            :groupNumber : index of the group instance
            :parentLabel : parent symbol for added menu items
        Returns:
            :none
        """
        if int(groupNumber) == 1:
            enable4pMenu = qtouchComponent.createBooleanSymbol("ENABLE_BOOST", parentLabel)
            enable4pMenu.setLabel("Enable Boost")
            enable4pMenu.setDefaultValue(False)
            touch4pNumGroup = qtouchComponent.createIntegerSymbol("MUTL_4P_NUM_GROUP", parentLabel)
            touch4pNumGroup.setVisible(True)
            touch4pNodeKeyMap = qtouchComponent.createStringSymbol("MUTL_4P_NODE_KEY_MAP", parentLabel)
            touch4pNodeKeyMap.setLabel("4P Node to key map")
            touch4pNodeKeyMap.setVisible(True)
            touch4pXLines = qtouchComponent.createStringSymbol("MUTL_4P_X_LINE", parentLabel)
            touch4pXLines.setLabel("4P X Config")
            touch4pXLines.setVisible(True)
            touch4pYLines = qtouchComponent.createStringSymbol("MUTL_4P_Y_LINE", parentLabel)
            touch4pYLines.setLabel("4P Y Config")
            touch4pYLines.setVisible(True)
            touch4pcsd = qtouchComponent.createStringSymbol("MUTL_4P_CSD", parentLabel)
            touch4pcsd.setLabel("4P CSD Config")
            touch4pcsd.setVisible(True)
            touch4pres = qtouchComponent.createStringSymbol("MUTL_4P_Y_RES", parentLabel)
            touch4pres.setLabel("4P RES Config")
            touch4pres.setVisible(True)
            touch4pprsc = qtouchComponent.createStringSymbol("MUTL_4P_PRSC", parentLabel)
            touch4pprsc.setLabel("4P PRSC Config")
            touch4pprsc.setVisible(True)
            touch4pagain = qtouchComponent.createStringSymbol("MUTL_4P_AGAIN", parentLabel)
            touch4pagain.setLabel("4P AGAIN Config")
            touch4pagain.setVisible(True)
            touch4pdgain = qtouchComponent.createStringSymbol("MUTL_4P_DGAIN", parentLabel)
            touch4pdgain.setLabel("4P DGAIN Config")
            touch4pdgain.setVisible(True)
            touch4pfl = qtouchComponent.createStringSymbol("MUTL_4P_FL", parentLabel)
            touch4pfl.setLabel("4P FL Config")
            touch4pfl.setVisible(True)
        else:
            enable4pMenu = qtouchComponent.createBooleanSymbol("GROUP_"+str(groupNumber)+"ENABLE_BOOST", parentLabel)
            enable4pMenu.setLabel("Enable Boost")
            enable4pMenu.setDefaultValue(False)
            touch4pNumGroup = qtouchComponent.createIntegerSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_NUM_GROUP", parentLabel)
            touch4pNumGroup.setVisible(True)
            touch4pNodeKeyMap = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_NODE_KEY_MAP", parentLabel)
            touch4pNodeKeyMap.setLabel("4P Node to key map")
            touch4pNodeKeyMap.setVisible(True)
            touch4pXLines = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_X_LINE", parentLabel)
            touch4pXLines.setLabel("4P X Config")
            touch4pXLines.setVisible(True)
            touch4pYLines = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_Y_LINE", parentLabel)
            touch4pYLines.setLabel("4P Y Config")
            touch4pYLines.setVisible(True)
            touch4pcsd = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_CSD", parentLabel)
            touch4pcsd.setLabel("4P CSD Config")
            touch4pcsd.setVisible(True)
            touch4pres = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_Y_RES", parentLabel)
            touch4pres.setLabel("4P RES Config")
            touch4pres.setVisible(True)
            touch4pprsc = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_PRSC", parentLabel)
            touch4pprsc.setLabel("4P PRSC Config")
            touch4pprsc.setVisible(True)
            touch4pagain = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_AGAIN", parentLabel)
            touch4pagain.setLabel("4P AGAIN Config")
            touch4pagain.setVisible(True)
            touch4pdgain = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_DGAIN", parentLabel)
            touch4pdgain.setLabel("4P DGAIN Config")
            touch4pdgain.setVisible(True)
            touch4pfl = qtouchComponent.createStringSymbol("GROUP_"+str(groupNumber)+"MUTL_4P_FL", parentLabel)
            touch4pfl.setLabel("4P FL Config")
            touch4pfl.setVisible(True)

    def updateBoostModeGroups(symbol,event):
        """Event Handler for number of boost mode groups being used. Triggered by qtouch.updateGroupsCounts(symbol,event)
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
            grpId = "BOOST_MENU_" +str(x)
            component.getSymbolByID(grpId).setEnabled(False)
            component.getSymbolByID(grpId).setVisible(False)
            if(currentVal >= x):
                component.getSymbolByID(grpId).setEnabled(True)
                component.getSymbolByID(grpId).setVisible(True)

    def getMaxGroups(self):
        """Get maximum boost mode groups
        Arguments:
            :none
        Returns:
            :number of boost mode groups  as (int)
        """
        return int(self.maxGroups)

    def setMaxGroups(self,newMax):
        """Set maximum boost mode groups
        Arguments:
            :newMax - new maximum (int)
        Returns:
            :none
        """
        self.maxGroups = int(newMax)


    def getBoostSupported(self):
        """
        Checks if the target device supports boost mode
        Arguments : targetDevice
        Returns : True / False
        """

        return self.json_data["features"]["boost_mode"]
        
        # if(targetDevice in self.boost_mode_support):
        #     if(targetDevice in self.boost_mode_remove_support_temporarily):
        #         return False
        #     else:
        #         return True
        # else:
        #     return False

    def processBoostMode(self,symbol,event,targetDevice,nodeCount):
        """Handler for managing boost mode configuration 
        Triggered by qtouch.ongenerate function 
        scans node and surface to update references
        Arguments:
            :symbol : the symbol that triggered the callback
            :event : the new value. 
        Returns:
            :none
        """

        touchNumChannel = nodeCount
        boostModeEnabled = False

        localComponent = symbol.getComponent()
        touchSenseTechnology = localComponent.getSymbolByID("SENSE_TECHNOLOGY").getValue()
        surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
        lump_config = localComponent.getSymbolByID("LUMP_CONFIG").getValue()
        
        if self.getBoostSupported():
            if localComponent.getSymbolByID("ENABLE_BOOST").getValue():
                boostModeEnabled = True

        if localComponent.getSymbolByID("ENABLE_BOOST").getValue():
                localComponent.getSymbolByID("MODULE_ID").setValue(self.json_data["acquisition"]["boost_mode"]["module_id"])
                boostModeEnabled = True

        if not boostModeEnabled:
            return

        if (self.getBoostSupported()):
            # maximum number of boost mode group is limited to 32 in the script
            touch4pMaxGroup = 32

            localComponent = symbol.getComponent()
            surface_enabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
            surface_ver_num = int(localComponent.getSymbolByID("VERT_NUM_KEY").getValue())
            surface_hor_num = int(localComponent.getSymbolByID("HORI_NUM_KEY").getValue())
            surface_ver_start = int(localComponent.getSymbolByID("VERT_START_KEY").getValue())
            surface_hor_start = int(localComponent.getSymbolByID("HORI_START_KEY").getValue())

            y_lines = []
            x_lines = []
            csd = []
            resistor = []
            prsc = []
            filterlevel = []
            again = []
            dgain = []

            surface_y_lines = []
            surface_x_lines = []
            surface_csd = []
            surface_resistor = []
            surface_prsc = []
            surface_filterlevel = []
            surface_again = []
            surface_dgain = []

            y_lines_unique = []
            x_lines_for_each_unique_y = []
            csd_for_each_unique_y = []
            resistor_for_each_unique_y = []
            prsc_for_each_unique_y = []
            filterlevel_for_each_unique_y = []
            again_for_each_unique_y = []
            dgain_for_each_unique_y = []

            y_lines_group_of_4 = []
            x_lines_group_of_4 = []
            csd_group_of_4 = []
            resistor_group_of_4 = []
            prsc_group_of_4 = []
            filterlevel_group_of_4 = []
            again_group_of_4 = []
            dgain_group_of_4 = []

            key_to_node_map_temp = []
            key_to_node_map = []
            node_count = 0
            x_none_cnt = 0

            tempSymbol = localComponent.getSymbolByID("MUTL_4P_X_LINE")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_Y_LINE")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_CSD")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_Y_RES")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_PRSC")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_AGAIN")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_DGAIN")
            tempSymbol.setValue("")
            tempSymbol = localComponent.getSymbolByID("MUTL_4P_FL")
            tempSymbol.setValue("")
            for channel_num in range(0, touchNumChannel):
                tempSymbol = localComponent.getSymbolByID("MUTL-X-INPUT_"+ str(channel_num))
                x_lines.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("MUTL-Y-INPUT_"+ str(channel_num))
                # print(str(tempSymbol))
                y_lines.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("DEF_TOUCH_CHARGE_SHARE_DELAY"+str(channel_num))
                csd.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("DEF_NOD_SERIES_RESISTOR"+str(channel_num))
                resistor.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("DEF_NOD_PTC_PRESCALER"+str(channel_num))
                prsc.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("DEF_NOD_GAIN_ANA"+str(channel_num))
                again.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("DEF_DIGI_FILT_GAIN"+str(channel_num))
                dgain.append(tempSymbol.getValue())
                tempSymbol = localComponent.getSymbolByID("DEF_DIGI_FILT_OVERSAMPLING"+str(channel_num))
                filterlevel.append(tempSymbol.getValue())

            if lump_config != "":
                lump_ind = lump_config.split(";")
                nolump = len(lump_ind)
                for length in range(nolump):
                    # check for empty configuration
                    if lump_ind[length] == "":
                        continue
                    currLump = lump_ind[length]
                    channelnum = int(currLump.split(":")[0])
                    whichChannels = currLump.split(":")[1].split(",")
                    tempx = []
                    tempy = []
                    for jj in [int(i) for i in whichChannels]:
                        if x_lines[jj] not in tempx:
                            tempx.append(x_lines[jj])
                        if y_lines[jj] not in tempy:
                            tempy.append(y_lines[jj])
                    if len(tempy) == 1:
                        y_lines[channelnum] = tempy[0]
                    else:
                        y_lines[channelnum] = tempy
                    x_lines[channelnum] = tempx

            if surface_enabled == True:
                for channel_num in range(0, touchNumChannel):
                    if (channel_num < surface_ver_start) or (channel_num >= (surface_hor_start+surface_hor_num)):
                        surface_x_lines.append(x_lines[channel_num])
                        surface_y_lines.append(y_lines[channel_num])
                        surface_csd.append(csd[channel_num])
                        surface_resistor.append(resistor[channel_num])
                        surface_prsc.append(prsc[channel_num])
                        surface_again.append(again[channel_num])
                        surface_dgain.append(dgain[channel_num])
                        surface_filterlevel.append(filterlevel[channel_num])
                    elif channel_num == surface_ver_start:
                        for ver_num in range(0,surface_ver_num):
                            for hor_num in range(0,surface_hor_num):
                                surface_x_lines.append(x_lines[surface_hor_start+hor_num])
                                surface_y_lines.append(y_lines[surface_ver_start+ver_num])
                                surface_csd.append(csd[surface_ver_start+ver_num])
                                surface_resistor.append(resistor[surface_ver_start+ver_num])
                                surface_prsc.append(prsc[surface_ver_start+ver_num])
                                surface_again.append(again[surface_ver_start+ver_num])
                                surface_dgain.append(dgain[surface_ver_start+ver_num])
                                surface_filterlevel.append(filterlevel[surface_ver_start+ver_num])
                #replace with surface computed
                y_lines = surface_y_lines
                x_lines = surface_x_lines
                csd = surface_csd
                resistor = surface_resistor
                prsc = surface_prsc
                again = surface_again
                dgain = surface_dgain
                filterlevel = surface_filterlevel
            #identify unique Y lines
            for each_y_line in y_lines:
                if each_y_line not in y_lines_unique:
                    y_lines_unique.append(each_y_line)
            #for each unique Y line find the other parameters including x lines
            for each_unique_y_line in y_lines_unique:
                x_lines_for_this_y_line = []
                csd_for_this_y_line = []
                res_for_this_y_line = []
                prsc_for_this_y_line = []
                again_for_this_y_line = []
                dgain_for_this_y_line = []
                filterlevel_for_this_y_line = []
                for num in range(0,len(x_lines)):
                    if each_unique_y_line == y_lines[num]:
                        key_to_node_map_temp.append(num)
                        x_lines_for_this_y_line.append(x_lines[num])
                        csd_for_this_y_line.append(csd[num])
                        res_for_this_y_line.append(resistor[num])
                        prsc_for_this_y_line.append(prsc[num])
                        again_for_this_y_line.append(again[num])
                        dgain_for_this_y_line.append(dgain[num])
                        filterlevel_for_this_y_line.append(filterlevel[num])
                x_lines_for_each_unique_y.append(x_lines_for_this_y_line)
                csd_for_each_unique_y.append(csd_for_this_y_line)
                resistor_for_each_unique_y.append(res_for_this_y_line)
                prsc_for_each_unique_y.append(prsc_for_this_y_line)
                filterlevel_for_each_unique_y.append(filterlevel_for_this_y_line)
                again_for_each_unique_y.append(again_for_this_y_line)
                dgain_for_each_unique_y.append(dgain_for_this_y_line)
            # Now group them in 4 numbers
            # if more than 4 elements, split them in to multiple groups
            # if less than 4 elements, append X_NONE
            for x_group_num in range(0,len(y_lines_unique)):
                this_x_group = x_lines_for_each_unique_y[x_group_num]
                if len(this_x_group) <= 4: # less than 4 elements
                    while len(this_x_group) < 4:
                        this_x_group.append("X_NONE")
                    x_lines_group_of_4.append(this_x_group)
                    y_lines_group_of_4.append(y_lines_unique[x_group_num])
                    csd_group_of_4.append(csd_for_each_unique_y[x_group_num])
                    resistor_group_of_4.append(resistor_for_each_unique_y[x_group_num])
                    prsc_group_of_4.append(prsc_for_each_unique_y[x_group_num])
                    again_group_of_4.append(again_for_each_unique_y[x_group_num])
                    dgain_group_of_4.append(dgain_for_each_unique_y[x_group_num])
                    filterlevel_group_of_4.append(filterlevel_for_each_unique_y[x_group_num])
                else: # more than 4 elements
                    x_group_4 = []
                    for x_len in range(0,len(this_x_group)):
                        x_group_4.append(this_x_group[x_len])
                        if len(x_group_4) == 4:
                            x_lines_group_of_4.append(x_group_4)
                            y_lines_group_of_4.append(y_lines_unique[x_group_num])
                            csd_group_of_4.append(csd_for_each_unique_y[x_group_num])
                            resistor_group_of_4.append(resistor_for_each_unique_y[x_group_num])
                            prsc_group_of_4.append(prsc_for_each_unique_y[x_group_num])
                            again_group_of_4.append(again_for_each_unique_y[x_group_num])
                            dgain_group_of_4.append(dgain_for_each_unique_y[x_group_num])
                            filterlevel_group_of_4.append(filterlevel_for_each_unique_y[x_group_num])
                            x_group_4 = []
                    if len(x_group_4) != 0: # residual X lines. num of x line is < 4
                        while len(x_group_4) < 4:
                            x_group_4.append("X_NONE")
                        x_lines_group_of_4.append(x_group_4)
                        y_lines_group_of_4.append(y_lines_unique[x_group_num])
                        csd_group_of_4.append(csd_for_each_unique_y[x_group_num])
                        resistor_group_of_4.append(resistor_for_each_unique_y[x_group_num])
                        prsc_group_of_4.append(prsc_for_each_unique_y[x_group_num])
                        again_group_of_4.append(again_for_each_unique_y[x_group_num])
                        dgain_group_of_4.append(dgain_for_each_unique_y[x_group_num])
                        filterlevel_group_of_4.append(filterlevel_for_each_unique_y[x_group_num])
            for j in range(0,len(x_lines_group_of_4)):
                if j < touch4pMaxGroup:
                    temp_string = "{ "
                    for i in x_lines_group_of_4[j]:
                        if isinstance(i, list): #lump
                            key_to_node_map.insert(key_to_node_map_temp[node_count], node_count+x_none_cnt)
                            node_count = node_count + 1
                            for eachI in i:
                                temp_string = temp_string + 'X(' + str(eachI) + ')|'
                            temp_string = temp_string[:-1] +","
                        elif i != "X_NONE":
                                key_to_node_map.insert(key_to_node_map_temp[node_count], node_count+x_none_cnt)
                                node_count = node_count + 1
                                temp_string = temp_string + 'X(' + str(i) + '),'
                        else:
                            x_none_cnt = x_none_cnt + 1
                            temp_string = temp_string + "X_NONE,"
                    temp_string = temp_string[:-1] + ' }'
                    tempSymbol = localComponent.getSymbolByID("MUTL_4P_X_LINE")
                    temp_string1 = tempSymbol.getValue()
                    if temp_string1 != "":
                        temp_string1 = temp_string1 + '+'
                    temp_string1 = temp_string1 + temp_string
                    tempSymbol.setValue(temp_string1)

                    tempSymbol = localComponent.getSymbolByID("MUTL_4P_Y_LINE")
                    temp_string = tempSymbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    current_y = y_lines_group_of_4[j]
                    if isinstance(current_y, list):
                        for eachI in current_y:
                            temp_string = temp_string + 'Y(' + str(eachI) + ')|'
                        temp_string = temp_string[:-1]
                    else:
                        temp_string = temp_string + 'Y('+str(y_lines_group_of_4[j])+')'
                    tempSymbol.setValue(temp_string)

                    tempSymbol = localComponent.getSymbolByID("MUTL_4P_CSD")
                    temp_string = tempSymbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    temp_string = temp_string + str(max(csd_group_of_4[j]))
                    tempSymbol.setValue(temp_string)

                    tempSymbol = localComponent.getSymbolByID("MUTL_4P_Y_RES")
                    tempSymbol_1 = localComponent.getSymbolByID("DEF_NOD_SERIES_RESISTOR0")
                    temp_string = tempSymbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    temp_string = temp_string + str(tempSymbol_1.getKeyValue(max(resistor_group_of_4[j])))
                    tempSymbol.setValue(temp_string)

                    tempSmbol = localComponent.getSymbolByID("MUTL_4P_PRSC")
                    tempSymbol_1 = localComponent.getSymbolByID("DEF_NOD_PTC_PRESCALER0")
                    temp_string = tempSmbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    temp_string = temp_string + str(tempSymbol_1.getKeyValue(max(prsc_group_of_4[j])))
                    tempSmbol.setValue(temp_string)

                    tempSmbol = localComponent.getSymbolByID("MUTL_4P_AGAIN")
                    tempSymbol_1 = localComponent.getSymbolByID("DEF_NOD_GAIN_ANA0")
                    temp_string = tempSmbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    temp_string = temp_string + str(tempSymbol_1.getKeyValue(max(again_group_of_4[j])))
                    tempSmbol.setValue(temp_string)

                    tempSmbol = localComponent.getSymbolByID("MUTL_4P_DGAIN")
                    tempSymbol_1 = localComponent.getSymbolByID("DEF_DIGI_FILT_GAIN0")
                    temp_string = tempSmbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    temp_string = temp_string + str(tempSymbol_1.getKeyValue(max(dgain_group_of_4[j])))
                    tempSmbol.setValue(temp_string)

                    tempSmbol = localComponent.getSymbolByID("MUTL_4P_FL")
                    tempSymbol_1 = localComponent.getSymbolByID("DEF_DIGI_FILT_OVERSAMPLING0")
                    temp_string = tempSmbol.getValue()
                    if temp_string != "":
                        temp_string = temp_string + '+'
                    temp_string = temp_string + str(tempSymbol_1.getKeyValue(max(filterlevel_group_of_4[j])))
                    tempSmbol.setValue(temp_string)
            # store total number of groups
            tempSmbol = localComponent.getSymbolByID("MUTL_4P_NUM_GROUP")
            tempSmbol.setValue(len(x_lines_group_of_4))
            # combine the node to key map with commas
            temp_string = ""
            for i in key_to_node_map:
                if temp_string == "":
                    temp_string = str(i)
                else:
                    temp_string = temp_string + ',' + str(i)
            tempSmbol = localComponent.getSymbolByID("MUTL_4P_NODE_KEY_MAP")
            tempSmbol.setValue(temp_string)
            