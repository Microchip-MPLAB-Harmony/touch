<#assign pic_devices = ["PIC32MZW","PIC32MZDA"]>
<#assign device_allpins_xy = ["PIC32CMLS00","PIC32CMLE00","SAML10","SAML11","SAME54","SAME53","SAME51","SAMD51"]>
<#macro nodeComponent>
<#assign CSD = 0>
<#list ["PIC32CMLS00","PIC32CMLE00","SAML10","SAML11","SAML22","SAMC20","SAMC21","SAME54","SAME53","SAME51","SAMD51","PIC32MZW","PIC32MZDA"] as csdSupported>
    <#if DEVICE_NAME == csdSupported>
        <#assign CSD = 1>
    </#if>
</#list>

<#if pic_devices?seq_contains(DEVICE_NAME)>
/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay, 0, NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */
<#else>
<#if CSD == 1>
/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay, NODE_RSEL_PRSC(series resistor, prescaler), NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */
<#else>
/* Defines node parameter setting
 * {X-line, Y-line, NODE_RSEL_PRSC, NODE_GAIN(Analog Gain , Digital Gain), filter level}
 */
</#if>
</#if>


<#if CSD == 1 && pic_devices?seq_contains(DEVICE_NAME)>
    <@Pic32mzwWithCSD/>
<#elseif CSD == 1>
    <#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
        <@boostCSD/>
    <#else>
        <@noBoostCSD/>
    </#if>
<#else>
    <@noBoostNoCSD/>
</#if>
</#macro>

<#macro Pic32mzwWithCSD>
    <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
        <#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},0, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
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
            <#lt>   ${x_lines}, ${y_lines}, ${csd}, NODE_RSEL_PRSC(${res}, ${prsc}), NODE_GAIN(${again}, ${dgain}), ${filter}                   \
            <#lt>}
        </#list>
</#macro>

<#macro noBoostCSD>
    <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
        <#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#elseif (SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#else>
            <#if  device_allpins_xy?seq_contains(DEVICE_NAME) && (ENABLE_SURFACE == true)>
                    <#if (i < VERT_START_KEY) || (i >= (HORI_NUM_KEY + HORI_START_KEY)) >
                <#lt>#define NODE_${i}_PARAMS                                                                                               \
                <#lt>{                                                                                                                  \
                <#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                <#lt>}
                    <#else>
            <#assign x_lines_surface = .vars["TOUCH_CH_SURFACE_X_LINES"]?split("+")[i-VERT_START_KEY]>
            <#assign y_lines_surface = .vars["TOUCH_CH_SURFACE_Y_LINES"]?split("+")[i-VERT_START_KEY]>
                <#lt>#define NODE_${i}_PARAMS                                                                                               \
                <#lt>{                                                                                                                  \
                <#lt>   ${x_lines_surface}, ${y_lines_surface}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]},NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                            <#lt>}
                    </#if>
            <#else>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   ${.vars["MUTL-X-INPUT_" + i]}, ${.vars["MUTL-Y-INPUT_" + i]}, ${.vars["DEF_TOUCH_CHARGE_SHARE_DELAY" + i]}, NODE_RSEL_PRSC(${.vars["DEF_NOD_SERIES_RESISTOR" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}), NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
            </#if>
        </#if>
    </#list>
</#macro>

<#macro noBoostNoCSD>
    <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
        <#if (SENSE_TECHNOLOGY == "NODE_SELFCAP")>
                    <#lt>#define NODE_${i}_PARAMS                                                                                               \
                    <#lt>{                                                                                                                  \
                    <#lt>   X_NONE, ${.vars["SELFCAP-INPUT_" + i]}, ${.vars["DEF_NOD_PTC_PRESCALER" + i]}, NODE_GAIN(${.vars["DEF_NOD_GAIN_ANA" + i]}, ${.vars["DEF_DIGI_FILT_GAIN" + i]}), ${.vars["DEF_DIGI_FILT_OVERSAMPLING" + i]}                   \
                    <#lt>}
        <#elseif (SENSE_TECHNOLOGY == "NODE_SELFCAP_SHIELD")>
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
</#macro>
