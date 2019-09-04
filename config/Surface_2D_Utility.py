################################################################################
#### Global Variables ####
################################################################################

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
tchKronocommUartHeaderFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_ADAPTOR_HEADER", None)
tchKronocommUartHeaderFile.setSourcePath("/templates/kronocommadaptor.h.ftl")
tchKronocommUartHeaderFile.setOutputName("kronocommadaptor.h")
tchKronocommUartHeaderFile.setDestPath("/touch/datastreamer/")
tchKronocommUartHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchKronocommUartHeaderFile.setType("HEADER")
tchKronocommUartHeaderFile.setEnabled(False)
tchKronocommUartHeaderFile.setMarkup(False)

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
tchKronocommUartSourceFile = qtouchComponent.createFileSymbol("TOUCH_KRONOCOMM_ADAPTOR_SOURCE", None)
tchKronocommUartSourceFile.setSourcePath("/templates/kronocommadaptor.c.ftl")
tchKronocommUartSourceFile.setOutputName("kronocommadaptor.c")
tchKronocommUartSourceFile.setDestPath("/touch/datastreamer/")
tchKronocommUartSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchKronocommUartSourceFile.setType("SOURCE")
tchKronocommUartSourceFile.setEnabled(False)
tchKronocommUartSourceFile.setMarkup(True)

################################################################################
#### Component ####
################################################################################
