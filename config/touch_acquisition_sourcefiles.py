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

class classTouchAcquisitionSourceFiles():
    def __init__(self):
        tempvar = 0

    def setAcquisitionFiles(self,configName, qtouchComponent, targetDevice, useTrustZone):
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
        fileList.append(self.setAcquisitionLibraryFile(configName, qtouchComponent, targetDevice))
        # touchAcqAutoLibraryFile
        fileList.append(self.setAutoAcquisitionLibraryFile(configName, qtouchComponent, targetDevice))
        # touchBindLibraryFile
        fileList.append(self.setBindLibraryFile(configName, qtouchComponent, targetDevice))
        # touchAcqHeaderFile
        fileList.append(self.setAcqHeaderFile(configName, qtouchComponent, targetDevice))
        # touchAcqHeaderFile2 (some devices)
        if(targetDevice in set(["SAMDA1","SAMHA1","SAMC20","SAMD51","SAME51","SAME53","PIC32MZW","PIC32MZDA", "PIC32CXBZ31", "WBZ35","WBZ65"])):
            fileList.append(self.setAcqHeaderFile2(configName, qtouchComponent, targetDevice))
        # touchBindHeaderFile
        fileList.append(self.setBindHeaderFile(configName, qtouchComponent, targetDevice))
        # touchCommonHeaderFile
        fileList.append(self.setCommonHeaderFile(configName, qtouchComponent, targetDevice))

        if(useTrustZone == False):
            del fileList[:]

        return fileList


    def setBindHeaderFile(self,configName, qtouchComponent, targetDevice):
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

    def setCommonHeaderFile(self,configName, qtouchComponent, targetDevice):
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

    def setAcquisitionLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates acquisition library file
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        if (targetDevice == "PIC32MZW") or (targetDevice == "PIC32MZDA")or (targetDevice == "PIC32CXBZ31")or (targetDevice == "WBZ35")or (targetDevice == "WBZ65"):
            touchAcqLibraryFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_LIB", None)   
            touchAcqLibraryFile.setDestPath("/touch/")
            touchAcqLibraryFile.setProjectPath("config/" + configName + "/touch/")
        else:
            touchAcqLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_LIB", None)   
            touchAcqLibraryFile.setDestPath("/touch/lib/")
        touchAcqLibraryFile.setEnabled(True)
        touchAcqLibraryFile.setDependencies(self.enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])

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
        elif(targetDevice in set(["SAML11","SAML1xE"])):
            touchAcqLibraryFile.setSourcePath("/src/libraries/0x0027_qtm_saml11_acq.X.a")
            touchAcqLibraryFile.setOutputName("0x0027_qtm_saml11_acq.X.a")
        elif(targetDevice == "PIC32MZW"):
            touchAcqLibraryFile.setSourcePath("/src/libraries/hcvd_driver_PIC32MZ1025W104.c")
            touchAcqLibraryFile.setOutputName("hcvd_driver_PIC32MZ1025W104.c")
        elif(targetDevice == "PIC32MZDA"):
            touchAcqLibraryFile.setSourcePath("/src/libraries/cvd_driver_PIC32MZ.c")
            touchAcqLibraryFile.setOutputName("cvd_driver_PIC32MZ.c")
        elif(targetDevice in ["PIC32CXBZ31", "WBZ35","WBZ65"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/hcvd_driver_PIC32CX.c")
            touchAcqLibraryFile.setOutputName("hcvd_driver_PIC32CX.c")
        elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cm_le_0x0040.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32cm_le_0x0040.X.a")
        elif(targetDevice == "SAML21"):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml21_0x0026.X.a")
            touchAcqLibraryFile.setOutputName("qtm_saml21_acq_0x0026.X.a")
        elif(targetDevice == "SAML22"):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml22_0x0028.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_saml22_0x0028.X.a")
        elif(targetDevice in ["PIC32CMJH00","PIC32CMJH01"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cmjh_0x002f.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32cmjh_0x002f.X.a")
        elif(targetDevice in ["PIC32CZCA80"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cz_ca80_0x004a.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32cz_ca80_0x004a.X.a")
        elif(targetDevice in ["PIC32CZCA90"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cz_ca90_0x004a.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32cz_ca90_0x004a.X.a")
        elif(targetDevice in ["PIC32CMGC00"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cm_gc_0x0053.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32cm_gc_0x0053.X.a")
        elif(targetDevice in ["PIC32CKGC00","PIC32CKGC01"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32ckgc_0x004e.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32ckgc_0x004e.X.a")
        elif(targetDevice in ["PIC32CKSG00","PIC32CKSG01"]):
            touchAcqLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cksg_0x004e.X.a")
            touchAcqLibraryFile.setOutputName("qtm_acq_pic32cksg_0x004e.X.a")
        else:
            touchAcqLibraryFile.setSourcePath("Error_setAcquisitionLibraryFile")
            touchAcqLibraryFile.setOutputName("Error_setAcquisitionLibraryFile")
        return touchAcqLibraryFile

    def setAutoAcquisitionLibraryFile(self,configName, qtouchComponent, targetDevice):
        """
        Generates auto acquisition library file per device
            :configName : see Variables.get("__CONFIGURATION_NAME")  on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
            :qtouchComponent : touchModule
            :targetDevice : see interface.getDeviceSeries()
        Returns:
            file symbol
        """
        if (targetDevice == "PIC32MZW") or (targetDevice == "PIC32MZDA") or (targetDevice == "PIC32CXBZ31") or (targetDevice == "WBZ35") or (targetDevice == "WBZ65"):
            touchAcqAutoLibraryFile = qtouchComponent.createFileSymbol("TOUCH_ACQ_AUTO_LIB", None)
            touchAcqAutoLibraryFile.setDestPath("/touch/")
            touchAcqAutoLibraryFile.setProjectPath("config/" + configName + "/touch/")
        else:
            touchAcqAutoLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_ACQ_AUTO_LIB", None)
            touchAcqAutoLibraryFile.setDestPath("/touch/lib/")
        touchAcqAutoLibraryFile.setEnabled(False)
        touchAcqAutoLibraryFile.setDependencies(self.enableAutoTuneFunctionality,["TUNE_MODE_SELECTED"])

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
        elif(targetDevice in set(["SAML11","SAML1xE"])):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/0x0027_qtm_saml11_acq.X.a")
            touchAcqAutoLibraryFile.setOutputName("0x0027_qtm_saml11_acq.X.a")   
        elif(targetDevice == "PIC32MZW"):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/hcvd_driver_PIC32MZ1025W104.C")
            touchAcqAutoLibraryFile.setOutputName("hcvd_driver_PIC32MZ1025W104.C")
        elif(targetDevice == "PIC32MZDA"):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/cvd_driver_PIC32MZ.c")
            touchAcqAutoLibraryFile.setOutputName("cvd_driver_PIC32MZ.c")
        elif(targetDevice in ["PIC32CXBZ31", "WBZ35","WBZ65"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/hcvd_driver_PIC32CX.c")
            touchAcqAutoLibraryFile.setOutputName("hcvd_driver_PIC32CX.c")
        elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cm_le_0x0040.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32cm_le_0x0040.X.a")
        elif(targetDevice == "SAML21"):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_saml21_acq_0x0026.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_saml21_0x0026.X.a")
        elif(targetDevice == "SAML22"):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_saml22_0x0028.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_saml22_0x0028.X.a")
        elif(targetDevice in ["PIC32CMJH00","PIC32CMJH01"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cmjh_0x002f.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32cmjh_0x002f.X.a")
        elif(targetDevice in ["PIC32CZCA80"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cz_ca80_0x004a.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32cz_ca80_0x004a.X.a")
        elif(targetDevice in ["PIC32CZCA90"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cz_ca90_0x004a.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32cz_ca90_0x004a.X.a")
        elif(targetDevice in ["PIC32CMGC00"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cm_gc_0x0053.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32cm_gc_0x0053.X.a")
        elif(targetDevice in ["PIC32CKGC00","PIC32CKGC01"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32ckgc_0x004e.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32ckgc_0x004e.X.a")
        elif(targetDevice in ["PIC32CKSG00","PIC32CKSG01"]):
            touchAcqAutoLibraryFile.setSourcePath("/src/libraries/qtm_acq_pic32cksg_0x004e.X.a")
            touchAcqAutoLibraryFile.setOutputName("qtm_acq_pic32cksg_0x004e.X.a")
        else:
            touchAcqAutoLibraryFile.setOutputName("Error_setAutoAcquisitionLibraryFile")
            touchAcqAutoLibraryFile.setOutputName("Error_setAutoAcquisitionLibraryFile")
        return touchAcqAutoLibraryFile

    def setBindLibraryFile(self,configName, qtouchComponent, targetDevice):
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

        if (targetDevice in set(["SAMC21","SAMC20","SAMD10","SAMD11","SAMD20","SAMD21","SAMDA1","SAMHA1","SAML21","SAML22"]) ):
            touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm0p_0x0005.X.a")
            touchBindLibraryFile.setOutputName("qtm_binding_layer_cm0p_0x0005.X.a")
        elif(targetDevice in set(["SAMD51","SAME51","SAME53","SAME54"])):
            touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm4_0x0005.X.a")
            touchBindLibraryFile.setOutputName("qtm_binding_layer_cm4_0x0005.X.a")
        elif(targetDevice in set(["SAML10","SAML11","SAML1xE"])):
            touchBindLibraryFile.setSourcePath("/src/libraries/qtm_binding_layer_cm23_0x0005.X.a")
            touchBindLibraryFile.setOutputName("qtm_binding_layer_cm23_0x0005.X.a")
        else:
            touchBindLibraryFile.setOutputName("Error_setBindLibraryFile")
            touchBindLibraryFile.setOutputName("Error_setBindLibraryFile")
        return touchBindLibraryFile

    def setAcqHeaderFile(self,configName, qtouchComponent, targetDevice):
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
        elif(targetDevice in set(["SAML11","SAML1xE"])):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_saml11_0x0027_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_saml11_0x0027_api.h")    
        elif(targetDevice == "PIC32MZW"):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32mzw_0x003e_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32mzw_0x003e_api.h")
        elif(targetDevice == "PIC32MZDA"):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32mzda_0x0046_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32mzda_0x0046_api.h")
        elif(targetDevice in ["PIC32CXBZ31", "WBZ35","WBZ65"]):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32cx_0x003e_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32cx_0x003e_api.h")
        elif(targetDevice in ["PIC32CMLE00","PIC32CMLS00"]):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32cm_le_0x0040_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32cm_le_0x0040_api.h")
        elif(targetDevice == "SAML21"):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_saml21_0x0026_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_saml21_0x0026_api.h")
        elif(targetDevice == "SAML22"):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_saml22_0x0028_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_saml22_0x0028_api.h")
        elif(targetDevice in ["PIC32CMJH00","PIC32CMJH01"]):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32cmjh_0x002f_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32cmjh_0x002f_api.h")
        elif(targetDevice in ["PIC32CZCA80", "PIC32CZCA90"]):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32czca_0x004a_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32czca_0x004a_api.h")
        elif(targetDevice in ["PIC32CMGC00"]):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32cm_gc_0x0053_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32cm_gc_0x0053_api.h")            
        elif(targetDevice in ["PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01"]):
            touchAcqHeaderFile.setSourcePath("/src/qtm_acq_pic32ck_0x004e_api.h")
            touchAcqHeaderFile.setOutputName("qtm_acq_pic32ck_0x004e_api.h")
        else:
            touchAcqHeaderFile.setSourcePath("Error_setAcqHeaderFile")
            touchAcqHeaderFile.setOutputName("Error_setAcqHeaderFile")
        return touchAcqHeaderFile

    def setAcqHeaderFile2(self,configName, qtouchComponent, targetDevice):
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
        elif(targetDevice == "PIC32MZW"):
            touchAcqHeaderFile2.setSourcePath("/src/libraries/hcvd_driver_PIC32MZ1025W104.h")
            touchAcqHeaderFile2.setOutputName("hcvd_driver_PIC32MZ1025W104.h")
        elif(targetDevice == "PIC32MZDA"):
            touchAcqHeaderFile2.setSourcePath("/src/libraries/cvd_driver_PIC32MZ.h")
            touchAcqHeaderFile2.setOutputName("cvd_driver_PIC32MZ.h")
        elif(targetDevice in ["PIC32CXBZ31", "WBZ35","WBZ65"]):
            touchAcqHeaderFile2.setSourcePath("/src/libraries/hcvd_driver_PIC32CX.h.ftl")
            touchAcqHeaderFile2.setOutputName("hcvd_driver_PIC32CX.h")
            touchAcqHeaderFile2.setMarkup(True)
        else:
            touchAcqHeaderFile2.setSourcePath("Error_setAcqHeaderFile2")
            touchAcqHeaderFile2.setOutputName("Error_setAcqHeaderFile2")
        return touchAcqHeaderFile2


    def enableAutoTuneFunctionality(self,symbol,event):
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