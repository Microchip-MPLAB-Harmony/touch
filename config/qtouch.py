InterruptVector = "PTC" + "_INTERRUPT_ENABLE"
InterruptHandler = "PTC" + "_INTERRUPT_HANDLER"

global nonSecureStatus
nonSecureStatus = "SECURE"

global InterruptVectorSecurity
InterruptVectorSecurity = []

global qtouchFilesArray
qtouchFilesArray = []

global IDArray
IDArray = ["TOUCH_ACQ_LIB","TOUCH_ACQ_AUTO_LIB","TOUCH_ACQ_HEADER",
"TOUCH_BIND_LIB","TOUCH_BIND_HEADER","TOUCH_COMMON_HEADER",
"TOUCH_KEY_LIB","TOUCH_KEY_HEADER",
"TOUCH_SCR_LIB","TOUCH_SCR_HEADER",
"TOUCH_HOP_LIB","TOUCH_HOP_AUTO_LIB","TOUCH_HOP_HEADER","TOUCH_HOP_AUTO_HEADER"
"TOUCH_SURFACE1T_LIB","TOUCH_SURFACE1T_HEADER",
"TOUCH_SURFACE2T_LIB","TOUCH_SURFACE2T_HEADER"]

timer_based_driven_shield_supported_device = ["SAMD21","SAMDA1","SAMHA1","SAME54","SAME53","SAME51","SAMD51","SAMC21","SAMC20","SAML21","SAML22"]
adc_based_touch_acqusition_device = ["SAME54","SAME53","SAME51","SAMD51"]
lump_not_supported_device = []
device_with_hardware_driven_shield_support = ["SAML10","SAML11","PIC32MZW"]
boost_mode_supported_devices = ["SAML10","SAML1xE","SAML11"]
event_system_based_low_power = ["SAMD20","SAMD21","SAMDA1","SAMHA1","SAML11","SAML10","SAMC21","SAMC20"]
software_based_low_power = ["SAMD20","SAMD21","SAMDA1","SAMHA1","SAML11","SAML10","SAMC21","SAMC20"]


def processBoostMode(symbol,event):
	global touchNumChannel
	if (getDeviceName.getDefaultValue() in boost_mode_supported_devices):
		localComponent = symbol.getComponent()
		# maximum number of boost mode group is limited to 32 in the script
		touch4pMaxGroup = 32
		y_lines = []
		x_lines = []
		csd = []
		resistor = []
		prsc = []
		filterlevel = []
		again = []
		dgain = []

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
		for channel_num in range(0, touchNumChannel.getValue()):
			tempSymbol = localComponent.getSymbolByID("MUTL-X-INPUT_"+ str(channel_num))
			x_lines.append(tempSymbol.getValue())
			tempSymbol = localComponent.getSymbolByID("MUTL-Y-INPUT_"+ str(channel_num))
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
			for num in range(0,touchNumChannel.getValue()):
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
					if i != "X_NONE":
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

def searchqtouchFilesArray(idString):
    retVal = False
    for x in qtouchFilesArray:
        if str(x.getID()) == idString:
            retVal = True
            break
    return retVal;

def checkqtouchFilesArray(symbol,idString):
    component = symbol
    if component.getSymbolByID(idString).getEnabled() == True:
        if searchqtouchFilesArray(idString) == False:
            qtouchFilesArray.append(component.getSymbolByID(idString))
            print("------------------Added : " + idString)
    else:
        if searchqtouchFilesArray(idString) == True:
            qtouchFilesArray.remove(component.getSymbolByID(idString))
            print("------------------Removed : " + idString)
    return     
 
def securefileUpdate(symbol, event):
    global nonSecureStatus
    global qtouchFilesArray
    global InterruptVectorSecurity
    global IDArray
    
    component = symbol.getComponent()
    
    # for currID in IDArray:
        # checkqtouchFilesArray(component,currID)
   
    if event["value"] == False:
        nonSecureStatus = "SECURE"

        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, False)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        nonSecureStatus = "NON_SECURE"

        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, True)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, True)
        
    checknonsecureStatus();

def checknonsecureStatus():
    global checkname
    global qtouchComponent
    ptcNonSecureState = Database.getSymbolValue("core", "PTC_IS_NON_SECURE")
    if ptcNonSecureState == False:
        nonSecureStatus = "SECURE"
    else:
        nonSecureStatus = "NON_SECURE"    
        
    
    print("*** checknonsecureStatus Updated : "+ nonSecureStatus)
    print("*** Number of entries in file array : " + str(len(qtouchFilesArray)))

    
    for kx in range(len(qtouchFilesArray)):    
        checkname = str(qtouchFilesArray[kx].getID()).split('_')       
        if ("LIB" in checkname):
            if(nonSecureStatus == "SECURE"):
                qtouchFilesArray[kx].setDestPath("../../../../../Secure/firmware/src/config/default/touch/lib/")
            else:
                qtouchFilesArray[kx].setDestPath("../../../../../NonSecure/firmware/src/config/default/touch/lib/")
            #print(str(qtouchFilesArray[kx].getDestPath()))
        #else:
            #print("--- lib NOT FOUND---")
        qtouchFilesArray[kx].setSecurity(nonSecureStatus)
        #print(str(checkname) + " = " + str(nonSecureStatus))
    
def onAttachmentConnected(source,target):
    global nonSecureStatus
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if (connectID == "Touch_timer"):
        plibUsed = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if targetID == "RTC_TMR":
            if (Database.getSymbolValue(remoteID, "RTC_MODE0_MATCHCLR") == False):
                Database.setSymbolValue(remoteID, "RTC_MODE0_MATCHCLR", True)
            if (Database.getSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE") == False):
                Database.setSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE", True)
                Database.setSymbolValue(remoteID, "RTC_MODULE_SELECTION", 0)
        else:
            Database.setSymbolValue(remoteID, "TIMER_PRE_SCALER", 0)
            Database.setSymbolValue(remoteID, "TMR_INTERRUPT_MODE", True)
    if (connectID == "Touch_sercom"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if (Database.getSymbolValue(remoteID, "USART_INTERRUPT_MODE") == True):
            Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", False)

    if (connectID == "Touch_sercom_Krono"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if (Database.getSymbolValue(remoteID, "USART_INTERRUPT_MODE") == False):
            Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", True)


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if (connectID == "Touch_timer"):
        plibUsed = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE")
        plibUsed.clearValue()
    
    if (connectID == "Touch_sercom"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE")
        plibUsed.clearValue()
    if (connectID == "Touch_sercom_Krono"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE")
        plibUsed.clearValue()

def enableHopFiles(symbol,event):
    component = symbol.getComponent()
    hopAutoEnabled = enableFreqHopAutoTuneMenu.getValue()
    print(hopAutoEnabled)
    if(event["value"] == True) and (hopAutoEnabled == True):
        component.getSymbolByID("TOUCH_HOP_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_HOP_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_HOP_AUTO_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_HOP_AUTO_HEADER").setEnabled(True)
    elif(event["value"] == True):
        component.getSymbolByID("TOUCH_HOP_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_HOP_HEADER").setEnabled(True)
    else:
        component.getSymbolByID("TOUCH_HOP_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_HOP_HEADER").setEnabled(False)

def enableDataStreamerFtlFiles(symbol,event):
    component = symbol.getComponent()

    if(event["value"] == True):
        #tchDataStreamerHeaderFile.setEnabled(True)
        component.setDependencyEnabled("Touch_sercom", True)
        component.getSymbolByID("TOUCH_SERCOM_INSTANCE").setVisible(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_SOURCE").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_db").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_ds").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(True)
    else:
        #tchDataStreamerHeaderFile.setEnabled(False)
        component.setDependencyEnabled("Touch_sercom", False)
        component.getSymbolByID("TOUCH_SERCOM_INSTANCE").setVisible(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_SOURCE").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_db").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_ds").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(False)
        

def enableScroller(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("TOUCH_SCR_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_SCR_HEADER").setEnabled(True)
    else:
        component.getSymbolByID("TOUCH_SCR_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_SCR_HEADER").setEnabled(False)

def enableGestureFiles(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("TOUCH_GESTURE_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_GESTURE_HEADER").setEnabled(True)
    else:
        component.getSymbolByID("TOUCH_GESTURE_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_GESTURE_HEADER").setEnabled(False)

def enable2DSurfaceFtlFiles(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        #tchKronocommUartHeaderFile.setEnabled(True)
        component.setDependencyEnabled("Touch_sercom_Krono", True)
        component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_SOURCE").setEnabled(True)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_SOURCE").setEnabled(True)
    else:
        #tchKronocommUartHeaderFile.setEnabled(False)
        component.setDependencyEnabled("Touch_sercom_Krono", False)
        component.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE").setVisible(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_UART_SOURCE").setEnabled(False)
        component.getSymbolByID("TOUCH_KRONOCOMM_ADAPTOR_SOURCE").setEnabled(False)

def processLump(symbol, event):
	global touchNumChannel
	global enableDrivenShieldAdjacent
	global enableDrivenShieldDedicated
	global drivenShieldDedicatedPin
	totalChannelCount = touchNumChannel.getValue()
	for i in range(0,totalChannelCount):
		if(touchSenseTechnology.getValue() == 0):
			tchMutXPinSelection[int(i)].setKeyValue(str(i),"X_NONE")
			tchMutXPinSelection[int(i)].setValue(int(i))
	if (getDeviceName.getDefaultValue() not in lump_not_supported_device):
		global lumpSymbol
		lump_feature = lumpSymbol.getValue()
		if (lump_feature != ""):
			lump_items = lump_feature.split(";")
			num_of_lumps = len(lump_items)
			for lmp in range(0,num_of_lumps):
				lump_x = []
				lump_y = []
				lump_split = lump_items[lmp].split(":")
				lump_node = lump_split[0]
				lump_node_array = lump_split[1].split(",")
				if ((touchSenseTechnology.getValue() == 0) or (touchSenseTechnology.getValue() == 2)):
					for item in lump_node_array:
						val = tchSelfPinSelection[int(item)].getValue()
						yCh = tchSelfPinSelection[int(item)].getKeyValue(val)
						if yCh not in lump_y:
							lump_y.append(yCh)
					lumpy = "|".join(lump_y)
					tchSelfPinSelection[int(lump_node)].setKeyValue(str(0),lumpy)
					tchSelfPinSelection[int(lump_node)].setValue(0)
				elif (touchSenseTechnology.getValue() == 1):
					for item in lump_node_array:
						val1 = tchMutXPinSelection[int(item)].getValue()
						val2 = tchMutYPinSelection[int(item)].getValue()
						xCh = tchMutXPinSelection[int(item)].getKeyValue(val1)
						yCh = tchMutYPinSelection[int(item)].getKeyValue(val2)
						if xCh not in lump_x:
							lump_x.append(xCh)
						if yCh not in lump_y:
							lump_y.append(yCh)
					lumpx = "|".join(lump_x)
					tchMutXPinSelection[int(lump_node)].setKeyValue(str(0),lumpx)
					tchMutXPinSelection[int(lump_node)].setValue(0)
					lumpy = "|".join(lump_y)
					tchMutYPinSelection[int(lump_node)].setKeyValue(str(0),lumpy)
					tchMutYPinSelection[int(lump_node)].setValue(0)

	for i in range(0,totalChannelCount):
		if (getDeviceName.getDefaultValue() in device_with_hardware_driven_shield_support):
			if((enableDrivenShieldAdjacent.getValue() == True)or(enableDrivenShieldDedicated.getValue() == True)):
				shieldPins = []
				if (enableDrivenShieldDedicated.getValue() == True):
					shieldY = drivenShieldDedicatedPin.getValue()
					shieldY = drivenShieldDedicatedPin.getKeyValue(shieldY)
					shieldPins.append(shieldY)
				if (enableDrivenShieldAdjacent.getValue() == True):
					if (lump_feature != ""):
						LUMP_INDI = lump_feature.split(";")
						LUMP_NUM = len(LUMP_INDI)
						input0 =[]
						for a in range(0,(totalChannelCount-LUMP_NUM)):
							value = tchSelfPinSelection[int(a)].getValue()
							input0.append(tchSelfPinSelection[int(a)].getKeyValue(value))
						if (i < totalChannelCount-LUMP_NUM):
							for j in range(0,(totalChannelCount-LUMP_NUM)):
								value1 = tchSelfPinSelection[int(i)].getValue()
								if ((tchSelfPinSelection[int(i)].getKeyValue(value1)) != input0[j]):
									shieldPins.append(input0[j])
						else:
							LUMP_NODE_VAL = tchSelfPinSelection[int(i)].getValue()
							LUMP_NODE_INDI = tchSelfPinSelection[int(i)].getKeyValue(LUMP_NODE_VAL).split("|")
							LUMP_NODE_SIZE = len(LUMP_NODE_INDI)
							for j in range(0,(totalChannelCount-LUMP_NUM)):
								par = 0
								for y in range(0,LUMP_NODE_SIZE):
									if (LUMP_NODE_INDI[y] == input0[j]):
										par = 1
								if par == 0:
									shieldPins.append(input0[j])
					else:
						for j in range(0,totalChannelCount):
							if (i != j):
								shildY = tchSelfPinSelection[int(j)].getValue()
								shieldY = tchSelfPinSelection[int(j)].getKeyValue(shildY)
								shieldPins.append(shieldY)
				if(shieldPins != []):
					drivenPin = "|".join(shieldPins)
				else:
					drivenPin = "X_NONE"
				tchMutXPinSelection[int(i)].setKeyValue(str(i),drivenPin)
				tchMutXPinSelection[int(i)].setValue(int(i))
			elif(touchSenseTechnology.getValue() == 0):
				tchMutXPinSelection[int(i)].setKeyValue(str(i),"X_NONE")
				tchMutXPinSelection[int(i)].setValue(int(i))

	if (touchSenseTechnology.getValue() == 1) and (enableSurfaceMenu.getValue() == True):
		MUTL_SURFACE_X = []
		MUTL_SURFACE_Y = []
		HORI_START_KEY = horiStartKey.getValue()
		HORI_NUM_KEY = horiNumKey.getValue()
		VERT_START_KEY = vertStartKey.getValue()
		VERT_NUM_KEY = vertNumKey.getValue()
		for i in range(HORI_START_KEY,(HORI_START_KEY+HORI_NUM_KEY)):
			vals = tchMutXPinSelection[int(i)].getValue()
			MUTL_SURFACE_X.append(tchMutXPinSelection[int(i)].getKeyValue(vals))
		MUTL_SURFACE_X = "|".join(MUTL_SURFACE_X)
		for j in range(VERT_START_KEY,(VERT_START_KEY+VERT_NUM_KEY)):
			vals = tchMutYPinSelection[int(j)].getValue()
			MUTL_SURFACE_Y.append(tchMutYPinSelection[int(j)].getKeyValue(vals))
		MUTL_SURFACE_Y = "|".join(MUTL_SURFACE_Y)
		if (VERT_START_KEY >0):
			for i in range(0,VERT_START_KEY):
				vals1 = tchMutXPinSelection[int(i)].getValue()
				vals2 = tchMutYPinSelection[int(i)].getValue()
				tchMutXPinSelection[int(i)].setValue(vals1)
				tchMutYPinSelection[int(i)].setValue(vals2)
		for i in range(VERT_START_KEY,(VERT_START_KEY+VERT_NUM_KEY)):
			vals1 = tchMutXPinSelection[int(i)].getValue()
			vals2 = tchMutYPinSelection[int(i)].getValue()
			tchMutXPinSelection[int(i)].setKeyValue(str(vals1),MUTL_SURFACE_X)
			tchMutXPinSelection[int(i)].setValue(vals1)
			tchMutYPinSelection[int(i)].setValue(vals2)
		for i in range(HORI_START_KEY,(HORI_START_KEY+HORI_NUM_KEY)):
			vals1 = tchMutXPinSelection[int(i)].getValue()
			vals2 = tchMutYPinSelection[int(i)].getValue()
			tchMutYPinSelection[int(i)].setKeyValue(str(vals2),MUTL_SURFACE_Y)
			tchMutXPinSelection[int(i)].setValue(vals1)
			tchMutYPinSelection[int(i)].setValue(vals2)
		if (totalChannelCount - (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY ) >0):
			for i in range((VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY),totalChannelCount):
				vals1 = tchMutXPinSelection[int(i)].getValue()
				vals2 = tchMutYPinSelection[int(i)].getValue()
				tchMutXPinSelection[int(i)].setValue(vals1)
				tchMutYPinSelection[int(i)].setValue(vals2)

def onGenerate(symbol,event):
	processBoostMode(symbol,event)
	processLump(symbol,event)
    
def onPTCClock(symbol,event):
    component = symbol.getComponent()
    if component.getSymbolValue("TOUCH_LOADED"):
        frequency = event['symbol'].getValue()
        channels = component.getSymbolValue("TOUCH_CHAN_ENABLE_CNT")
        if frequency > 0 and channels > 0:   
            symbol.setValue(symbol.getDefaultValue()+":sync")
            sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
            sevent.setValue("ptcclock")
            sevent.setValue("")
    
    
def onWarning(symbol,event):
    if event['symbol'].getID() == "PTC_CLOCK_FREQ":
        if "sync" in event['symbol'].getValue():
            symbol.setLabel("!!!Warning PTC clock out of sync")
            symbol.setDescription("Open touch configurator and save project")
            symbol.setVisible(True)
        elif "range" in event['symbol'].getValue():
            symbol.setLabel("!!!Warning PTC clock out of range")
            symbol.setDescription("Open clock configurator and adjust input clock")
            symbol.setVisible(True)
        else:
            symbol.setLabel("")
            symbol.setDescription("")
            symbol.setVisible(False)

autoComponentIDTable = ["rtc"]
autoConnectTable = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"]]

#used for driven shield 
ptcYPads = []
touchChannels = []

################################################################################
#### Component ####
################################################################################
def instantiateComponent(qtouchComponent):
    global autoComponentIDTable
    global autoConnectTable
    global lumpSymbol
    global qtouchFilesArray
    global InterruptVector
    global IDArray
    
    qtouchFilesArray = []
	
    configName = Variables.get("__CONFIGURATION_NAME")

    touchMenu = qtouchComponent.createMenuSymbol("TOUCH_MENU", None)
    touchMenu.setLabel("Touch Configuration")
    
    touchInfoMenu = qtouchComponent.createMenuSymbol("TOUCH_INFO", None)
    touchInfoMenu.setLabel("Touch Configuration Helper")
    #touchInfoMenu.setVisible(False)
    
    touchScriptEvent = qtouchComponent.createStringSymbol("TOUCH_SCRIPT_EVENT", touchInfoMenu)
    touchScriptEvent.setLabel("Script Event ")
    touchScriptEvent.setReadOnly(True)
	
    ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance@[name=\"PTC\"]/parameters/param@[name=\"GCLK_ID\"]")
    if ptcClockInfo is None:
        ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/parameters/param@[name=\"GCLK_ID\"]")
    ptcFreqencyId= qtouchComponent.createStringSymbol("PTC_CLOCK_FREQ", touchInfoMenu)
    ptcFreqencyId.setLabel("PTC Freqency Id ")
    ptcFreqencyId.setReadOnly(True)
    ptcFreqencyId.setDefaultValue("GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ")
    ptcFreqencyId.setDependencies(onPTCClock,["core."+"GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ"])
    
    enableGenerate = qtouchComponent.createBooleanSymbol("TOUCH_PRE_GENERATE", touchInfoMenu)
    enableGenerate.setLabel("Generate Project")
    enableGenerate.setDefaultValue(False)
    enableGenerate.setDependencies(onGenerate,["TOUCH_PRE_GENERATE"])
    
    enableLoaded = qtouchComponent.createBooleanSymbol("TOUCH_LOADED", touchInfoMenu)
    enableLoaded.setLabel("Project Loaded")
    enableLoaded.setDefaultValue(False)
	
    execfile(Module.getPath() +"/config/interface.py")
    execfile(Module.getPath() +"/config/acquisition_"+getDeviceName.getDefaultValue().lower()+".py")
    if (getDeviceName.getDefaultValue() not in lump_not_supported_device):
        lumpSymbol = qtouchComponent.createStringSymbol("LUMP_CONFIG", touchMenu)
        lumpSymbol.setLabel("Lump Configuration")
        lumpSymbol.setDefaultValue("")
        lumpSymbol.setVisible(True)
    if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
        execfile(Module.getPath() +"/config/node_E5X.py")
    elif (getDeviceName.getDefaultValue() in ["SAMD20","SAMD21","SAMDA1","SAMHA1"]):
        execfile(Module.getPath() +"/config/node_D2X.py")
    elif (getDeviceName.getDefaultValue() in ["SAML21"]):
        execfile(Module.getPath() +"/config/node_L21.py")
    elif (getDeviceName.getDefaultValue() in ["SAML22"]):
        execfile(Module.getPath() +"/config/node_L22.py")
    elif (getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
        execfile(Module.getPath() +"/config/node_L1x.py")
    elif (getDeviceName.getDefaultValue() in ["SAMD10","SAMD11"]):
        execfile(Module.getPath() +"/config/node_D1X.py")
    elif (getDeviceName.getDefaultValue() in ["PIC32MZW"]):
        execfile(Module.getPath() +"/config/node_pic32mz.py")
        autoComponentIDTable = ["adchs","tmr2"]
        autoConnectTable = [["lib_qtouch", "Touch_timer","tmr2","TMR2_TMR"]]
    else:
        execfile(Module.getPath() +"/config/node_C2X.py")
    
    if (getDeviceName.getDefaultValue() in timer_based_driven_shield_supported_device):
        execfile(Module.getPath() +"/config/drivenshield.py")

    if (getDeviceName.getDefaultValue() in boost_mode_supported_devices):
        execfile(Module.getPath() +"/config/boost_mode.py")

    execfile(Module.getPath() +"/config/key.py")
    execfile(Module.getPath() +"/config/sensor.py")

	#Low power
    if (getDeviceName.getDefaultValue() in event_system_based_low_power):
        execfile(Module.getPath() +"/config/eventlowpower.py")
    if (getDeviceName.getDefaultValue() in software_based_low_power):
        execfile(Module.getPath() +"/config/softwarelowpower.py")
    # Enable Scroller 
    enableScrollerMenu = qtouchComponent.createBooleanSymbol("ENABLE_SCROLLER", touchMenu)
    enableScrollerMenu.setLabel("Enable Scroller")
    enableScrollerMenu.setDefaultValue(False)
    execfile(Module.getPath() +"/config/scroller.py")
    enableScrollerMenu.setDependencies(enableScroller,["ENABLE_SCROLLER"])
    global enableSurfaceMenu
    # Enable Surface 
    enableSurfaceMenu = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE", touchMenu)
    enableSurfaceMenu.setLabel("Enable Surface")
    enableSurfaceMenu.setDefaultValue(False)
    execfile(Module.getPath() +"/config/surface.py")

    # Enable Gesture 
    enableGestureMenu = qtouchComponent.createBooleanSymbol("ENABLE_GESTURE", touchMenu)
    enableGestureMenu.setLabel("Enable Gesture")
    enableGestureMenu.setDefaultValue(False)
    execfile(Module.getPath() +"/config/gesture.py")
    enableGestureMenu.setDependencies(enableGestureFiles,["ENABLE_GESTURE"])

    global enableFreqHopMenu
    # Enable Frequency Hop  
    enableFreqHopMenu = qtouchComponent.createBooleanSymbol("ENABLE_FREQ_HOP", touchMenu)
    enableFreqHopMenu.setLabel("Enable Frequency Hop")
    enableFreqHopMenu.setDefaultValue(False)
    enableFreqHopMenu.setDescription("Frequency Hop is a mechanism used in touch measurement to avoid noisy signal value. In Frequency Hop, more than one bursting frequency (user configurable) is used. Refer QTouch Modular Library Userguide for more details on Frequency Hop.")
    execfile(Module.getPath() +"/config/freq_hop.py")
    enableFreqHopMenu.setDependencies(enableHopFiles,["ENABLE_FREQ_HOP"])

    # Enable Datastreamer  
    enableDataStreamerMenu = qtouchComponent.createBooleanSymbol("ENABLE_DATA_STREAMER", touchMenu)
    enableDataStreamerMenu.setLabel("Enable Data Visualizer")
    enableDataStreamerMenu.setDefaultValue(False)
    enableDataStreamerMenu.setDescription("The Data Visualizer allows touch sensor debug information to be relayed on the USART interface to Data Visualizer software tool. This setting should be enabled for initial sensor tuning and can be disabled later to avoid using USART and additionally save code memory. More information can be found in Microchip Developer Help page.")
    enableDataStreamerMenu.setDependencies(enableDataStreamerFtlFiles,["ENABLE_DATA_STREAMER"])
    execfile(Module.getPath() +"/config/datastreamer.py")

    # Enable 2D Surface Visualizer 
    enableSurfaceUtilityMenu = qtouchComponent.createBooleanSymbol("ENABLE_KRONOCOMM", touchMenu)
    enableSurfaceUtilityMenu.setLabel("Enable 2D Surface Utility")
    enableSurfaceUtilityMenu.setDefaultValue(False)
    enableSurfaceUtilityMenu.setDescription("The 2D Surface Utility allows touch sensor debug information to be relayed on the USART interface to 2D Surface Utility software tool. This setting should be enabled for evaluating gestures and touch performance in surface applications. More information can be found in Microchip Developer Help page.")
    enableSurfaceUtilityMenu.setDependencies(enable2DSurfaceFtlFiles,["ENABLE_KRONOCOMM"])
    execfile(Module.getPath() +"/config/Surface_2D_Utility.py")

    qtouchTimerComponent = qtouchComponent.createStringSymbol("TOUCH_TIMER_INSTANCE", None)
    qtouchTimerComponent.setLabel("Timer Component Chosen for Touch middleware")
    qtouchTimerComponent.setReadOnly(True)
    qtouchTimerComponent.setDefaultValue("")
    
    qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_INSTANCE", None)
    qtouchSercomComponent.setLabel("Sercom Component Chosen for Touch middleware")
    qtouchSercomComponent.setReadOnly(True)
    qtouchSercomComponent.setVisible(False)
    qtouchSercomComponent.setDefaultValue("")

    qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_KRONO_INSTANCE", None)
    qtouchSercomComponent.setLabel("Sercom Component Chosen for Touch middleware")
    qtouchSercomComponent.setReadOnly(True)
    qtouchSercomComponent.setVisible(False)
    qtouchSercomComponent.setDefaultValue("")
    
    #keep it as last displayed tree config
    touchWarning = qtouchComponent.createMenuSymbol("TOUCH_WARNING", None)
    touchWarning.setLabel("")
    touchWarning.setVisible(False)
    touchWarning.setDependencies(onWarning,["PTC_CLOCK_FREQ"])
############################################################################
#### Code Generation ####
############################################################################
    #configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER", None)
    touchHeaderFile.setSourcePath("/templates/touch.h.ftl")
    touchHeaderFile.setOutputName("touch.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(True)
    
    # Header File
    touchHeaderFile1 = qtouchComponent.createFileSymbol("TOUCH_HEADER1", None)
    touchHeaderFile1.setSourcePath("/templates/touch_api_ptc.h.ftl")
    touchHeaderFile1.setOutputName("touch_api_ptc.h")
    touchHeaderFile1.setDestPath("/touch/")
    touchHeaderFile1.setProjectPath("config/" + configName + "/touch/")
    touchHeaderFile1.setType("HEADER")
    touchHeaderFile1.setMarkup(True)    
    
    # Source File
    touchSourceFile = qtouchComponent.createFileSymbol("TOUCH_SOURCE", None)
    touchSourceFile.setSourcePath("/templates/touch.c.ftl")
    touchSourceFile.setOutputName("touch.c")
    touchSourceFile.setDestPath("/touch/")
    touchSourceFile.setProjectPath("config/" + configName +"/touch/")
    touchSourceFile.setType("SOURCE")
    touchSourceFile.setMarkup(True)

    #System Initialization
    ptcSystemInitFile = qtouchComponent.createFileSymbol("PTC_SYS_INIT", None)
    ptcSystemInitFile.setType("STRING")
    ptcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
    ptcSystemInitFile.setSourcePath("../touch/templates/system/initialization.c.ftl")
    ptcSystemInitFile.setMarkup(True)

    # System Definition
    ptcSystemDefFile = qtouchComponent.createFileSymbol("PTC_SYS_DEF", None)
    ptcSystemDefFile.setType("STRING")
    ptcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ptcSystemDefFile.setSourcePath("../touch/templates/system/definitions.h.ftl")
    ptcSystemDefFile.setMarkup(True)
    
   
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        
        ptcSystemDefFile.setDependencies(securefileUpdate, ["core.PTC_IS_NON_SECURE"])
        ptcSystemDefFile.setDependencies(securefileUpdate, ["core.NVIC_42_0_SECURITY_TYPE"])
        
        print("***********PTC secure Dependency is setup*************")

        qtouchFilesArray.append(ptcSystemDefFile)
        qtouchFilesArray.append(ptcSystemInitFile)
        qtouchFilesArray.append(touchSourceFile)
        qtouchFilesArray.append(touchHeaderFile)
        qtouchFilesArray.append(touchHeaderFile1)
        checknonsecureStatus()

    else:
        print("TE ERROR")

    qtouchComponent.addPlugin("../touch/plugin/ptc_manager_c21.jar")

def finalizeComponent(qtouchComponent):
    res = Database.activateComponents(autoComponentIDTable)
    res = Database.connectDependencies(autoConnectTable)