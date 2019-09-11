
/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.

  File Name:
    qtm_gestures_2d_0x0023_api.h

  Summary:
    QTouch Modular Library

  Description:
    API for Gesture Module
	
*******************************************************************************/

/*******************************************************************************
Copyright (c) Microchip Technology Inc.  All rights reserved.

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

/*============================================================================
Filename : qtm_gestures_api.h
Project : QTouch Modular Library
Purpose : Structs and definitions for use within modules
------------------------------------------------------------------------------
Copyright (C) 2019 Microchip. All rights reserved.
------------------------------------------------------------------------------
============================================================================*/

#ifndef TOUCH_API_GESTURE_2D_H
#define TOUCH_API_GESTURE_2D_H

/* Include files */
#include <stdint.h>
#include "qtm_common_components_api.h"

/* Timebase */
#define GESTURE_TIMEBASE_DEFAULT         10u

/* gesture IDs */
#define NO_GESTURE                      0x00u
#define RIGHT_SWIPE                     0x10u
#define RIGHT_SWIPE_HOLD                0x12u
#define RIGHT_EDGE_SWIPE                0x11u
#define RIGHT_EDGE_SWIPE_HOLD           0x13u
#define RIGHT_SWIPE_DUAL                0x14u
#define RIGHT_SWIPE_HOLD_DUAL           0x16u
#define RIGHT_EDGE_SWIPE_DUAL           0x15u
#define RIGHT_EDGE_SWIPE_HOLD_DUAL      0x17u

#define LEFT_SWIPE                      0x20u
#define LEFT_SWIPE_HOLD                 0x22u
#define LEFT_EDGE_SWIPE                 0x21u
#define LEFT_EDGE_SWIPE_HOLD            0x23u
#define LEFT_SWIPE_DUAL                 0x24u
#define LEFT_SWIPE_HOLD_DUAL            0x26u
#define LEFT_EDGE_SWIPE_DUAL            0x25u
#define LEFT_EDGE_SWIPE_HOLD_DUAL       0x27u

#define UP_SWIPE                        0x30u
#define UP_SWIPE_HOLD                   0x32u
#define UP_EDGE_SWIPE                   0x31u
#define UP_EDGE_SWIPE_HOLD              0x33u
#define UP_SWIPE_DUAL                   0x34u
#define UP_SWIPE_HOLD_DUAL              0x36u
#define UP_EDGE_SWIPE_DUAL              0x35u
#define UP_EDGE_SWIPE_HOLD_DUAL         0x37u

#define DOWN_SWIPE                      0x40u
#define DOWN_SWIPE_HOLD                 0x42u
#define DOWN_EDGE_SWIPE                 0x41u
#define DOWN_EDGE_SWIPE_HOLD            0x43u
#define DOWN_SWIPE_DUAL                 0x44u
#define DOWN_SWIPE_HOLD_DUAL            0x46u
#define DOWN_EDGE_SWIPE_DUAL            0x45u
#define DOWN_EDGE_SWIPE_HOLD_DUAL       0x47u

#define HOLD_TAP                        0xd0u
#define HOLD_TAP_DUAL                   0xd4u
#define PRE_TAP                         0x8fu
#define TAP                             0x90u
#define DOUBLE_TAP		            	0x92u
#define TAP_DUAL                        0xa0u
#define PALM                            0xb0u

#define PINCH                           0xc0u
#define ZOOM                            0xc1u


#define GESTURE_RELEASED                0xA8u

#define CW_WHEEL                        0xf0u
#define CCW_WHEEL                       0xf1u
#define CW_WHEEL_DUAL                   0xf4u
#define CCW_WHEEL_DUAL                  0xf5u

/*----------------------------------------------------------------------------
* Structure Declarations
*----------------------------------------------------------------------------*/

/* Gestures 2D Configuration */
typedef struct
{
	uint16_t *horiz_position0;
	uint16_t *vertical_position0;
	uint8_t *surface_status0;
	uint16_t *horiz_position1;
	uint16_t *vertical_position1;
	uint8_t *surface_status1;
	uint8_t surface_resolution;
	uint8_t tapReleaseTimeout;
	uint8_t tapHoldTimeout;
	uint8_t swipeTimeout;
	uint8_t xSwipeDistanceThreshold;
	uint8_t ySwipeDistanceThreshold;
	uint8_t edgeSwipeDistanceThreshold;
	uint8_t tapDistanceThreshold;
	uint8_t seqTapDistanceThreshold;
	uint8_t edgeBoundary;
	int8_t wheelPostscaler;
	int8_t wheelStartQuadrantCount;
	int8_t wheelReverseQuadrantCount;
	uint8_t pinchZoomThreshold;
}qtm_gestures_2d_config_t;

/* Surface CS Data */
typedef struct
{
	uint8_t gestures_status;
	uint8_t gestures_which_gesture;
	uint8_t gestures_info;
}qtm_gestures_2d_data_t;

/* Container */
typedef struct
{
	qtm_gestures_2d_data_t *qtm_gestures_2d_data;
	qtm_gestures_2d_config_t *qtm_gestures_2d_config;
} qtm_gestures_2d_control_t;

/*----------------------------------------------------------------------------
* prototypes
*----------------------------------------------------------------------------*/
void qtm_gestures_2d_clearGesture(void);

/*============================================================================
touch_ret_t qtm_init_gestures_2d(void);
------------------------------------------------------------------------------
Purpose: Initialize gesture tracking variables
Input : -
Output : TOUCH_SUCCESS
Notes : none
============================================================================*/
touch_ret_t qtm_init_gestures_2d(void);

/*============================================================================
touch_ret_t qtm_gestures_2d_process(qtm_gestures_2d_control_t *qtm_gestures_2d_control);
------------------------------------------------------------------------------
Purpose: Gesture engine processes updated touch info
Input : Gesture control struct pointer
Output : ?TOUCH_SUCCESS?
Notes : none
============================================================================*/
touch_ret_t qtm_gestures_2d_process(qtm_gestures_2d_control_t *qtm_gestures_2d_control);

/*============================================================================
void qtm_update_gesture_2d_timer(uint16_t time_elapsed_since_update);
------------------------------------------------------------------------------
Purpose: Updates local variable with time period
Input  : Number of ms since last update
Output : none
Notes  : none
============================================================================*/
void qtm_update_gesture_2d_timer(uint16_t time_elapsed_since_update);

/*============================================================================
uint16_t qtm_get_gesture_2d_module_id(void);
------------------------------------------------------------------------------
Purpose: Returns the module ID
Input : none
Output : Module ID
Notes : none
============================================================================*/
uint16_t qtm_get_gesture_2d_module_id(void);

/*============================================================================
uint8_t qtm_get_gesture_2d_module_ver(void);
------------------------------------------------------------------------------
Purpose: Returns the module Firmware version
Input : none
Output : Module ID - Upper nibble major / Lower nibble minor
Notes : none
============================================================================*/
uint8_t qtm_get_gesture_2d_module_ver(void);

#endif /* TOUCH_API_GESTURE_2D_H */
