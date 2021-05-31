"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
def setAcquisitionFiles(configName, qtouchComponent, targetDevice):
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
    # touchAcqLibraryFile
    fileList.append(setAcquisitionLibraryFile(configName, qtouchComponent, targetDevice))
    # touchAcqAutoLibraryFile
    fileList.append(setAutoAcquisitionLibraryFile(configName, qtouchComponent, targetDevice))
    # touchBindLibraryFile
    fileList.append(setBindLibraryFile(configName, qtouchComponent, targetDevice))
    # touchAcqHeaderFile
    fileList.append(setAcqHeaderFile(configName, qtouchComponent, targetDevice))
    # touchAcqHeaderFile2 (some devices)
    if(targetDevice in set(["SAMDA1","SAMHA1","SAMC20","SAMD51","SAME51","SAME53"])):
       fileList.append(setAcqHeaderFile2(configName, qtouchComponent, targetDevice))
    # touchBindHeaderFile
    fileList.append(setBindHeaderFile(configName, qtouchComponent, targetDevice))
    # touchCommonHeaderFile
    fileList.append(setCommonHeaderFile(configName, qtouchComponent, targetDevice))
    return fileList


def setBindHeaderFile(configName, qtouchComponent, targetDevice):
    """
    Generates binding layer header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchBindHeaderFile = qtouchComponent.createFileSymbol("TOUCH_BIND_HEADER", None)
    touchBindHeaderFile.setDestPath("/touch/")
    touchBindHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchBindHeaderFile.setType("HEADER")
    touchBindHeaderFile.setMarkup(False)
    touchBindHeaderFile.setEnabled(False)
    touchBindHeaderFile.setSourcePath("/src/qtm_binding_layer_0x0005_api.h")
    touchBindHeaderFile.setOutputName("qtm_binding_layer_0x0005_api.h")
    return touchBindHeaderFile

def setCommonHeaderFile(configName, qtouchComponent, targetDevice):
    """
    Generates common components api header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchCommonHeaderFile = qtouchComponent.createFileSymbol("TOUCH_COMMON_HEADER", None)
    touchCommonHeaderFile.setSourcePath("/src/qtm_common_components_api.h")
    touchCommonHeaderFile.setOutputName("qtm_common_components_api.h")
    touchCommonHeaderFile.setDestPath("/touch/")
    touchCommonHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchCommonHeaderFile.setType("HEADER")
    touchCommonHeaderFile.setMarkup(False)
    return touchCommonHeaderFile

def setAcquisitionLibraryFile(configName, qtouchComponent, targetDevice):
    """
    Generates acquisition library file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchAcqLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_LIB", None)   
    touchAcqLibraryFile.setDestPath("/touch/lib/")
    touchAcqLibraryFile.setEnabled(True)
    touchAcqLibraryFile.setDependencies(enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])

    if (targetDevice == "SAMC21"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samc21_0x0020.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samc21_0x0020.X.a")
    elif(targetDevice == "SAMC20"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samc20_0x0020.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samc20_0x0020.X.a")
    elif(targetDevice == "SAMD10"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd10_0x0009.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd10_0x0009.X.a")
    elif(targetDevice == "SAMD11"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd11_0x0009.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd11_0x0009.X.a")
    elif(targetDevice == "SAMD20"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd20_0x000e.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd20_0x000e.X.a")
    elif(targetDevice == "SAMD21"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
    elif(targetDevice == "SAMDA1"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
    elif(targetDevice == "SAMHA1"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
    elif(targetDevice == "SAMD51"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd51_0x000f.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_samd51_0x000f.X.a")
    elif(targetDevice == "SAME51"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_same51_0x000f.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_same51_0x000f.X.a")
    elif(targetDevice == "SAME53"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_same53_0x000f.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_same53_0x000f.X.a")
    elif(targetDevice == "SAME54"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_same54_0x000f.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_same54_0x000f.X.a")
    elif(targetDevice == "SAML10"):
        touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml10_0x0027.X.a")
        touchAcqLibraryFile.setOutputName("qtm_acq_saml10_0x0027.X.a")
    else:
        touchAcqLibraryFile.setSourcePath("Error_setAcquisitionLibraryFile")
        touchAcqLibraryFile.setOutputName("Error_setAcquisitionLibraryFile")
    return touchAcqLibraryFile

def setAutoAcquisitionLibraryFile(configName, qtouchComponent, targetDevice):
    """
    Generates auto acquisition library file per device
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB", None)    
    touchAcqAutoLibraryFile.setDestPath("/touch/lib/")
    touchAcqAutoLibraryFile.setEnabled(False)
    touchAcqAutoLibraryFile.setDependencies(enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])

    if (targetDevice == "SAMC21"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samc21_0x0020.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samc21_0x0020.X.a")
    elif(targetDevice == "SAMC20"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samc20_0x0020.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samc20_0x0020.X.a")
    elif(targetDevice == "SAMD10"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd10_0x0009.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd10_0x0009.X.a")
    elif(targetDevice == "SAMD11"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd11_0x0009.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd11_0x0009.X.a")
    elif(targetDevice == "SAMD20"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd20_0x000e.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd20_0x000e.X.a")
    elif(targetDevice == "SAMD21"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
    elif(targetDevice == "SAMDA1"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
    elif(targetDevice == "SAMHA1"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd21_0x0024.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd21_0x0024.X.a")
    elif(targetDevice == "SAMD51"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_samd51_0x000f.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_samd51_0x000f.X.a")
    elif(targetDevice == "SAME51"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_same51_0x000f.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_same51_0x000f.X.a")
    elif(targetDevice == "SAME53"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_same53_0x000f.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_same53_0x000f.X.a")
    elif(targetDevice == "SAME54"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_same54_0x000f.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_same54_0x000f.X.a")
    elif(targetDevice == "SAML10"):
        touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml10_0x0027.X.a")
        touchAcqAutoLibraryFile.setOutputName("qtm_acq_saml10_0x0027.X.a")
    else:
        touchAcqAutoLibraryFile.setOutputName("Error_setAutoAcquisitionLibraryFile")
        touchAcqAutoLibraryFile.setOutputName("Error_setAutoAcquisitionLibraryFile")
    return touchAcqAutoLibraryFile

def setBindLibraryFile(configName, qtouchComponent, targetDevice):
    """
    Generates binding layer library file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchBindLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_BIND_LIB", None)
    touchBindLibraryFile.setDestPath("/touch/lib/")
    touchBindLibraryFile.setEnabled(False)

    if (targetDevice in set(["SAMC21","SAMC20","SAMD10","SAMD11","SAMD20","SAMD21","SAMDA1","SAMHA1"]) ):
        touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm0p_0x0005.X.a")
        touchBindLibraryFile.setOutputName("qtm_binding_layer_cm0p_0x0005.X.a")
    elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
        touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm4_0x0005.X.a")
        touchBindLibraryFile.setOutputName("qtm_binding_layer_cm4_0x0005.X.a")
    elif(targetDevice in set(["SAML10"])):
        touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm23_0x0005.X.a")
        touchBindLibraryFile.setOutputName("qtm_binding_layer_cm23_0x0005.X.a")
    else:
        touchBindLibraryFile.setOutputName("Error_setBindLibraryFile")
        touchBindLibraryFile.setOutputName("Error_setBindLibraryFile")
    return touchBindLibraryFile

def setAcqHeaderFile(configName, qtouchComponent, targetDevice):
    """
    Generates acquisition api header file per device
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchAcqHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER", None)
    touchAcqHeaderFile.setDestPath("/touch/")
    touchAcqHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchAcqHeaderFile.setType("HEADER")
    touchAcqHeaderFile.setMarkup(False)

    if (targetDevice == "SAMC21"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samc21_0x0020_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samc21_0x0020_api.h")
    elif(targetDevice == "SAMC20"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samc20_0x0020_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samc20_0x0020_api.h")
    elif(targetDevice in set(["SAMD10","SAMD11"])):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samd1x_0x0009_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samd1x_0x0009_api.h")
    elif(targetDevice == "SAMD20"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samd20_0x000e_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samd20_0x000e_api.h")
    elif(targetDevice == "SAMD21"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samd21_0x0024_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samd21_0x0024_api.h")
    elif(targetDevice == "SAMDA1"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samda1_0x0024_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samda1_0x0024_api.h")
    elif(targetDevice == "SAMHA1"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samha1_0x0024_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samha1_0x0024_api.h")
    elif(targetDevice == "SAMD51"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_samd51_0x000f_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_samd51_0x000f_api.h")
    elif(targetDevice == "SAME51"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_same51_0x000f_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_same51_0x000f_api.h")
    elif(targetDevice == "SAME53"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_same53_0x000f_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_same53_0x000f_api.h")
    elif(targetDevice == "SAME54"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_same54_0x000f_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_same54_0x000f_api.h")
    elif(targetDevice == "SAML10"):
        touchAcqHeaderFile.setSourcePath("/src/qtm_acq_saml10_0x0027_api.h")
        touchAcqHeaderFile.setOutputName("qtm_acq_saml10_0x0027_api.h")
    else:
        touchAcqHeaderFile.setSourcePath("Error_setAcqHeaderFile")
        touchAcqHeaderFile.setOutputName("Error_setAcqHeaderFile")
    return touchAcqHeaderFile

def setAcqHeaderFile2(configName, qtouchComponent, targetDevice):
    """
    Generates 2nd acquisition header file (required for some devices)
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchAcqHeaderFile2 = qtouchComponent.createFileSymbol("TOUCH_ACQ_HEADER_2", None)
    touchAcqHeaderFile2.setDestPath("/touch/")
    touchAcqHeaderFile2.setProjectPath("config/" + configName + "/touch/")
    touchAcqHeaderFile2.setType("HEADER")
    touchAcqHeaderFile2.setMarkup(False)

    if (targetDevice == "SAMC20"):
        #need also c21
        touchAcqHeaderFile2.setSourcePath("/src/qtm_acq_samc21_0x0020_api.h")
        touchAcqHeaderFile2.setOutputName("qtm_acq_samc21_0x0020_api.h")
    elif(targetDevice in set(["SAME51","SAME53","SAMD51"])):
        #also need E54
        touchAcqHeaderFile2.setSourcePath("/src/qtm_acq_same54_0x000f_api.h")
        touchAcqHeaderFile2.setOutputName("qtm_acq_same54_0x000f_api.h")
    elif(targetDevice in set(["SAMDA1","SAMHA1"]) ):
        #also need D21
        touchAcqHeaderFile2.setSourcePath("/src/qtm_acq_samd21_0x0024_api.h")
        touchAcqHeaderFile2.setOutputName("qtm_acq_samd21_0x0024_api.h")
    else:
        touchAcqHeaderFile2.setSourcePath("Error_setAcqHeaderFile2")
        touchAcqHeaderFile2.setOutputName("Error_setAcqHeaderFile2")
    return touchAcqHeaderFile2


def enableAutoTuneFunctionality(symbol,event):
    """Handler for auto tune library selection.
    Arguments:
        :symbol : the symbol that triggered the event
        :event : new value of the symbol 
    Returns:
        :none
    """
    localcomponent = symbol.getComponent()
    touchAcqLibraryFile = localcomponent.getSymbolByID("TOUCH_ACQ_LIB")
    touchAcqAutoLibraryFile = localcomponent.getSymbolByID("TOUCH_ACQ_AUTO_LIB")

    if(event["value"] == 0):
        touchAcqAutoLibraryFile.setEnabled(False)
        touchAcqLibraryFile.setEnabled(True)
    else:
        touchAcqAutoLibraryFile.setEnabled(True)
        touchAcqLibraryFile.setEnabled(False)