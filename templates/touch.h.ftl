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
<#if TOUCH_CHAN_ENABLE_CNT == 0>
#error "Number of Touch sensor is defined as ZERO. Include atleast one touch sensor or remove Touch library in MCC."
<#else>
#include "device.h"

<#assign pic_devices = ["PIC32MZW","PIC32MZDA","PIC32CXBZ31","WBZ35"]>
<#assign pic32cz = ["PIC32CZCA80", "PIC32CZCA90"]>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END
//${DEVICE_NAME}
<#if pic_devices?seq_contains(DEVICE_NAME)>
<#else>
<#if LOW_POWER_KEYS?exists && LOW_POWER_KEYS !="">
    <#import "/eventlowpower.ftl" as eventlp>
    <#import "/softwarelowpower.ftl" as softwarelp>
</#if>
</#if>
<#import "/node.h.ftl" as node>

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
#define DEF_TOUCH_MEASUREMENT_PERIOD_MS ${DEF_TOUCH_MEASUREMENT_PERIOD_MS}u

/* Defines the Type of sensor
 * Default value: NODE_MUTUAL.
 */
    <#if SENSE_TECHNOLOGY == "NODE_SELFCAP">
        <#if ((DS_ADJACENT_SENSE_LINE_AS_SHIELD?exists)&&(DS_DEDICATED_PIN_ENABLE?exists))>
            <#if (DS_ADJACENT_SENSE_LINE_AS_SHIELD == true) || (DS_DEDICATED_PIN_ENABLE == true)> 
#define DEF_SENSOR_TYPE NODE_SELFCAP_SHIELD
            <#else>
#define DEF_SENSOR_TYPE ${SENSE_TECHNOLOGY}
            </#if>
        <#else>
#define DEF_SENSOR_TYPE ${SENSE_TECHNOLOGY}
        </#if>
    <#else>
        <#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
#define DEF_SENSOR_TYPE NODE_MUTUAL_4P
        <#else>
#define DEF_SENSOR_TYPE ${SENSE_TECHNOLOGY}
        </#if>
    </#if>

<#if pic32cz?seq_contains(DEVICE_NAME)>
<#else>
/* Set sensor calibration mode for charge share delay ,Prescaler or series resistor.
 * Range: CAL_AUTO_TUNE_NONE / CAL_AUTO_TUNE_RSEL / CAL_AUTO_TUNE_PRSC / CAL_AUTO_TUNE_CSD
 * Default value: CAL_AUTO_TUNE_NONE.
 */

#define DEF_PTC_CAL_OPTION   ${TUNE_MODE_SELECTED}

/* Calibration option to ensure full charge transfer */
/* Bits 7:0 = XX | TT SELECT_TAU | X | CAL_OPTION */
#define DEF_PTC_TAU_TARGET CAL_CHRG_5TAU
#define DEF_PTC_CAL_AUTO_TUNE (uint8_t)((DEF_PTC_TAU_TARGET << CAL_CHRG_TIME_POS) | DEF_PTC_CAL_OPTION)
</#if>

<#if pic_devices?seq_contains(DEVICE_NAME)>
<#else>
/* Defines the interrupt priority for the PTC. Set low priority to PTC interrupt for applications having interrupt time
 * constraints.
 */
#define DEF_PTC_INTERRUPT_PRIORITY ${DEF_PTC_INTERRUPT_PRIORITY}u
</#if>

/* Set default bootup acquisition frequency.
 * Range: FREQ_SEL_0 - FREQ_SEL_15 , FREQ_SEL_SPREAD
 * Default value: FREQ_SEL_0.
 */
#define DEF_SEL_FREQ_INIT ${DEF_SEL_FREQ_INIT}

<#if pic32cz?seq_contains(DEVICE_NAME)>
/* Set default wakeup exponent.
 * Range: 4u to 15u
 * Default value: 4u.
 */    
#define DEF_PTC_WAKEUP_EXP ${DEF_PTC_WAKEUP_EXP}u
</#if>

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
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
#define DEF_NUM_CHANNELS (${MUTL_4P_NUM_GROUP}u<<2u)
<#else>
#define DEF_NUM_CHANNELS (${TOUCH_CHAN_ENABLE_CNT}u)
</#if>

<@node.nodeComponent/>

/**********************************************************/
/***************** Key Params   ******************/
/**********************************************************/
<#if ENABLE_SELF_MUTUAL?exists && ENABLE_SELF_MUTUAL == true>

<#else>
/* Defines the number of key sensors
 * Range: 1 to 65535.
 * Default value: 1
 */
#define DEF_NUM_SENSORS (${TOUCH_KEY_ENABLE_CNT}u)

/* Defines Key Sensor setting
 * {Sensor Threshold, Sensor Hysterisis, Sensor AKS}
 */
 <#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#assign TOUCH_ENABLE_KEY_ = "TOUCH_ENABLE_KEY_" + i>
	<#assign DEF_SENSOR_DET_THRESHOLD = ("DEF_SENSOR_DET_THRESHOLD" + i)>
	<#assign DEF_SENSOR_HYST = "DEF_SENSOR_HYST" + i>
	<#assign DEF_NOD_AKS = "DEF_NOD_AKS" + i>

    <#lt>#define KEY_${i}_PARAMS                                                                                            \
		<#lt>{                                                                                                              \
		<#lt>    ${.vars[DEF_SENSOR_DET_THRESHOLD]}, (uint8_t)${.vars[DEF_SENSOR_HYST]}, (uint8_t)${.vars[DEF_NOD_AKS]}                       \
		<#lt>}

 </#list>

/* De-bounce counter for additional measurements to confirm touch detection
 * Range: 0 to 255.
 * Default value: 4.
 */
#define DEF_TOUCH_DET_INT ${DEF_TOUCH_DET_INT}u

/* De-bounce counter for additional measurements to confirm away from touch signal
 * to initiate Away from touch re-calibration.
 * Range: 0 to 255.
 * Default value: 5.
 */
#define DEF_ANTI_TCH_DET_INT ${DEF_ANTI_TCH_DET_INT}u

/* Threshold beyond with automatic sensor recalibration is initiated.
 * Range: RECAL_100/ RECAL_50 / RECAL_25 / RECAL_12_5 / RECAL_6_25 / MAX_RECAL
 * Default value: RECAL_100.
 */
#define DEF_ANTI_TCH_RECAL_THRSHLD (uint8_t)${DEF_ANTI_TCH_RECAL_THRSHLD}

/* Rate at which sensor reference value is adjusted towards sensor signal value
 * when signal value is greater than reference.
 * Units: 200ms
 * Range: 0-255
 * Default value: 20u = 4 seconds.
 */
#define DEF_TCH_DRIFT_RATE ${DEF_TCH_DRIFT_RATE}u

/* Rate at which sensor reference value is adjusted towards sensor signal value
 * when signal value is less than reference.
 * Units: 200ms
 * Range: 0-255
 * Default value: 5u = 1 second.
 */
#define DEF_ANTI_TCH_DRIFT_RATE ${DEF_ANTI_TCH_DRIFT_RATE}u

/* Time to restrict drift on all sensor when one or more sensors are activated.
 * Units: 200ms
 * Range: 0-255
 * Default value: 20u = 4 seconds.
 */
#define DEF_DRIFT_HOLD_TIME ${DEF_DRIFT_HOLD_TIME}u

/* Set mode for additional sensor measurements based on touch activity.
 * Range: REBURST_NONE / REBURST_UNRESOLVED / REBURST_ALL
 * Default value: REBURST_UNRESOLVED
 */
#define DEF_REBURST_MODE (uint8_t)${DEF_REBURST_MODE}

/* Sensor maximum ON duration upon touch.
 * Range: 0-255
 * Default value: 0
 */
#define DEF_MAX_ON_DURATION ${DEF_MAX_ON_DURATION}u

</#if>
<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
/**********************************************************/
/***************** Slider/Wheel Parameters ****************/
/**********************************************************/
/* Defines the number of scrollers (sliders or wheels)
 */
#define DEF_NUM_SCROLLERS ${TOUCH_SCROLLER_ENABLE_CNT}u

/* Defines scroller parameter setting
 * {touch_scroller_type, touch_start_key, touch_scroller_size,
 * SCROLLER_RESOL_DEADBAND(touch_scroller_resolution,touch_scroller_deadband), touch_scroller_hysterisis,
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
		<#lt>    (uint8_t)${.vars[DEF_SCR_TYPE]}, ${.vars[TOUCH_SCR_START_KEY]}, ${.vars[TOUCH_SCR_SIZE]},                            \
		SCROLLER_RESOL_DEADBAND((uint8_t)${.vars[DEF_SCR_RESOLUTION]}, (uint8_t)${.vars[DEF_SCR_DEADBAND]}),(uint8_t)${.vars[DEF_SCR_POS_HYS]},${.vars[DEF_SCR_CONTACT_THRESHOLD]}\
		<#lt>}
	</#if>
	</#if>
 </#list>
</#if>
</#if>

<#if ENABLE_SURFACE==true>
/**********************************************************/
/***************** Surface Parameters ****************/
/**********************************************************/

/* Horizontal Start Key <0-65534>
 * Start key of horizontal axis
 * Range: 0 to 65534
 */
#define SURFACE_CS_START_KEY_H ${HORI_START_KEY}u
/* Horizontal Number of Channel <0-255>
 * Number of Channels forming horizontal axis
 * Range: 0 to 255
 */
#define SURFACE_CS_NUM_KEYS_H ${HORI_NUM_KEY}u
/* Vertical Start Key <0-65534>
 * Start key of vertical axis
 * Range: 0 to 65534
 */
#define SURFACE_CS_START_KEY_V ${VERT_START_KEY}u
/* Vertical Number of Channel <0-255>
 * Number of Channels forming vertical axis
 * Range: 0 to 255
 */
#define SURFACE_CS_NUM_KEYS_V ${VERT_NUM_KEY}u
/*  Position Resolution and Deadband Percentage
 *  Full scale position resolution reported for the axis and the deadband Percentage
 *  RESOL_2_BIT - RESOL_12_BIT
 *  DB_NONE - DB_15_PERCENT
 */
#define SURFACE_CS_RESOL_DB SCR_RESOL_DEADBAND((uint8_t)${DEF_POS_RESOLUTION}, (uint8_t)${DEF_DEADBAND_PERCENT})
/* Median filter enable and  IIR filter Config
 * Median Filter <0-1>
 * Enable or Disable Median Filter
 * enable - 1
 * disable - 0
 * IIR filter <0-3>
 * Configure IIR filter
 *  0 - None
 *  1 - 25%
 *  2 - 50%
 *  3 - 75%
 */
#define SURFACE_CS_FILT_CFG SCR_MEDIAN_IIR(${ENABLE_MED_FILTER}u, ${ENABLE_IIR_FILTER}u)
/* Position Hystersis <0-255>
 * The minimum travel distance to be reported after contact or direction change
 * Applicable to Horizontal and Vertical directions
 */
#define SURFACE_CS_POS_HYST ${DEF_POS_HYS}u
/* Minimum Contact <0-65534>
 * The minimum contact size measurement for persistent contact tracking.
 * Contact size is the sum of neighbouring keys' touch deltas forming the touch contact.
 */
#define SURFACE_CS_MIN_CONTACT ${DEF_CONTACT_THRESHOLD}u
</#if>

<#if ENABLE_GESTURE==true>
/**********************************************************/
/***************** Gesture Parameters ****************/
/**********************************************************/

/*	Tap Release timeout  <3-255>
 *	The TAP_RELEASE_TIMEOUT parameter limits the amount of time allowed between the initial finger press and the
 *liftoff. Exceeding this value will cause the firmware to not consider the gesture as a tap gesture.
 *  TAP_RELEASE_TIMEOUT should be lesser than the TAP_HOLD_TIMEOUT and SWIPE_TIMEOUT.
 *  Unit: x10 ms
 *  Example: if TAP_RELEASE_TIMEOUT is configured as 3, then the user should finish tapping within 30 ms to qualify the
 *gesture as tap.
 */
#define TAP_RELEASE_TIMEOUT ${TAP_RELEASE_TIMEOUT}u
/*  Tap Hold timeout <0-255>
 *	If a finger stays within the bounds set by TAP_AREA and is not removed, the firmware will report a Tap Hold gesture
 *once the gesture timer exceeds the TAP_HOLD_TIMEOUT value. HOLD_TAP is a single finger gesture whereas HOLD_TAP_DUAL
 *is dual finger gesture. Ideally, TAP_HOLD_TIMEOUT should be greater than the TAP_RELEASE_TIMEOUT and SWIPE_TIMEOUT.
 *  Unit: x10 ms
 *  Example: if TAP_HOLD_TIMEOUT is configured as 6, then the user should tap and hold inside the TAP_AREA for 60 ms to
 *qualify the gesture as tap and hold.
 */
#define TAP_HOLD_TIMEOUT ${TAP_HOLD_TIMEOUT}u
/*  Swipe timeout <0-255>
 *	The SWIPE_TIMEOUT limits the amount of time allowed for the swipe gesture (initial finger press, moving in a
 *particular direction crossing the distance threshold and the liftoff). Ideally, SWIPE_TIMEOUT should be greater than
 *TAP_RELEASE_TIMEOUT but smaller than the TAP_HOLD_TIMEOUT. Unit: x10 ms Example: if SWIPE_TIMEOUT is configured as 5,
 *then the user should swipe in a particular direction and liftoff within 50 ms to qualify the gesture as swipe.
 */
#define SWIPE_TIMEOUT ${SWIPE_TIMEOUT}u
/*  Horizontal Swipe distance threshold <0-255>
 *	HORIZONTAL_SWIPE_DISTANCE_THRESHOLD controls the distance travelled in the X axis direction for detecting Left and
 *Right Swipe gestures. Unit: X-coordinate Example: If HORIZONTAL_SWIPE_DISTANCE_THRESHOLD is configured as 50, and a
 *user places their finger at x-coordinate 100, they must move to at least x-coordinate 50 to record a left swipe
 *gesture.
 */
#define HORIZONTAL_SWIPE_DISTANCE_THRESHOLD ${HORIZONTAL_SWIPE_DISTANCE_THRESHOLD}u
/* 	Vertical swipe distance threshold <0-255>
 *	VERTICAL_SWIPE_DISTANCE_THRESHOLD controls the distance travelled in the Y axis direction for detecting Up and Down
 *Swipe gestures. Unit: Y-coordinate Example: if VERTICAL_SWIPE_DISTANCE_THRESHOLD is configured as 30, and a user
 *places their finger at y-coordinate 100, they must move to at least y-coordinate 70 to record a down swipe gesture.
 */
#define VERTICAL_SWIPE_DISTANCE_THRESHOLD ${VERTICAL_SWIPE_DISTANCE_THRESHOLD}u
/* 	Tap area <0-255>
 *	The TAP_AREA bounds the finger to an area it must stay within to be considered a tap gesture when the finger is
 *removed and tap and hold gesture if the finger is not removed for sometime. Unit: coordinates Example: if TAP_AREA is
 *configured as 20, then user should tap within 20 coordinates to detect the tap gesture.
 */
#define TAP_AREA ${TAP_AREA}u
/* 	Seq Tap distance threshold <0-255>
 *	The SEQ_TAP_DIST_THRESHOLD parameter limits the allowable distance of the current touch's initial press from the
 *liftoff position of the previous touch. It is used for multiple taps (double-tap, triple-tap etc). If the taps
 *following the first are within this threshold, then the tap counter will be incremented. If the following tap
 *gestures exceed this threshold, the previous touch is sent as a single tap and the current touch will reset the tap
 *counter. Unit: coordinates Example: if SEQ_TAP_DIST_THRESHOLD is configured as 20, after the first tap, if the user
 *taps again within 20 coordinates, it is considered as double tap gesture.
 */
#define SEQ_TAP_DIST_THRESHOLD ${DISTANCE_THRESHOLD}u
/* 	Edge Boundary <0-255>
 *	The firmware can also be modified to define an edge region along the border of the touch sensor.
 *	With Edge Boundary defined, swipe gestures that start in an edge region will be reported as edge swipe gestures in
 *place of normal swipe gestures. To create an edge region, the EDGE_BOUNDARY is set with the size (in touch
 *coordinates) of the edge region. Unit: coordinates Example: Setting the EDGE_BOUNDARY parameter to 100 will designate
 *the area 100 units in from each edge as the edge region.
 */
#define EDGE_BOUNDARY ${EDGE_BOUNDARY}u
/*  Wheel Post-scaler <0-255>
 *	The clockwise wheel is performed with 4 swipes (right->down->left->up). Similarly, the anti-clockwise wheel is
 *performed with 4 swipes (left->down->right->up). To detect a wheel, the minimum number of swipe required is wheel
 *start quadrant count + wheel post scaler. Once the wheel is detected, for post scaler number of swipe detections, the
 *wheel counter will be incremented by 1. Example: if wheel post scaler is 2, then for each two swipe detection, the
 *wheel counter will be incremented by 1.
 */
#define WHEEL_POSTSCALER ${WHEEL_POSTSCALER}u
/* 	Wheel Start Quadrant count <2-255>
 *	The wheel gesture movement can be broken down into 90 degree arcs.
 *	The firmware watches for a certain number of arcs to occur in a circular pattern before starting to report wheel
 *gesture information. The number of arcs that must be first detected is determined by the WHEEL_START_QUADRANT_COUNT
 *parameter. Lower values for this parameter make it faster to start a wheel gesture, but it also makes the firmware
 *prone to prematurely reporting wheel gesture information. Example: if WHEEL_START_QUADRANT_COUNT is configured as 2,
 *then after 180 degree, the gesture is updated as Wheel.
 */
#define WHEEL_START_QUADRANT_COUNT ${WHEEL_START_QUADRANT_COUNT}u
/* 	Wheel Reverse Quadrant count <2-255>
 *	The WHEEL_REVERSE_QUADRANT_COUNT performs a similar function as WHEEL_START_QUADRANT_COUNT except it is used when
 *changing the direction of the wheel instead of starting it new. This is used to prevent quick toggling between
 *directions. Example: If WHEEL_REVERSE_QUADRANT_COUNT is set as 4 and after some wheel gestures, if the user changes
 *the direction of rotation, then only after 360 degree, it will be detected as one wheel gesture.
 */
#define WHEEL_REVERSE_QUADRANT_COUNT ${WHEEL_REVERSE_QUADRANT_COUNT}u
<#if ENABLE_SURFACE2T==true>

/* Pinch Zoom Threshold <0-255>
 * The PINCH_ZOOM_THRESHOLD limits the allowable distance between the two fingers to detect the pinch and the zoom
 * gestures. After crossing the PINCH_ZOOM_THRESHOLD, if the distance between the contacts is reducing, then the gesture
 * is reported as 'PINCH'. After crossing the PINCH_ZOOM_THRESHOLD, if the distance between the contacts is increasing,
 * then the gesture is reported as 'ZOOM'. Unit: coordinates Example: if PINCH_ZOOM_THRESHOLD is configured as 20, then
 * after crossing 20 coordinates, it will be reported as the pinch gesture or the zoom gesture.
 */
#define PINCH_ZOOM_THRESHOLD ${PINCH_ZOOM_THRESHOLD}u
</#if>
#define DEF_GESTURE_TIME_BASE_MS 10u
</#if>

<#if ENABLE_FREQ_HOP==true>
/**********************************************************/
/********* Frequency Hop Module ****************/
/**********************************************************/

/* sets the frequency steps for hop.
 * Range: 3 to 7.
 * Default value: 3
 */
#define NUM_FREQ_STEPS ${FREQ_HOP_STEPS}u

/* PTC Sampling Delay Selection - 0 to 15 PTC CLK cycles */

#define DEF_MEDIAN_FILTER_FREQUENCIES <#list 0..FREQ_HOP_STEPS-1 as i><#assign HOP_FREQ = "HOP_FREQ"+i><#if i == FREQ_HOP_STEPS-1>(uint8_t)${.vars[HOP_FREQ]}<#else>(uint8_t)${.vars[HOP_FREQ]},</#if></#list>

<#if FREQ_AUTOTUNE==true>
/* Enable / Disable the frequency hop auto tune
 * Range: 0 / 1
 * Default value: 1
 */
#define DEF_FREQ_AUTOTUNE_ENABLE ${(FREQ_AUTOTUNE)?then('1', '0')}u

/* sets the maximum variance for Frequency Hop Auto tune.
 * Range: 1 to 255.
 * Default value: 15
 */
#define FREQ_AUTOTUNE_MAX_VARIANCE ${DEF_TOUCH_MAX_VARIANCE}u

/* sets the Tune in count for Frequency Hop Auto tune.
 * Range: 1 to 255.
 * Default value: 6
 */
#define FREQ_AUTOTUNE_COUNT_IN ${DEF_TOUCH_TUNE_IN_COUNT}u
</#if>
</#if>

<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>  
    <#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == true>
        <#if (DEVICE_NAME == "SAML10")||(DEVICE_NAME == "SAML11")||(DEVICE_NAME == "SAML1xE")> 
            <@eventlp.lowpower_SAML/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "PIC32CMLE00")||(DEVICE_NAME == "PIC32CMLS00")||(DEVICE_NAME == "PIC32CMLS60")>
            <@eventlp.lowpower_PIC32CM/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "SAMD21")||(DEVICE_NAME == "SAMDA1")||(DEVICE_NAME == "SAMHA1")>
            <@eventlp.lowpower_samd21_da1_ha1/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "SAMD20")>
            <@eventlp.lowpower_samd20/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "SAML22")>
            <@eventlp.lowpower_SAML22/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "SAML21")>
            <@eventlp.lowpower_SAML21/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "SAMC20")||(DEVICE_NAME == "SAMC21")||(DEVICE_NAME == "PIC32CMJH01")||(DEVICE_NAME == "PIC32CMJH00")>
            <@eventlp.lowpower_samc20_c21/>
            <@eventlp.lowpower_params_common/>
        <#elseif (DEVICE_NAME == "PIC32CZCA80")||(DEVICE_NAME == "PIC32CZCA90")>
            <@eventlp.lowpower_PIC32CZ/>
            <@eventlp.lowpower_params_common/>
        </#if>
    </#if>
    <#if ENABLE_EVENT_LP?exists>
    <#if ENABLE_EVENT_LP == false>
        <#--  <#if (DEVICE_NAME == "SAML10")||(DEVICE_NAME == "SAML11")>
            <@softwarelp.lowpower_SAML/>
        <#elseif (DEVICE_NAME == "PIC32CMLE00")||(DEVICE_NAME == "PIC32CMLS00")||(DEVICE_NAME == "PIC32CMLS60")>
            <@softwarelp.lowpower_PIC32CM/>
            <@eventlp.lowpower_params_saml/>
        <#elseif (DEVICE_NAME == "SAMD20")||(DEVICE_NAME == "SAMD21")||(DEVICE_NAME == "SAMDA1")||(DEVICE_NAME == "SAMHA1")>
            <@softwarelp.lowpower_samd21_da1_ha1/>
            <@eventlp.lowpower_params_samdx/>
        <#elseif (DEVICE_NAME == "SAMD20")>
            <@softwarelp.lowpower_samd20/>
            <@eventlp.lowpower_params_samdx/>
        <#elseif (DEVICE_NAME == "SAMC20")||(DEVICE_NAME == "SAMC21")||(DEVICE_NAME == "PIC32CMJH01")||(DEVICE_NAME == "PIC32CMJH00")>
            <@softwarelp.lowpower_samc20_c21/>
            <@eventlp.lowpower_params_samc2x/>
        </#if>  -->
        <@softwarelp.lowpower_params_noevs/>
    </#if>
    <#else>
    <@softwarelp.lowpower_params_noevs/> 
    </#if>
</#if>
/**********************************************************/
/***************** Communication - Data Streamer ******************/
/**********************************************************/
#define DEF_TOUCH_DATA_STREAMER_ENABLE ${(ENABLE_DATA_STREAMER)?then('1u', '0u')}

<#if ENABLE_TOUCH_TUNE_WITH_PLUGIN == true>
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
#warning "MPLAB Touch does not work with Boost Mode. Instead use Data Visualizer from Touch Configurator->Parameters->Tune option."
#define DEF_TOUCH_TUNE_ENABLE 0u
<#else>
#define DEF_TOUCH_TUNE_ENABLE ${(ENABLE_TOUCH_TUNE_WITH_PLUGIN)?then('1u', '0u')}
</#if>
</#if>


<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if ((DS_DEDICATED_ENABLE == true) || (DS_PLUS_ENABLE == true)) >
/**********************************************************/
/***************** Enable/Disbale Driven shield ***********/
/**********************************************************/
#define DEF_ENABLE_DRIVEN_SHIELD 1u
</#if>
</#if>
/**********************************************************/

<#if ENABLE_KRONOCOMM == true>
#define KRONOCOMM_UART 1u
#define KRONOCOMM_ENABLE 1u
<#if ENABLE_GESTURE==true>
#define KRONO_GESTURE_ENABLE 1u
<#else>
#define KRONO_GESTURE_ENABLE 0u
</#if>
</#if>

<#if DEVICE_NAME == "PIC32MZDA">
#define TOUCH_DMA_CHANNEL ${TOUCH_PIC32MZDA_DMA}u
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // TOUCH_H
</#if>
