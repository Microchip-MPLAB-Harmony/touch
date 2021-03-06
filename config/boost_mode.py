boostMenu = qtouchComponent.createMenuSymbol("Boost_MENU", touchMenu)
boostMenu.setLabel("Boost Mode Configuration")
boostMenu.setVisible(False)
#-------------- Boost Mode Related ---------------------#
enable4pMenu = qtouchComponent.createBooleanSymbol("ENABLE_BOOST", boostMenu)
enable4pMenu.setLabel("Enable Boost")
enable4pMenu.setDefaultValue(False)
touch4pNumGroup = qtouchComponent.createIntegerSymbol("MUTL_4P_NUM_GROUP", boostMenu)
touch4pNumGroup.setVisible(True)
touch4pNodeKeyMap = qtouchComponent.createStringSymbol("MUTL_4P_NODE_KEY_MAP", boostMenu)
touch4pNodeKeyMap.setLabel("4P Node to key map")
touch4pNodeKeyMap.setVisible(True)
touch4pXLines = qtouchComponent.createStringSymbol("MUTL_4P_X_LINE", boostMenu)
touch4pXLines.setLabel("4P X Config")
touch4pXLines.setVisible(True)
touch4pYLines = qtouchComponent.createStringSymbol("MUTL_4P_Y_LINE", boostMenu)
touch4pYLines.setLabel("4P Y Config")
touch4pYLines.setVisible(True)
touch4pcsd = qtouchComponent.createStringSymbol("MUTL_4P_CSD", boostMenu)
touch4pcsd.setLabel("4P CSD Config")
touch4pcsd.setVisible(True)
touch4pres = qtouchComponent.createStringSymbol("MUTL_4P_Y_RES", boostMenu)
touch4pres.setLabel("4P RES Config")
touch4pres.setVisible(True)
touch4pprsc = qtouchComponent.createStringSymbol("MUTL_4P_PRSC", boostMenu)
touch4pprsc.setLabel("4P PRSC Config")
touch4pprsc.setVisible(True)
touch4pagain = qtouchComponent.createStringSymbol("MUTL_4P_AGAIN", boostMenu)
touch4pagain.setLabel("4P AGAIN Config")
touch4pagain.setVisible(True)
touch4pdgain = qtouchComponent.createStringSymbol("MUTL_4P_DGAIN", boostMenu)
touch4pdgain.setLabel("4P DGAIN Config")
touch4pdgain.setVisible(True)
touch4pfl = qtouchComponent.createStringSymbol("MUTL_4P_FL", boostMenu)
touch4pfl.setLabel("4P FL Config")
touch4pfl.setVisible(True)
