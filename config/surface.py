def enableSurface1TFiles(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("TOUCH_SURFACE1T_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_SURFACE1T_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_SURFACE2T_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_SURFACE2T_HEADER").setEnabled(False)
    else:
        component.getSymbolByID("TOUCH_SURFACE1T_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_SURFACE1T_HEADER").setEnabled(False)
        
def enableSurface2TFiles(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        component.getSymbolByID("TOUCH_SURFACE2T_LIB").setEnabled(True)
        component.getSymbolByID("TOUCH_SURFACE2T_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_SURFACE1T_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_SURFACE1T_HEADER").setEnabled(False)
    else:
        component.getSymbolByID("TOUCH_SURFACE2T_LIB").setEnabled(False)
        component.getSymbolByID("TOUCH_SURFACE2T_HEADER").setEnabled(False)

############################################################################
#### Code Generation ####
############################################################################
#SURFACE 1T
if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
    # Library File
    surface1TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE1T_LIB", None)
    surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_cm4_0x0021.X.a")
    surface1TLibraryFile.setOutputName("qtm_surface_cs_cm4_0x0021.X.a")
    surface1TLibraryFile.setDestPath("/touch/lib/")
    surface1TLibraryFile.setEnabled(False)
elif(getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
    surface1TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE1T_LIB", None)
    surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_cm23_0x0021.X.a")
    surface1TLibraryFile.setOutputName("qtm_surface_cs_cm23_0x0021.X.a")
    surface1TLibraryFile.setDestPath("/touch/lib/")
    surface1TLibraryFile.setEnabled(False)
elif (getDeviceName.getDefaultValue() in ["PIC32MZW"]):
    # Library File
    surface1TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE1T_LIB", None)
    surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_pic32mz_0x0021.X.a")
    surface1TLibraryFile.setOutputName("qtm_surface_cs_pic32mz_0x0021.X.a")
    surface1TLibraryFile.setDestPath("/touch/lib/")
    surface1TLibraryFile.setEnabled(False)
else:
    # Library File
    surface1TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE1T_LIB", None)
    surface1TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_cm0p_0x0021.X.a")
    surface1TLibraryFile.setOutputName("qtm_surface_cs_cm0p_0x0021.X.a")
    surface1TLibraryFile.setDestPath("/touch/lib/")
    surface1TLibraryFile.setEnabled(False)
# Header File
surface1THeaderFile = qtouchComponent.createFileSymbol("TOUCH_SURFACE1T_HEADER", None)
surface1THeaderFile.setSourcePath("/src/qtm_surface_cs_0x0021_api.h")
surface1THeaderFile.setOutputName("qtm_surface_cs_0x0021_api.h")
surface1THeaderFile.setDestPath("/touch/")
surface1THeaderFile.setProjectPath("config/" + configName + "/touch/")
surface1THeaderFile.setType("HEADER")
surface1THeaderFile.setMarkup(False)
surface1THeaderFile.setEnabled(False)

#SURFACE 2T
if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
    # Library File
    surface2TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE2T_LIB", None)
    surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_cm4_0x0025.X.a")
    surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_cm4_0x0025.X.a")
    surface2TLibraryFile.setDestPath("/touch/lib/")
    surface2TLibraryFile.setEnabled(False)
elif (getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
    # Library File
    surface2TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE2T_LIB", None)
    surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_cm23_0x0025.X.a")
    surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_cm23_0x0025.X.a")
    surface2TLibraryFile.setDestPath("/touch/lib/")
    surface2TLibraryFile.setEnabled(False)
elif (getDeviceName.getDefaultValue() in ["PIC32MZW"]):
    # Library File
    surface2TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE2T_LIB", None)
    surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_pic32mz_0x0025.X.a")
    surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_pic32mz_0x0025.X.a")
    surface2TLibraryFile.setDestPath("/touch/lib/")
    surface2TLibraryFile.setEnabled(False)
else:
    # Library File
    surface2TLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_SURFACE2T_LIB", None)
    surface2TLibraryFile.setSourcePath("/src/libraries/qtm_surface_cs_2t_cm0p_0x0025.X.a")
    surface2TLibraryFile.setOutputName("qtm_surface_cs_2t_cm0p_0x0025.X.a")
    surface2TLibraryFile.setDestPath("/touch/lib/")
    surface2TLibraryFile.setEnabled(False)
# Header File
surface2THeaderFile = qtouchComponent.createFileSymbol("TOUCH_SURFACE2T_HEADER", None)
surface2THeaderFile.setSourcePath("/src/qtm_surface_cs2t_0x0025_api.h")
surface2THeaderFile.setOutputName("qtm_surface_cs2t_0x0025_api.h")
surface2THeaderFile.setDestPath("/touch/")
surface2THeaderFile.setProjectPath("config/" + configName + "/touch/")
surface2THeaderFile.setType("HEADER")
surface2THeaderFile.setMarkup(False)
surface2THeaderFile.setEnabled(False)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    qtouchFilesArray.append(surface1THeaderFile)
    qtouchFilesArray.append(surface1TLibraryFile)
    qtouchFilesArray.append(surface2THeaderFile)
    qtouchFilesArray.append(surface2TLibraryFile)

################################################################################
#### Components ####
################################################################################

surfaceMenu = qtouchComponent.createMenuSymbol("SURFACE_MENU", enableSurfaceMenu)
surfaceMenu.setLabel("Surface Configuration")
surfaceMenu.setDescription("Configure Surface")

# Enable Surface1T 
enableSurface1T = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE1T", surfaceMenu)
enableSurface1T.setLabel("Enable Surface 1T")
enableSurface1T.setDefaultValue(False)
enableSurface1T.setDependencies(enableSurface1TFiles,["ENABLE_SURFACE1T"])

# Enable Surface2T 
enableSurface2T = qtouchComponent.createBooleanSymbol("ENABLE_SURFACE2T", surfaceMenu)
enableSurface2T.setLabel("Enable Surface 2T")
enableSurface2T.setDefaultValue(False)
enableSurface2T.setDependencies(enableSurface2TFiles,["ENABLE_SURFACE2T"])

#Surface Parameters
global horiStartKey
horiStartKey = qtouchComponent.createIntegerSymbol("HORI_START_KEY", surfaceMenu)
horiStartKey.setLabel("Horizontal Start Key")
horiStartKey.setDefaultValue(0)
horiStartKey.setMin(0)
horiStartKey.setMax(touchKeyCountMax)
horiStartKey.setDescription("Start key of horizontal axis.")
global horiNumKey
horiNumKey = qtouchComponent.createIntegerSymbol("HORI_NUM_KEY", surfaceMenu)
horiNumKey.setLabel("Horizontal Number of Channel")
horiNumKey.setDefaultValue(2)
horiNumKey.setMin(0)
horiNumKey.setMax(255)
horiNumKey.setDescription("Number of Channels forming horizontal axis.")
global vertStartKey
vertStartKey = qtouchComponent.createIntegerSymbol("VERT_START_KEY", surfaceMenu)
vertStartKey.setLabel("Vertical Start Key")
vertStartKey.setDefaultValue(2)
vertStartKey.setMin(0)
vertStartKey.setMax(touchKeyCountMax)
vertStartKey.setDescription("Start key of Vertical axis.")
global vertNumKey
vertNumKey = qtouchComponent.createIntegerSymbol("VERT_NUM_KEY", surfaceMenu)
vertNumKey.setLabel("Vertical Number of Channel")
vertNumKey.setDefaultValue(2)
vertNumKey.setMin(0)
vertNumKey.setMax(255)
vertNumKey.setDescription("Number of Channels forming Vertical axis.")

#Surface Position Resolution
positionResol = qtouchComponent.createKeyValueSetSymbol("DEF_POS_RESOLUTION", surfaceMenu)
positionResol.setLabel("Position Resolution ")
positionResol.addKey("RESOL_2_BIT","RESOL_2_BIT","2 Bit")
positionResol.addKey("RESOL_3_BIT","RESOL_3_BIT","3 Bit")
positionResol.addKey("RESOL_4_BIT","RESOL_4_BIT","4 Bit")
positionResol.addKey("RESOL_5_BIT","RESOL_5_BIT","5 Bit")
positionResol.addKey("RESOL_6_BIT","RESOL_6_BIT","6 Bit")
positionResol.addKey("RESOL_7_BIT","RESOL_7_BIT","7 Bit")
positionResol.addKey("RESOL_8_BIT","RESOL_8_BIT","8 Bit")
positionResol.addKey("RESOL_9_BIT","RESOL_9_BIT","9 Bit")
positionResol.addKey("RESOL_10_BIT","RESOL_10_BIT","10 Bit")
positionResol.addKey("RESOL_11_BIT","RESOL_11_BIT","11 Bit")
positionResol.addKey("RESOL_12_BIT","RESOL_12_BIT","12 Bit")
positionResol.setDefaultValue(6)
positionResol.setOutputMode("Value")
positionResol.setDisplayMode("Key")
positionResol.setDescription("Full scale position resolution reported for the axis. Options are RESOL_2_BIT - RESOL_12_BIT")

#Surface Deadband
deadbandPercent = qtouchComponent.createKeyValueSetSymbol("DEF_DEADBAND_PERCENT", surfaceMenu)
deadbandPercent.setLabel("Deadband Percentage")
deadbandPercent.addKey("DB_NONE", "DB_NONE", "no deadband")
deadbandPercent.addKey("DB_1_PERCENT", "DB_1_PERCENT", "1 Percent")
deadbandPercent.addKey("DB_2_PERCENT", "DB_2_PERCENT", "2 Percent")
deadbandPercent.addKey("DB_3_PERCENT", "DB_3_PERCENT", "3 Percent")
deadbandPercent.addKey("DB_4_PERCENT", "DB_4_PERCENT", "4 Percent")
deadbandPercent.addKey("DB_5_PERCENT", "DB_5_PERCENT", "5 Percent")
deadbandPercent.addKey("DB_6_PERCENT", "DB_6_PERCENT", "6 Percent")
deadbandPercent.addKey("DB_7_PERCENT", "DB_7_PERCENT", "7 Percent")
deadbandPercent.addKey("DB_8_PERCENT", "DB_8_PERCENT", "8 Percent")
deadbandPercent.addKey("DB_9_PERCENT", "DB_9_PERCENT", "9 Percent")
deadbandPercent.addKey("DB_10_PERCENT", "DB_10_PERCENT", "10 Percent")
deadbandPercent.addKey("DB_11_PERCENT", "DB_11_PERCENT", "11 Percent")
deadbandPercent.addKey("DB_12_PERCENT", "DB_12_PERCENT", "12 Percent")
deadbandPercent.addKey("DB_13_PERCENT", "DB_13_PERCENT", "13 Percent")
deadbandPercent.addKey("DB_14_PERCENT", "DB_14_PERCENT", "14 Percent")
deadbandPercent.addKey("DB_15_PERCENT", "DB_15_PERCENT", "15 Percent")
deadbandPercent.setDefaultValue(1)
deadbandPercent.setOutputMode("Value")
deadbandPercent.setDisplayMode("Key")
deadbandPercent.setDescription("Size of the edge correction deadbands as a percentage of the full scale range. Options are DB_1_PERCENT - DB_15_PERCENT")

medianFilter = qtouchComponent.createIntegerSymbol("EANBLE_MED_FILTER", surfaceMenu)
medianFilter.setLabel("Median Filter")
medianFilter.setMin(0)
medianFilter.setMax(1)
medianFilter.setDefaultValue(1)
medianFilter.setDescription("Enable or Disable Median Filter. Enable- 1, Disable - 0")

iirFilter = qtouchComponent.createIntegerSymbol("EANBLE_IIR_FILTER", surfaceMenu)
iirFilter.setLabel("IIR Filter")
iirFilter.setMin(0)
iirFilter.setMax(3)
iirFilter.setDefaultValue(3)
iirFilter.setDescription("Configure IIR filter. 0 - None, 1 - 25%, 2 - 50%, 3 - 75%")

#Position Hysterisis
posHysterisis = qtouchComponent.createIntegerSymbol("DEF_POS_HYS", surfaceMenu)
posHysterisis.setLabel("Surface Position Hysterisis")
posHysterisis.setDefaultValue(3)
posHysterisis.setMin(0)
posHysterisis.setMax(255)
posHysterisis.setDescription("The minimum travel distance to be reported after contact or direction change. Applicable to Horizontal and Vertical directions")

#Contact min threshold
contactMinThreshold = qtouchComponent.createIntegerSymbol("DEF_CONTACT_THRESHOLD", surfaceMenu)
contactMinThreshold.setLabel("Surface Detect threshold")
contactMinThreshold.setDefaultValue(60)
contactMinThreshold.setMin(0)
contactMinThreshold.setMax(65535)
contactMinThreshold.setDescription("The minimum contact size measurement for persistent contact tracking. Contact size is the sum of neighbouring keys' touch deltas forming the touch contact.")

