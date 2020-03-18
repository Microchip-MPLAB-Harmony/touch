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
	#define DEF_SENSOR_TYPE ${SENSE_TECHNOLOGY}
</#if>


/* Set sensor calibration mode for charge share delay ,Prescaler or series resistor.
 * Range: CAL_AUTO_TUNE_NONE / CAL_AUTO_TUNE_RSEL / CAL_AUTO_TUNE_PRSC / CAL_AUTO_TUNE_CSD
 * Default value: CAL_AUTO_TUNE_NONE.
 */

#define DEF_PTC_CAL_OPTION   ${TUNE_MODE_SELECTED}

/* Defines the interrupt priority for the PTC. Set low priority to PTC interrupt for applications having interrupt time
 * constraints.
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

<#if DEVICE_NAME == "PIC32MZW">
/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay, 0, NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */
<#else>
/* Defines node parameter setting
 * {X-line, Y-line, Charge Share Delay, NODE_RSEL_PRSC(series resistor, prescaler), NODE_G(Analog Gain , Digital Gain),
 * filter level}
 */
</#if>
<#import "/node.h.ftl" as node>	
	
<@node.nodeComponent/>
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

<#if ENABLE_SURFACE==true>
/**********************************************************/
/***************** Surface Parameters ****************/
/**********************************************************/

/* Horizontal Start Key <0-65534>
 * Start key of horizontal axis
 * Range: 0 to 65534
 */
#define SURFACE_CS_START_KEY_H ${HORI_START_KEY}
/* Horizontal Number of Channel <0-255>
 * Number of Channels forming horizontal axis
 * Range: 0 to 255
 */
#define SURFACE_CS_NUM_KEYS_H ${HORI_NUM_KEY}
/* Vertical Start Key <0-65534>
 * Start key of vertical axis
 * Range: 0 to 65534
 */
#define SURFACE_CS_START_KEY_V ${VERT_START_KEY}
/* Vertical Number of Channel <0-255>
 * Number of Channels forming vertical axis
 * Range: 0 to 255
 */
#define SURFACE_CS_NUM_KEYS_V ${VERT_NUM_KEY}
/*  Position Resolution and Deadband Percentage
 *  Full scale position resolution reported for the axis and the deadband Percentage
 *  RESOL_2_BIT - RESOL_12_BIT
 *  DB_NONE - DB_15_PERCENT
 */
#define SURFACE_CS_RESOL_DB SCR_RESOL_DEADBAND(${DEF_POS_RESOLUTION}, ${DEF_DEADBAND_PERCENT})
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
#define SURFACE_CS_FILT_CFG SCR_MEDIAN_IIR(${EANBLE_MED_FILTER}, ${EANBLE_IIR_FILTER})
/* Position Hystersis <0-255>
 * The minimum travel distance to be reported after contact or direction change
 * Applicable to Horizontal and Vertical directions
 */
#define SURFACE_CS_POS_HYST ${DEF_POS_HYS}
/* Minimum Contact <0-65534>
 * The minimum contact size measurement for persistent contact tracking.
 * Contact size is the sum of neighbouring keys' touch deltas forming the touch contact.
 */
#define SURFACE_CS_MIN_CONTACT ${DEF_CONTACT_THRESHOLD}
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
#define TAP_RELEASE_TIMEOUT ${TAP_RELEASE_TIMEOUT}
/*  Tap Hold timeout <0-255>
 *	If a finger stays within the bounds set by TAP_AREA and is not removed, the firmware will report a Tap Hold gesture
 *once the gesture timer exceeds the TAP_HOLD_TIMEOUT value. HOLD_TAP is a single finger gesture whereas HOLD_TAP_DUAL
 *is dual finger gesture. Ideally, TAP_HOLD_TIMEOUT should be greater than the TAP_RELEASE_TIMEOUT and SWIPE_TIMEOUT.
 *  Unit: x10 ms
 *  Example: if TAP_HOLD_TIMEOUT is configured as 6, then the user should tap and hold inside the TAP_AREA for 60 ms to
 *qualify the gesture as tap and hold.
 */
#define TAP_HOLD_TIMEOUT ${TAP_HOLD_TIMEOUT}
/*  Swipe timeout <0-255>
 *	The SWIPE_TIMEOUT limits the amount of time allowed for the swipe gesture (initial finger press, moving in a
 *particular direction crossing the distance threshold and the liftoff). Ideally, SWIPE_TIMEOUT should be greater than
 *TAP_RELEASE_TIMEOUT but smaller than the TAP_HOLD_TIMEOUT. Unit: x10 ms Example: if SWIPE_TIMEOUT is configured as 5,
 *then the user should swipe in a particular direction and liftoff within 50 ms to qualify the gesture as swipe.
 */
#define SWIPE_TIMEOUT ${SWIPE_TIMEOUT}
/*  Horizontal Swipe distance threshold <0-255>
 *	HORIZONTAL_SWIPE_DISTANCE_THRESHOLD controls the distance travelled in the X axis direction for detecting Left and
 *Right Swipe gestures. Unit: X-coordinate Example: If HORIZONTAL_SWIPE_DISTANCE_THRESHOLD is configured as 50, and a
 *user places their finger at x-coordinate 100, they must move to at least x-coordinate 50 to record a left swipe
 *gesture.
 */
#define HORIZONTAL_SWIPE_DISTANCE_THRESHOLD ${HORIZONTAL_SWIPE_DISTANCE_THRESHOLD}
/* 	Vertical swipe distance threshold <0-255>
 *	VERTICAL_SWIPE_DISTANCE_THRESHOLD controls the distance travelled in the Y axis direction for detecting Up and Down
 *Swipe gestures. Unit: Y-coordinate Example: if VERTICAL_SWIPE_DISTANCE_THRESHOLD is configured as 30, and a user
 *places their finger at y-coordinate 100, they must move to at least y-coordinate 70 to record a down swipe gesture.
 */
#define VERTICAL_SWIPE_DISTANCE_THRESHOLD ${VERTICAL_SWIPE_DISTANCE_THRESHOLD}
/* 	Tap area <0-255>
 *	The TAP_AREA bounds the finger to an area it must stay within to be considered a tap gesture when the finger is
 *removed and tap and hold gesture if the finger is not removed for sometime. Unit: coordinates Example: if TAP_AREA is
 *configured as 20, then user should tap within 20 coordinates to detect the tap gesture.
 */
#define TAP_AREA ${TAP_AREA}
/* 	Seq Tap distance threshold <0-255>
 *	The SEQ_TAP_DIST_THRESHOLD parameter limits the allowable distance of the current touch's initial press from the
 *liftoff position of the previous touch. It is used for multiple taps (double-tap, triple-tap etc). If the taps
 *following the first are within this threshold, then the tap counter will be incremented. If the following tap
 *gestures exceed this threshold, the previous touch is sent as a single tap and the current touch will reset the tap
 *counter. Unit: coordinates Example: if SEQ_TAP_DIST_THRESHOLD is configured as 20, after the first tap, if the user
 *taps again within 20 coordinates, it is considered as double tap gesture.
 */
#define SEQ_TAP_DIST_THRESHOLD ${DISTANCE_THRESHOLD}
/* 	Edge Boundary <0-255>
 *	The firmware can also be modified to define an edge region along the border of the touch sensor.
 *	With Edge Boundary defined, swipe gestures that start in an edge region will be reported as edge swipe gestures in
 *place of normal swipe gestures. To create an edge region, the EDGE_BOUNDARY is set with the size (in touch
 *coordinates) of the edge region. Unit: coordinates Example: Setting the EDGE_BOUNDARY parameter to 100 will designate
 *the area 100 units in from each edge as the edge region.
 */
#define EDGE_BOUNDARY ${EDGE_BOUNDARY}
/*  Wheel Post-scaler <0-255>
 *	The clockwise wheel is performed with 4 swipes (right->down->left->up). Similarly, the anti-clockwise wheel is
 *performed with 4 swipes (left->down->right->up). To detect a wheel, the minimum number of swipe required is wheel
 *start quadrant count + wheel post scaler. Once the wheel is detected, for post scaler number of swipe detections, the
 *wheel counter will be incremented by 1. Example: if wheel post scaler is 2, then for each two swipe detection, the
 *wheel counter will be incremented by 1.
 */
#define WHEEL_POSTSCALER ${WHEEL_POSTSCALER}
/* 	Wheel Start Quadrant count <2-255>
 *	The wheel gesture movement can be broken down into 90 degree arcs.
 *	The firmware watches for a certain number of arcs to occur in a circular pattern before starting to report wheel
 *gesture information. The number of arcs that must be first detected is determined by the WHEEL_START_QUADRANT_COUNT
 *parameter. Lower values for this parameter make it faster to start a wheel gesture, but it also makes the firmware
 *prone to prematurely reporting wheel gesture information. Example: if WHEEL_START_QUADRANT_COUNT is configured as 2,
 *then after 180 degree, the gesture is updated as Wheel.
 */
#define WHEEL_START_QUADRANT_COUNT ${WHEEL_START_QUADRANT_COUNT}
/* 	Wheel Reverse Quadrant count <2-255>
 *	The WHEEL_REVERSE_QUADRANT_COUNT performs a similar function as WHEEL_START_QUADRANT_COUNT except it is used when
 *changing the direction of the wheel instead of starting it new. This is used to prevent quick toggling between
 *directions. Example: If WHEEL_REVERSE_QUADRANT_COUNT is set as 4 and after some wheel gestures, if the user changes
 *the direction of rotation, then only after 360 degree, it will be detected as one wheel gesture.
 */
#define WHEEL_REVERSE_QUADRANT_COUNT ${WHEEL_REVERSE_QUADRANT_COUNT}
<#if ENABLE_SURFACE2T==true>

/* Pinch Zoom Threshold <0-255>
 * The PINCH_ZOOM_THRESHOLD limits the allowable distance between the two fingers to detect the pinch and the zoom
 * gestures. After crossing the PINCH_ZOOM_THRESHOLD, if the distance between the contacts is reducing, then the gesture
 * is reported as 'PINCH'. After crossing the PINCH_ZOOM_THRESHOLD, if the distance between the contacts is increasing,
 * then the gesture is reported as 'ZOOM'. Unit: coordinates Example: if PINCH_ZOOM_THRESHOLD is configured as 20, then
 * after crossing 20 coordinates, it will be reported as the pinch gesture or the zoom gesture.
 */
#define PINCH_ZOOM_THRESHOLD ${PINCH_ZOOM_THRESHOLD}
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

/***************** Enable/Disbale Driven shield ***********/
/**********************************************************/
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if ((DS_DEDICATED_ENABLE == true) || (DS_PLUS_ENABLE == true)) >
#define DEF_ENABLE_DRIVEN_SHIELD 1u
<#else>
#define DEF_ENABLE_DRIVEN_SHIELD 0u
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

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // TOUCH_H
