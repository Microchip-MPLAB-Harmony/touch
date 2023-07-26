
/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    touch_api_ptc.h

  Summary:
    QTouch Modular Library

  Description:
    Includes the Module API header files based on the configured modules,
    prototypes for touch.c file and Application helper API functions
*******************************************************************************/

/*******************************************************************************
Copyright (C) [${REL_YEAR}], Microchip Technology Inc., and its subsidiaries. All rights reserved.

The software and documentation is provided by microchip and its contributors
"as is" and any express, implied or statutory warranties, including, but not
limited to, the implied warranties of merchantability, fitness for a particular
purpose and non-infringement of third party intellectual property rights are
disclaimed to the fullest extent permitted by law. In no event shall microchip
or its contributors be liable for any direct, indirect, incidental, special,
exemplary, or consequential damages (including, but not limited to, procurement
of substitute goods or services; loss of use, data, or profits; or business
interruption) however caused and on any theory of liability, whether in contract,
strict liability, or tort (including negligence or otherwise) arising in any way
out of the use of the software and documentation, even if advised of the
possibility of such damage.

Except as expressly permitted hereunder and subject to the applicable license terms
for any third-party software incorporated in the software and any applicable open
source software license terms, no license or other rights, whether express or
implied, are granted under any patent or other intellectual property rights of
Microchip or any third party.
************************************************************************************/

#ifndef TOUCH_API_PTC_H
#define TOUCH_API_PTC_H

#ifdef __cplusplus
extern "C" {
#endif // __cplusplus

/*----------------------------------------------------------------------------
 *     include files
 *----------------------------------------------------------------------------*/

#include "qtm_common_components_api.h"
<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
#include "qtm_acq_samd1x_0x0009_api.h"
<#elseif  DEVICE_NAME == "PIC32CMJH01"|| DEVICE_NAME=="PIC32CMJH00">
#include "qtm_acq_pic32cmjh_0x002f_api.h"
<#elseif ["PIC32CXBZ31","WBZ35"]?seq_contains(DEVICE_NAME) >
#include "qtm_acq_pic32cx_0x003e_api.h"
<#else>
    <#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
        <#if DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00"|| DEVICE_NAME=="PIC32CMLS60">
#include "qtm_acq_4p_pic32cm_le_0x0041_api.h"
        <#elseif  DEVICE_NAME == "PIC32CZCA80" || DEVICE_NAME == "PIC32CZCA90">
#include "qtm_global_pic32czca_0x0049_api.h"
        <#else>
#include "qtm_acq_4p_${DEVICE_NAME?lower_case}_${MODULE_ID}_api.h"
        </#if>
    <#else>
        <#if DEVICE_NAME == "PIC32CMLE00" || DEVICE_NAME == "PIC32CMLS00"|| DEVICE_NAME=="PIC32CMLS60">
#include "qtm_acq_pic32cm_le_0x0040_api.h"
        <#elseif  DEVICE_NAME == "PIC32CZCA80"|| DEVICE_NAME == "PIC32CZCA90">
#include "qtm_acq_pic32czca_0x004a_api.h"
        <#else>
#include "qtm_acq_${DEVICE_NAME?lower_case}_${MODULE_ID}_api.h"
        </#if>
    </#if>
</#if>
#include "qtm_touch_key_0x0002_api.h"
<#if ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE!=true>
#include "qtm_freq_hop_0x0006_api.h"
<#elseif ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE==true>
#include "qtm_freq_hop_auto_0x0004_api.h"
</#if>
<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
#include "qtm_scroller_0x000b_api.h"
</#if>
</#if>
<#if ENABLE_SURFACE==true>
    <#if ENABLE_SURFACE1T== true>
#include "qtm_surface_cs_0x0021_api.h"
    </#if>
    <#if ENABLE_SURFACE2T== true>
#include "qtm_surface_cs2t_0x0025_api.h"
    </#if>
    <#if ENABLE_GESTURE == true>
#include "qtm_gestures_2d_0x0023_api.h"
    </#if>
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
<#if ENABLE_SCROLLER == true>
uint8_t  get_scroller_state(uint16_t sensor_node);
uint16_t get_scroller_position(uint16_t sensor_node);
</#if>
<#if ENABLE_SURFACE==true>
<#if ENABLE_SURFACE1T== true>
#define HOR_POS 0u
#define VER_POS 1u
uint8_t get_surface_status(void);
uint16_t get_surface_position(uint8_t ver_or_hor);
</#if>
<#if ENABLE_SURFACE2T== true>
#define HOR_POS 0u
#define VER_POS 1u
uint8_t get_surface_status(void);
uint16_t get_surface_position(uint8_t ver_or_hor, uint8_t contact);
</#if>
</#if>

void touch_timer_handler(void);
void touch_init(void);
void touch_process(void);

void touch_timer_config(void);

#ifdef __cplusplus
}
#endif

#endif /* TOUCH_API_PTC_H */
