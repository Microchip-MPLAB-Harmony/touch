"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""

def setTouchFiles(configName, qtouchComponent):
    """
    Generates as List of touch source files
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        fileList: list of file symbols
    """
    fileList = []
    fileList.append(setTouchHeaderFile(configName, qtouchComponent))
    fileList.append(setTouchAPIHeaderFile(configName, qtouchComponent))
    fileList.append(setTouchSourceFile(configName, qtouchComponent))
    fileList.append(setPTCSystemInitFile(configName, qtouchComponent))
    fileList.append(setPTCSystemDefFile(configName, qtouchComponent))
    return fileList

def setTouchHeaderFile(configName, qtouchComponent):
    """
    Generates touch header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER", None)
    touchHeaderFile.setSourcePath("/templates/touch.h.ftl")
    touchHeaderFile.setOutputName("touch.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(True)
    return touchHeaderFile

def setTouchAPIHeaderFile(configName, qtouchComponent):
    """
    Generates touch api header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    touchAPIHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER1", None)
    touchAPIHeaderFile.setSourcePath("/templates/touch_api_ptc.h.ftl")
    touchAPIHeaderFile.setOutputName("touch_api_ptc.h")
    touchAPIHeaderFile.setDestPath("/touch/")
    touchAPIHeaderFile.setProjectPath("config/" + configName + "/touch/")
    touchAPIHeaderFile.setType("HEADER")
    touchAPIHeaderFile.setMarkup(True)
    return touchAPIHeaderFile

def setTouchSourceFile(configName, qtouchComponent):
    """
    Generates touch source file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    touchSourceFile = qtouchComponent.createFileSymbol("TOUCH_SOURCE", None)
    touchSourceFile.setSourcePath("/templates/touch.c.ftl")
    touchSourceFile.setOutputName("touch.c")
    touchSourceFile.setDestPath("/touch/")
    touchSourceFile.setProjectPath("config/" + configName +"/touch/")
    touchSourceFile.setType("SOURCE")
    touchSourceFile.setMarkup(True)
    return touchSourceFile

def setPTCSystemInitFile(configName, qtouchComponent):
    """
    Generates initialization source file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    ptcSystemInitFile = qtouchComponent.createFileSymbol("PTC_SYS_INIT", None)
    ptcSystemInitFile.setType("STRING")
    ptcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
    ptcSystemInitFile.setSourcePath("../touch/templates/system/initialization.c.ftl")
    ptcSystemInitFile.setMarkup(True)
    return ptcSystemInitFile


def setPTCSystemDefFile(configName, qtouchComponent):
    """
    Generates definitions header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    ptcSystemDefFile = qtouchComponent.createFileSymbol("PTC_SYS_DEF", None)
    ptcSystemDefFile.setType("STRING")
    ptcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ptcSystemDefFile.setSourcePath("../touch/templates/system/definitions.h.ftl")
    ptcSystemDefFile.setMarkup(True)
    return ptcSystemDefFile