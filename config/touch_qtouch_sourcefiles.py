"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchQTouch():

    def __init__(self):
        self.systemDefFileSymbol = []

    def setTouchFiles(self,configName, qtouchComponent,useTrustZone):
        """
        Generates as List of touch source files
        Arguments:
            :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            fileList: list of file symbols
        """
        fileList = []
        fileList.append(self.setTouchHeaderFile(configName, qtouchComponent))
        fileList.append(self.setTouchAPIHeaderFile(configName, qtouchComponent))
        fileList.append(self.setTouchSourceFile(configName, qtouchComponent))
        fileList.append(self.setTouchExampleFile(configName, qtouchComponent))
        fileList.append(self.setTouchExampleHeaderFile(configName, qtouchComponent))
        fileList.append(self.setPTCSystemInitFile(configName, qtouchComponent))
        fileList.append(self.setPTCSystemDefFile(configName, qtouchComponent))
        if(useTrustZone == False):
            del fileList[:]
        return fileList

    def getSystemDefFileSymbol(self):
        return self.systemDefFileSymbol[0]

    def setTouchHeaderFile(self,configName, qtouchComponent):
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

    def setTouchAPIHeaderFile(self,configName, qtouchComponent):
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

    def setTouchExampleFile(self,configName, qtouchComponent):
        """
        Generates touch source file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        touchExampleFile = qtouchComponent.createFileSymbol("TOUCH_EXAMPLE_SOURCE", None)
        touchExampleFile.setSourcePath("/templates/touch_example.c.ftl")
        touchExampleFile.setOutputName("touch_example.c")
        touchExampleFile.setDestPath("/touch/")
        touchExampleFile.setProjectPath("config/" + configName +"/touch/")
        touchExampleFile.setType("SOURCE")
        touchExampleFile.setMarkup(True)
        return touchExampleFile

    def setTouchExampleHeaderFile(self,configName, qtouchComponent):
        """
        Generates touch header file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
        Returns:
            file symbol
        """
        touchExampleHeaderFile = qtouchComponent.createFileSymbol("TOUCH_EXAMPLE_HEADER", None)
        touchExampleHeaderFile.setSourcePath("/templates/touch_example.h.ftl")
        touchExampleHeaderFile.setOutputName("touch_example.h")
        touchExampleHeaderFile.setDestPath("/touch/")
        touchExampleHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchExampleHeaderFile.setType("HEADER")
        touchExampleHeaderFile.setMarkup(True)
        return touchExampleHeaderFile

    def setTouchSourceFile(self,configName, qtouchComponent):
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

    def setPTCSystemInitFile(self,configName, qtouchComponent):
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


    def setPTCSystemDefFile(self,configName, qtouchComponent):
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
        self.systemDefFileSymbol.append(ptcSystemDefFile)
        return ptcSystemDefFile