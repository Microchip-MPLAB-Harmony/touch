"""
MHC Python Interface documentation website <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
"""
global Database
nonSecureStatus = "SECURE"
localProjectFilesList = []

def initTrustzoneInstance(configName, qtouchComponent, parentLabel , targetDevice, projectFilesList):
    """Creates trustzone support. 
    Facilitates moving sourcefiles and libraries between secure / non secure projects.
    Arguments:
        :configName : see Variables.get("__CONFIGURATION_NAME") on MHC api documentation <http://confluence.microchip.com/display/MH/MHC+Python+Interface>
        :qtouchComponent : touchModule
        :parentLabel : parent symbol for added symbols
        :targetDevice : see interface.getDeviceSeries()
        :projectFilesList : List of file symbols from qtouch.py
    Returns:
        fileList: list of file symbols
    """
    localProjectFilesList = projectFilesList
    enableTrustzoneUtility = qtouchComponent.createBooleanSymbol("TZ_ENABLED",parentLabel)
    enableTrustzoneUtility.setDefaultValue(False)  
    enableTrustzoneUtility.setVisible(False)
    enableTrustzoneUtility.setDefaultValue(True)
    ptcNonSecureState = Database.getSymbolValue("core", "PTC_IS_NON_SECURE")
    ptcSystemDefFile = qtouchComponent.getSymbolByID("PTC_SYS_DEF")
    ptcSystemDefFile.setDependencies(securefileUpdate, ["core.PTC_IS_NON_SECURE"])
    ptcSystemDefFile.setDependencies(securefileUpdate, ["core.NVIC_42_0_SECURITY_TYPE"])
    checknonsecureStatus()

def searchlLocalProjectFilesList(idString):
    """Search file list by for ID 
    Arguments:
        :idString : string to search for
    Returns:
        True / False if idString was found
    """
    retVal = False
    for x in localProjectFilesList:
        if str(x.getID()) == idString:
            retVal = True
            break
    return retVal

def checkLocalProjectFilesList(symbol,idString):

    component = symbol
    if component.getSymbolByID(idString).getEnabled() == True:
        if searchlLocalProjectFilesList(idString) == False:
            localProjectFilesList.append(component.getSymbolByID(idString))
    else:
        if searchlLocalProjectFilesList(idString) == True:
            localProjectFilesList.remove(component.getSymbolByID(idString))
    return     
 
def securefileUpdate(symbol, event):
    """Handler for updating source files. 
    Triggered when PTC peripheral is moved between secure projects.
    Arguments:
        :symbol : the symbol that triggered the callback
        :event : the new value. 
    Returns:
        :none
    """
    if event["value"] == False:
        nonSecureStatus = "SECURE"
    else:
        nonSecureStatus = "NON_SECURE"
        
    checknonsecureStatus()

def checknonsecureStatus():
    """Checks whether PTC is assigned as a secure peripheral. 
    If Secure then files associated with touch operation are moved to secure project.
    Arguments:
        :none
    Returns:
        none
    """
    if (Database.getSymbolValue("core", "PTC_IS_NON_SECURE") == False):
        nonSecureStatus = "SECURE"
    else:
        nonSecureStatus = "NON_SECURE"
        
    for kx in range(len(localProjectFilesList)):    
        entryname = localProjectFilesList[kx].getID()
        splitname = entryname.split('_')     
        
        if "PTC_SYS_DEF" == entryname :
            if (nonSecureStatus == "SECURE"):
                localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
            else:
                localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        
        if "PTC_SYS_INIT" == entryname:
            if (nonSecureStatus == "SECURE"):
                localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            else:
                localProjectFilesList[kx].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        
        localProjectFilesList[kx].setSecurity(nonSecureStatus)