class touchTrustZone():
    def __init__(self):
        self.nonSecureStatus = "SECURE"
        self.localProjectFilesList = []
        self.symbolList = []
        self.depFuncName = []
        self.dependencies = []

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
        print "self.localProjectFilesList", self.localProjectFilesList
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
            
            self.localProjectFilesList[kx].setSecurity(secureStatus)