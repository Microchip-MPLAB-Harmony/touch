################################################################################
#### Global Variables ####
################################################################################
global qtouchFilesArray
############################################################################
#### Code Generation ####
############################################################################
# Header File
tchKronocommUartHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_UART_HEADER", None)
tchKronocommUartHeaderFile.setSourcePath("/templates/kronocommuart.h.ftl")
tchKronocommUartHeaderFile.setOutputName("kronocommuart_sam.h")
tchKronocommUartHeaderFile.setDestPath("/touch/datastreamer/")
tchKronocommUartHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchKronocommUartHeaderFile.setType("HEADER")
tchKronocommUartHeaderFile.setEnabled(False)
tchKronocommUartHeaderFile.setMarkup(False)

# Header File
tchKronocommAdapterHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_ADAPTOR_HEADER", None)
tchKronocommAdapterHeaderFile.setSourcePath("/templates/kronocommadaptor.h.ftl")
tchKronocommAdapterHeaderFile.setOutputName("kronocommadaptor.h")
tchKronocommAdapterHeaderFile.setDestPath("/touch/datastreamer/")
tchKronocommAdapterHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchKronocommAdapterHeaderFile.setType("HEADER")
tchKronocommAdapterHeaderFile.setEnabled(False)
tchKronocommAdapterHeaderFile.setMarkup(False)

# Source File
tchKronocommUartSourceFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_UART_SOURCE", None)
tchKronocommUartSourceFile.setSourcePath("/templates/kronocommuart.c.ftl")
tchKronocommUartSourceFile.setOutputName("kronocommuart_sam.c")
tchKronocommUartSourceFile.setDestPath("/touch/datastreamer/")
tchKronocommUartSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchKronocommUartSourceFile.setType("SOURCE")
tchKronocommUartSourceFile.setEnabled(False)
tchKronocommUartSourceFile.setMarkup(True)

# Source File
tchKronocommAdapterSourceFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_ADAPTOR_SOURCE", None)
tchKronocommAdapterSourceFile.setSourcePath("/templates/kronocommadaptor.c.ftl")
tchKronocommAdapterSourceFile.setOutputName("kronocommadaptor.c")
tchKronocommAdapterSourceFile.setDestPath("/touch/datastreamer/")
tchKronocommAdapterSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchKronocommAdapterSourceFile.setType("SOURCE")
tchKronocommAdapterSourceFile.setEnabled(False)
tchKronocommAdapterSourceFile.setMarkup(True)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    qtouchFilesArray.append(tchKronocommUartHeaderFile)
    qtouchFilesArray.append(tchKronocommAdapterHeaderFile)
    qtouchFilesArray.append(tchKronocommUartSourceFile)
    qtouchFilesArray.append(tchKronocommAdapterSourceFile)

################################################################################
#### Component ####
################################################################################
