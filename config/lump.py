def getPinValue(symbol,event):
	global enableLump
	if (enableLump.getValue() == True):
		global lumpSymbol
		lump_feature = lumpSymbol.getValue() 
		lump_items = lump_feature.split(";") 
		num_of_lumps = len(lump_items)
		for lmp in range(0,num_of_lumps):
			lump_x = [] 
			lump_y = []
			lump_split = lump_items[lmp].split(":")
			lump_node = lump_split[0]
			lump_node_array = lump_split[1].split(",")
			if ((touchSenseTechnology.getValue() == 0) or (touchSenseTechnology.getValue() == 2)):
				for item in lump_node_array:
					yCh = tchSelfPinSelection[int(item)].getValue()
					yCh = "Y(" +str(yCh) + ")"
					if yCh not in lump_y:
						lump_y.append(yCh)
				lumpy = "|".join(lump_y)
				tchSelfPinSelection[int(lump_node)].setKeyValue(lump_node,lumpy)
				tchSelfPinSelection[int(lump_node)].setValue(int(lump_node))
			elif (touchSenseTechnology.getValue() == 1):
				for item in lump_node_array:
					xCh = tchMutXPinSelection[int(item)].getValue()
					yCh = tchMutYPinSelection[int(item)].getValue()
					xCh = "X(" +str(xCh) + ")"
					yCh = "Y(" +str(yCh) + ")"
					if xCh not in lump_x:
						lump_x.append(xCh)
					if yCh not in lump_y:
						lump_y.append(yCh)
				lumpx = "|".join(lump_x)
				tchMutXPinSelection[int(lump_node)].setKeyValue(lump_node,lumpx)
				tchMutXPinSelection[int(lump_node)].setValue(int(lump_node))
				lumpy = "|".join(lump_y)
				tchMutYPinSelection[int(lump_node)].setKeyValue(lump_node,lumpy)
				tchMutYPinSelection[int(lump_node)].setValue(int(lump_node))

global lumpSymbol
lumpSymbol = qtouchComponent.createStringSymbol("LUMP_CONFIG", touchMenu)
lumpSymbol.setLabel("Lump Configuration")
lumpSymbol.setDefaultValue("")
lumpSymbol.setVisible(True)
lumpSymbol.setDependencies(getPinValue,["LUMP_CONFIG"])
global enableLump
enableLump = qtouchComponent.createBooleanSymbol("ENABLE_LUMP", touchMenu)
enableLump.setLabel("Enable Lump")
enableLump.setDefaultValue(False)