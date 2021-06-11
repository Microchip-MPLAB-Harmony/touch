"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
def setDrivenShieldFiles(configName, qtouchComponent,useTrustZone):
    """
    Generates as List of source files required for Driven shield support
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        fileList: list of file symbols
    """
    # freqHopHeaderFile
    fileList = []
    fileList.append(setDrivenShieldHeaderFile(configName, qtouchComponent))
    # freqHopAutoHeaderFile
    fileList.append(setDrivenShieldSourceile(configName, qtouchComponent))
    if(useTrustZone ==  False):
        del fileList[:]
    return fileList

def setDrivenShieldHeaderFile(configName, qtouchComponent):
    """
    Generates Driven shield header file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    drivenShieldHeadFile = qtouchComponent.createFileSymbol("HEADER_DRIVENSHIELD", None)
    drivenShieldHeadFile.setSourcePath("/templates/driven_shield.h.ftl")
    drivenShieldHeadFile.setOutputName("driven_shield.h")
    drivenShieldHeadFile.setDestPath("/touch/")
    drivenShieldHeadFile.setProjectPath("config/" + configName + "/touch/")
    drivenShieldHeadFile.setType("HEADER")
    drivenShieldHeadFile.setMarkup(True)
    drivenShieldHeadFile.setEnabled(False)
    drivenShieldHeadFile.setDependencies(enableDrivenShieldFiles,["DS_DEDICATED_ENABLE"])
    drivenShieldHeadFile.setDependencies(enableDrivenShieldFiles,["DS_PLUS_ENABLE"])
    return drivenShieldHeadFile

def setDrivenShieldSourceile(configName, qtouchComponent):
    """
    Generates Driven shield source file
        :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
    Returns:
        file symbol
    """
    drivenShieldSourceFile = qtouchComponent.createFileSymbol("SOURCE_DRIVENSHIELD", None)
    drivenShieldSourceFile.setSourcePath("/templates/driven_shield.c.ftl")
    drivenShieldSourceFile.setOutputName("driven_shield.c")
    drivenShieldSourceFile.setDestPath("/touch/")
    drivenShieldSourceFile.setProjectPath("config/" + configName + "/touch/")
    drivenShieldSourceFile.setType("SOURCE")
    drivenShieldSourceFile.setMarkup(True)
    drivenShieldSourceFile.setEnabled(False)
    drivenShieldSourceFile.setDependencies(enableDrivenShieldFiles,["DS_DEDICATED_ENABLE"])
    drivenShieldSourceFile.setDependencies(enableDrivenShieldFiles,["DS_PLUS_ENABLE"])
    return drivenShieldSourceFile

def enableDrivenShieldFiles(symbol,event):
    """Handler for enabling source / header files.
    Arguments:
        :symbol : the symbol that triggered the event
        :event : new value of the symbol 
    Returns:
        :none
    """
    localComponent= symbol.getComponent()
    enableSourceFiles = bool(event['symbol'].getValue())
    localComponent.getSymbolByID("HEADER_DRIVENSHIELD").setEnabled(enableSourceFiles)
    localComponent.getSymbolByID("SOURCE_DRIVENSHIELD").setEnabled(enableSourceFiles)