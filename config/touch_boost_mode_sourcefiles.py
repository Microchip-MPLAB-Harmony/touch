"""
Copyright (C) [2023], Microchip Technology Inc., and its subsidiaries. All rights reserved.

The software and documentation is provided by microchip and its contributors
"as is" and any express, implied or statutory warranties, including, but not
limited to, the implied warranties of merchantability, fitness for a particular
purpose and non-infringement of third party intellectual property rights are
disclaimed to the fullest extent permitted by law. In no event shall microchip
or its contributors be liable for any direct, indirect, incidental, special,
exemplary, or consequential damages (including, but not limited to, procurement
of substitute goods or services; loss of use, data, or profits; or business
interruption) however caused and on any theory of liability, whether in contract,
strict liability, or tort (including negligence or otherwise) arising in any way
out of the use of the software and documentation, even if advised of the
possibility of such damage.

Except as expressly permitted hereunder and subject to the applicable license terms
for any third-party software incorporated in the software and any applicable open
source software license terms, no license or other rights, whether express or
implied, are granted under any patent or other intellectual property rights of
Microchip or any third party.
"""
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
        elif(targetDevice in ["SAML11","SAML1xE"]):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_saml11_0x0033.X.a")
            touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_saml11_0x0033.X.a")
        elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_pic32cm_le_0x0041.X.a")
            touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_pic32cm_le_0x0041.X.a")
        elif(targetDevice in ["PIC32CZCA80"]):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_global_pic32cz_ca80_0x0049.X.a")
            touchAcq4pLibraryFile.setOutputName("qtm_acq_global_pic32cz_ca80_0x0049.X.a")
        elif(targetDevice in ["PIC32CZCA90"]):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_global_pic32cz_ca90_0x0049.X.a")
            touchAcq4pLibraryFile.setOutputName("qtm_acq_global_pic32cz_ca90_0x0049.X.a")
        elif(targetDevice in ["PIC32CKSG00","PIC32CKSG01"]):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_pic32ck_sg_0x004f.X.a")
            touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_pic32ck_sg_0x004f.X.a")
        elif(targetDevice in ["PIC32CKGC00","PIC32CKGC01"]):
            touchAcq4pLibraryFile.setSourcePath("/src/libraries/qtm_acq_4p_pic32ck_gc_0x004f.X.a")
            touchAcq4pLibraryFile.setOutputName("qtm_acq_4p_pic32ck_gc_0x004f.X.a")
        else:
            touchAcq4pLibraryFile.setSourcePath("Error_setBoostModeLibraryFile")
            touchAcq4pLibraryFile.setOutputName("Error_setBoostModeLibraryFile")
        return touchAcq4pLibraryFile

    def setBoostModeHeaderFile(self,configName, qtouchComponent, targetDevice):
        touchAcq4pHeaderFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_4P_HEADER", None)
        touchAcq4pHeaderFile.setDestPath("/touch/")
        touchAcq4pHeaderFile.setProjectPath("config/" + configName + "/touch/")
        touchAcq4pHeaderFile.setType("HEADER")
        touchAcq4pHeaderFile.setMarkup(False)
        touchAcq4pHeaderFile.setEnabled(False)
        self.addDepSymbol(touchAcq4pHeaderFile, "libChangeBoostMode", ["ENABLE_BOOST"])
        if(targetDevice == "SAML10"):
            touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_saml10_0x0033_api.h")
            touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_saml10_0x0033_api.h")
        elif(targetDevice in ["SAML11","SAML1xE"]):
            touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_saml11_0x0033_api.h")
            touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_saml11_0x0033_api.h")
        elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
            touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_pic32cm_le_0x0041_api.h")
            touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_pic32cm_le_0x0041_api.h")
        elif(targetDevice in ["PIC32CZCA80", "PIC32CZCA90"]):
            touchAcq4pHeaderFile.setSourcePath("/src/qtm_global_pic32czca_0x0049_api.h")
            touchAcq4pHeaderFile.setOutputName("qtm_global_pic32czca_0x0049_api.h")
        elif(targetDevice in ["PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01"]):
            touchAcq4pHeaderFile.setSourcePath("/src/qtm_acq_4p_pic32ck_0x004f_api.h")
            touchAcq4pHeaderFile.setOutputName("qtm_acq_4p_pic32ck_0x004f_api.h")
        else:
            touchAcq4pHeaderFile.setSourcePath("Error_setBoostModeHeaderFile")
            touchAcq4pHeaderFile.setOutputName("Error_setBoostModeHeaderFile")
        return touchAcq4pHeaderFile


