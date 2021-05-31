"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
def setKeysFiles(configName, qtouchComponent, targetDevice):
    """
    Generates as List of source files required for Keys support
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        fileList: list of file symbols
    """
    fileList = []
    fileList.append(setTouchLibraryFile(configName, qtouchComponent, targetDevice))
    fileList.append(setTouchHeaderFile(configName, qtouchComponent))
    return fileList

def setTouchLibraryFile(configName, qtouchComponent, targetDevice):
    """
    Generates Keys library file (device dependent)
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    touchLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_KEY_LIB", None)
    touchLibraryFile.setDestPath("/touch/lib/")
    touchLibraryFile.setEnabled(True)

    if (targetDevice in set(["SAME51","SAME53","SAME54","SAMD51"])):
        touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm4_0x0002.X.a")
        touchLibraryFile.setOutputName("qtm_touch_key_cm4_0x0002.X.a")
    elif (targetDevice in set(["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"])):
        touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm23_0x0002.X.a")
        touchLibraryFile.setOutputName("qtm_touch_key_cm23_0x0002.X.a")
    elif (targetDevice in set(["PIC32MZW"])):
        touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_pic32mz_0x0002.X.a")
        touchLibraryFile.setOutputName("qtm_touch_key_pic32mz_0x0002.X.a")
    else:
        touchLibraryFile.setSourcePath("/src/libraries/qtm_touch_key_cm0p_0x0002.X.a")
        touchLibraryFile.setOutputName("qtm_touch_key_cm0p_0x0002.X.a")
    return touchLibraryFile

def setTouchHeaderFile(configName, qtouchComponent):
    """
    Generates keys api header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KEY_HEADER", None)
    touchHeaderFile.setSourcePath("/src/qtm_touch_key_0x0002_api.h")
    touchHeaderFile.setOutputName("qtm_touch_key_0x0002_api.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(False)
    return touchHeaderFile