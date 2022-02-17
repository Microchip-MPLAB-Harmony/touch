"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
class classTouchBoostModeFiles():

    def __init__(self):
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def setBoostModeFiles(self,configName, qtouchComponent, targetDevice,useTrustZone):
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
        fileList.append(self.setBoostModeLibraryFile(configName, qtouchComponent, targetDevice))
        fileList.append(self.setBoostModeHeaderFile(configName, qtouchComponent, targetDevice))

        if(useTrustZone == False):
            del fileList[:]

        return fileList

    def setBoostModeLibraryFile(self,configName, qtouchComponent, targetDevice):
        touchAcq4pLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_4P_LIB", None)
        touchAcq4pLibraryFile.setDestPath("/touch/lib/")
        touchAcq4pLibraryFile.setEnabled(False)
        self.addDepSymbol(touchAcq4pLibraryFile, "libChangeBoostMode", ["ENABLE_BOOST"])

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
        return "TOUCH_ACQ_4P_LIB"

    def setBoostModeHeaderFile(self,configName, qtouchComponent, targetDevice):
        touchAcq4pHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_4P_HEADER", None)
        touchAcq4pHeaderFile.setDestPath("/touch/")
        touchAcq4pHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchAcq4pHeaderFile.setType("HEADER")
        touchAcq4pHeaderFile.setMarkup(False)
        self.addDepSymbol(touchAcq4pHeaderFile, "libChangeBoostMode", ["ENABLE_BOOST"])
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
        return "TOUCH_ACQ_4P_HEADER"


