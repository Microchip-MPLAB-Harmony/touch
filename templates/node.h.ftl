<#macro nodeComponent>
<#assign CSD = 0>

<#list ["SAML10","SAML11","SAML22","SAMC20","SAMC21","SAME54","SAME53","SAME51","SAMD51","PIC32MZW"] as i>
	<#if DEVICE_NAME == i>
		<#assign CSD = 1>
	</#if>
</#list>
<#if CSD == 1 && DEVICE_NAME == "PIC32MZW">
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		<#elseif SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD">
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["DS_DEDICATED_PIN"]}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		<#else>
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		</#if>
	</#list>

<#elseif CSD == 1>
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
	<#list 0..MUTL_4P_NUM_GROUP-1 as i>
	<#assign x_lines = .vars["MUTL_4P_X_LINE"]?split("+")[i]>
	<#assign y_lines = .vars["MUTL_4P_Y_LINE"]?split("+")[i]>
	<#assign csd = .vars["MUTL_4P_CSD"]?split("+")[i]>
	<#assign res = .vars["MUTL_4P_Y_RES"]?split("+")[i]>
	<#assign prsc = .vars["MUTL_4P_PRSC"]?split("+")[i]>
	<#assign again = .vars["MUTL_4P_AGAIN"]?split("+")[i]>
	<#assign dgain = .vars["MUTL_4P_DGAIN"]?split("+")[i]>
	<#assign filter = .vars["MUTL_4P_FL"]?split("+")[i]>
		<#lt>#define GRP_${i}_4P_PARAMS                                                                                               \
		<#lt>{                                                                                                                  \
		<#lt>   ${x_lines}, ${y_lines}, ${csd}, NODE_RSEL_PRSC(${res}, ${prsc}), NODE_GAIN(${again}, ${dgain}), ${filter}                   \
		<#lt>}
	</#list>
<#else>
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")||(SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		<#else>
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		</#if>
	</#list>
</#if>
<#else>
	<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
		<#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")||(SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		<#else>
					<#lt>#define NODE_${i}_PARAMS                                                                                               \
					<#lt>{                                                                                                                  \
					<#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]},  NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
					<#lt>}
		</#if>
	</#list>
</#if>

</#macro>