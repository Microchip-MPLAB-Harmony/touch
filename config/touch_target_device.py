"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
import os.path
import inspect
import xml.etree.ElementTree as ET

class classTouchTargetDevice():
    def __init__(self):
        self.xPads = set()
        self.yPads = set()
        self.adc_based_acquisition = set(["SAME54","SAME53","SAME51","SAMD51"])
        self.no_csd_support = set(["SAMD20","SAMD21","SAMDA1","SAMHA1"])
        self.non_lump_support = set(["PIC32MZW", "PIC32MZDA"])
        self.picDevices = ["PIC32MZW", "PIC32MZDA"]
        self.timer_driven_shield_support = set(["SAMD21","SAMDA1","SAMHA1","SAME54","SAME53","SAME51","SAMD51","SAMC21","SAMC20","SAML21","SAML22","SAMD10","SAMD11","SAMD20"])
        self.hardware_driven_shield_support = set(["SAML10","SAML11","PIC32MZW","PIC32CMLE00","PIC32CMLS00"])
        self.touchChannelSelf = 0
        self.touchChannelMutual = 0
        self.ptcPinValues =[]

    def getSelfCount(self):
        """Get self capacitance channels
        Arguments:
            :none
        Returns:
            :number of self capacitance channels as (int)
        """
        return self.touchChannelSelf

    def getMutualCount(self):
        """Get mutual capacitance channels
        Arguments:
            :none
        Returns:
            :number of mutual capacitance channels as (int)
        """
        return self.touchChannelMutual

    def setModuleID(self,qtouchComponent,touchMenu,targetDevice):
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
        elif(targetDevice == "PIC32MZW"):
            getModuleID.setDefaultValue("0x003e")
        elif(targetDevice == "PIC32MZDA"):
            getModuleID.setDefaultValue("0x003e")
        else:
            print("Error_setModuleID - Device Not Supported")
            #getModuleID.setDefaultValue("Error_setModuleID")

    # Minimum Interrupt priority
    def getMinInterrupt(self,targetDevice):
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
    def getMaxInterrupt(self,targetDevice):
        """Get targeDevice maximum interupt
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :maximum Interrupt as (int)
        """
        if targetDevice not in self.picDevices:
            if (targetDevice in set(["SAMC20","SAMC21","SAMD20","SAMD21","SAMDA1","SAMHA1","SAMD10","SAMD11","SAML10"])):
                return 3
            elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
                return 7
            else:
                return -1

    # Default Interrupt priority
    def getDefaultInterrupt(self,targetDevice):
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
            if targetDevice not in self.picDevices:
                print(" Unsupported device ")

    # Clock xml 
    def setClockXML(self,qtouchComponent,touchMenu,targetDevice):
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
        elif(targetDevice == "PIC32MZW"):
            clockXml.setDefaultValue("pic32mzw_clock_config")
        else:
            if targetDevice not in self.picDevices:
                print ("error - setClockXML")

    def setPTCInterruptVector(self,Database,targetDevice):
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


    def setADCInterruptVector(self,Database,targetDevice):
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
    def setPTCClock(self,Database,targetDevice):
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
    def setPTCClockEnable(self,Database,targetDevice):
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
    def setADCClock(self,Database,targetDevice):
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

    def getCSDMode(self,targetDevice):
        """Get charge share delay bit resolution based on targetDevice. 
        Used to determine node / acquistion configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :csd support mode(string)
        """
        if(targetDevice in self.no_csd_support):
            return "NoCSD"
        elif(targetDevice in self.adc_based_acquisition):
            return "8bitCSD"
        else:
            return "16bitCSD" 

    def getRSelMode(self,targetDevice):
        """Get Series resistor mode based on targetDevice. 
        Used to determine node configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :support mode(string)
        """
        if (targetDevice in self.adc_based_acquisition):
            return "e5x"
        elif (targetDevice in ["SAML22"]):
            return "l22"
        else:
            return "std"

    def getShieldMode(self,targetDevice):
        """Get driven shield mode based on targetDevice. 
        Used to determine node configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            : driven shield support mode(string)
        """

        if(targetDevice in self.timer_driven_shield_support):
            return "timer"
        elif(targetDevice in self.hardware_driven_shield_support):
            return "hardware"
        else:
            return "none"

    def getLumpSupported(self,targetDevice):
        """Get lumpmode mode support based on targetDevice. 
        Used to determine node configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            : lump supported (boolean)
        """
        if (targetDevice in self.non_lump_support):
            return False
        else:
            return True

    def setLumpSupport(self,qtouchComponent,touchMenu,targetDevice):
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

    def setGCLKconfig(self,qtouchComponent,ATDF,parentSymbol,targetDevice):
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
        if targetDevice not in self.picDevices:
            ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance@[name=\"PTC\"]/parameters/param@[name=\"GCLK_ID\"]")
            if ptcClockInfo is None:
                ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/parameters/param@[name=\"GCLK_ID\"]")
            ptcFreqencyId= qtouchComponent.createStringSymbol("PTC_CLOCK_FREQ", parentSymbol)
            ptcFreqencyId.setLabel("PTC Freqency Id ")
            ptcFreqencyId.setReadOnly(True)
            ptcFreqencyId.setDefaultValue("GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ")
            ptcFreqencyId.setDependencies(self.onPTCClock,["core."+"GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ"])

    def onPTCClock(self,symbol,event):
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

    def setDevicePinValues(self,ATDF,withConsoleOutput, lumpsupport, targetDevice):
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
        if (targetDevice in self.picDevices):
            currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
            pinoutXmlPath = os.path.join(currentPath, "../../csp/peripheral/gpio_02467/plugin/pin_xml/pins/MZ_W1_132.xml")
            print(pinoutXmlPath)
            tree = ET.parse(pinoutXmlPath)
            root = tree.getroot()
            cvdTPins = []
            cvdRPins = []
            cvdTPinsTemp = []
            cvdRPinsTemp = []
            cvdTPinsIndex = []
            cvdRPinsIndex = []
            self.ptcPinValues = []
            for myPins in root.findall('pins'):
                for myPin in myPins.findall('pin'):
                    for myFunction in myPin.findall('function'):
                        if myFunction.get("name").startswith("CVDT"):
                            tempstring = myPin.get("name")
                            index = myFunction.get("name")
                            index.replace("CVDT",'')
                            cvdTPinsIndex.append(int(index[4:]))
                            cvdTPinsTemp.append(tempstring)
                        elif myFunction.get("name").startswith("CVDR"):
                            tempstring = myPin.get("name")
                            index = myFunction.get("name")
                            index.replace("CVDR",'')
                            cvdRPinsIndex.append(int(index[4:]))
                            cvdRPinsTemp.append(tempstring)

            cvdRPins = [x for _,x in sorted(zip(cvdRPinsIndex,cvdRPinsTemp))]
            cvdTPins = [x for _,x in sorted(zip(cvdTPinsIndex,cvdTPinsTemp))]
            print(cvdRPins)
            print(cvdTPins)
            self.touchChannelSelf = len(cvdRPins)
            self.touchChannelMutual = len(cvdTPins)
            print(self.touchChannelSelf)
            print(self.touchChannelMutual)
            self.ptcPinValues.append(cvdRPins)
            self.ptcPinValues.append(cvdTPins)
        else:
            if (targetDevice in self.adc_based_acquisition):
                ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/signals")
            else:
                ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")

            self.ptcPinValues = []
            selectablePins =set()
            self.ptcPinValues = ptcSignalsATDF.getChildren()

            for index in range(0, len(self.ptcPinValues)):
                if(self.ptcPinValues[index].getAttribute("group") == "X"):
                    self.xPads.add(self.ptcPinValues[index].getAttribute("pad"))
                elif(self.ptcPinValues[index].getAttribute("group") == "Y"):
                    self.yPads.add(self.ptcPinValues[index].getAttribute("pad"))

            selectablePins = self.xPads.intersection(self.yPads)

            ylen = len(self.yPads)
            xlen = len(self.xPads)
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
            self.touchChannelSelf = 5#ylen 
            self.touchChannelMutual = 5#maxMutuals
            # adust for lump support
            if(lumpsupport):
                self.touchChannelSelf +=16
                self.touchChannelMutual +=16
            # Print results to screen
            if(withConsoleOutput):
                print("====================================================")
                print("Largest non Lump Mutual Config : " + str(maxMutuals))
                print("Lump Supported : "+ str(lumpsupport))
                print("self.touchChannelSelf : " + str(self.touchChannelSelf))
                print("self.touchChannelMutual : " + str(self.touchChannelMutual))
                print("====================================================")
                print("X pins length: " + str(xlen))
                print("X Pins:")
                print(self.xPads)
                print("====================================================")
                print("Y pins length: " + str(ylen))
                print("Y Pins :")
                print(self.yPads)
                print("====================================================")
                print("Selectable pins length: " + str(selLen))
                print("Selectable Pins:")
                print(selectablePins)
                print("====================================================")
        
        return self.ptcPinValues


    def setInterruptVector(self,Database,targetDevice):
        """
        Configures Interrups vectore based on PTC vs ADC support 
        Arguments:
            :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
            :targetDevice :see interface.getDeviceSeries()
        Returns:
            :none
        """
        if targetDevice not in self.picDevices:
            if(targetDevice in self.adc_based_acquisition):
                self.setADCInterruptVector(Database,targetDevice)
            else:
                self.setPTCInterruptVector(Database,targetDevice)

    def initTargetParameters(self,qtouchComponent,touchMenu,targetDevice,Database):
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
        self.setModuleID(qtouchComponent,touchMenu,targetDevice)
        self.setClockXML(qtouchComponent,touchMenu,targetDevice)
        self.setInterruptVector(Database,targetDevice)

if __name__ == "__main__":
    print "adding target device .py file"