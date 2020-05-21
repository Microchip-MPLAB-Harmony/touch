
import xml.etree.ElementTree as ET
import os.path
import inspect

################################################################################
#### Global Variables ####
################################################################################
touchChannelCountMax =totalChannelCountMutl.getValue()

################################################################################
#### Component ####
################################################################################
nodeMenu = qtouchComponent.createMenuSymbol("NODE_MENU", touchMenu)
nodeMenu.setLabel("Node Configuration")
global touchNumChannel
# Touch Channel Enable Count
touchNumChannel = qtouchComponent.createIntegerSymbol("TOUCH_CHAN_ENABLE_CNT", nodeMenu)
touchNumChannel.setLabel("Number of Channels to enable")
touchNumChannel.setDefaultValue(0)
touchNumChannel.setMin(0)
touchNumChannel.setMax(touchChannelCountMax)

tchSelfPinSelection = []
tchMutXPinSelection = []
tchMutYPinSelection = []
tchCVDPinSelection = []
cvdTPins = []
cvdRPins = []
cvdTPinsTemp = []
cvdRPinsTemp = []
cvdTPinsIndex = []
cvdRPinsIndex = []

currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
pinoutXmlPath = os.path.join(currentPath, "../../csp/peripheral/gpio_02467/plugin/pin_xml/pins/MZ_W1_132.xml")
tree = ET.parse(pinoutXmlPath)
root = tree.getroot()
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

for channelID in range(0, touchChannelCountMax):

    touchChEnable = qtouchComponent.createBooleanSymbol("TOUCH_ENABLE_CH_" + str(channelID), nodeMenu)
    touchChEnable.setLabel("Use touch channel " + str(channelID))

    tchSelfPinSelection.append(qtouchComponent.createKeyValueSetSymbol("SELFCAP-INPUT_"+ str(channelID), touchChEnable))
    tchSelfPinSelection[channelID].setLabel("Select Y Pin for Channel "+ str(channelID))
    tchSelfPinSelection[channelID].setDefaultValue(0)
    tchSelfPinSelection[channelID].setOutputMode("Key")
    tchSelfPinSelection[channelID].setDisplayMode("Description")
    for index in range(0, len(cvdRPins)):
        tchSelfPinSelection[channelID].addKey("Y("+str(index+1)+")",
        str(index+1),
        "Y"+str(index+1)+"  ("+cvdRPins[index]+")")

    tchMutXPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-X-INPUT_"+ str(channelID), touchChEnable))
    tchMutXPinSelection[channelID].setLabel("Select X Pin for Channel "+ str(channelID))
    tchMutXPinSelection[channelID].setDefaultValue(0)
    tchMutXPinSelection[channelID].setOutputMode("Key")
    tchMutXPinSelection[channelID].setDisplayMode("Description")
    for index in range(0, len(cvdTPins)):
        tchMutXPinSelection[channelID].addKey("X("+str(index)+")",
        str(index),
        "X"+str(index)+"  ("+cvdTPins[index]+")")

    tchMutYPinSelection.append(qtouchComponent.createKeyValueSetSymbol("MUTL-Y-INPUT_"+ str(channelID), touchChEnable))
    tchMutYPinSelection[channelID].setLabel("Select Y Pin for Channel "+ str(channelID))
    tchMutYPinSelection[channelID].setDefaultValue(0)
    tchMutYPinSelection[channelID].setOutputMode("Key")
    tchMutYPinSelection[channelID].setDisplayMode("Description")
    for index in range(0, len(cvdRPins)):
        tchMutYPinSelection[channelID].addKey("Y("+str(index+1)+")",
        str(index+1),
        "Y"+str(index+1)+"  ("+cvdRPins[index]+")")

    #Charge Share Delay
    touchSym_CSD_Val = qtouchComponent.createIntegerSymbol("DEF_TOUCH_CHARGE_SHARE_DELAY" + str(channelID), touchChEnable)
    touchSym_CSD_Val.setLabel("Additional Charge Share Delay")
    touchSym_CSD_Val.setDefaultValue(0)
    touchSym_CSD_Val.setMin(0)
    touchSym_CSD_Val.setMax(255)
    touchSym_CSD_Val.setDescription("Increase in Charge Share Delay increases sensor charging time and so the touch measurement time. It indicates the number of additional cycles that are inserted within a touch measurement cycle.")

    #Analog Gain
    touchSym_ANALOG_GAIN_Val = qtouchComponent.createKeyValueSetSymbol("DEF_NOD_GAIN_ANA" + str(channelID), touchChEnable)
    touchSym_ANALOG_GAIN_Val.setLabel("Analog Gain")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN1", "GAIN_1", "1")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN2", "GAIN_2", "2")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN4", "GAIN_4", "4")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN8", "GAIN_8", "8")
    touchSym_ANALOG_GAIN_Val.addKey("ANA_GAIN16", "GAIN_16", "16")
    touchSym_ANALOG_GAIN_Val.setDefaultValue(0)
    touchSym_ANALOG_GAIN_Val.setOutputMode("Value")
    touchSym_ANALOG_GAIN_Val.setDisplayMode("Description")
    touchSym_ANALOG_GAIN_Val.setDescription("Gain setting for touch delta value.Higher gain setting increases touch delta as well as noise.So, optimum gain setting should be used.Gain should be tuned such that the touch delta is between 40~60 counts.")
	
    #Digital Filter Gain - Accumulated sum is scaled to Digital Gain
    touchSym_DIGI_FILT_GAIN_Val = qtouchComponent.createKeyValueSetSymbol("DEF_DIGI_FILT_GAIN"  + str(channelID), touchChEnable)
    touchSym_DIGI_FILT_GAIN_Val.setLabel("Digital Filter Gain")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN1", "GAIN_1", "1")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN2", "GAIN_2", "2")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN4", "GAIN_4", "4")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN8", "GAIN_8", "8")
    touchSym_DIGI_FILT_GAIN_Val.addKey("GAIN16", "GAIN_16", "16")
    touchSym_DIGI_FILT_GAIN_Val.setDefaultValue(0)
    touchSym_DIGI_FILT_GAIN_Val.setOutputMode("Value")
    touchSym_DIGI_FILT_GAIN_Val.setDisplayMode("Description")
    touchSym_DIGI_FILT_GAIN_Val.setDescription("Gain setting for touch delta value. Higher gain setting increases touch delta as well as noise. So, optimum gain setting should be used.Gain should be tuned such that the touch delta is between 40~60 counts. ")
	
    #Digital Filter Oversampling - Number of samples for each measurement
    touchSym_DIGI_FILT_OVERSAMPLING_Val = qtouchComponent.createKeyValueSetSymbol("DEF_DIGI_FILT_OVERSAMPLING" + str(channelID), touchChEnable)
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setLabel("Digital Filter Oversampling")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE1", "FILTER_LEVEL_1", "1 sample")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE2", "FILTER_LEVEL_2", "2 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE4", "FILTER_LEVEL_4", "4 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE8", "FILTER_LEVEL_8", "8 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE16", "FILTER_LEVEL_16", "16 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE32", "FILTER_LEVEL_32", "32 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.addKey("DF_OVERSAMPLE64", "FILTER_LEVEL_64", "64 samples")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setDefaultValue(4)
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setOutputMode("Value")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setDisplayMode("Description")
    touchSym_DIGI_FILT_OVERSAMPLING_Val.setDescription("Defines the number of samples taken for each measurement.Higher filter level settings, for each measurements more number of samples taken which helps to average out the noise.Higher filter level settings takes long time to do a touch measurement which affects response time.So, start with default value and increase depends on noise levels.")