
/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.

  File Name:
    qtm_surface_cs2t_0x0025_api.h

  Summary:
    QTouch Modular Library

  Description:
    API for Surface two-touch module
	
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
Filename : qtm_surface_2finger_touch_api.h
Project : QTouch Modular Library
Purpose : Structs and definitions for use within modules
------------------------------------------------------------------------------
Copyright (C) 2019 Microchip. All rights reserved.
------------------------------------------------------------------------------
============================================================================*/

#ifndef TOUCH_API_SURFACE_CS2T_H
#define TOUCH_API_SURFACE_CS2T_H

/* Include files */
#include <stdint.h>
#include "qtm_common_components_api.h"

/* Common status bits */
#define TOUCH_ACTIVE                (uint8_t)((uint8_t)1u<<0u) 		/* Bit 0 */
#define SURFACE_REBURST	    	    (uint8_t)((uint8_t)1u<<7u) 		/* Bit 7 */

/* Contact status bits */
#define POSITION_CHANGE		    (uint8_t)((uint8_t)1u<<1u) 		/* Bit 1 */
#define POSITION_H_INC		    (uint8_t)((uint8_t)1u<<2u) 		/* Bit 2 */
#define POSITION_H_DEC		    (uint8_t)((uint8_t)1u<<3u) 		/* Bit 3 */
#define POSITION_V_INC		    (uint8_t)((uint8_t)1u<<4u) 		/* Bit 4 */
#define POSITION_V_DEC		    (uint8_t)((uint8_t)1u<<5u) 		/* Bit 5 */

/* Surface status bits */
#define POS_MERGED_H		    (uint8_t)((uint8_t)1u<<4u) 		/* Bit 4 */
#define POS_MERGED_V		    (uint8_t)((uint8_t)1u<<5u) 		/* Bit 5 */


/* Extract Resolution / Deadband */
#define SCR_RESOLUTION(m) ((uint8_t)(((m) & 0xF0u) >> 4u))
#define SCR_DEADBAND(m) ((uint8_t)((m) & 0x0Fu))

/* Combine Resolution / Deadband */
#define SCR_RESOL_DEADBAND(r,p) ((uint8_t)(((r) << 4u)|(p)))

/* Position filtering */
#define POSITION_IIR_MASK		0x03u
#define POSITION_MEDIAN_ENABLE	0x10u
#define SCR_MEDIAN_IIR(r,p) ((uint8_t)(((r) << 4u)|(p)))

/* scroller resolution setting */
typedef enum tag_resolution_t
{
  RESOL_2_BIT = 2,
  RESOL_3_BIT,
  RESOL_4_BIT,
  RESOL_5_BIT,
  RESOL_6_BIT,
  RESOL_7_BIT,
  RESOL_8_BIT,
  RESOL_9_BIT,
  RESOL_10_BIT,
  RESOL_11_BIT,
  RESOL_12_BIT	
}
scr_resolution_t;


/* scroller deadband percentage setting */
typedef enum tag_deadband_t
{
  DB_NONE,
  DB_1_PERCENT,
  DB_2_PERCENT,
  DB_3_PERCENT,
  DB_4_PERCENT,
  DB_5_PERCENT,
  DB_6_PERCENT,
  DB_7_PERCENT,
  DB_8_PERCENT,
  DB_9_PERCENT,
  DB_10_PERCENT,
  DB_11_PERCENT,
  DB_12_PERCENT,
  DB_13_PERCENT,
  DB_14_PERCENT,
  DB_15_PERCENT
}
scr_deadband_t;

/*----------------------------------------------------------------------------
*     Structure Declarations
*----------------------------------------------------------------------------*/

/* Surface CS Configuration */
typedef struct
{
  uint16_t start_key_h;				/* Start key of horizontal axis */
  uint8_t number_of_keys_h;			/* Number of keys in horizontal axis */
  uint16_t start_key_v;				/* Start key of vertical axis */
  uint8_t number_of_keys_v;			/* Number of keys in vertical axis */
  uint8_t resol_deadband;			    /* Resolution 2 to 12 bits | Deadband 0% to 15% */
  uint8_t position_hysteresis;		/* Distance threshold for initial move or direction change */
  uint8_t position_filter;			/* Bits 1:0 = IIR (0% / 25% / 50% / 75%), Bit 4 = Enable Median Filter (3-point) */
  uint16_t contact_min_threshold;		/* Contact threshold / Sum of 4 deltas */
  qtm_touch_key_data_t *qtm_touch_key_data;	/* Pointer to touch key data */
}qtm_surface_cs_config_t;

/* Surface Data */
typedef struct
{
  uint8_t qt_surface_cs2t_status;
}qtm_surface_cs2t_data_t;

/* Contact Data */
typedef struct
{
  uint8_t qt_contact_status;
  uint16_t h_position_abs;
  uint16_t h_position;
  uint16_t v_position_abs;
  uint16_t v_position;
  uint16_t contact_size;
}qtm_surface_contact_data_t;


/* Container */
typedef struct
{
  qtm_surface_cs2t_data_t *qtm_surface_cs2t_data;
  qtm_surface_contact_data_t *qtm_surface_contact_data;    
  qtm_surface_cs_config_t *qtm_surface_cs_config;
} qtm_surface_cs2t_control_t;

/*----------------------------------------------------------------------------
*   prototypes
*----------------------------------------------------------------------------*/

/*============================================================================
touch_ret_t qtm_init_surface_cs2t(qtm_surface_cs_control_t *qtm_surface_cs_control);
------------------------------------------------------------------------------
Purpose: Initialize a scroller
Input  : Pointer to scroller group control data
Output : TOUCH_SUCCESS
Notes  : none
============================================================================*/
touch_ret_t qtm_init_surface_cs2t(qtm_surface_cs2t_control_t *qtm_surface_cs2t_control);

/*============================================================================
touch_ret_t qtm_surface_cs_process(qtm_surface_cs_control_t *qtm_surface_cs_control);
------------------------------------------------------------------------------
Purpose: Scroller position calculation and filtering
Input  : Pointer to scroller group control data
Output : TOUCH_SUCCESS
Notes  : none
============================================================================*/
touch_ret_t qtm_surface_cs2t_process(qtm_surface_cs2t_control_t *qtm_surface_cs2t_control);

/*============================================================================
uint16_t qtm_get_surface_cs2t_module_id(void)
------------------------------------------------------------------------------
Purpose: Returns the module ID
Input  : none
Output : Module ID
Notes  : none
============================================================================*/
uint16_t qtm_get_surface_cs2t_module_id(void);

/*============================================================================
uint8_t qtm_get_surface_cs2t_module_ver(void)
------------------------------------------------------------------------------
Purpose: Returns the module Firmware version
Input  : none
Output : Module ID - Upper nibble major / Lower nibble minor
Notes  : none
============================================================================*/
uint8_t qtm_get_surface_cs2t_module_ver(void);

#endif    /* TOUCH_API_SURFACE_CS2T_H */
