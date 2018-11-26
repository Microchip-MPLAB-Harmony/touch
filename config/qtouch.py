def enableFrequencyHopSymbols(symbol,event):
    component = symbol.getComponent()
    if(event["value"] == True):
        #tchDataStreamerHeaderFile.setEnabled(True)
        component.getSymbolByID("FREQ_HOP_STEPS").setVisible(True)
        component.getSymbolByID("FREQ_AUTOTUNE").setVisible(True)
        component.getSymbolByID("HOP_FREQ0").setVisible(True)
        component.getSymbolByID("HOP_FREQ1").setVisible(True)
        component.getSymbolByID("HOP_FREQ2").setVisible(True)
    else:
        #tchDataStreamerHeaderFile.setEnabled(False)
        component.getSymbolByID("FREQ_HOP_STEPS").setVisible(False)
        component.getSymbolByID("FREQ_AUTOTUNE").setVisible(False)
        component.getSymbolByID("HOP_FREQ0").setVisible(False)
        component.getSymbolByID("HOP_FREQ1").setVisible(False)
        component.getSymbolByID("HOP_FREQ2").setVisible(False)
       #component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(False)

def enableDataStreamerFtlFiles(symbol,event):
    component = symbol.getComponent()

    if(event["value"] == True):
        #tchDataStreamerHeaderFile.setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_SOURCE").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_db").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_ds").setEnabled(True)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(True)
    else:
        #tchDataStreamerHeaderFile.setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_SOURCE").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_db").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_ds").setEnabled(False)
        component.getSymbolByID("TOUCH_DATA_STREAMER_HEADER_sc").setEnabled(False)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(qtouchComponent):

    touchMenu = qtouchComponent.createMenuSymbol("TOUCH_MENU", None)
    touchMenu.setLabel("Touch Configuration")

    execfile(Module.getPath() +"/config/acquisition.py")
    execfile(Module.getPath() +"/config/node.py")	
    execfile(Module.getPath() +"/config/key.py")
    execfile(Module.getPath() +"/config/sensor.py")
    # Enable Frequency Hop  
    enableFreqHopMenu = qtouchComponent.createBooleanSymbol("ENABLE_FREQ_HOP", touchMenu)
    enableFreqHopMenu.setLabel("Enable Frequency Hop")
    enableFreqHopMenu.setDefaultValue(False)
    enableFreqHopMenu.setDependencies(enableFrequencyHopSymbols,["ENABLE_FREQ_HOP"])
    execfile(Module.getPath() +"/config/freq_hop.py")
    # Enable Datastreamer  
    enableDataStreamerMenu = qtouchComponent.createBooleanSymbol("ENABLE_DATA_STREAMER", touchMenu)
    enableDataStreamerMenu.setLabel("Enable Data-Streamer")
    enableDataStreamerMenu.setDefaultValue(False)
    enableDataStreamerMenu.setDependencies(enableDataStreamerFtlFiles,["ENABLE_DATA_STREAMER"])
    execfile(Module.getPath() +"/config/datastreamer.py")
         
############################################################################
#### Code Generation ####
############################################################################
    #configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER", None)
    touchHeaderFile.setSourcePath("/templates/touch.h.ftl")
    touchHeaderFile.setOutputName("touch.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(True)
	
    # Header File
    touchHeaderFile = qtouchComponent.createFileSymbol("TOUCH_HEADER1", None)
    touchHeaderFile.setSourcePath("/templates/touch_api_ptc.h.ftl")
    touchHeaderFile.setOutputName("touch_api_ptc.h")
    touchHeaderFile.setDestPath("/touch/")
    touchHeaderFile.setProjectPath("config/" + "/touch/")
    touchHeaderFile.setType("HEADER")
    touchHeaderFile.setMarkup(True)
	
    # Source File
    touchSourceFile = qtouchComponent.createFileSymbol("TOUCH_SOURCE", None)
    touchSourceFile.setSourcePath("/templates/touch.c.ftl")
    touchSourceFile.setOutputName("touch.c")
    touchSourceFile.setDestPath("/touch/")
    touchSourceFile.setProjectPath("config/" + "/touch/")
    touchSourceFile.setType("SOURCE")
    touchSourceFile.setMarkup(True)


