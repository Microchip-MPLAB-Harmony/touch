"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
def setBoostModeFiles(configName, qtouchComponent, targetDevice):
    """
    Generates as List of source files required for Acquisition
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        fileList: list of file symbols
    """
    fileList = []
    fileList.append(setBoostModeLibraryFile(configName, qtouchComponent, targetDevice))
    fileList.append(setBoostModeHeaderFile(configName, qtouchComponent, targetDevice))
    return fileList

def setBoostModeLibraryFile(configName, qtouchComponent, targetDevice):
    touchAcq4pLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_4P_LIB", None)
    touchAcq4pLibraryFile.setDestPath("/touch/lib/")
    touchAcq4pLibraryFile.setEnabled(False)
    touchAcq4pLibraryFile.setDependencies(libChangeBoostMode,["ENABLE_BOOST"])

    if(targetDevice == "SAML10"):
        touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_saml10_0x0033.X.a")
        touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_saml10_0x0033.X.a")
    elif(targetDevice == "SAML11"):
        touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_saml11_0x0033.X.a")
        touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_saml11_0x0033.X.a")
    elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
        touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_pic32cm_le_0x0041.X.a")
        touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_pic32cm_le_0x0041.X.a")
    else:
        touchAcq4pLibraryFile.setSourcePath("Error_setBoostModeLibraryFile")
        touchAcq4pLibraryFile.setOutputName("Error_setBoostModeLibraryFile")
    return touchAcq4pLibraryFile

def setBoostModeHeaderFile(configName, qtouchComponent, targetDevice):
    touchAcq4pHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_4P_HEADER", None)
    touchAcq4pHeaderFile.setDestPath("/touch/")
    touchAcq4pHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchAcq4pHeaderFile.setType("HEADER")
    touchAcq4pHeaderFile.setMarkup(False)
    touchAcq4pHeaderFile.setDependencies(libChangeBoostMode,["ENABLE_BOOST"])
    if(targetDevice == "SAML10"):
        touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_saml10_0x0033_api.h")
        touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_saml10_0x0033_api.h")
    elif(targetDevice == "SAML11"):
        touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_saml11_0x0033_api.h")
        touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_saml11_0x0033_api.h")
    elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
        touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_pic32cm_le_0x0041_api.h")
        touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_pic32cm_le_0x0041_api.h")
    else:
        touchAcq4pHeaderFile.setSourcePath("Error_setBoostModeHeaderFile")
        touchAcq4pHeaderFile.setOutputName("Error_setBoostModeHeaderFile")
    return touchAcq4pHeaderFile


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