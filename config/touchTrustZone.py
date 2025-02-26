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
class touchTrustZone():
    def __init__(self):
        self.nonSecureStatus = "SECURE"
        self.localProjectFilesList = []
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []
        self.configName = ""

    def addDepSymbol(self, symbol, func, depen):
        self.symbolList.append(symbol)
        self.depFuncName.append(func)
        self.dependencies.append(depen)

    def getDepDetails(self):
        return self.symbolList, self.depFuncName, self.dependencies

    def initTrustzoneInstance(self, configName, qtouchComponent, parentLabel , targetDevice, projectFilesList,ptcSystemDefFile,secureStatus):
        self.nonSecureStatus = secureStatus
        self.localProjectFilesList = projectFilesList
        enableTrustzoneUtility = qtouchComponent.createBooleanSymbol("TZ_ENABLED",parentLabel)
        enableTrustzoneUtility.setDefaultValue(False)  
        enableTrustzoneUtility.setVisible(False)
        enableTrustzoneUtility.setDefaultValue(True)
        #ptcNonSecureState = Database.getSymbolValue("core", "PTC_IS_NON_SECURE")
        self.configName = configName
        
        self.addDepSymbol(ptcSystemDefFile, "securefileUpdate", ["core.PTC_IS_NON_SECURE"])
        self.addDepSymbol(ptcSystemDefFile, "securefileUpdate", ["core.NVIC_42_0_SECURITY_TYPE"])
        self.checknonsecureStatus(qtouchComponent, secureStatus)

    def searchlocalProjectFilesList(self,idString):
        retVal = False
        for x in self.localProjectFilesList:
            if str(x.getID()) == idString:
                retVal = True
                break
        return retVal

    def checklocalProjectFilesList(self,symbol,idString):

        component = symbol.getComponent()
        if component.getSymbolByID(idString).getEnabled() == True:
            if self.searchlocalProjectFilesList(idString) == False:
                self.localProjectFilesList.append(component.getSymbolByID(idString))
        else:
            if self.searchlocalProjectFilesList(idString) == True:
                self.localProjectFilesList.remove(component.getSymbolByID(idString))
        return     
    
    def securefileUpdate(self,symbol, event):
        localComponent = symbol.getComponent()
        if event["value"] == False:
            self.nonSecureStatus = "SECURE"
        else:
            self.nonSecureStatus = "NON_SECURE"
            
        self.checknonsecureStatus(qtouchComponent, self.nonSecureStatus)

    def checknonsecureStatus(self, qtouchComponent, secureStatus):
        for kx in range(len(self.localProjectFilesList)):
            entryname = self.localProjectFilesList[kx].getID()
            splitname = entryname.split('_')
            if "PTC_SYS_DEF" == entryname :
                if (secureStatus == "SECURE"):
                    self.localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
                else:
                    self.localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
            
            if "PTC_SYS_INIT" == entryname:
                if (secureStatus == "SECURE"):
                    self.localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
                else:
                    self.localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            
            if ("LIB" in entryname):
                if(secureStatus == "SECURE"):
                    self.localProjectFilesList[kx].setDestPath("../../../src/config/"+self.configName+"/touch/lib/")
                else:
                    self.localProjectFilesList[kx].setDestPath("../../../src/config/"+self.configName+"/touch/lib/")

            self.localProjectFilesList[kx].setSecurity(secureStatus)