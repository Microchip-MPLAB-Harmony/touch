"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
import sys

try:
    #try required for pydoc server
    sys.path.append(Module.getPath() + "config")
except (NameError):
    pass


import interface
import acquisition_groups
import key_groups
import node_groups
import sensor_groups
import scroller_groups
import drivenshield_groups
import boost_mode_groups
import freq_hop_groups
import surface
import gesture
import surface_2D_Utility
import target_device
import datastreamer
import trustzone
import lowpower
import acquisition_sourcefiles
import key_sourcefiles
import scroller_sourcefiles
import drivenshield_sourcefiles
import freq_hop_sourcefiles
import surface_sourcefiles
import gesture_sourcefiles
import qtouch_sourcefiles

autoComponentIDTable = ["rtc"]
autoConnectTable = [["lib_qtouch", "Touch_timer","rtc", "RTC_TMR"]]
InterruptVector = "PTC" + "_INTERRUPT_ENABLE"
InterruptHandler = "PTC" + "_INTERRUPT_HANDLER"

#used for driven shield 
touchChannels = []
touchChannelSelf =0
touchChannelMutual=0



global touchMenu

def onAttachmentConnected(source,target):
    """Handler for peripheral assignment to touch module.
    MHC reference : <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-voidonAttachmentConnected(source,target)>
    Arguments:
        :source : the touch module
        :target : peripheral being connected 
    Returns:
        :none
    """
    global Database
    global nonSecureStatus
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    targetDevice = interface.getDeviceSeries()

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
    totalChannelCount = target_device.getMutualCount()
    lumpSupported = target_device.getLumpSupported(targetDevice)
    shieldMode = target_device.getShieldMode(targetDevice)
    surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
    touchtech = str(touchSenseTechnology.getSelectedKey())
    if (lumpSupported ==  True):
        lumpSymbol = localComponent.getSymbolByID("LUMP_CONFIG")
        lumpFeature = localComponent.getSymbolByID("LUMP_CONFIG").getValue()
        print("lump is supported")
        if(lumpFeature !=""):
            print("lump is not empty")
            node_groups.updateLumpMode(lumpSymbol,touchtech)

        if(shieldMode == "hardware"):
            print("shield is hardware")
            drivenshield_groups.updateLumpModeDrivenShield(symbol,event,totalChannelCount,lumpFeature)

        if (surfaceEnabled == True):
            if (surface.getSurfaceRearrangeRequired(targetDevice) == False):
                surface.updateLumpModeSurface(symbol,touchSenseTechnology,totalChannelCount)

def onGenerate(symbol,event):
    """Handler for generate code menu click event. 
    Triggers updates for touch sub modules, lump,surface,lowpower,boostmode
    Arguments:
        :symbol : the symbol that triggered the event
        :event : new value of the symbol 
    Returns:
        :none
    """
    localComponent = symbol.getComponent()
    targetDevice = localComponent.getSymbolByID("DEVICE_NAME").getValue()
    surfaceEnabled = localComponent.getSymbolByID("ENABLE_SURFACE").getValue()
    nodeCount = target_device.getMutualCount()

    if boost_mode_groups.getBoostSupported(targetDevice):
        print("Entering ProcessBoostmode")
        boost_mode_groups.processBoostMode(symbol,event,targetDevice,nodeCount)

    print("Entering ProcessLump")
    processLump(symbol,event,targetDevice)

    if(surfaceEnabled ==True):
        print("Entering surface_rearrange")
        surface.surface_rearrange(symbol,event)

    lowpower.processSoftwareLP(symbol,event)


def onWarning(symbol,event):
    """Handler for clock parameter sync error event. 
    Arguments:
        :symbol : the symbol that triggered the event
        :event : new value of the symbol 
    Returns:
        :none
    """
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


    

def updateGroupsCounts(symbol,event):
    """Handler for updating module group counts
    Triggers updates for touch sub modules with multiple groups:
        node, sensor, key, scroller, frequency hop, boost mode, driven shield
    Arguments:
        :symbol : the symbol that triggered the event
        :event : new value of the symbol 
    Returns:
        :none
    """
    acquisition_groups.updateAcquisitionGroups(symbol,event)
    node_groups.updateNodeGroups(symbol,event)
    key_groups.updateKeyGroups(symbol,event)
    sensor_groups.updateSensorGroups(symbol,event)
    scroller_groups.updateScrollerGroups(symbol,event)
    drivenshield_groups.updateDrivenShieldGroups(symbol,event)
    freq_hop_groups.updateFreqHopGroups(symbol,event)
    boost_mode_groups.updateBoostModeGroups(symbol,event)


def instantiateComponent(qtouchComponent):
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
    global autoComponentIDTable
    global autoConnectTable
    global InterruptVector
    global touchChannelSelf
    global touchChannelMutual
    global touchMenu

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

    #targetDevice
    interface.getTargetDeviceInfo(ATDF,qtouchComponent,touchMenu)
    targetDevice =interface.getDeviceSeries()
    target_device.initTargetParameters(qtouchComponent,touchMenu,targetDevice,Database)

    # Interrupts
    ptcInterruptConfig = qtouchComponent.createIntegerSymbol("DEF_PTC_INTERRUPT_PRIORITY", touchMenu)
    ptcInterruptConfig.setLabel("PTC Interrupt Priority")
    ptcInterruptMin = target_device.getMinInterrupt(targetDevice)
    ptcInterruptConfig.setMin(ptcInterruptMin)
    ptcInterruptMax = target_device.getMaxInterrupt(targetDevice)
    ptcInterruptConfig.setMax(ptcInterruptMax)
    ptcInterruptDefault= target_device.getDefaultInterrupt(targetDevice)
    ptcInterruptConfig.setDefaultValue(ptcInterruptDefault)
    ptcInterruptConfig.setDescription("Defines the interrupt priority for the PTC. Set low priority to PTC interrupt for applications having interrupt time constraints.")
    

    # Lump support
    lumpSupported = target_device.getLumpSupported(targetDevice)
    if (lumpSupported == True):
        lumpSymbol = qtouchComponent.createStringSymbol("LUMP_CONFIG", touchMenu)
        lumpSymbol.setLabel("Lump Configuration")
        lumpSymbol.setDefaultValue("")
        lumpSymbol.setDependencies(node_groups.updateLumpMode,["LUMP_CONFIG"])
        lumpSymbol.setVisible(True)
    
    # PinValues
    ptcPinValues = target_device.setDevicePinValues(ATDF,False,lumpSupported,targetDevice)
    # Channel Limits
    touchChannelSelf = target_device.getSelfCount()
    touchChannelMutual = target_device.getMutualCount()
    # clocksetup 
    target_device.setGCLKconfig(qtouchComponent,ATDF,touchInfoMenu,targetDevice)
    # CSD support
    csdMode = target_device.getCSDMode(targetDevice)
    # Rsel support
    rSelMode = target_device.getRSelMode(targetDevice)
    # Driven shield support
    shieldMode = target_device.getShieldMode(targetDevice)
    # Boost mode support
    boostMode = boost_mode_groups.getBoostSupported(targetDevice)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        useTrustZone = True
    else:
        useTrustZone = False

    #Self Mutual Related if not required then setMaxGroups(1)
    acquisition_groups.setMaxGroups(1) # Specifies the max number of acquisitions groups
    acquisitionGroupCountMenu = qtouchComponent.createIntegerSymbol("NUM_ACQUISITION_GROUPS", touchMenu)
    acquisitionGroupCountMenu.setDefaultValue(1)
    acquisitionGroupCountMenu.setMin(1)
    acquisitionGroupCountMenu.setMax(acquisition_groups.getMaxGroups()) # taken from acquisition_groups.py variable
    acquisitionGroupCountMenu.setDependencies(updateGroupsCounts,["NUM_ACQUISITION_GROUPS"])
    acquisitionGroupCountMenu.setLabel("Number of Acquisition Groups")
    if(acquisition_groups.getMaxGroups()>1):
        acquisitionGroupCountMenu.setVisible(True)
    else:
        acquisitionGroupCountMenu.setVisible(False)
    
    #groups limits defined by the acquisition group limit
    minGroupCount = acquisitionGroupCountMenu.getMin()
    maxGroupCount = acquisitionGroupCountMenu.getMax()

    projectFilesList = []

    # ----Acquisition----
    projectFilesList = projectFilesList + acquisition_sourcefiles.setAcquisitionFiles(configName, qtouchComponent, targetDevice,useTrustZone)
    acquisition_groups.initAcquisitionGroup(
        qtouchComponent, 
        touchMenu, 
        minGroupCount,
        maxGroupCount,
        touchChannelSelf,
        touchChannelMutual,
        targetDevice,
        csdMode,
        shieldMode)


    # ----Node----
    node_groups.initNodeGroup(
        qtouchComponent,
        touchMenu,
        minGroupCount,
        maxGroupCount,
        touchChannelSelf,
        touchChannelMutual,
        ptcPinValues,
        csdMode,
        rSelMode)

    # ----Keys----
    key_groups.initKeyGroup(
        qtouchComponent, 
        touchMenu, 
        minGroupCount,
        maxGroupCount,
        touchChannelSelf,
        touchChannelMutual)
    projectFilesList = projectFilesList + key_sourcefiles.setKeysFiles(configName, qtouchComponent, targetDevice,useTrustZone)

    # ----Sensor----
    sensor_groups.initSensorGroup(
        qtouchComponent, 
        touchMenu, 
        minGroupCount,
        maxGroupCount)

    # ----Scroller----
    projectFilesList = projectFilesList + scroller_sourcefiles.setScrollerFiles(configName, qtouchComponent, targetDevice,useTrustZone)
    scroller_groups.initScrollerGroup(
        qtouchComponent,
        touchMenu,
        minGroupCount,
        maxGroupCount,
        touchChannelSelf,
        touchChannelMutual)
    

    # ----Frequency Hop----
    projectFilesList = projectFilesList + freq_hop_sourcefiles.setFreqHopFiles(configName, qtouchComponent, targetDevice,useTrustZone)
    freq_hop_groups.initFreqHopGroup(
        qtouchComponent,
        touchMenu,
        minGroupCount,
        maxGroupCount,
        targetDevice)
    

    # ----Driven Shield----
    if (shieldMode != "none"):
        projectFilesList = projectFilesList + drivenshield_sourcefiles.setDrivenShieldFiles(configName, qtouchComponent,useTrustZone)
        drivenshield_groups.initDrivenShieldGroup(
            ATDF,
            qtouchComponent,
            touchMenu,
            touchInfoMenu,
            minGroupCount,
            maxGroupCount,
            touchChannelMutual,
            ptcPinValues,
            shieldMode)
        

    # ----Boost Mode----
    if(boostMode == True):
        boost_mode_groups.initBoostModeGroup(
            configName, 
            qtouchComponent, 
            touchMenu,
            minGroupCount,
            maxGroupCount,
            targetDevice)

    # ----Surface----
    surface.initSurfaceInstance(
        qtouchComponent, 
        touchMenu, 
        targetDevice, 
        touchChannelMutual)
    projectFilesList = projectFilesList + surface_sourcefiles.setSurfaceFiles(configName,qtouchComponent, targetDevice,useTrustZone)

    # ----2D Surface Visualizer----
    projectFilesList = projectFilesList + surface_2D_Utility.initSurface2DUtilityInstance(
        configName, 
        qtouchComponent, 
        touchMenu, 
        targetDevice, 
        touchChannelMutual)

    # ----Gesture----
    gesture.initGestureInstance(qtouchComponent, touchMenu)
    projectFilesList = projectFilesList + gesture_sourcefiles.setGestureFiles(configName, qtouchComponent, targetDevice,useTrustZone)

	#----Low power----
    if (lowpower.lowPowerSupported(targetDevice)):
        lowpower.initLowPowerInstance(qtouchComponent, touchMenu, targetDevice)

    # ----Datastreamer----
    projectFilesList = projectFilesList + datastreamer.initDataStreamer(configName, qtouchComponent, touchMenu)


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
    
    if targetDevice not in ["PIC32MZW"]:
        #keep it as last displayed tree config
        touchWarning = qtouchComponent.createMenuSymbol("TOUCH_WARNING", None)
        touchWarning.setLabel("")
        touchWarning.setVisible(False)
        touchWarning.setDependencies(onWarning,["PTC_CLOCK_FREQ"])

    projectFilesList = projectFilesList + qtouch_sourcefiles.setTouchFiles(configName, qtouchComponent,useTrustZone)

    if useTrustZone == True:
        trustzone.initTrustzoneInstance(configName, qtouchComponent, touchMenu , targetDevice, projectFilesList)

        
    qtouchComponent.addPlugin("../touch/plugin/ptc_manager_c21.jar")

def finalizeComponent(qtouchComponent):
    """
    MHC reference :<http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-voidfinalizeComponent(component,[index])>
    Arguments:
        :qtouchComponent : newly created module see module.loadModule()
    Returns:
        :none
    """
    res = Database.activateComponents(autoComponentIDTable)
    res = Database.connectDependencies(autoConnectTable)

def deactivateComponents(toRemove):
    Database.deactivateComponents(toRemove)

def activateComponents(toAdd):
    Database.deactivateComponents(toAdd)

def connectDependencies(toConnect):
    Database.connectDependencies(toConnect)