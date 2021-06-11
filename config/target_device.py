"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
xPads = set()
yPads = set()

adc_based_acquisition = set(["SAME54","SAME53","SAME51","SAMD51"])
no_csd_support = set(["SAMD20","SAMD21","SAMDA1","SAMHA1"])
non_lump_support = set(["PIC32MZW"])
timer_driven_shield_support = set(["SAMD21","SAMDA1","SAMHA1","SAME54","SAME53","SAME51","SAMD51","SAMC21","SAMC20","SAML21","SAML22"])
hardware_driven_shield_support = set(["SAML10","SAML11","PIC32MZW","PIC32CMLE00","PIC32CMLS00"])

touchChannelSelf = 0
touchChannelMutual = 0
ptcPinValues =[]

def getSelfCount():
    """Get self capacitance channels
    Arguments:
        :none
    Returns:
        :number of self capacitance channels as (int)
    """
    return touchChannelSelf

def getMutualCount():
    """Get mutual capacitance channels
    Arguments:
        :none
    Returns:
        :number of mutual capacitance channels as (int)
    """
    return touchChannelMutual

def setModuleID(qtouchComponent,touchMenu,targetDevice):
    """
    assigns the Module ID based on targetDevice
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        fileList: list of file symbols
    """
    getModuleID = qtouchComponent.createStringSymbol("MODULE_ID", touchMenu)
    getModuleID.setVisible(False)
    if (targetDevice in set(["SAMC21","SAMC20"])):    
        getModuleID.setDefaultValue("0x0020")
    elif(targetDevice in set(["SAMD10","SAMD11"])):
        getModuleID.setDefaultValue("0x0009")
    elif(targetDevice == "SAMD20"):
        getModuleID.setDefaultValue("0x000e")
    elif(targetDevice in set(["SAMD21","SAMDA1","SAMHA1"])):
        getModuleID.setDefaultValue("0x0024")
    elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        getModuleID.setDefaultValue("0x000f")
    elif(targetDevice == "SAML10"):
        getModuleID.setDefaultValue("0x0027")
    else:
        print("Error_setModuleID - Device Not Supported")
        getModuleID.setDefaultValue("Error_setModuleID")

# Minimum Interrupt priority
def getMinInterrupt(targetDevice):
    """Get targeDevice minimum interupt
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :minimum Interrupt as (int)
    """
    if (targetDevice in set(["SAMC20","SAMC21","SAMD20","SAMD21","SAMDA1","SAMHA1","SAMD10","SAMD11","SAMD51","SAME51","SAME53","SAME54","SAML10"])):
        return 0
    else:
        return -1

# Maximum Interrupt priority
def getMaxInterrupt(targetDevice):
    """Get targeDevice maximum interupt
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :maximum Interrupt as (int)
    """
    if (targetDevice in set(["SAMC20","SAMC21","SAMD20","SAMD21","SAMDA1","SAMHA1","SAMD10","SAMD11","SAML10"])):
        return 3
    elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        return 7
    else:
        return -1

# Default Interrupt priority
def getDefaultInterrupt(targetDevice):
    """Get targeDevice default interupt
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :default Interrupt as (int)
    """
    if (targetDevice in set(["SAMC20","SAMC21","SAMD20","SAMD21","SAMDA1","SAMHA1"])):
        return 3
    elif(targetDevice in set(["SAMD10","SAMD11","SAML10"])):
        return 2
    elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        return 7
    else:
        return -1

# Clock xml 
def setClockXML(qtouchComponent,touchMenu,targetDevice):
    """
    assigns the Clock configuration xml based on targetDevice
    Arguments:
        :qtouchComponent : touchModule
        :touchMenu : parent menu for new symbols
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    clockXml = qtouchComponent.createStringSymbol("CLOCK_XML", touchMenu)
    clockXml.setVisible(False)
    if (targetDevice in set(["SAMC21","SAMC20"])):
        clockXml.setDefaultValue("c21_clock_config")
    elif (targetDevice in set(["SAMD10", "SAMD11"])):
        clockXml.setDefaultValue("d1x_clock_config")
    elif (targetDevice in set(["SAMD20","SAMD21","SAMDA1"])):
        clockXml.setDefaultValue("d21_clock_config")
    elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        clockXml.setDefaultValue("e5x_clock_config")
    elif(targetDevice == "SAMHA1"):
        clockXml.setDefaultValue("ha1_clock_config")
    elif(targetDevice == "SAML10"):
        clockXml.setDefaultValue("l1x_clock_config")
    else:
        print ("error - setClockXML")




def setPTCInterruptVector(Database,targetDevice):
    """
    assigns the PTC interrupt handler based on targetDevice
    Arguments:
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    if (targetDevice in set(["SAMC21","SAMD10","SAMD11","SAMD21","SAMDA1","SAMHA1","SAML10"])):
        Database.setSymbolValue("core", "PTC_INTERRUPT_ENABLE", True)
        Database.setSymbolValue("core", "PTC_INTERRUPT_HANDLER", "PTC_Handler")
    elif (targetDevice in set(["SAMC20","SAMD20"])):
        Database.setSymbolValue("core", "PTC_INTERRUPT_ENABLE", True, 2)
        Database.setSymbolValue("core", "PTC_INTERRUPT_HANDLER", "PTC_Handler", 2)
    else:
        print ("error - setPTCInterruptVector")


def setADCInterruptVector(Database,targetDevice):
    """
    assigns the ADC interrupt based on targetDevice
    Arguments:
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    if (targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        Database.setSymbolValue("core", "NVIC_119_0_ENABLE", True)
        Database.setSymbolValue("core", "NVIC_119_0_HANDLER", "ADC0_1_Handler")
    else:
        print ("error - setADCInterruptVector")

# PTC Clock
def setPTCClock(Database,targetDevice):
    """
    assigns the PTC peripheral Gclock based on targetDevice
    Arguments:
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    if (targetDevice in set(["SAMC21"])): 
        Database.clearSymbolValue("core", "GCLK_ID_37_GENSEL")
        Database.setSymbolValue("core", "GCLK_ID_37_GENSEL", 1)
    elif(targetDevice in set(["SAMC20"])):
        Database.clearSymbolValue("core", "GCLK_ID_37_GENSEL")
        Database.setSymbolValue("core", "GCLK_ID_37_GENSEL", 1, 2)
    elif(targetDevice in set(["SAMD10","SAMD11"])):
        Database.clearSymbolValue("core", "GCLK_ID_23_GENSEL")
        Database.setSymbolValue("core", "GCLK_ID_23_GENSEL", 1)
    elif(targetDevice in set(["SAMD20"])):
        Database.clearSymbolValue("core", "GCLK_ID_27_GENSEL")
        Database.setSymbolValue("core", "GCLK_ID_27_GENSEL", 2)
    elif(targetDevice in set(["SAMD21","SAMDA1","SAMHA1"])):
        Database.setSymbolValue("core", "GCLK_ID_4_GENSEL", 1)
        Database.setSymbolValue("core", "GCLK_ID_34_GENSEL", 2)
    elif(targetDevice == "SAML10"):
        Database.clearSymbolValue("core", "GCLK_ID_19_GENSEL")
        Database.setSymbolValue("core", "GCLK_ID_19_GENSEL", 1)
    else:
        print ("error - setPTCClock")

# PTC Clock Enable
def setPTCClockEnable(Database,targetDevice):
    """
    assigns the PTC clock enable config based on targetDevice
    Arguments:
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    if (targetDevice in set(["SAMC21","SAMD20","SAMD21","SAMHA1","SAMDA1","SAMD10","SAMD11"])):
        Database.clearSymbolValue("core", "PTC_CLOCK_ENABLE")
        Database.setSymbolValue("core", "PTC_CLOCK_ENABLE", True)
    elif(targetDevice in set(["SAMC20"])):
        Database.clearSymbolValue("core", "PTC_CLOCK_ENABLE")
        Database.setSymbolValue("core", "PTC_CLOCK_ENABLE", True, 2)
    else:
        print ("error - setPTCClockEnable")

# ADC Clock
def setADCClock(Database,targetDevice):
    """
    assigns the ADC clock enable config based on targetDevice
    Arguments:
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    if (targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        Database.clearSymbolValue("core", "ADC0_CLOCK_ENABLE")
        Database.setSymbolValue("core", "GCLK_ID_40_CHEN", True)
        Database.setSymbolValue("core", "ADC0_CLOCK_ENABLE", True)
        Database.clearSymbolValue("core", "GCLK_ID_40_GENSEL")
        Database.setSymbolValue("core", "GCLK_ID_40_GENSEL", 1)
    else:
        print ("error - setADCClock")

def getCSDMode(targetDevice):
    """Get charge share delay bit resolution based on targetDevice. 
    Used to determine node / acquistion configuration
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :csd support mode(string)
    """
    if(targetDevice in no_csd_support):
        return "NoCSD"
    elif(targetDevice in adc_based_acquisition):
        return "8bitCSD"
    else:
        return "16bitCSD" 

def getRSelMode(targetDevice):
    """Get Series resistor mode based on targetDevice. 
    Used to determine node configuration
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :support mode(string)
    """
    if (targetDevice in adc_based_acquisition):
        return "e5x"
    elif (targetDevice in ["SAML22"]):
        return "l22"
    else:
        return "std"

def getShieldMode(targetDevice):
    """Get driven shield mode based on targetDevice. 
    Used to determine node configuration
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        : driven shield support mode(string)
    """

    if(targetDevice in timer_driven_shield_support):
        return "timer"
    elif(targetDevice in hardware_driven_shield_support):
        return "hardware"
    else:
        return "none"


def getLumpSupported(targetDevice):
    """Get lumpmode mode support based on targetDevice. 
    Used to determine node configuration
    Arguments:
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        : lump supported (boolean)
    """
    if (targetDevice in non_lump_support):
        return False
    else:
        return True

def setLumpSupport(qtouchComponent,touchMenu,targetDevice):
    """
    assigns the lump symbol based on targetDevice
    Arguments:
        :qtouchComponent : touchModule
        :touchMenu : parent menu for new symbols
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    lumpsupport = False

    return lumpsupport

def setGCLKconfig(qtouchComponent,ATDF,parentSymbol,targetDevice):
    """
    Assigns the lump symbol based on targetDevice
    Arguments:
        :qtouchComponent : touchModule
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :parentSymbol : parent menu for new symbols
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :none
    """
    if targetDevice not in ["PIC32MZW"]:
        ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance@[name=\"PTC\"]/parameters/param@[name=\"GCLK_ID\"]")
        if ptcClockInfo is None:
            ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/parameters/param@[name=\"GCLK_ID\"]")
        ptcFreqencyId= qtouchComponent.createStringSymbol("PTC_CLOCK_FREQ", parentSymbol)
        ptcFreqencyId.setLabel("PTC Freqency Id ")
        ptcFreqencyId.setReadOnly(True)
        ptcFreqencyId.setDefaultValue("GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ")
        ptcFreqencyId.setDependencies(onPTCClock,["core."+"GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ"])

def onPTCClock(symbol,event):
    """Handler for setGCLKconfig gclkID frequency
    Arguments:
        :symbol : the symbol that triggered the callback
        :event : the new value. 
    Returns:
        :none
    """
    component = symbol.getComponent()
    if component.getSymbolValue("TOUCH_LOADED"):
        frequency = event['symbol'].getValue()
        channels = component.getSymbolValue("TOUCH_CHAN_ENABLE_CNT")
        if frequency > 0 and channels > 0:   
            symbol.setValue(symbol.getDefaultValue()+":sync")
            sevent = component.getSymbolByID("TOUCH_SCRIPT_EVENT")
            sevent.setValue("ptcclock")
            sevent.setValue("")

def setDevicePinValues(ATDF,withConsoleOutput, lumpsupport, targetDevice):
    """
    Retrieves all touch pads, then sorts into x,y and multiplexed
    Arguments:
        :ATDF : MHC reference: <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-ATDFInterface>
        :withConsoleOutput: output to console for debugging (boolean)
        :lumpsupport : see target_device.setLumpSupport
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        :ptcpinvalues: atdf children
    """
    global touchChannelSelf
    global touchChannelMutual
    global ptcPinValues 

    if (targetDevice in adc_based_acquisition):
        ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/signals")
    else:
        ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")

    ptcPinValues = []
    selectablePins =set()
    ptcPinValues = ptcSignalsATDF.getChildren()

    for index in range(0, len(ptcPinValues)):
        if(ptcPinValues[index].getAttribute("group") == "X"):
            xPads.add(ptcPinValues[index].getAttribute("pad"))
        elif(ptcPinValues[index].getAttribute("group") == "Y"):
            yPads.add(ptcPinValues[index].getAttribute("pad"))

    selectablePins = xPads.intersection(yPads)

    ylen = len(yPads)
    xlen = len(xPads)
    selLen = len(selectablePins)
    # Determine largest Mutual config
    maxMutuals = 0
    thisMax = 0
    if(selLen ==0):
        for index in range(0,ylen):
            thisMax = (ylen-index)*(xlen+index)
            if(thisMax > maxMutuals):
                maxMutuals = thisMax
    else:
        for index in range(0,selLen):
            thisMax = (ylen-index-selLen)*(xlen+index)
            if(thisMax > maxMutuals):
                maxMutuals = thisMax
    # set the global counts for self and mutual
    touchChannelSelf = ylen 
    touchChannelMutual = maxMutuals
    # adust for lump support
    if(lumpsupport):
        touchChannelSelf +=16
        touchChannelMutual +=16
    
    # Print results to screen
    if(withConsoleOutput):
        print("====================================================")
        print("Largest non Lump Mutual Config : " + str(maxMutuals))
        print("Lump Supported : "+ str(lumpsupport))
        print("touchChannelSelf : " + str(touchChannelSelf))
        print("touchChannelMutual : " + str(touchChannelMutual))
        print("====================================================")
        print("X pins length: " + str(xlen))
        print("X Pins:")
        print(xPads)
        print("====================================================")
        print("Y pins length: " + str(ylen))
        print("Y Pins :")
        print(yPads)
        print("====================================================")
        print("Selectable pins length: " + str(selLen))
        print("Selectable Pins:")
        print(selectablePins)
        print("====================================================")
    
    return ptcPinValues


def setInterruptVector(Database,targetDevice):
    """
    Configures Interrups vectore based on PTC vs ADC support 
    Arguments:
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
        :targetDevice :see interface.getDeviceSeries()
    Returns:
        :none
    """
    if(targetDevice in adc_based_acquisition):
        setADCInterruptVector(Database,targetDevice)
    else:
        setPTCInterruptVector(Database,targetDevice)


def initTargetParameters(qtouchComponent,touchMenu,targetDevice,Database):
    """
    sets Module Id, Clock config and Interrupt vector parameters
    Arguments:
        :qtouchComponent : touchModule
        :touchMenu : parent Menu symbol
        :targetDevice : see interface.getDeviceSeries()
        :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
    Returns:
        :none
    """
    setModuleID(qtouchComponent,touchMenu,targetDevice)
    setClockXML(qtouchComponent,touchMenu,targetDevice)
    setInterruptVector(Database,targetDevice)