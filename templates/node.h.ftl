<#macro nodeComponent>
<#assign CSD = 0>
<#assign drivenShieldSupported = 0>
<#list ["SAML10","SAML11","SAML22","SAMC20","SAMC21","SAME54","SAME53","SAME51","SAMD51","PIC32MZW"] as i>
	<#if DEVICE_NAME == i>
		<#assign CSD = 1>
	</#if>
</#list>
<#list ["SAML10","SAML11","PIC32MZW"] as i>
	<#if DEVICE_NAME == i>
		<#assign drivenShieldSupported = 1>
	</#if>
</#list>
<#if ENABLE_LUMP == true>
<#assign LUMP_INDI = []>
 <#list LUMP_CONFIG?split(";")as x>
<#assign LUMP_INDI = LUMP_INDI + [x]>
</#list>
<#assign LUMP_NUM = LUMP_INDI?size>
<#assign input0 =[]>
<#assign input1 =[]>

<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM)as a>
<#assign input0 += [.vars["SELFCAP-INPUT_" + a]]>
</#list>
<#list (TOUCH_CHAN_ENABLE_CNT-LUMP_NUM)..(TOUCH_CHAN_ENABLE_CNT-1)as b>
<#assign input1 += [.vars["SELFCAP-INPUT_" + b]]>
</#list>
</#if>
<#if DEVICE_NAME == "PIC32MZW">
<#if (TOUCH_CHAN_ENABLE_CNT > 0) >
<#assign MUTL_SURFACE_X = []>
<#list HORI_START_KEY..(HORI_START_KEY+HORI_NUM_KEY-1) as j>
	<#if MUTL_SURFACE_X ?seq_contains(.vars["MUTL-X-INPUT_" + j])>			    
	<#else>
		<#assign MUTL_SURFACE_X +=  [.vars["MUTL-X-INPUT_" + j]]>
	</#if>	
</#list>
<#assign MUTL_SURFACE_Y = []>
<#list VERT_START_KEY..(VERT_START_KEY+VERT_NUM_KEY-1) as j>
	<#if MUTL_SURFACE_Y ?seq_contains(.vars["MUTL-Y-INPUT_" + j])>			    
	<#else>
		<#assign MUTL_SURFACE_Y +=  [.vars["MUTL-Y-INPUT_" + j]]>
	</#if>	
</#list>	 
<#if CSD == 1>
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")||(SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
			<#if drivenShieldSupported == 1>
				<#if (DS_DEDICATED_PIN_ENABLE == true)>
					<#assign DRIVEN_SHIELD_PIN_TOTAL = []>
					<#if DS_DEDICATED_PIN_ENABLE == true>
						<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["DS_DEDICATED_PIN"]]>
					</#if>
					<#lt>#define NODE_${i}_PARAMS                                                           \
					<#lt>{                                                                              \
					<#lt>   ${DRIVEN_SHIELD_PIN_TOTAL?join("|")}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
			<#else>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
			</#if>
			<#else>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
			</#if>
		</#if>	
	</#list>
	<#if (ENABLE_SURFACE == false && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
			<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
		</#list>	
	</#if>
	<#if (ENABLE_SURFACE == true && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#if (VERT_START_KEY >0)>
			<#list 0..(VERT_START_KEY-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
		<#list VERT_START_KEY..(VERT_START_KEY+VERT_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                           \
			<#lt>{                                                                              \
			<#lt>  ${MUTL_SURFACE_X?join("|")},  ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#list HORI_START_KEY..(HORI_START_KEY+HORI_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                           \
			<#lt>{                                                                              \
			<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${MUTL_SURFACE_Y?join("|")} , ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#if (TOUCH_CHAN_ENABLE_CNT - (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY ) >0)>
			<#list (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY)..(TOUCH_CHAN_ENABLE_CNT-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
	</#if>
<#else>
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")||(SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
			<#if drivenShieldSupported == 1>
				<#if (DS_DEDICATED_PIN_ENABLE == true)||(DS_ADJACENT_SENSE_LINE_AS_SHIELD == true)>
					<#assign DRIVEN_SHIELD_PIN_TOTAL = []>
					<#if DS_DEDICATED_PIN_ENABLE == true>
						<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["DS_DEDICATED_PIN"]]>
					</#if>
					<#if DS_ADJACENT_SENSE_LINE_AS_SHIELD == true>
<#if ENABLE_LUMP == true>
<#if i < TOUCH_CHAN_ENABLE_CNT-LUMP_NUM >
<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM) as j>
	<#if .vars["SELFCAP-INPUT_" + i] != input0[j]>
	<#assign DRIVEN_SHIELD_PIN_TOTAL += [input0[j]]>
	</#if>
</#list>
<#else>
<#assign LUMP_NODE_INDI = []>
	<#list .vars["SELFCAP-INPUT_" + i]?split("|")as x>
	<#assign LUMP_NODE_INDI = LUMP_NODE_INDI + [x]>
	</#list>
<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM) as j>
<#assign par = 0>
	<#list 0..((LUMP_NODE_INDI?size)-1) as y>
		<#if (LUMP_NODE_INDI[y] == input0[j])>
		<#assign par = 1>
		</#if>
	</#list>
<#if par == 0>
<#assign DRIVEN_SHIELD_PIN_TOTAL += [input0[j]]>
</#if>
</#list>
</#if>
					<#else>
						<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as j>
							<#if i != j>
								<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["SELFCAP-INPUT_" + j]]>
							</#if>
						</#list>
					</#if>
					</#if>					
					<#lt>#define NODE_${i}_PARAMS                                                           \
					<#lt>{                                                                              \
					<#lt>   ${DRIVEN_SHIELD_PIN_TOTAL?join("|")}, ${.vars["SELFCAP-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
				<#else>
					<#lt>#define NODE_${i}_PARAMS                                                           \
					<#lt>{                                                                              \
					<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
				</#if>
			<#else>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
			</#if>
		</#if>	
	</#list>
	<#if (ENABLE_SURFACE == false && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
			<#lt>#define NODE_${i}_PARAMS                                                           \
			<#lt>{                                                                              \
			<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
			<#lt>}
		</#list>	
	</#if>
	<#if (ENABLE_SURFACE == true && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#if (VERT_START_KEY >0)>
			<#list 0..(VERT_START_KEY-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
		<#list VERT_START_KEY..(VERT_START_KEY+VERT_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                           \
			<#lt>{                                                                              \
			<#lt>  ${MUTL_SURFACE_X?join("|")},  ${.vars["MUTL-Y-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#list HORI_START_KEY..(HORI_START_KEY+HORI_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                           \
			<#lt>{                                                                              \
			<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${MUTL_SURFACE_Y?join("|")} , 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#if (TOUCH_CHAN_ENABLE_CNT - (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY ) >0)>
			<#list (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY)..(TOUCH_CHAN_ENABLE_CNT-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                           \
				<#lt>{                                                                              \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, 0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
	</#if>
</#if>

</#if>
<#else>
<#if (TOUCH_CHAN_ENABLE_CNT > 0) >
<#assign MUTL_SURFACE_X = []>
<#list HORI_START_KEY..(HORI_START_KEY+HORI_NUM_KEY-1) as j>
	<#if MUTL_SURFACE_X ?seq_contains(.vars["MUTL-X-INPUT_" + j])>			    
	<#else>
		<#assign MUTL_SURFACE_X +=  [.vars["MUTL-X-INPUT_" + j]]>
	</#if>	
</#list>
<#assign MUTL_SURFACE_Y = []>
<#list VERT_START_KEY..(VERT_START_KEY+VERT_NUM_KEY-1) as j>
	<#if MUTL_SURFACE_Y ?seq_contains(.vars["MUTL-Y-INPUT_" + j])>			    
	<#else>
		<#assign MUTL_SURFACE_Y +=  [.vars["MUTL-Y-INPUT_" + j]]>
	</#if>	
</#list>	 
<#if CSD == 1>
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")||(SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
			<#if drivenShieldSupported == 1>
				<#if (DS_DEDICATED_PIN_ENABLE == true)||(DS_ADJACENT_SENSE_LINE_AS_SHIELD == true)>
					<#assign DRIVEN_SHIELD_PIN_TOTAL = []>
					<#if DS_DEDICATED_PIN_ENABLE == true>
						<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["DS_DEDICATED_PIN"]]>
					</#if>
					<#if DS_ADJACENT_SENSE_LINE_AS_SHIELD == true>
<#if ENABLE_LUMP == true>
<#if i < TOUCH_CHAN_ENABLE_CNT-LUMP_NUM >
<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM) as j>
	<#if .vars["SELFCAP-INPUT_" + i] != input0[j]>
	<#assign DRIVEN_SHIELD_PIN_TOTAL += [input0[j]]>
	</#if>
</#list>
<#else>
<#assign LUMP_NODE_INDI = []>
	<#list .vars["SELFCAP-INPUT_" + i]?split("|")as x>
	<#assign LUMP_NODE_INDI = LUMP_NODE_INDI + [x]>
	</#list>
<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM) as j>
<#assign par = 0>
	<#list 0..((LUMP_NODE_INDI?size)-1) as y>
		<#if (LUMP_NODE_INDI[y] == input0[j])>
		<#assign par = 1>
		</#if>
	</#list>
<#if par == 0>
<#assign DRIVEN_SHIELD_PIN_TOTAL += [input0[j]]>
</#if>
</#list>
</#if>
					<#else>
						<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as j>
							<#if i != j>
								<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["SELFCAP-INPUT_" + j]]>
							</#if>
						</#list>
					</#if>
					</#if>					
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${DRIVEN_SHIELD_PIN_TOTAL?join("|")}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
			<#else>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
			</#if>
			<#else>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
			</#if>
		</#if>	
	</#list>
	<#if (ENABLE_SURFACE == false && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
			<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
		</#list>	
	</#if>
	<#if (ENABLE_SURFACE == true && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#if (VERT_START_KEY >0)>
			<#list 0..(VERT_START_KEY-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
		<#list VERT_START_KEY..(VERT_START_KEY+VERT_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                                                               \
			<#lt>{                                                                                                                  \
			<#lt>  ${MUTL_SURFACE_X?join("|")},  ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#list HORI_START_KEY..(HORI_START_KEY+HORI_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                                                               \
			<#lt>{                                                                                                                  \
			<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${MUTL_SURFACE_Y?join("|")} , ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#if (TOUCH_CHAN_ENABLE_CNT - (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY ) >0)>
			<#list (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY)..(TOUCH_CHAN_ENABLE_CNT-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
	</#if>
<#else>
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")||(SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
			<#if drivenShieldSupported == 1>
				<#if (DS_DEDICATED_PIN_ENABLE == true)||(DS_ADJACENT_SENSE_LINE_AS_SHIELD == true)>
					<#assign DRIVEN_SHIELD_PIN_TOTAL = []>
					<#if DS_DEDICATED_PIN_ENABLE == true>
						<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["DS_DEDICATED_PIN"]]>
					</#if>
					<#if DS_ADJACENT_SENSE_LINE_AS_SHIELD == true>
<#if ENABLE_LUMP == true>
<#if i < TOUCH_CHAN_ENABLE_CNT-LUMP_NUM >
<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM) as j>
	<#if .vars["SELFCAP-INPUT_" + i] != input0[j]>
	<#assign DRIVEN_SHIELD_PIN_TOTAL += [input0[j]]>
	</#if>
</#list>
<#else>
<#assign LUMP_NODE_INDI = []>
	<#list .vars["SELFCAP-INPUT_" + i]?split("|")as x>
	<#assign LUMP_NODE_INDI = LUMP_NODE_INDI + [x]>
	</#list>
<#list 0..(TOUCH_CHAN_ENABLE_CNT-1-LUMP_NUM) as j>
<#assign par = 0>
	<#list 0..((LUMP_NODE_INDI?size)-1) as y>
		<#if (LUMP_NODE_INDI[y] == input0[j])>
		<#assign par = 1>
		</#if>
	</#list>
<#if par == 0>
<#assign DRIVEN_SHIELD_PIN_TOTAL += [input0[j]]>
</#if>
</#list>
</#if>
					<#else>
						<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as j>
							<#if i != j>
								<#assign DRIVEN_SHIELD_PIN_TOTAL += [.vars["SELFCAP-INPUT_" + j]]>
							</#if>
						</#list>
					</#if>
					</#if>					
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${DRIVEN_SHIELD_PIN_TOTAL?join("|")}, ${.vars["SELFCAP-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
				<#else>
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
				</#if>
			<#else>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
				<#lt>}
			</#if>
		</#if>	
	</#list>
	<#if (ENABLE_SURFACE == false && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
			<#lt>#define NODE_${i}_PARAMS                                                                                               \
			<#lt>{                                                                                                                  \
			<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
			<#lt>}
		</#list>	
	</#if>
	<#if (ENABLE_SURFACE == true && SENSE_TECHNOLOGY == "NODE_MUTUAL")>
		<#if (VERT_START_KEY >0)>
			<#list 0..(VERT_START_KEY-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
		<#list VERT_START_KEY..(VERT_START_KEY+VERT_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                                                               \
			<#lt>{                                                                                                                  \
			<#lt>  ${MUTL_SURFACE_X?join("|")},  ${.vars["MUTL-Y-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#list HORI_START_KEY..(HORI_START_KEY+HORI_NUM_KEY-1) as i>	
			<#lt>#define NODE_${i}_PARAMS                                                                                               \
			<#lt>{                                                                                                                  \
			<#lt>  ${.vars["MUTL-X-INPUT_" + i]}, ${MUTL_SURFACE_Y?join("|")} , NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
			<#lt>}
		</#list>
		<#if (TOUCH_CHAN_ENABLE_CNT - (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY ) >0)>
			<#list (VERT_START_KEY + VERT_NUM_KEY + HORI_NUM_KEY)..(TOUCH_CHAN_ENABLE_CNT-1) as i>
				<#lt>#define NODE_${i}_PARAMS                                                                                               \
				<#lt>{                                                                                                                  \
				<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}\
				<#lt>}
			</#list>
		</#if>
	</#if>
</#if>
</#if>
</#if>

</#macro>