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
import touch_boost_mode_sourcefiles
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
        if (Database.getSymbolValue(remoteID, "USART_INTERRUPT_MODE") == True):
            Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", False)

    if (connectID == "Touch_sercom_Krono"):
        plibUsed = localComponent.getSymbolByID("TOUCH_SERCOM_KRONO_INSTANCE")
        plibUsed.clearValue()
        plibUsed.setValue(remoteID.upper(), 1)
        if (Database.getSymbolValue(remoteID, "USART_INTERRUPT_MODE") == False):
            Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", True)

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
        autoComponentIDTable[:] = ["adchs","tmr4"]
        autoConnectTable[:] = [["lib_qtouch", "Touch_timer","tmr4","TMR4_TMR"],
                                ["lib_qtouch", "Acq_Engine","adchs","ADCHS_ADC"]]
    else:
        autoComponentIDTable[:] = ["rtc"]
        autoConnectTable[:] = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"]]
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
    print("---------Entering apply DSTimers----------")
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
        component.setDependencyEnabled("Drivenshield_"+timer, True)
    
    if len(toRemove)!=0:
        Database.deactivateComponents(toRemove)
    if len(toAdd)!=0:
        Database.activateComponents(toAdd)
        if len(toConnect)!=0:
            Database.connectDependencies(toConnect)
        sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
        sevent.setValue("dstimer")
        sevent.setValue("")
    print("---------Leaving apply DSTimers----------")

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
    touchSenseTechnology = localComponent.getSymbolByID("SENSE_TECHNOLOGY")
    totalChannelCount = qtouchInst['target_deviceInst'].getMutualCount()
    lumpSupported = qtouchInst['target_deviceInst'].getLumpSupported(targetDevice)
    shieldMode = qtouchInst['target_deviceInst'].getShieldMode(targetDevice)
    surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
    touchtech = str(touchSenseTechnology.getSelectedKey())
    if (lumpSupported ==  True):
        lumpSymbol = localComponent.getSymbolByID("LUMP_CONFIG")
        lumpFeature = localComponent.getSymbolByID("LUMP_CONFIG").getValue()
        print("lump is supported")
        print(lumpFeature)
        if(lumpFeature !=""):
            print("lump is not empty")
            qtouchInst['node_groupInst'].updateLumpMode(lumpSymbol,touchtech)

        if(shieldMode == "hardware"):
            print("shield is hardware")
            qtouchInst['ds_groupInst'].updateLumpModeDrivenShield(symbol,event,totalChannelCount,lumpFeature)

        if (surfaceEnabled == True):
            if (qtouchInst['surfaceInst'].getSurfaceRearrangeRequired(targetDevice) == False):
                qtouchInst['surfaceInst'].updateLumpModeSurface(symbol,touchSenseTechnology,totalChannelCount)

def updatePinsSettings(symbol,event):
    touchPads = qtouchInst['padsInfo'].getTouchPads()
    touchModule = qtouchInst['padsInfo'].getTouchModule()
    #print touchModule
    #print touchPads
    component = symbol.getComponent()
    #clear setting
    for pad in touchPads:
        setting = touchPads[pad]
        value = Database.getSymbolValue("core", "PIN_"+setting["index"]+"_FUNCTION_TYPE")
        if touchModule in value:
            Database.setSymbolValue("core", "PIN_"+setting["index"]+"_FUNCTION_TYPE", "")
    activePds = set()
    count = component.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()
    for i in range(count):
        if "SELF" in symbol.getID():
            signalSymbol = component.getSymbolByID("SELFCAP-INPUT_"+str(i))
            padDesc = signalSymbol.getKeyDescription(signalSymbol.getValue())
            padName = padDesc[padDesc.index("(")+1:padDesc.index(")")]
            activePds.add(padName)
        if "MUTL" in symbol.getID():
            signalSymbol = component.getSymbolByID("MUTL-X-INPUT_"+str(i))
            padDesc = signalSymbol.getKeyDescription(signalSymbol.getValue())
            padName = padDesc[padDesc.index("(")+1:padDesc.index(")")]
            activePds.add(padName)
            signalSymbol = component.getSymbolByID("MUTL-Y-INPUT_"+str(i))
            padDesc = signalSymbol.getKeyDescription(signalSymbol.getValue())
            padName = padDesc[padDesc.index("(")+1:padDesc.index(")")]
            activePds.add(padName)
    for pad in activePds:
        setting = touchPads[pad]
        Database.setSymbolValue("core", "PIN_"+setting["index"]+"_FUNCTION_TYPE", setting["function"])

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
    targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()
    surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
    nodeCount = localComponent.getSymbolByID("TOUCH_CHAN_ENABLE_CNT").getValue()

    if qtouchInst['boostModeInst'].getBoostSupported(targetDevice):
        print("Entering ProcessBoostmode")
        qtouchInst['boostModeInst'].processBoostMode(symbol,event,targetDevice,nodeCount)

    if targetDevice not in qtouchInst['target_deviceInst'].non_lump_support:
        print("Entering ProcessLump")
        processLump(symbol,event,targetDevice)

    if(surfaceEnabled ==True):
        print("Entering surface_rearrange")
        qtouchInst['surfaceInst'].surface_rearrange(symbol,event)
    
    if (qtouchInst['lowpowerInst'].lowPowerSupported(targetDevice)):
        qtouchInst['lowpowerInst'].processSoftwareLP(symbol,event)

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
        if frequency > 0 and channels > 0:   
            symbol.setValue(symbol.getDefaultValue()+":sync")
            sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
            sevent.setValue("ptcclock")
            sevent.setValue("")

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
    showConfiguration = True
    configName = Variables.get("__CONFIGURATION_NAME")
 
    touchConfigurator = qtouchComponent.createMenuSymbol("TOUCH_CONFIGURATOR", None)
    touchConfigurator.setLabel("Goto Menu, MHC > Tools > Touch Configuration")    
    
    touchMenu = qtouchComponent.createMenuSymbol("TOUCH_MENU", None)
    touchMenu.setLabel("Touch Configuration")
    touchMenu.setVisible(showConfiguration)

    touchInfoMenu = qtouchComponent.createMenuSymbol("TOUCH_INFO", None)
    touchInfoMenu.setLabel("Touch Configuration Helper")
    touchInfoMenu.setVisible(showConfiguration)
    
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

    print("Kamal")
    print(interfaceInst.getDeviceSeries())

    if device == "PIC32MZDA":
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
        lumpSymbol.setDependencies(node_groupInst.updateLumpMode,["LUMP_CONFIG"])
        lumpSymbol.setVisible(True)
    
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
    # Rsel support
    rSelMode = target_deviceInst.getRSelMode(device)
    # Driven shield support
    shieldMode = target_deviceInst.getShieldMode(device)
    
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        useTrustZone = True
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
            device)
    qtouchInst['boostModeInst'] = boostModeInst

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

    # ----2D Surface Visualizer----
    surfaceUtiInst = touch_surface_2D_utility.classTouchSurface2DUtility()
    projectFilesList = projectFilesList + surfaceUtiInst.initSurface2DUtilityInstance(
        configName, 
        qtouchComponent, 
        touchMenu, 
        device, 
        touchChannelMutual)
    qtouchInst['surfaceUtiInst'] = surfaceUtiInst

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

    # ----Datastreamer----
    datastreamerInst = touch_datastreamer.classTouchDataStreamer()
    projectFilesList = projectFilesList + datastreamerInst.initDataStreamer(configName, qtouchComponent, touchMenu)
    qtouchInst['datastreamerInst'] = datastreamerInst

    qtouchTimerComponent = qtouchComponent.createStringSymbol("TOUCH_TIMER_INSTANCE", None)
    qtouchTimerComponent.setLabel("Timer Component Chosen for Touch middleware")
    qtouchTimerComponent.setReadOnly(True)
    qtouchTimerComponent.setVisible(False)
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
    
    touchFiles = touch_qtouch_sourcefiles.classTouchQTouch()
    projectFilesList = projectFilesList + touchFiles.setTouchFiles(configName, qtouchComponent,useTrustZone)

    qtouchComponent.addPlugin("../touch/plugin/ptc_manager_c21.jar")

    print("Depenedency details")
    symbol,func,depen = target_deviceInst.getDepDetails()
    print symbol,func,depen
    qtouchSetDependencies(symbol, func, depen)

    # symbol,func,depen = customInst.getDepDetails()
    # qtouchSetDependencies(symbol, func, depen)
    qtouchInst['touchFiles'] = touchFiles
    print qtouchInst