/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    touch.h

  Summary:
    QTouch Modular Library

  Description:
    Configuration macros for touch library

*******************************************************************************/

/*******************************************************************************
Copyright (c) ${REL_YEAR} released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef TOUCH_H
#define TOUCH_H

#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END



/*----------------------------------------------------------------------------
 *     include files
 *----------------------------------------------------------------------------*/

#include "touch_api_ptc.h"

/**********************************************************/
/******************* Acquisition controls *****************/
/**********************************************************/
/* Defines the Measurement Time in milli seconds.
 * Range: 1 to 255.
 * Default value: 20.
 */
#define DEF_TOUCH_MEASUREMENT_PERIOD_MS ${DEF_TOUCH_MEASUREMENT_PERIOD_MS}

/* Defines the Type of sensor
 * Default value: NODE_MUTUAL.
 */
#define DEF_SENSOR_TYPE ${SENSE_TECHNOLOGY}

/* Set sensor calibration mode for charge share delay ,Prescaler or series resistor.
 * Range: CAL_AUTO_TUNE_NONE / CAL_AUTO_TUNE_RSEL / CAL_AUTO_TUNE_PRSC / CAL_AUTO_TUNE_CSD
 * Default value: CAL_AUTO_TUNE_NONE.
 */

#define DEF_PTC_CAL_OPTION   ${TUNE_MODE_SELECTED}

/* Defines the interrupt priority for the PTC. Set low priority to PTC interrupt for applications having interrupt time
 * constraints. Range: 0 to 2 Default: 2 (Lowest Priority)
 */
#define DEF_PTC_INTERRUPT_PRIORITY ${DEF_PTC_INTERRUPT_PRIORITY}

/* Calibration option to ensure full charge transfer */
/* Bits 7:0 = XX | TT SELECT_TAU | X | CAL_OPTION */
#define DEF_PTC_TAU_TARGET CAL_CHRG_5TAU
#define DEF_PTC_CAL_AUTO_TUNE (uint8_t)((DEF_PTC_TAU_TARGET << CAL_CHRG_TIME_POS) | DEF_PTC_CAL_OPTION)

/* Set default bootup acquisition frequency.
 * Range: FREQ_SEL_0 - FREQ_SEL_15 , FREQ_SEL_SPREAD
 * Default value: FREQ_SEL_0.
 */
#define DEF_SEL_FREQ_INIT ${DEF_SEL_FREQ_INIT}

/*----------------------------------------------------------------------------
 *     defines
 *----------------------------------------------------------------------------*/

/**********************************************************/
/***************** Node Params   ******************/
/**********************************************************/
/* Acquisition Set 1 */
/* Defines the number of sensor nodes in the acquisition set
 * Range: 1 to 65535.
 * Default value: 1
 */
#define DEF_NUM_CHANNELS (${TOUCH_CHAN_ENABLE_CNT})

/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay, NODE_RSEL_PRSC(series resistor, prescaler), NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */

 <#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
    <#assign TOUCH_ENABLE_CH_ = "TOUCH_ENABLE_CH_" + i>
    <#assign DEF_TOUCH_CHARGE_SHARE_DELAY = "DEF_TOUCH_CHARGE_SHARE_DELAY" + i>
    <#assign DEF_NOD_SERIES_RESISTOR = "DEF_NOD_SERIES_RESISTOR" + i>
    <#assign DEF_NOD_PTC_PRESCALER = "DEF_NOD_PTC_PRESCALER" + i>
    <#assign DEF_NOD_GAIN_ANA = "DEF_NOD_GAIN_ANA" + i>
    <#assign DEF_DIGI_FILT_GAIN = "DEF_DIGI_FILT_GAIN" + i>
    <#assign DEF_DIGI_FILT_OVERSAMPLING = "DEF_DIGI_FILT_OVERSAMPLING" + i>
	<#assign SELFCAP_INPUT = "SELFCAP-INPUT_" + i>
	<#assign MUTLCAP_X_INPUT = "MUTL-X-INPUT_" + i>
	<#assign MUTLCAP_Y_INPUT = "MUTL-Y-INPUT_" + i>
	
    <#if .vars[TOUCH_ENABLE_CH_]?has_content>
    <#if (.vars[TOUCH_ENABLE_CH_] != false)>  
	<#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
    <#lt>#define NODE_${i}_PARAMS                                                                                               \
		<#lt>{                                                                                                                  \
		<#lt>   X_NONE, ${.vars[SELFCAP_INPUT]}, ${.vars[DEF_TOUCH_CHARGE_SHARE_DELAY]}, NODE_RSEL_PRSC(${.vars[DEF_NOD_SERIES_RESISTOR]}, ${.vars[DEF_NOD_PTC_PRESCALER]}), NODE_GAIN(${.vars[DEF_NOD_GAIN_ANA]}, ${.vars[DEF_DIGI_FILT_GAIN]}), ${.vars[DEF_DIGI_FILT_OVERSAMPLING]}                   \
		<#lt>}
	<#else>
	<#lt>#define NODE_${i}_PARAMS                                                                                               \
		<#lt>{                                                                                                                  \
		<#lt>   ${.vars[MUTLCAP_X_INPUT]}, ${.vars[MUTLCAP_Y_INPUT]}, ${.vars[DEF_TOUCH_CHARGE_SHARE_DELAY]}, NODE_RSEL_PRSC(${.vars[DEF_NOD_SERIES_RESISTOR]}, ${.vars[DEF_NOD_PTC_PRESCALER]}), NODE_GAIN(${.vars[DEF_NOD_GAIN_ANA]}, ${.vars[DEF_DIGI_FILT_GAIN]}), ${.vars[DEF_DIGI_FILT_OVERSAMPLING]}\
		<#lt>}
	</#if>
    </#if>
    </#if>
</#list>

/**********************************************************/
/***************** Key Params   ******************/
/**********************************************************/
/* Defines the number of key sensors
 * Range: 1 to 65535.
 * Default value: 1
 */
#define DEF_NUM_SENSORS (${TOUCH_KEY_ENABLE_CNT})

/* Defines Key Sensor setting
 * {Sensor Threshold, Sensor Hysterisis, Sensor AKS}
 */
 <#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#assign TOUCH_ENABLE_KEY_ = "TOUCH_ENABLE_KEY_" + i>
	<#assign DEF_SENSOR_DET_THRESHOLD = "DEF_SENSOR_DET_THRESHOLD" + i>
	<#assign DEF_SENSOR_HYST = "DEF_SENSOR_HYST" + i>
	<#assign DEF_NOD_AKS = "DEF_NOD_AKS" + i>
	<#if .vars[TOUCH_ENABLE_KEY_]?has_content>
	<#if (.vars[TOUCH_ENABLE_KEY_] != false)>
    <#lt>#define KEY_${i}_PARAMS                                                                                            \
		<#lt>{                                                                                                              \
		<#lt>    ${.vars[DEF_SENSOR_DET_THRESHOLD]}, ${.vars[DEF_SENSOR_HYST]}, ${.vars[DEF_NOD_AKS]}                       \
		<#lt>}
	</#if>
	</#if>
 </#list>

/* De-bounce counter for additional measurements to confirm touch detection
 * Range: 0 to 255.
 * Default value: 4.
 */
#define DEF_TOUCH_DET_INT ${DEF_TOUCH_DET_INT}

/* De-bounce counter for additional measurements to confirm away from touch signal
 * to initiate Away from touch re-calibration.
 * Range: 0 to 255.
 * Default value: 5.
 */
#define DEF_ANTI_TCH_DET_INT ${DEF_ANTI_TCH_DET_INT}

/* Threshold beyond with automatic sensor recalibration is initiated.
 * Range: RECAL_100/ RECAL_50 / RECAL_25 / RECAL_12_5 / RECAL_6_25 / MAX_RECAL
 * Default value: RECAL_100.
 */
#define DEF_ANTI_TCH_RECAL_THRSHLD ${DEF_ANTI_TCH_RECAL_THRSHLD}

/* Rate at which sensor reference value is adjusted towards sensor signal value
 * when signal value is greater than reference.
 * Units: 200ms
 * Range: 0-255
 * Default value: 20u = 4 seconds.
 */
#define DEF_TCH_DRIFT_RATE ${DEF_TCH_DRIFT_RATE}

/* Rate at which sensor reference value is adjusted towards sensor signal value
 * when signal value is less than reference.
 * Units: 200ms
 * Range: 0-255
 * Default value: 5u = 1 second.
 */
#define DEF_ANTI_TCH_DRIFT_RATE ${DEF_ANTI_TCH_DRIFT_RATE}

/* Time to restrict drift on all sensor when one or more sensors are activated.
 * Units: 200ms
 * Range: 0-255
 * Default value: 20u = 4 seconds.
 */
#define DEF_DRIFT_HOLD_TIME ${DEF_DRIFT_HOLD_TIME}

/* Set mode for additional sensor measurements based on touch activity.
 * Range: REBURST_NONE / REBURST_UNRESOLVED / REBURST_ALL
 * Default value: REBURST_UNRESOLVED
 */
#define DEF_REBURST_MODE ${DEF_REBURST_MODE}

/* Sensor maximum ON duration upon touch.
 * Range: 0-255
 * Default value: 0
 */
#define DEF_MAX_ON_DURATION ${DEF_MAX_ON_DURATION}

<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
/**********************************************************/
/***************** Slider/Wheel Parameters ****************/
/**********************************************************/
/* Defines the number of scrollers (sliders or wheels)
 */
#define DEF_NUM_SCROLLERS ${TOUCH_SCROLLER_ENABLE_CNT}

/* Defines scroller parameter setting
 * {touch_scroller_type, touch_start_key, touch_scroller_size,
 * SCR_RESOL_DEADBAND(touch_scroller_resolution,touch_scroller_deadband), touch_scroller_hysterisis,
 * touch_scr_detect_threshold}
 * Configuring scr_detect_threshold: By default, scr_detect_threshold parameter should be
 * set equal to threshold value of the underlying keys. Then the parameter has to be tuned based on the actual contact
 * size of the touch when moved over the scroller. The contact size of the moving touch can be observed from
 * "contact_size" parameter on scroller runtime data structure.
 */
 <#list 0..TOUCH_SCROLLER_ENABLE_CNT-1 as i>
	<#assign TOUCH_ENABLE_SCROLLER_ = "TOUCH_ENABLE_SCROLLER_" + i>
	<#assign DEF_SCR_TYPE = "DEF_SCR_TYPE" + i>
	<#assign TOUCH_SCR_SIZE = "TOUCH_SCR_SIZE" + i>
	<#assign TOUCH_SCR_START_KEY = "TOUCH_SCR_START_KEY" + i>
	<#assign DEF_SCR_RESOLUTION = "DEF_SCR_RESOLUTION" + i>
	<#assign DEF_SCR_DEADBAND = "DEF_SCR_DEADBAND" + i>
	<#assign DEF_SCR_POS_HYS = "DEF_SCR_POS_HYS" + i>
	<#assign DEF_SCR_CONTACT_THRESHOLD = "DEF_SCR_CONTACT_THRESHOLD" + i>
	<#if .vars[TOUCH_ENABLE_SCROLLER_]?has_content>
	<#if (.vars[TOUCH_ENABLE_SCROLLER_] != false)>
    <#lt>#define SCROLLER_${i}_PARAMS                                                                                       \
		<#lt>{                                                                                                              \
		<#lt>    ${.vars[DEF_SCR_TYPE]}, ${.vars[TOUCH_SCR_START_KEY]}, ${.vars[TOUCH_SCR_SIZE]},                            \
		SCR_RESOL_DEADBAND(${.vars[DEF_SCR_RESOLUTION]}, ${.vars[DEF_SCR_DEADBAND]}),${.vars[DEF_SCR_POS_HYS]},${.vars[DEF_SCR_CONTACT_THRESHOLD]}\
		<#lt>}
	</#if>
	</#if>
 </#list>
</#if>

<#if ENABLE_FREQ_HOP==true>
/**********************************************************/
/********* Frequency Hop Module ****************/
/**********************************************************/

/* sets the frequency steps for hop.
 * Range: 3 to 7.
 * Default value: 3
 */
#define NUM_FREQ_STEPS ${FREQ_HOP_STEPS}

/* PTC Sampling Delay Selection - 0 to 15 PTC CLK cycles */

#define DEF_MEDIAN_FILTER_FREQUENCIES <#list 0..FREQ_HOP_STEPS-1 as i><#assign HOP_FREQ = "HOP_FREQ"+i><#if i == FREQ_HOP_STEPS-1>${.vars[HOP_FREQ]}<#else>${.vars[HOP_FREQ]},</#if></#list>

<#if FREQ_AUTOTUNE==true>
/* Enable / Disable the frequency hop auto tune
 * Range: 0 / 1
 * Default value: 1
 */
#define DEF_FREQ_AUTOTUNE_ENABLE ${(FREQ_AUTOTUNE)?then('1', '0')}

/* sets the maximum variance for Frequency Hop Auto tune.
 * Range: 1 to 255.
 * Default value: 15
 */
#define FREQ_AUTOTUNE_MAX_VARIANCE ${DEF_TOUCH_MAX_VARIANCE}

/* sets the Tune in count for Frequency Hop Auto tune.
 * Range: 1 to 255.
 * Default value: 6
 */
#define FREQ_AUTOTUNE_COUNT_IN ${DEF_TOUCH_TUNE_IN_COUNT}
</#if>
</#if>

/**********************************************************/
/***************** Communication - Data Streamer ******************/
/**********************************************************/
#define DEF_TOUCH_DATA_STREAMER_ENABLE ${(ENABLE_DATA_STREAMER)?then('1u', '0u')}

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // TOUCH_H
