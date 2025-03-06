<#macro nodeComponent>

<#if JSONDATA?eval.features.core == "CVD">
/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay (CSD), 0, NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */
<#else>
<#if JSONDATA?eval.features.csd == true>
/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay (CSD), NODE_RSEL_PRSC(series resistor, prescaler), NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */
<#else>
/* Defines node parameter setting
 * {X-line, Y-line, NODE_RSEL_PRSC(series resistor, prescaler), NODE_GAIN(Analog Gain , Digital Gain), filter level}
 */
</#if>
</#if>


<#if JSONDATA?eval.features.csd == true && JSONDATA?eval.features.core == "CVD">
    <@Pic32mzwWithCSD/>
<#elseif JSONDATA?eval.features.csd == true>
    <#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
        <#if JSONDATA?eval.acquisition.boost_mode.global == true>
        <@boostPIC32CZ/>
        <#else>
        <@boostCSD/>
        </#if>
    <#else>
        <@noBoostCSD/>
    </#if>
<#else>
    <@noBoostNoCSD/>
</#if>
</#macro>

<#macro Pic32mzwWithCSD>
    <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
	    <#assign xInfo = .vars["FTL_X_INFO"]?split(",")[i]>
	    <#assign yInfo = .vars["FTL_Y_INFO"]?split(",")[i]>
		<#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   X_NONE, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#elseif SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD">
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${xInfo}, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#else>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${xInfo}, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        </#if>
    </#list>
</#macro>

<#macro boostCSD>
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
            <#lt>   ${x_lines}, ${y_lines}, ${csd}, NODE_RSEL_PRSC(${res}, (uint8_t)${prsc}), NODE_GAIN(${again}, ${dgain}), (uint8_t)${filter}                   \
            <#lt>}
        </#list>
</#macro>

<#macro boostPIC32CZ>
#define DEF_NUM_NODE_SETS (${MUTL_4P_NUM_GROUP}u)
    /* Number of node data */
#define DEF_NUM_NODES       (DEF_NUM_NODE_SETS * 4u)   
/* Number of pin definitions */
#define DEF_NUM_PINDEFS     (DEF_NUM_NODE_SETS * NUM_PINDEFS_MUTUAL_4P)

/* Bit mask forming */
#define TOUCH_BITMASK(np)  (uint32_t)((uint32_t) 1u << (np) )            
    
/* Touch constant definitions */
#define X(n)        TOUCH_BITMASK((n))
#define Y(n)        TOUCH_BITMASK((n))
#define X_NONE      (0u)
#define Y_NONE      (0u)
#define CEXT_NONE   (0xFFu)


/* X defined by bit mask for 4P - 4 bit masks per group */

<#list 0..MUTL_4P_NUM_GROUP-1 as i>
        <#assign x_lines = .vars["MUTL_4P_X_LINE"]?split("+")[i]>
        <#assign y_lines = .vars["MUTL_4P_Y_LINE"]?split("+")[i]>
#define X_MASK_ALL_${i}    ${x_lines?replace("{"," ")?replace("}"," ")}

#define Y_MASK_${i}         ${y_lines}
</#list>

/* Y mask of all groups */
#define Y_MASK_ALL  <#list 0..MUTL_4P_NUM_GROUP-1 as i>Y_MASK_${i},</#list>
/* X mask of all groups */
#define X_MASK_ALL  <#list 0..MUTL_4P_NUM_GROUP-1 as i>X_MASK_ALL_${i},</#list>

    <#list 0..MUTL_4P_NUM_GROUP-1 as i>
        <#assign csd = .vars["MUTL_4P_CSD"]?split("+")[i]>
        <#assign res = .vars["MUTL_4P_Y_RES"]?split("+")[i]>
        <#assign prsc = .vars["MUTL_4P_PRSC"]?split("+")[i]>
        <#assign again = .vars["MUTL_4P_AGAIN"]?split("+")[i]>
        <#assign dgain = .vars["MUTL_4P_DGAIN"]?split("+")[i]>
        <#assign filter = .vars["MUTL_4P_FL"]?split("+")[i]>
            <#lt>#define GRP_${i}_4P_PARAMS                                                                                               \
            <#lt>{                                                                                                                  \
            <#lt>    ${csd}, NODE_RSEL_PRSC(${res}, (uint8_t)${prsc}), NODE_GAIN(${again}, ${dgain}), (uint8_t)${filter}                   \
            <#lt>}
        </#list>
</#macro>

<#macro noBoostCSD>
    <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
        <#assign xInfo = .vars["FTL_X_INFO"]?split(",")[i]>
        <#assign yInfo = .vars["FTL_Y_INFO"]?split(",")[i]>
        <#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   X_NONE, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},(uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#elseif (SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${xInfo}, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},(uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#else>
            <#if  JSONDATA?eval.features.xy_multiplex == true && (ENABLE_SURFACE == true)>
                    <#if (i < VERT_START_KEY) || (i >= (HORI_NUM_KEY + HORI_START_KEY)) >
                <#lt>#define NODE_${i}_PARAMS                                                                                               \
                <#lt>{                                                                                                                  \
                <#lt>   ${xInfo}, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, (uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                <#lt>}
                    <#else>
                <#lt>#define NODE_${i}_PARAMS                                                                                               \
                <#lt>{                                                                                                                  \
                <#lt>  ${xInfo}, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, (uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                            <#lt>}
                    </#if>
            <#else>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt> ${xInfo}, ${yInfo}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, (uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
            </#if>
        </#if>
    </#list>
</#macro>

<#macro noBoostNoCSD>
    <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
	    <#assign xInfo = .vars["FTL_X_INFO"]?split(",")[i]>
	    <#assign yInfo = .vars["FTL_Y_INFO"]?split(",")[i]>
        <#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   X_NONE, ${yInfo}, (uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#elseif (SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${xInfo}, ${yInfo}, (uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#else>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${xInfo}, ${yInfo},  NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, (uint8_t)${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), (uint8_t)${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        </#if>
    </#list>
</#macro>
