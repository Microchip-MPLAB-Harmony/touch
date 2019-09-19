<#macro nodeComponent>
<#assign noCSD = 0>
<#list ["SAMD20","SAMD21", "SAML21", "SAMD10","SAMD11"] as i>
<#if DEVICE_NAME == i>
<#assign noCSD = 1>
</#if>
</#list>
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
<#if noCSD == 0>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
	<#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
    <#lt>#define NODE_${i}_PARAMS                                                                                               \
		<#lt>{                                                                                                                  \
		<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
		<#lt>}
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
	<#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
    <#lt>#define NODE_${i}_PARAMS                                                                                               \
		<#lt>{                                                                                                                  \
		<#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
		<#lt>}
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
</#macro>