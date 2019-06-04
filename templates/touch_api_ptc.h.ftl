
/*============================================================================
  Touch Library ${REL_VER} Release
  
Company  : Microchip Technology Inc.

File Name: touch_api_ptc.h

Summary  : QTouch Modular Library

Purpose  : Includes the Module API header files based on the configured modules,
          prototypes for touch.c file and Application helper API functions
	  
Important Note: Do not edit this file manually.

Usage License: Refer mplab_harmony_license.md file for license information

Support: Visit http://www.microchip.com/support/hottopics.aspx
               to create MySupport case.

------------------------------------------------------------------------------
Copyright (c) ${REL_YEAR} Microchip. All rights reserved.
------------------------------------------------------------------------------
============================================================================*/

#ifndef TOUCH_API_PTC_H
#define TOUCH_API_PTC_H

#ifdef __cplusplus
extern "C" {
#endif // __cplusplus

/*----------------------------------------------------------------------------
 *     include files
 *----------------------------------------------------------------------------*/


#include "qtm_common_components_api.h"
#include "qtm_binding_layer_0x0005_api.h"
#include "qtm_acq_${DEVICE_NAME?lower_case}_${MODULE_ID}_api.h"
#include "qtm_touch_key_0x0002_api.h"
<#if ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE!=true>
#include "qtm_freq_hop_0x0006_api.h"
<#elseif ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE==true>
#include "qtm_freq_hop_auto_0x0004_api.h"
</#if>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
#include "qtm_scroller_0x000b_api.h"
</#if>
<#if ENABLE_SURFACE1T==true>
#include "qtm_surface_cs_0x0021_api.h"
</#if>
<#if ENABLE_SURFACE2T==true>
#include "qtm_surface_cs2t_0x0025_api.h"
</#if>
<#if ENABLE_GESTURE==true>
#include "qtm_gestures_2d_0x0023_api.h"
</#if>
/*----------------------------------------------------------------------------
 *   prototypes
 *----------------------------------------------------------------------------*/
/* Application Helper API's */
uint16_t get_sensor_node_signal(uint16_t sensor_node);
void     update_sensor_node_signal(uint16_t sensor_node, uint16_t new_signal);
uint16_t get_sensor_node_reference(uint16_t sensor_node);
void     update_sensor_node_reference(uint16_t sensor_node, uint16_t new_reference);
uint16_t get_sensor_cc_val(uint16_t sensor_node);
void     update_sensor_cc_val(uint16_t sensor_node, uint16_t new_cc_value);
uint8_t  get_sensor_state(uint16_t sensor_node);
void     update_sensor_state(uint16_t sensor_node, uint8_t new_state);
void     calibrate_node(uint16_t sensor_node);
uint8_t  get_scroller_state(uint16_t sensor_node);
uint16_t get_scroller_position(uint16_t sensor_node);

void touch_timer_handler(void);
void touch_init(void);
void touch_process(void);

void touch_timer_config(void);

#ifdef __cplusplus
}
#endif

#endif /* TOUCH_API_PTC_H */
