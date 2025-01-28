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
import sys

try:
	#try required for pydoc server
	sys.path.append(Module.getPath() + "config")
except (NameError):
	pass

import touch_target_device
import touch_interface
import touch_node_groups
import touch_boost_mode_groups
import touch_acquisition_groups
import touch_acquisition_sourcefiles
import touch_key_groups
import touch_key_sourcefiles
import touch_sensor_groups
import touch_scroller_groups
import touch_scroller_sourcefiles
import touch_surface
import touch_surface_sourcefiles
import touch_freq_hop_groups
import touch_freq_hop_sourcefiles
import touch_ds_groups
import touch_ds_sourcefiles
import touch_gesture
import touch_gesture_sourcefiles
import touch_lowpower
import touch_datastreamer
import touch_qtouch_sourcefiles
import touch_surface_2D_utility
import touch_custom_pic32mzda
import touch_pad
import touch_tune_with_plugin
import touchTrustZone

qtouchInst = {}

def onAttachmentConnected(source,target):
	"""Handler for peripheral assignment to touch module.
	MHC reference : <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-voidonAttachmentConnected(source,target)>
	Arguments:
		:source : the touch module
		:target : peripheral being connected 
	Returns:
		:none
	"""
	localComponent = source["component"]
	remoteComponent = target["component"]
	remoteID = remoteComponent.getID()
	connectID = source["id"]
	targetID = target["id"]
	targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()

	if (connectID == "Touch_timer"):
		plibUsed = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE")
		plibUsed.clearValue()
		plibUsed.setValue(remoteID.upper(), 1)
		if targetID == "RTC_TMR":
			if (Database.getSymbolValue(remoteID, "RTC_MODE0_MATCHCLR") == False):
				Database.setSymbolValue(remoteID, "RTC_MODE0_MATCHCLR", True)
			if (Database.getSymbolValue(remoteID, "RTC_COUNTSYNC_ENABLE") == True):
				Database.setSymbolValue(remoteID, "RTC_COUNTSYNC_ENABLE", False)
			if (Database.getSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE") == False):
				Database.setSymbolValue(remoteID, "RTC_MODE0_INTENSET_CMP0_ENABLE", True)
				Database.setSymbolValue(remoteID, "RTC_MODULE_SELECTION", 0)
				Database.setSymbolValue(remoteID, "RTC_MODE0_TIMER_COMPARE",long(1))
			if (targetDevice in ["SAME51","SAME53","SAME54","SAMD51"]):
				Database.setSymbolValue(remoteID, "RTC_MODE0_PRESCALER", 1)
				Database.setSymbolValue(remoteID, "RTC_MODE0_TIMER_COMPARE0",long(1))
		else:
			Database.setSymbolValue(remoteID, "TIMER_PRE_SCALER", 0)
			Database.setSymbolValue(remoteID, "TMR_INTERRUPT_MODE", True)
	if (connectID == "Touch_sercom"):
		plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE")
		plibUsed.clearValue()
		plibUsed.setValue(remoteID.upper(), 1)
		if (Database.getSymbolValue(remoteID, "USART_OPERATING_MODE") == 1):
			Database.setSymbolValue(remoteID, "USART_OPERATING_MODE", 0)
	if (connectID == "Touch_sercom_Krono"):
		plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE")
		plibUsed.clearValue()
		plibUsed.setValue(remoteID.upper(), 1)
		if (Database.getSymbolValue(remoteID, "USART_OPERATING_MODE") == 0):
			Database.setSymbolValue(remoteID, "USART_OPERATING_MODE", 1)

	if localComponent.getSymbolValue("TOUCH_PRE_GENERATE"):
		localComponent.setSymbolValue("TOUCH_PRE_GENERATE", False)
	localComponent.setSymbolValue("TOUCH_PRE_GENERATE", True)

def onAttachmentDisconnected(source, target):
	"""Handler for disconnect from touch module.
	MHC reference : <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-voidonAttachmentConnected(source,target)>
	Arguments:
		:source : the touch module
		:target : peripheral being connected 
	Returns:
		:none
	"""
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

	if localComponent.getSymbolValue("TOUCH_PRE_GENERATE"):
		localComponent.setSymbolValue("TOUCH_PRE_GENERATE", False)
	localComponent.setSymbolValue("TOUCH_PRE_GENERATE", True)

def destroyComponent(qtouchComponent):
	print "Destroy touch module"

def finalizeComponent(qtouchComponent):
	"""
	MHC reference :<http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-voidfinalizeComponent(component,[index])>
	Arguments:
		:qtouchComponent : newly created module see module.loadModule()
	Returns:
		:none
	"""
	autoComponentIDTable = []
	autoConnectTable = []
	if qtouchInst['interfaceInst'].getDeviceSeries() in qtouchInst['target_deviceInst'].picDevices:
		if qtouchInst['interfaceInst'].getDeviceSeries() in ["PIC32CXBZ31", "WBZ35","PIC32WM_BZ6"]:
			autoComponentIDTable[:] = ["adchs","rtc"]
			autoConnectTable[:] = [["lib_qtouch", "Touch_timer","rtc","RTC_TMR"],
									["lib_qtouch", "Acq_Engine","adchs","ADCHS_ADC"]]
		else:
			autoComponentIDTable[:] = ["adchs","tmr4"]
			autoConnectTable[:] = [["lib_qtouch", "Touch_timer","tmr4","TMR4_TMR"],
									["lib_qtouch", "Acq_Engine","adchs","ADCHS_ADC"]]
	else:
		if qtouchInst['interfaceInst'].getDeviceSeries() in qtouchInst['target_deviceInst'].adc_based_acquisition:
			autoComponentIDTable[:] = ["rtc","ptc","adc0"]
			autoConnectTable[:] = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"], ["lib_qtouch", "lib_acquire", "ptc", "ptc_Acq_Engine"], ["ptc", "lib_acquire", "adc0", "ADC0_ADC"]]
		else:
			autoComponentIDTable[:] = ["rtc","ptc"]
			autoConnectTable[:] = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"], ["lib_qtouch", "lib_acquire", "ptc", "ptc_Acq_Engine"]]
	InterruptVector = "PTC" + "_INTERRUPT_ENABLE"
	InterruptHandler = "PTC" + "_INTERRUPT_HANDLER"
	print(autoComponentIDTable)
	print(autoConnectTable)
	res = Database.activateComponents(autoComponentIDTable)
	res = Database.connectDependencies(autoConnectTable)

def activateOcmpAndConfigure(ocmp):
	Database.activateComponents([ocmp])
	Database.setSymbolValue(ocmp, "OCMP_OCxCON_OCM", 6)

def onPic32mzdaChange(symbol, event):
	print("entering onPic32mzdaChange")
	localComponent = symbol.getComponent()
	currentActive =  Database.getActiveComponentIDs()
	print currentActive
	print symbol.getID()
	print symbol.getValue()
	print qtouchInst['customInst'].getCurrentOCMPChannel()
	print qtouchInst['customInst'].getCurrentTMRChannel()

	if symbol.getID() == "TOUCH_PIC32MZDA_DMA":
		if qtouchInst['customInst'].getCurrentDmaChannel != "":
			tempstr = qtouchInst['customInst'].getCurrentDmaChannel()
			setSym = "DMAC_CHAN"+tempstr+"_ENBL"
			Database.clearSymbolValue("core",setSym)
			setSym = "DMAC_REQUEST_"+tempstr+"_SOURCE"
			Database.clearSymbolValue("core",setSym)

		setSym = "DMAC_CHAN"+str(symbol.getValue())+"_ENBL"
		Database.setSymbolValue("core",setSym, True)
		setSym = "DMAC_REQUEST_"+str(symbol.getValue())+"_SOURCE"
		Database.setSymbolValue("core",setSym, "ADC_DC1")
		qtouchInst['customInst'].setCurrentDmaChannel(str(symbol.getValue()))
	
	elif symbol.getID() == "TOUCH_DRIVEN_SHIELD_ENABLE":
		setSym = localComponent.getSymbolByID("TOUCH_DS_COMP")
		setSymTmr = localComponent.getSymbolByID("TOUCH_DS_TMR")
		if symbol.getValue() == True:
			if qtouchInst['customInst'].getCurrentOCMPChannel() == "":
				# first itme driven shield is enabled
				setSym.setVisible(True)
				setSymTmr.setVisible(True)
				for cnt in range(setSym.getKeyCount()):
					compValue = setSym.getKeyValue(cnt)
					if compValue.lower() not in currentActive:
						setSym.setValue(cnt)
						qtouchInst['customInst'].setCurrentOCMPChannel(compValue.lower())
						Database.activateComponents([compValue.lower()])
						Database.setSymbolValue(compValue.lower(), "OCMP_OCxCON_OCM", 6)
						break
		else:
			Database.deactivateComponents([qtouchInst['customInst'].getCurrentOCMPChannel()])
			qtouchInst['customInst'].setCurrentOCMPChannel("")
			setSym.setVisible(False)
			setSymTmr.setVisible(False)
	elif symbol.getID() == "TOUCH_DS_COMP":
		ocmp = symbol.getValue()
		ocmp = symbol.getKeyValue(ocmp).lower()
		if ocmp not in currentActive:
			Database.activateComponents([ocmp])
		Database.setSymbolValue(ocmp, "OCMP_OCxCON_OCM", 6)
		if qtouchInst['customInst'].getCurrentOCMPChannel() in currentActive:
			if ocmp != qtouchInst['customInst'].getCurrentOCMPChannel():
				Database.deactivateComponents([qtouchInst['customInst'].getCurrentOCMPChannel()])
		qtouchInst['customInst'].setCurrentOCMPChannel(ocmp)

def applyDrivenShieldTimers(symbol, event):
	"""apply driven shield timers. Triggered by Driven shield plus application.
	Arguments:
		:symbol : the symbol that triggered the callback
		:event : the new value. 
	Returns:
		:none
	"""	
	# print("---------Entering apply DSTimers----------")
	component = symbol.getComponent()
	toRemove = []
	toAdd = []
	toConnect = []
	tIndex = 0
	toremove = []
	toadd = []
	
	applyTimers = symbol.getValue().split(">")
	if len(applyTimers[0].strip("]["))!=0:
		toremove = applyTimers[0].strip("][").split(", ")
	if len(applyTimers[1].strip("]["))!=0:
		toadd = applyTimers[1].strip("][").split(", ")
	
	for timer in toremove:
		toRemove.append(timer.lower())
		component.setDependencyEnabled("Drivenshield_"+timer, False)
	for timer in toadd:
		toAdd.append(timer.lower())
		if "TCC" not in timer:
			toConnect.append(["lib_qtouch", "Drivenshield_"+timer,timer.lower(), timer+"_TMR"])
		else:
			toConnect.append(["lib_qtouch", "Drivenshield_"+timer,timer.lower(), timer+"_PWM"])
		component.setDependencyEnabled("Drivenshield_"+timer, True)
	
	if len(toRemove)!=0:
		Database.deactivateComponents(toRemove)
	if len(toAdd)!=0:
		Database.activateComponents(toAdd)
		if len(toConnect)!=0:
			Database.connectDependencies(toConnect)
		sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
		sevent.setValue("dstimer")
		#sevent.setValue("")
	# print("---------Leaving apply DSTimers----------")

def libChangeBoostMode(symbol,event):
	localcomponent = symbol.getComponent()
	touchAcqLibraryFile = localcomponent.getSymbolByID("TOUCH_ACQ_LIB")
	touchAcqHeaderFile = localcomponent.getSymbolByID("TOUCH_ACQ_HEADER")
	touchAcq4pLibraryFile = localcomponent.getSymbolByID("TOUCH_ACQ_4P_LIB")
	touchAcq4pHeaderFile = localcomponent.getSymbolByID("TOUCH_ACQ_4P_HEADER")

	if(event["value"] == False):
		touchAcqLibraryFile.setEnabled(True)
		touchAcqHeaderFile.setEnabled(True)
		touchAcq4pLibraryFile.setEnabled(False)
		touchAcq4pHeaderFile.setEnabled(False)
	else:
		touchAcqLibraryFile.setEnabled(False)
		touchAcqHeaderFile.setEnabled(False)
		touchAcq4pLibraryFile.setEnabled(True)
		touchAcq4pHeaderFile.setEnabled(True)

	updateParameters(symbol, event)

def qtouchSetDependencies(symbol, func, dependency):
	for i, sym in enumerate(symbol):
		#print sym,func,dependency
		if(func[i] == "applyDrivenShieldTimers"):
			sym.setDependencies(applyDrivenShieldTimers,dependency[i])
		elif(func[i] == "onPTCClock"):
			sym.setDependencies(onPTCClock, dependency[i])
		elif(func[i] == "onPic32mzdaChange"):
			sym.setDependencies(onPic32mzdaChange, dependency[i])
		elif(func[i] == "updatePinsSettings"):
			sym.setDependencies(updatePinsSettings, dependency[i])
		elif(func[i] == "updateParameter"):
			sym.setDependencies(updateParameters, dependency[i])
		elif(func[i] == "enablePM"):
			sym.setDependencies(enablePM, dependency[i])
		elif(func[i] == "libChangeBoostMode"):
			sym.setDependencies(libChangeBoostMode, dependency[i])
		elif(func[i] == "securefileUpdate"):
			sym.setDependencies(securefileUpdate, dependency[i])
		elif(func[i] == "onGenerate"):
			sym.setDependencies(onGenerate, dependency[i])

def securefileUpdate(symbol,event):
	print "securefileUpdate"
	component = symbol.getComponent()
	device = component.getSymbolByID("DEVICE_NAME").getValue()
	if qtouchInst['target_deviceInst'].isSecureDevice(device):
		nvicid = qtouchInst['target_deviceInst'].getSecureNVICID(device)
		secureStatus = ""
		if (Database.getSymbolValue("core", "PTC_IS_NON_SECURE") == False):
			secureStatus = "SECURE"
			Database.setSymbolValue("core",nvicid, 0)
		else:
			secureStatus = "NON_SECURE"
			Database.setSymbolValue("core",nvicid, 1)
		qtouchInst['trustZoneInst'].checknonsecureStatus(component,secureStatus)

def processLump(symbol, event, targetDevice):
	"""Handler for lump mode support menu click event. 
	Triggers updates for touch sub modules including : lumpmode, surface, drivenshield
	Arguments:
		:symbol : the symbol that triggered the event
		:event : new value of the symbol 
	Returns:
		:none
	"""
	localComponent = symbol.getComponent()
	touchSenseTechnology = localComponent.getSymbolByID("SENSE_TECHNOLOGY").getSelectedKey()
	totalChannelCount = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
	lumpSupported = qtouchInst['target_deviceInst'].getLumpSupported(targetDevice)
	shieldMode = qtouchInst['target_deviceInst'].getShieldMode(targetDevice)
	surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()

	if(totalChannelCount == 0):
		return

	if (lumpSupported ==  True):
		lumpSymbol = localComponent.getSymbolByID("LUMP_CONFIG")
		lumpFeature = localComponent.getSymbolByID("LUMP_CONFIG").getValue()

		print("lump is supported")
		print(lumpFeature)
		if(lumpFeature !=""):
			print("lump is not empty")
			qtouchInst['node_groupInst'].updateLumpMode(lumpSymbol,touchSenseTechnology)

		if(shieldMode == "hardware" and (touchSenseTechnology == "SelfCapShield")):
			print("shield is hardware")
			qtouchInst['ds_groupInst'].updateLumpModeDrivenShield(qtouchInst,symbol,event,totalChannelCount,lumpSymbol)

		if (surfaceEnabled == True):
			qtouchInst['surfaceInst'].updateLumpModeSurface(symbol,touchSenseTechnology,totalChannelCount)

def updateParameters(symbol, event):
	# parameter update is required only for boost mode.
	# For non-boost mode, parameters are taken direclty from symbol values.
	localComponent = symbol.getComponent()
	targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()

	if qtouchInst['boostModeInst'].getBoostSupported(targetDevice):
		boostModeEnabled = localComponent.getSymbolByID("ENABLE_BOOST").getValue()
		if boostModeEnabled:
			nodeCount = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
			print("Entering ProcessBoostmode to updateParameters")
			qtouchInst['boostModeInst'].processBoostMode(symbol,event,targetDevice,nodeCount)

def updatePinsSettings(symbol,event):
	localComponent = symbol.getComponent()
	targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()
	if targetDevice not in ["PIC32MZW", "PIC32MZDA", "PIC32CXBZ31", "WBZ35","PIC32WM_BZ6"]:
		touchPads = qtouchInst['padsInfo'].getTouchPads()
		touchModule = qtouchInst['padsInfo'].getTouchModule()
		#print touchModule
		#print touchPads
		component = symbol.getComponent()
		#clear setting
		for pad in touchPads:
			setting = touchPads[pad]
			value = Database.getSymbolValue("core", "PIN_"+setting["index"]+"_FUNCTION_TYPE")
			Database.setSymbolValue("core", "PIN_"+setting["index"]+"_FUNCTION_TYPE", "")
		activePds = set()
		count = component.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
		for i in range(count):
			if "SELF" in symbol.getID():
				signalSymbol = component.getSymbolByID("SELFCAP-INPUT_"+str(i))
				if signalSymbol.getValue() != -1:
					padDesc = signalSymbol.getKeyDescription(signalSymbol.getValue())
					padName = padDesc[padDesc.index("(")+1:padDesc.index(")")]
				activePds.add(padName)
			if "MUTL" in symbol.getID():
				signalSymbol = component.getSymbolByID("MUTL-X-INPUT_"+str(i))
				if signalSymbol.getValue() != -1:
					padDesc = signalSymbol.getKeyDescription(signalSymbol.getValue())
					padName = padDesc[padDesc.index("(")+1:padDesc.index(")")]
					activePds.add(padName)
					signalSymbol = component.getSymbolByID("MUTL-Y-INPUT_"+str(i))
				if signalSymbol.getValue() != -1:
					padDesc = signalSymbol.getKeyDescription(signalSymbol.getValue())
					padName = padDesc[padDesc.index("(")+1:padDesc.index(")")]
					activePds.add(padName)
		for pad in activePds:
			setting = touchPads[pad]
			Database.setSymbolValue("core", "PIN_"+setting["index"]+"_FUNCTION_TYPE", setting["function"])

	updateParameters(symbol, event)
	onGenerate(symbol, event)

def useSysTimeEvent(symbol,event):
	localComponent = symbol.getComponent()
	localComponent.setDependencyEnabled("SW_Timer", event['value'])
	warning = localComponent.getSymbolByID("SYS_TIME_WARNING")
	# tmrInstance = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE")
	if event['value'] is True:
		# tmrInstance.clearValue()
		localComponent.setDependencyEnabled("Touch_timer", False)
		warning.setVisible(True)
	else:
		localComponent.setDependencyEnabled("Touch_timer", True)
		warning.setVisible(False)


def onGenerate(symbol,event):
	"""Handler for generate code menu click event. 
	Triggers updates for touch sub modules, lump,surface,lowpower,boostmode
	Arguments:
		:symbol : the symbol that triggered the event
		:event : new value of the symbol 
	Returns:
		:none
	""" 
	if event['value'] is False:
		return


	localComponent = symbol.getComponent()
	touchSenseTechnology = localComponent.getSymbolByID("SENSE_TECHNOLOGY").getSelectedKey()
	targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()
	surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
	nodeCount = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
	sercom = localComponent.getSymbolByID("TOUCH_SERCOM_INSTANCE").getValue()
	timer = localComponent.getSymbolByID("TOUCH_TIMER_INSTANCE").getValue()
	if targetDevice in ["PIC32CZCA80","PIC32CZCA90","PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01","PIC32CMGC00","PIC32CMSG00"]:
		ptcClockFrequencyDefault =  Database.getSymbolValue("core", "PTC_CLOCK_FREQUENCY")
		localComponent.getSymbolByID("GET_PTC_CLOCK_FREQUENCY").setValue(ptcClockFrequencyDefault)

	if int(nodeCount) == 0:
		Log.writeErrorMessage("Touch Error: Number of sensor is ZERO")
	if sercom == "":
		dv = localComponent.getSymbolByID("ENABLE_DATA_STREAMER").getValue()
		krono = localComponent.getSymbolByID("ENABLE_KRONOCOMM").getValue()
		if krono or dv:
			Log.writeErrorMessage("Touch Error: UART not connected")
	if timer == "":
		Log.writeErrorMessage("Touch Error: TIMER not connected")

	# print "Symbol is :", symbol
	# print "Symbol value is :", symbol.getValue()

	if int(nodeCount) == 0:
		return

	getXYinfo(localComponent)

	if touchSenseTechnology == "MutualCap":
		if qtouchInst['boostModeInst'].getBoostSupported(targetDevice):
			print("Entering ProcessBoostmode")
			qtouchInst['boostModeInst'].processBoostMode(symbol,event,targetDevice,nodeCount)
			# qtouchprocessBoostMode(symbol,event,targetDevice,nodeCount)

	if targetDevice not in qtouchInst['target_deviceInst'].non_lump_support:
		# lump is processed if in "ProcessBoostmode" if boost mode is enabled
		if qtouchInst['boostModeInst'].getBoostSupported(targetDevice):
			if not localComponent.getSymbolByID("ENABLE_BOOST").getValue():
				print("Entering ProcessLump boost mode = False")
				processLump(symbol,event,targetDevice)
		else:
			print("Entering ProcessLump No boost mode")
			processLump(symbol,event,targetDevice)
	elif qtouchInst['target_deviceInst'].getShieldMode(targetDevice) == "hardware":
		localComponent = symbol.getComponent()
		touchSenseTechnology = localComponent.getSymbolByID("SENSE_TECHNOLOGY").getSelectedKey()
		totalChannelCount = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()

		if(touchSenseTechnology == "SelfCapShield"):
			qtouchInst['ds_groupInst'].updateLumpModeDrivenShieldNoLump(qtouchInst,symbol,event,totalChannelCount)


	# if(surfaceEnabled ==True):
	# 	print("Entering surface_rearrange")
	# 	qtouchInst['surfaceInst'].surface_rearrange(symbol, event)
	
	if (qtouchInst['lowpowerInst'].lowPowerSupported(targetDevice)):
		qtouchInst['lowpowerInst'].processSoftwareLP(symbol,event)

def enablePM(symbol,event):
		"""Event Handler enabling low power mode, updates pm and supc as required by targetDevice
		Arguments:
			:symbol : the symbol that triggered the callback
			:event : the new value. 
		Returns:
			:none
		"""
		localComponent = symbol.getComponent()
		targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()
		lowPowerKey = localComponent.getSymbolByID("LOW_POWER_KEYS").getValue()
		pmComponentID = ["pm"]
		supcComponentID = ["supc"]
		if(targetDevice in ["PIC32CZCA80","PIC32CZCA90"]):
			Database.activateComponents(supcComponentID)
		if(lowPowerKey != ""):
			Database.activateComponents(pmComponentID)
			if (targetDevice in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
				Database.activateComponents(supcComponentID)
		else:
			if(targetDevice in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
				Database.deactivateComponents(supcComponentID)
			if(targetDevice not in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
				Database.deactivateComponents(pmComponentID)

def onPTCClock(symbol,event):
	"""Handler for setGCLKconfig gclkID frequency
	Arguments:
		:symbol : the symbol that triggered the callback
		:event : the new value. 
	Returns:
		:none
	"""

	print "calling onPTCClock function"
	component = symbol.getComponent()
	if component.getSymbolValue("TOUCH_LOADED"):
		frequency = event['symbol'].getValue()
		channels = component.getSymbolValue("TOUCH_CHAN_ENABLE_CNT")
		prescaler = component.getSymbolByID("DEF_NOD_PTC_PRESCALER0") 
		if frequency > 0 and channels > 0 and prescaler != None:   
			symbol.setValue(symbol.getDefaultValue()+":sync")
			sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
			sevent.setValue("ptcclock")
			#sevent.setValue("")
			
			
			
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

def getXYinfo(localComponent):

	touchtech = localComponent.getSymbolByID("SENSE_TECHNOLOGY").getSelectedKey()
	totalChannelCount = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
	tchSelfPinSelection = qtouchInst['node_groupInst'].getTchSelfPinSelection()
	tchMutXPinSelection = qtouchInst['node_groupInst'].getTchMutXPinSelection()
	tchMutYPinSelection = qtouchInst['node_groupInst'].getTchMutYPinSelection()
	
	xLumpList = []
	yLumpList = []

	for lmp in range(0,totalChannelCount):
		# print("lmp", lmp, totalChannelCount)
		if ((touchtech == "SelfCap") or (touchtech == "SelfCapShield")):
			val = tchSelfPinSelection[int(lmp)].getValue()
			yCh = tchSelfPinSelection[int(lmp)].getKeyValue(val)
			xLumpList.append("X_NONE")
			yLumpList.append(yCh)
		elif (touchtech == "MutualCap"):
			val1 = tchMutXPinSelection[int(lmp)].getValue()
			xCh = tchMutXPinSelection[int(lmp)].getKeyValue(val1)
			val2 = tchMutYPinSelection[int(lmp)].getValue()
			yCh = tchMutYPinSelection[int(lmp)].getKeyValue(val2)
			xLumpList.append(xCh)
			yLumpList.append(yCh)

	temp = ",".join(xLumpList)
	localComponent.getSymbolByID("FTL_X_INFO").setValue(temp)
	temp = ",".join(yLumpList)
	localComponent.getSymbolByID("FTL_Y_INFO").setValue(temp)

def instantiateComponent(qtouchComponent):
	# import sys;sys.path.append(r'C:\Programs\eclipse\plugins\org.python.pydev.core_8.3.0.202104101217\pysrc')
	# #import sys;sys.path.append(r'C:/Programs/Python/Python39/Scripts')
	# import pydevd;pydevd.settrace()
	"""Start Point for instantiation of the touch Module. 
	MHC reference : <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-voidinstantiateComponent(component,[index])>
	Builds and populates tree view menu in MHC. 
	Determines target device and capabilities. 
	Configures all required submodules. 
	Triggers updates for touch sub modules with multiple groups:
		node, sensor, key, scroller, frequency hop, boost mode, driven shield
	Arguments:
		:qtouchComponent : newly created touchModule see module.loadModule()
	Returns:
		:none
	"""
	print ("Entering initialise")
	# import sys;sys.path.append(r'C:\Users\i70418\Downloads\eclipse-java-2020-12-R-win32-x86_64\eclipse\plugins\org.python.pydev.core_8.2.0.202102211157\pysrc')
	# import pydevd;pydevd.settrace()
	showConfiguration = False
	configName = Variables.get("__CONFIGURATION_NAME")

	touchConfigurator = qtouchComponent.createMenuSymbol("TOUCH_CONFIGURATOR", None)
	touchConfigurator.setLabel("Select Project Graph -> Plugins > Touch Configuration")
	
	touchMenu = qtouchComponent.createMenuSymbol("TOUCH_MENU", None)
	touchMenu.setLabel("Touch Configuration")
	touchMenu.setVisible(showConfiguration)

	touchInfoMenu = qtouchComponent.createMenuSymbol("TOUCH_INFO", None)
	touchInfoMenu.setLabel("Touch Configuration Helper")
	touchInfoMenu.setVisible(showConfiguration)

	touchConfigMenu = qtouchComponent.createMenuSymbol("TOUCH_EXPERIMENTAL_FEATURES", None)
	touchConfigMenu.setLabel("Touch Experimental Features")
	touchConfigMenu.setVisible(True)

	useSysTime = qtouchComponent.createBooleanSymbol("USE_SYS_TIME", touchConfigMenu)
	useSysTime.setLabel("Use SYS_TIME")
	useSysTime.setDefaultValue(False)
	useSysTime.setDependencies(useSysTimeEvent,["USE_SYS_TIME"])

	sysTimeWarning= qtouchComponent.createMenuSymbol("SYS_TIME_WARNING", touchConfigMenu)
	sysTimeWarning.setLabel("Using SYS TIME may not work with low-power Feature")
	sysTimeWarning.setVisible(False)
	
	touchScriptEvent = qtouchComponent.createStringSymbol("TOUCH_SCRIPT_EVENT", touchInfoMenu)
	touchScriptEvent.setLabel("Script Event ")
	touchScriptEvent.setReadOnly(True)

	enableGenerate = qtouchComponent.createBooleanSymbol("TOUCH_PRE_GENERATE", touchInfoMenu)
	enableGenerate.setLabel("Generate Project")
	enableGenerate.setDefaultValue(False)
	enableGenerate.setDependencies(onGenerate,["TOUCH_PRE_GENERATE"])

	enableLoaded = qtouchComponent.createBooleanSymbol("TOUCH_LOADED", touchInfoMenu)
	enableLoaded.setLabel("Project Loaded")
	enableLoaded.setDefaultValue(False)

	dmaInfo = qtouchComponent.createMenuSymbol("DMA_INFO", touchInfoMenu)
	dmaInfo.setLabel("DMA Info")

	dmaChannelsCount = qtouchComponent.createIntegerSymbol("DMA_CHANNEL_COUNT", dmaInfo)
	dmaChannelsCount.setLabel("Channels count ")
	dmaChannelsCount.setReadOnly(True)

	channelCountNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMAC\"]/instance/parameters/param@[name=\"CH_NUM\"]")
	if channelCountNode != None:
		dmaChannelsCount.setDefaultValue(int(channelCountNode.getAttribute("value")))

	#create evsys group
	evsysInfo = qtouchComponent.createMenuSymbol("EVSYS_INFO", touchInfoMenu)
	evsysInfo.setLabel("EVSYS Info")

	evsysChannelsCount = qtouchComponent.createIntegerSymbol("EVSYS_CHANNEL_COUNT", evsysInfo)
	evsysChannelsCount.setLabel("Channels count ")
	evsysChannelsCount.setReadOnly(True)

	channelCountNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EVSYS\"]/instance/parameters/param@[name=\"CHANNELS\"]")
	if channelCountNode != None:
		evsysChannelsCount.setDefaultValue(int(channelCountNode.getAttribute("value")))

	interfaceInst = touch_interface.classTouchInterface()
	qtouchInst['interfaceInst'] = interfaceInst
	interfaceInst.getTargetDeviceInfo(ATDF,qtouchComponent,touchMenu)
	device = interfaceInst.getDeviceSeries()
	deviceFullName = interfaceInst.getDeviceName()

	print(interfaceInst.getDeviceSeries())

	if device in ["PIC32MZDA","PIC32MZW"]:
		customInst = touch_custom_pic32mzda.classTouchCustAddition()
		customInst.initCustomMenu(ATDF,device, qtouchComponent, None, Database)
		qtouchInst['customInst'] = customInst

	target_deviceInst = touch_target_device.classTouchTargetDevice()
	target_deviceInst.initTargetParameters(qtouchComponent,touchMenu,device,Database)
	qtouchInst['target_deviceInst'] = target_deviceInst

	if device not in target_deviceInst.picDevices:
	# Interrupts
		ptcInterruptConfig = qtouchComponent.createIntegerSymbol("DEF_PTC_INTERRUPT_PRIORITY", touchMenu)
		ptcInterruptConfig.setLabel("PTC Interrupt Priority")
		ptcInterruptMin = target_deviceInst.getMinInterrupt(device)
		ptcInterruptConfig.setMin(ptcInterruptMin)
		ptcInterruptMax = target_deviceInst.getMaxInterrupt(device)
		ptcInterruptConfig.setMax(ptcInterruptMax)
		ptcInterruptDefault= target_deviceInst.getDefaultInterrupt(device)
		ptcInterruptConfig.setDefaultValue(ptcInterruptDefault)
		ptcInterruptConfig.setDescription("Defines the interrupt priority for the PTC. Set low priority to PTC interrupt for applications having interrupt time constraints.")
	
	node_groupInst = touch_node_groups.classTouchNodeGroups()
	qtouchInst['node_groupInst'] = node_groupInst
	# Lump support
	lumpSupported = target_deviceInst.getLumpSupported(device)
	if (lumpSupported == True):
		lumpSymbol = qtouchComponent.createStringSymbol("LUMP_CONFIG", touchMenu)
		lumpSymbol.setLabel("Lump Configuration")
		lumpSymbol.setDefaultValue("")
		# lumpSymbol.setDependencies(onGenerate,["LUMP_CONFIG"])
		lumpSymbol.setVisible(True)
		
	xInforSymbol = qtouchComponent.createStringSymbol("FTL_X_INFO", touchMenu)
	xInforSymbol.setLabel("Comma separated Lump X configuration per node")
	xInforSymbol.setDefaultValue("FTL_X_INFO")
	xInforSymbol.setVisible(True)
	
	yInofrSymbol = qtouchComponent.createStringSymbol("FTL_Y_INFO", touchMenu)
	yInofrSymbol.setLabel("Comma separated Lump Y configuration per node")
	yInofrSymbol.setDefaultValue("FTL_Y_INFO")
	yInofrSymbol.setVisible(True)
	
	# PinValues
	ptcPinValues = target_deviceInst.setDevicePinValues(ATDF,True,lumpSupported,device,deviceFullName)
	print target_deviceInst.getSelfCount()
	print target_deviceInst.getMutualCount()
	print ptcPinValues
	# Channel Limits
	touchChannelSelf = target_deviceInst.getSelfCount()
	touchChannelMutual = target_deviceInst.getMutualCount()
	# clocksetup 
	target_deviceInst.setGCLKconfig(qtouchComponent,ATDF,touchInfoMenu,device)
	# CSD support
	csdMode = target_deviceInst.getCSDMode(device)
	csdDefaultValue = target_deviceInst.getDefaultCSDValue(device)
	# Rsel support
	rSelMode = target_deviceInst.getRSelMode(device)
	# Driven shield support
	shieldMode = target_deviceInst.getShieldMode(device)
	autoTuneCSDDisableGetValue = target_deviceInst.getAutotuneCSDDisabled(device)
	autoTuneCSDDisable = qtouchComponent.createBooleanSymbol("DISABLE_AUTOTUNE_CSD", touchMenu)
	autoTuneCSDDisable.setLabel("Disable AutotuneCSD feature")
	if (autoTuneCSDDisableGetValue == 1):
		autoTuneCSDDisable.setValue(True)
	else:
		autoTuneCSDDisable.setValue(False)

	if device in ["PIC32CZCA80","PIC32CZCA90","PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01","PIC32CMGC00","PIC32CMSG00"]:
		ptcClockFrequency = qtouchComponent.createIntegerSymbol("GET_PTC_CLOCK_FREQUENCY", touchMenu)
		ptcClockFrequency.setLabel("Get PTC Clock Frequency")
		ptcClockFrequencyDefault =  Database.getSymbolValue("core", "PTC_CLOCK_FREQUENCY")
		ptcClockFrequency.setDefaultValue(ptcClockFrequencyDefault)
	
	if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
		useTrustZone = True
		touchTruzoneWarning = qtouchComponent.createMenuSymbol("TOUCH_TRUSTZONE", None)
		touchTruzoneWarning.setLabel("Set \"Secure\" project as \"Main Project\" in MPBABx before configuring Touch")
		Log.writeWarningMessage("Set \"Secure\" project as \"Main Project\" in MPBABx before configuring Touch!!!")
	else:
		useTrustZone = False

	if device not in target_deviceInst.picDevices:
		padsInfo = touch_pad.classTouchPads()
		padsInfo.collectPadInfo(ATDF)
		qtouchInst['padsInfo'] = padsInfo

	acquisition_groupsInst = touch_acquisition_groups.classTouchAcquisitionGroups()
	#Self Mutual Related if not required then setMaxGroups(1)
	acquisition_groupsInst.setMaxGroups(1) # Specifies the max number of acquisitions groups
	acquisitionGroupCountMenu = qtouchComponent.createIntegerSymbol("NUM_ACQUISITION_GROUPS", touchMenu)
	acquisitionGroupCountMenu.setDefaultValue(1)
	acquisitionGroupCountMenu.setMin(1)
	acquisitionGroupCountMenu.setMax(acquisition_groupsInst.getMaxGroups()) # taken from acquisition_groups.py variable
	acquisitionGroupCountMenu.setDependencies(acquisition_groupsInst.updateAcquisitionGroups,["NUM_ACQUISITION_GROUPS"])
	acquisitionGroupCountMenu.setLabel("Number of Acquisition Groups")
	if(acquisition_groupsInst.getMaxGroups()>1):
		acquisitionGroupCountMenu.setVisible(True)
	else:
		acquisitionGroupCountMenu.setVisible(False)
	
	#groups limits defined by the acquisition group limit
	minGroupCount = acquisitionGroupCountMenu.getMin()
	maxGroupCount = acquisitionGroupCountMenu.getMax()

	projectFilesList = []

	# ----Acquisition----
	acq_filesInst = touch_acquisition_sourcefiles.classTouchAcquisitionSourceFiles()
	projectFilesList = projectFilesList + acq_filesInst.setAcquisitionFiles(configName, qtouchComponent, device,useTrustZone)
	print(projectFilesList)
	acquisition_groupsInst.initAcquisitionGroup(
		qtouchComponent, 
		touchMenu, 
		minGroupCount,
		maxGroupCount,
		touchChannelSelf,
		touchChannelMutual,
		device,
		csdMode,
		shieldMode)

	# ----Node----
	node_groupInst.initNodeGroup(qtouchInst,
		qtouchComponent,
		touchMenu,
		minGroupCount,
		maxGroupCount,
		touchChannelSelf,
		touchChannelMutual,
		ptcPinValues,
		csdMode,
		csdDefaultValue,
		rSelMode)
	qtouchInst['node_groupInst'] = node_groupInst
	symbol,func,depen = node_groupInst.getDepDetails()
	qtouchSetDependencies(symbol, func, depen)

	# ----Keys----
	key_groupInst = touch_key_groups.classTouchKeyGroups()
	key_fileInst = touch_key_sourcefiles.classTouchKeySourceFiles()
	key_groupInst.initKeyGroup(
		qtouchComponent, 
		touchMenu, 
		minGroupCount,
		maxGroupCount,
		touchChannelSelf,
		touchChannelMutual)
	projectFilesList = projectFilesList + key_fileInst.setKeysFiles(configName, qtouchComponent, device,useTrustZone)
	qtouchInst['key_groupInst'] = key_groupInst
	# ----Sensor----
	sensorInst = touch_sensor_groups.classTouchSensorGroups()
	sensorInst.initSensorGroup(
		qtouchComponent, 
		touchMenu, 
		minGroupCount,
		maxGroupCount)
	qtouchInst['sensorInst'] = sensorInst
	# ----Scroller----
	scroller_groupInst = touch_scroller_groups.classTouchScrollerGroups()
	scroller_fileInst = touch_scroller_sourcefiles.classTouchScrollerSourceFiles()
	projectFilesList = projectFilesList + scroller_fileInst.setScrollerFiles(configName, qtouchComponent, device,useTrustZone)
	scroller_groupInst.initScrollerGroup(
		qtouchComponent,
		touchMenu,
		minGroupCount,
		maxGroupCount,
		touchChannelSelf,
		touchChannelMutual)
	qtouchInst['scroller_groupInst'] = scroller_groupInst

	# ----Frequency Hop----
	freqhop_groupInst = touch_freq_hop_groups.classTouchFreqGroups()
	freqhop_fileInst = touch_freq_hop_sourcefiles.classTouchFreqSourceFiles()
	projectFilesList = projectFilesList + freqhop_fileInst.setFreqHopFiles(configName, qtouchComponent, device,useTrustZone)
	freqhop_groupInst.initFreqHopGroup(
		qtouchComponent,
		touchMenu,
		minGroupCount,
		maxGroupCount,
		device)
	qtouchInst['freqhop_groupInst'] = freqhop_groupInst

	# ----Driven Shield----
	if (shieldMode != "none"):
		ds_groupInst = touch_ds_groups.classTouchDSGroup(node_groupInst, target_deviceInst)
		ds_fileInst = touch_ds_sourcefiles.classTouchDSFiles()
		projectFilesList = projectFilesList + ds_fileInst.setDrivenShieldFiles(configName, qtouchComponent,useTrustZone)
		ds_groupInst.initDrivenShieldGroup(qtouchInst,
			ATDF,
			qtouchComponent,
			touchMenu,
			touchInfoMenu,
			minGroupCount,
			maxGroupCount,
			touchChannelMutual,
			ptcPinValues,
			shieldMode)
		qtouchInst['ds_groupInst'] = ds_groupInst
		symbol,func,depen = ds_groupInst.getDepDetails()
		qtouchSetDependencies(symbol, func, depen)

	# ----Boost Mode----
	# Boost mode support
	boostModeInst = touch_boost_mode_groups.classTouchBoostModeGroups()
	boostMode = boostModeInst.getBoostSupported(device)
	if(boostMode == True):
		boostModeInst.initBoostModeGroup(
			configName, 
			qtouchComponent, 
			touchMenu,
			minGroupCount,
			maxGroupCount,
			device,
			useTrustZone)
	qtouchInst['boostModeInst'] = boostModeInst
	symbol,func,depen = boostModeInst.getDepDetails()
	qtouchSetDependencies(symbol, func, depen)

	# ----Surface----
	surfaceInst = touch_surface.classTouchSurface(node_groupInst)
	surfaceInst.initSurfaceInstance(
		qtouchComponent, 
		touchMenu, 
		device, 
		touchChannelMutual)
	surface_fileInst = touch_surface_sourcefiles.classTouchSurfaceFiles()
	projectFilesList = projectFilesList + surface_fileInst.setSurfaceFiles(configName,qtouchComponent, device,useTrustZone)
	qtouchInst['surfaceInst'] = surfaceInst



	# ----Gesture----
	gestureInst = touch_gesture.classTouchGesture()
	gestureInst.initGestureInstance(qtouchComponent, touchMenu)
	gesture_fileInst = touch_gesture_sourcefiles.classTouchGestureSourceFiles()
	projectFilesList = projectFilesList + gesture_fileInst.setGestureFiles(configName, qtouchComponent, device,useTrustZone)
	qtouchInst['gestureInst'] = gestureInst

	#----Low power----
	lowpowerInst = touch_lowpower.classTouchLP()
	if (lowpowerInst.lowPowerSupported(device)):
		lowpowerInst.initLowPowerInstance(qtouchComponent, touchMenu, device)
	qtouchInst['lowpowerInst'] = lowpowerInst
	symbol,func,depen = lowpowerInst.getDepDetails()
	qtouchSetDependencies(symbol, func, depen)

	tuneMenu = qtouchComponent.createMenuSymbol("TUNE_MENU", touchMenu)
	tuneMenu.setLabel("Touch Debug Configuration")
	tuneMenu.setVisible(showConfiguration)

	# ----Datastreamer----
	datastreamerInst = touch_datastreamer.classTouchDataStreamer()
	projectFilesList = projectFilesList + datastreamerInst.initDataStreamer(configName, qtouchComponent, tuneMenu)
	qtouchInst['datastreamerInst'] = datastreamerInst

	# ----TouchTune----
	touchTuneInst = touch_tune_with_plugin.classTouchTuneWithPlugin()
	projectFilesList = projectFilesList + touchTuneInst.initTouchTune(configName, qtouchComponent, tuneMenu)
	qtouchInst['touchTuneInst'] = touchTuneInst

	# ----2D Surface Visualizer----
	surfaceUtiInst = touch_surface_2D_utility.classTouchSurface2DUtility()
	projectFilesList = projectFilesList + surfaceUtiInst.initSurface2DUtilityInstance(
		configName, 
		qtouchComponent, 
		tuneMenu, 
		device, 
		touchChannelMutual)
	qtouchInst['surfaceUtiInst'] = surfaceUtiInst

	qtouchTimerComponent = qtouchComponent.createStringSymbol("TOUCH_TIMER_INSTANCE", None)
	qtouchTimerComponent.setLabel("Timer Component Chosen for Touch middleware")
	qtouchTimerComponent.setReadOnly(True)
	qtouchTimerComponent.setVisible(False)
	qtouchTimerComponent.setDefaultValue("")
	# qtouchTimerComponent.setDependencies(onGenerate, ["TOUCH_TIMER_INSTANCE"])
	
	qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_INSTANCE", None)
	qtouchSercomComponent.setLabel("Sercom Component Chosen for Touch middleware")
	qtouchSercomComponent.setReadOnly(True)
	qtouchSercomComponent.setVisible(False)
	qtouchSercomComponent.setDefaultValue("")
	# qtouchSercomComponent.setDependencies(onGenerate, ["TOUCH_SERCOM_INSTANCE"])

	qtouchSercomComponent = qtouchComponent.createStringSymbol("TOUCH_SERCOM_KRONO_INSTANCE", None)
	qtouchSercomComponent.setLabel("Sercom Component Chosen for Touch middleware")
	qtouchSercomComponent.setReadOnly(True)
	qtouchSercomComponent.setVisible(False)
	qtouchSercomComponent.setDefaultValue("")
	# qtouchSercomComponent.setDependencies(onGenerate, ["TOUCH_SERCOM_KRONO_INSTANCE"])
	
	touchWarning = qtouchComponent.createMenuSymbol("TOUCH_WARNING", None)
	touchWarning.setLabel("")
	touchWarning.setVisible(False)
	touchWarning.setDependencies(onWarning,["PTC_CLOCK_FREQ"])
	touchWarning.setDependencies(onGenerate,["PTC_CLOCK_FREQ"])
	
	touchFiles = touch_qtouch_sourcefiles.classTouchQTouch()
	projectFilesList = projectFilesList + touchFiles.setTouchFiles(configName, qtouchComponent,useTrustZone)

	ptcSystemDefFile = touchFiles.getSystemDefFileSymbol()

	# Trustzone - secure device updates
	if target_deviceInst.isSecureDevice(device):
		nvicid = target_deviceInst.getSecureNVICID(device)
		secureStatus = ""
		if (Database.getSymbolValue("core", "PTC_IS_NON_SECURE") == False):
			secureStatus = "SECURE"
			Database.setSymbolValue("core",nvicid, 0)
		else:
			secureStatus = "NON_SECURE"
			Database.setSymbolValue("core",nvicid, 1)

		trustZoneInst = touchTrustZone.touchTrustZone()
		trustZoneInst.initTrustzoneInstance(configName, qtouchComponent, touchMenu, device,projectFilesList,ptcSystemDefFile,secureStatus)
		qtouchInst['trustZoneInst'] = trustZoneInst
		symbol,func,depen = trustZoneInst.getDepDetails()
		qtouchSetDependencies(symbol, func, depen)

	# qtouchComponent.addPlugin("../touch/plugin/ptc_manager_c21.jar")
	qtouchComponent.addPlugin("../harmony-services/plugins/generic_plugin.jar", "TOUCH_CONFIGURATION_BETA", {"plugin_name": "Touch Configuration", "main_html_path": "touch/plugin/index.html"})

	print("Dependency details")
	symbol,func,depen = target_deviceInst.getDepDetails()
	print symbol,func,depen
	qtouchSetDependencies(symbol, func, depen)

	# symbol,func,depen = customInst.getDepDetails()
	# qtouchSetDependencies(symbol, func, depen)
	qtouchInst['touchFiles'] = touchFiles

	loadedTimers = qtouchComponent.createStringSymbol("LOADED_TIMERS", touchInfoMenu)
	loadedTimers.setLabel("Loaded Timers")
	loadedTimers.setDefaultValue("")
	touchScriptEvent.setReadOnly(True)
	loadedTimers.setVisible(True)
