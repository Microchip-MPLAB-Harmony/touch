"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
def setGestureFiles(configName, qtouchComponent, targetDevice):
    """
    Generates as List of source files required for gesture support
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        fileList: list of file symbols
    """
    fileList = []
    fileList.append(setGestureLibraryFile(configName, qtouchComponent, targetDevice))
    fileList.append(setGestureHeaderFile(configName, qtouchComponent))
    return fileList

def setGestureLibraryFile(configName, qtouchComponent, targetDevice):
    """
    Generates gesture library file per device
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :targetDevice : see interface.getDeviceSeries()
    Returns:
        file symbol
    """
    if (targetDevice in ["SAME51","SAME53","SAME54","SAMD51"]):
        # Library File
        gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
        gestureLibraryFile.setSourcePath("/src/libraries/qtm_surface_gestures_cm4_0x0023.X.a")
        gestureLibraryFile.setOutputName("qtm_surface_gestures_cm4_0x0023.X.a")
        gestureLibraryFile.setDestPath("/touch/lib/")
        gestureLibraryFile.setEnabled(False)
    elif (targetDevice in ["SAML10","SAML11","PIC32CMLE00","PIC32CMLS00"]):
        # Library File
        gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
        gestureLibraryFile.setSourcePath("/src/libraries/qtm_surface_gestures_cm23_0x0023.X.a")
        gestureLibraryFile.setOutputName("qtm_surface_gestures_cm23_0x0023.X.a")
        gestureLibraryFile.setDestPath("/touch/lib/")
        gestureLibraryFile.setEnabled(False)
    elif (targetDevice in ["PIC32MZW"]):
        # Library File
        gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
        gestureLibraryFile.setSourcePath("/src/libraries/qtm_surface_gestures_pic32mz_0x0023.X.a")
        gestureLibraryFile.setOutputName("qtm_surface_gestures_pic32mz_0x0023.X.a")
        gestureLibraryFile.setDestPath("/touch/lib/")
        gestureLibraryFile.setEnabled(False)
    else:
        # Library File
        gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
        gestureLibraryFile.setSourcePath("/src/libraries/qtm_surface_gestures_cm0p_0x0023.X.a")
        gestureLibraryFile.setOutputName("qtm_surface_gestures_cm0p_0x0023.X.a")
        gestureLibraryFile.setDestPath("/touch/lib/")
        gestureLibraryFile.setEnabled(False)
    return gestureLibraryFile

def setGestureHeaderFile(configName, qtouchComponent):
    """
    Generates gesture header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    gestureHeaderFile = qtouchComponent.createFileSymbol("TOUCH_GESTURE_HEADER", None)
    gestureHeaderFile.setSourcePath("/src/qtm_gestures_2d_0x0023_api.h")
    gestureHeaderFile.setOutputName("qtm_gestures_2d_0x0023_api.h")
    gestureHeaderFile.setDestPath("/touch/")
    gestureHeaderFile.setProjectPath("config/" + configName + "/touch/")
    gestureHeaderFile.setType("HEADER")
    gestureHeaderFile.setMarkup(False)
    gestureHeaderFile.setEnabled(False)
