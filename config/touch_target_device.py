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
import os.path
import inspect
import json
import xml.etree.ElementTree as ET
from json_loader import json_loader_instance

class classTouchTargetDevice():
    def __init__(self):
        self.xPads = set()
        self.yPads = set()
        self.touchChannelSelf = 0
        self.touchChannelMutual = 0
        self.ptcPinValues =[]
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []
        self.json_data=json_loader_instance.get_data()
        # self.version_data=json_loader_instance.get_version_data()

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

    def getSecureNVICID(self):
        return "NVIC_"+str(self.json_data["acquisition"]["trust_zone"]["nvicid"])+"_0_SECURITY_TYPE"

    def isSecureDevice(self):
        return self.json_data["features"]["trust_zone"]

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
        getModuleID.setDefaultValue(self.json_data["features"]["module_id"])
        

    def setFrontendSymbol(self,qtouchComponent,touchMenu):
        """
        assigns the Clock configuration xml based on targetDevice
        Arguments:
            :qtouchComponent : touchModule
            :touchMenu : parent menu for new symbols
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :none
        """
        version = qtouchComponent.createStringSymbol("ACQ_VERSION", touchMenu)
        version.setVisible(False)
        version.setDefaultValue(json.dumps(self.json_data["node"]["versions"],ensure_ascii=False))

        if self.json_data["features"]["timer_shield"]==True:
            driven_shield = qtouchComponent.createStringSymbol("DRIVEN_SHIELD", touchMenu)
            driven_shield.setVisible(False)
            driven_shield.setDefaultValue(json.dumps(self.json_data["driven_shield"],ensure_ascii=False))

        clock_config = qtouchComponent.createStringSymbol("CLOCK_CONFIG", touchMenu)
        clock_config.setVisible(False)
        clock_config.setDefaultValue(json.dumps(self.json_data["clock_config"],ensure_ascii=False))

        if self.json_data["features"]["core"]!="CVD":
            clock_range = qtouchComponent.createStringSymbol("CLOCK_RANGE", touchMenu)
            clock_range.setVisible(False)
            clock_range.setDefaultValue(json.dumps(self.json_data["node"]["ptc_clock_range"],ensure_ascii=False))

        timer_shield = qtouchComponent.createBooleanSymbol("TIMER_SHIELD", touchMenu)
        timer_shield.setVisible(False)
        timer_shield.setDefaultValue(self.json_data["features"]["timer_shield"])
        
        bi_tune = qtouchComponent.createBooleanSymbol("ENABLE_TOUCH_TUNE_WITH_PLUGIN_BI", touchMenu)
        bi_tune.setVisible(False)
        bi_tune.setDefaultValue(self.json_data["features"]["bidirectionalTune"])

        uni_tune = qtouchComponent.createBooleanSymbol("ENABLE_DATA_STREAMER_UNI", touchMenu)
        uni_tune.setVisible(False)
        uni_tune.setDefaultValue(self.json_data["features"]["unidirectionalTune"])
        
        mutual = qtouchComponent.createBooleanSymbol("MUTUAL_SUPPORT", touchMenu)
        mutual.setVisible(False)
        mutual.setDefaultValue(self.json_data["features"]["mutual"])
 
        lump = qtouchComponent.createBooleanSymbol("LUMP_SUPPORT", touchMenu)
        lump.setVisible(False)
        lump.setDefaultValue(self.json_data["features"]["lump_mode"])

    def setPTCInterruptVector(self,Database,targetDevice):
        """
        assigns the PTC interrupt handler based on targetDevice
        Arguments:
            :Database : MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface#MHCPythonInterface-Database>
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :none
        """
        if (self.json_data["features"]["core"]=="PTC"):
            Database.setSymbolValue("core", "PTC_INTERRUPT_ENABLE", True)
            Database.setSymbolValue("core", "PTC_INTERRUPT_HANDLER", "PTC_Handler")
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
        if(self.json_data["features"]["shared_single_adc"]):
            Database.setSymbolValue("core", "NVIC_13_0_ENABLE", True)
            Database.setSymbolValue("core", "NVIC_13_0_HANDLER", "ADC0_Handler")            

        elif (self.json_data["features"]["core"]=="ADC"):
            Database.setSymbolValue("core", "NVIC_119_0_ENABLE", True)
            Database.setSymbolValue("core", "NVIC_119_0_HANDLER", "ADC0_1_Handler")
        else:
            print ("error - setADCInterruptVector")

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
        if(self.json_data["features"]["core"]=="CVD"):
            Database.clearSymbolValue("core", "CVD_CLOCK_ENABLE")
            Database.setSymbolValue("core", "CVD_CLOCK_ENABLE", True)
        elif (self.json_data["features"]["core"]=="PTC"):
            Database.clearSymbolValue("core", "PTC_CLOCK_ENABLE")
            Database.setSymbolValue("core", "PTC_CLOCK_ENABLE", True)
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
        if (self.json_data["features"]["core"]=="ADC"):
            if (Database.getSymbolValue("core", "GCLK_ID_40_CHEN") == False):
                Database.setSymbolValue("core", "GCLK_ID_40_CHEN", True)
            if (Database.getSymbolValue("core", "ADC0_CLOCK_ENABLE") == False):
                Database.setSymbolValue("core", "ADC0_CLOCK_ENABLE", True)
            Database.clearSymbolValue("core", "GCLK_ID_40_GENSEL")
            Database.setSymbolValue("core", "GCLK_ID_40_GENSEL", 1)
        else:
            print ("error - setADCClock")

    def getDefaultCSDValue(self,targetDevice):
        if (self.json_data["features"]["core"]=="CVD"):
            return 30
        else:
            return 0

    def getAutotuneCSDDisabled(self,targetDevice):
        """Used to determine whether autotune CSD has to be supported or not 
        for devices with CSD feature based on targetDevice.       
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :True or False (boolean)
        """
        if(self.json_data["features"]["csd"] and ("CAL_AUTO_TUNE_CSD" not in self.json_data["acquisition"]["tune_mode"]["component_values"])):
            return 1
        else:
            return 0 

    def getCSDMode(self,targetDevice):
        """Get charge share delay bit resolution based on targetDevice. 
        Used to determine node / acquistion configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            :csd support mode(string)
        """
        if(self.json_data["features"]["csd"]==False):
            return "NoCSD"
        elif(self.json_data["features"]["core"]=="ADC"):
            return "8bitCSD"
        else:
            return "16bitCSD" 

    def getShieldMode(self):
        """Get driven shield mode based on targetDevice. 
        Used to determine node configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            : driven shield support mode(string)
        """

        if(self.json_data["features"]["timer_shield"]):
            return "timer"
        elif(self.json_data["features"]["hardware_shield"]):
            return "hardware"
        else:
            return "none"

    def getLumpSupported(self):
        """Get lumpmode mode support based on targetDevice. 
        Used to determine node configuration
        Arguments:
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            : lump supported (boolean)
        """
        return self.json_data["features"]["lump_mode"]
        # if (targetDevice in self.non_lump_support):
        #     return False
        # else:
        #     return True

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
        ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance@[name=\"PTC\"]/parameters/param@[name=\"GCLK_ID\"]")
        if ptcClockInfo is None:
            ptcClockInfo = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/parameters/param@[name=\"GCLK_ID\"]")
        ptcFreqencyId= qtouchComponent.createStringSymbol("PTC_CLOCK_FREQ", parentSymbol)
        ptcFreqencyId.setLabel("PTC Freqency Id ")
        ptcFreqencyId.setReadOnly(True)
        if(self.json_data["features"]["shared_single_adc"]):
            ptcFreqencyId.setDefaultValue("ADC0_CLOCK_FREQUENCY")
            self.addDepSymbol(ptcFreqencyId, "onPTCClock", ["core."+"ADC0_CLOCK_FREQUENCY"])        
        elif (self.json_data["features"]["core"]!="CVD"):
            ptcFreqencyId.setDefaultValue("GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ")
            self.addDepSymbol(ptcFreqencyId, "onPTCClock", ["core."+"GCLK_ID_"+ptcClockInfo.getAttribute("value")+"_FREQ"])
        else:
            ptcFreqencyId.setDefaultValue("ADCHS_CLOCK_FREQUENCY")
            self.addDepSymbol(ptcFreqencyId, "onPTCClock", ["core."+"ADCHS_CLOCK_FREQUENCY"])

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def setDevicePinValues(self,ATDF,withConsoleOutput, lumpsupport, targetDevice, deviceFullName):
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
        if (self.json_data["features"]["core"]=="CVD"):
            currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
            if targetDevice == "PIC32MZW":
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
            elif targetDevice == "PIC32MZDA":
                if "169" in deviceFullName:
                    pinoutXmlPath = os.path.join(currentPath, "../../csp/peripheral/gpio_02467/plugin/pin_xml/pins/MZ_DA_169LFBGA.xml")
                elif "176" in deviceFullName:
                    pinoutXmlPath = os.path.join(currentPath, "../../csp/peripheral/gpio_02467/plugin/pin_xml/pins/MZ_DA_176LQFP.xml")
                elif "288" in deviceFullName:
                    pinoutXmlPath = os.path.join(currentPath, "../../csp/peripheral/gpio_02467/plugin/pin_xml/pins/MZ_DA_288LFBGA.xml")
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
                            if myFunction.get("name").startswith("AN"):
                                tempstring = myPin.get("name")
                                tempstring = tempstring+"_"+myFunction.get("name")
                                index = myFunction.get("name")
                                print (index)
                                cvdRPinsIndex.append(int(index[2:]))
                                cvdRPinsTemp.append(tempstring)
                cvdRPins = [x for _,x in sorted(zip(cvdRPinsIndex,cvdRPinsTemp))]
                cvdTPins = [x for _,x in sorted(zip(cvdRPinsIndex,cvdRPinsTemp))]
                print(cvdRPins)
                print(cvdTPins)
                self.touchChannelSelf = len(cvdRPins)
                self.touchChannelMutual = len(cvdTPins)
                print(self.touchChannelSelf)
                print(self.touchChannelMutual)
                self.ptcPinValues.append(cvdRPins)
                self.ptcPinValues.append(cvdTPins)
            elif json_loader_instance.get_architecture()=="cm4":
                ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"CVD\"]/instance/signals")
                self.ptcPinValues = []
                selectablePins =set()
                self.ptcPinValues = ptcSignalsATDF.getChildren()
                print(self.ptcPinValues, len(self.ptcPinValues))
                sortedptcPinValues = []

                # sort the pins list by index
                for found in range(256):
                    for idx in range(0, len(self.ptcPinValues)):
                        if (self.ptcPinValues[idx].getAttribute("group") in ["CVDR", "CVDT"]):
                            if (int(self.ptcPinValues[idx].getAttribute("index")) == found):
                                sortedptcPinValues.append(self.ptcPinValues[idx])
                self.ptcPinValues = sortedptcPinValues

                for index in range(0, len(self.ptcPinValues)):
                    if(self.ptcPinValues[index].getAttribute("group") == "CVDT"):
                        self.xPads.add(self.ptcPinValues[index].getAttribute("pad"))
                    elif(self.ptcPinValues[index].getAttribute("group") == "CVDR"):
                        self.yPads.add(self.ptcPinValues[index].getAttribute("pad"))

                selectablePins = self.xPads.intersection(self.yPads)
                ylen = len(self.yPads)
                xlen = len(self.xPads)
                selLen = len(selectablePins)
                # Determine largest Mutual config
                maxMutuals = 0

                if(selLen ==0):
                    maxMutuals = ylen *xlen
                elif(selLen == xlen and xlen == ylen): #Full Mux
                    maxMutuals = (ylen/2) * (xlen/2)
                elif(ylen >= xlen):                     #Partial 1 more y than x
                    maxMutuals = xlen * (ylen-selLen)
                else:                                   #Partial 2 more x than y
                    maxMutuals = ylen * (xlen-selLen)
                
                # set the global counts for self and mutual
                self.touchChannelSelf = ylen 
                self.touchChannelMutual = maxMutuals

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

        else:
            if (self.json_data["features"]["core"]=="ADC"):
                ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC0\"]/signals")
            else:
                ptcSignalsATDF = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PTC\"]/instance/signals")

            self.ptcPinValues = []
            selectablePins =set()
            self.ptcPinValues = ptcSignalsATDF.getChildren()
            sortedptcPinValues = []
            # sort the pins list by index
            for found in range(0, 256):#len(self.ptcPinValues)):
                for idx in range(0, len(self.ptcPinValues)):
                    if (self.ptcPinValues[idx].getAttribute("group") in ["X", "Y"]):
                        if (int(self.ptcPinValues[idx].getAttribute("index")) == found):
                            sortedptcPinValues.append(self.ptcPinValues[idx])
                    elif (self.ptcPinValues[idx].getAttribute("group") in ["DRV"]):
                        if (int(self.ptcPinValues[idx].getAttribute("index")) == found):
                            sortedptcPinValues.append(self.ptcPinValues[idx])
                    elif (self.ptcPinValues[idx].getAttribute("group") in ["AIN"]):
                        if (int(self.ptcPinValues[idx].getAttribute("index")) == found):
                            sortedptcPinValues.append(self.ptcPinValues[idx])
            self.ptcPinValues = sortedptcPinValues

            for index in range(0, len(self.ptcPinValues)):
                if(self.ptcPinValues[index].getAttribute("group") == "X"):
                    self.xPads.add(self.ptcPinValues[index].getAttribute("pad"))
                elif(self.ptcPinValues[index].getAttribute("group") == "Y"):
                    self.yPads.add(self.ptcPinValues[index].getAttribute("pad"))
                elif(self.ptcPinValues[index].getAttribute("group") == "DRV"):
                    self.xPads.add(self.ptcPinValues[index].getAttribute("pad"))
                    self.yPads.add(self.ptcPinValues[index].getAttribute("pad"))
                elif(self.ptcPinValues[index].getAttribute("group") == "AIN"):
                    self.xPads.add(self.ptcPinValues[index].getAttribute("pad"))
                    self.yPads.add(self.ptcPinValues[index].getAttribute("pad"))

            selectablePins = self.xPads.intersection(self.yPads)

            ylen = len(self.yPads)
            xlen = len(self.xPads)
            selLen = len(selectablePins)
            # Determine largest Mutual config
            maxMutuals = 0

            if(selLen ==0):
                maxMutuals = ylen *xlen
            elif(selLen == xlen and xlen == ylen): #Full Mux
                maxMutuals = (ylen/2) * (xlen/2)
            elif(ylen >= xlen):                     #Partial 1 more y than x
                maxMutuals = xlen * (ylen-selLen)
            else:                                   #Partial 2 more x than y
                maxMutuals = ylen * (xlen-selLen)
            
            # set the global counts for self and mutual
            self.touchChannelSelf = ylen 
            self.touchChannelMutual = maxMutuals
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
        if (self.json_data["features"]["core"]!="CVD"):
            if(self.json_data["features"]["core"]=="ADC"):
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
        # self.setClockXML(qtouchComponent,touchMenu,targetDevice)
        self.setFrontendSymbol(qtouchComponent,touchMenu)
        self.setInterruptVector(Database,targetDevice)
        if(self.json_data["features"]["shared_single_adc"]):
            Database.clearSymbolValue("core", "ADC0_CLOCK_ENABLE")
            Database.setSymbolValue("core", "ADC0_CLOCK_ENABLE", True)
            self.setPTCClockEnable(Database, targetDevice)

        elif(self.json_data["features"]["core"]=="ADC"):
            self.setADCClock(Database,targetDevice)

        else:
            self.setPTCClockEnable(Database, targetDevice)
            #self.setPTCClock(Database, targetDevice)

if __name__ == "__main__":
    print "adding target device .py file"
