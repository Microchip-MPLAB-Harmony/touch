############################################################################
#### Code Generation ####
############################################################################


# Header File
tchDataStreamerHeaderFile = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER", None)
tchDataStreamerHeaderFile.setSourcePath("/src/datastreamer.h")
tchDataStreamerHeaderFile.setOutputName("datastreamer.h")
tchDataStreamerHeaderFile.setDestPath("/touch/datastreamer/")
tchDataStreamerHeaderFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchDataStreamerHeaderFile.setType("HEADER")
tchDataStreamerHeaderFile.setEnabled(False)
tchDataStreamerHeaderFile.setMarkup(False)

# Header File2
tchDsHeaderFileDb = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER_db", None)
tchDsHeaderFileDb.setSourcePath("/templates/03EB00000000000000AA5501.db.ftl")
tchDsHeaderFileDb.setOutputName("03EB00000000000000AA5501.db")
tchDsHeaderFileDb.setDestPath("/touch/datastreamer/")
tchDsHeaderFileDb.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchDsHeaderFileDb.setType("HEADER")
tchDsHeaderFileDb.setEnabled(False)
tchDsHeaderFileDb.setMarkup(True)

# Header File3
tchDsHeaderFileDs = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER_ds", None)
tchDsHeaderFileDs.setSourcePath("/templates/03EB00000000000000AA5501.ds.ftl")
tchDsHeaderFileDs.setOutputName("03EB00000000000000AA5501.ds")
tchDsHeaderFileDs.setDestPath("/touch/datastreamer/")
tchDsHeaderFileDs.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchDsHeaderFileDs.setType("HEADER")
tchDsHeaderFileDs.setEnabled(False)
tchDsHeaderFileDs.setMarkup(True)

# Header File4
tchDsHeaderFileSc = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_HEADER_sc", None)
tchDsHeaderFileSc.setSourcePath("/templates/03EB00000000000000AA5501.sc.ftl")
tchDsHeaderFileSc.setOutputName("03EB00000000000000AA5501.sc")
tchDsHeaderFileSc.setDestPath("/touch/datastreamer/")
tchDsHeaderFileSc.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchDsHeaderFileSc.setType("HEADER")
tchDsHeaderFileSc.setEnabled(False)
tchDsHeaderFileSc.setMarkup(True)

# Source File
tchDataStreamerSourceFile = qtouchComponent.createFileSymbol("TOUCH_DATA_STREAMER_SOURCE", None)
tchDataStreamerSourceFile.setSourcePath("/templates/datastreamer_UART_sam.c.ftl")
tchDataStreamerSourceFile.setOutputName("datastreamer_UART_sam.c")
tchDataStreamerSourceFile.setDestPath("/touch/datastreamer/")
tchDataStreamerSourceFile.setProjectPath("config/" + configName + "/touch/datastreamer/")
tchDataStreamerSourceFile.setType("SOURCE")
tchDataStreamerSourceFile.setEnabled(False)
tchDataStreamerSourceFile.setMarkup(True)