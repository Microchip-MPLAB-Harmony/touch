/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    touch_example.c

  Summary:
    QTouch Modular Library

  Description:
    Provides Initialization, Processing and ISR handler of touch library,
    Simple API functions to get/set the key touch parameters from/to the
    touch library data structures
*******************************************************************************/

/*******************************************************************************
Copyright (c)  ${REL_YEAR} released Microchip Technology Inc.  All rights reserved.

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

<#if TOUCH_CHAN_ENABLE_CNT == 0>
#error "Number of Touch sensor is defined as ZERO. Include atleast one touch sensor or remove Touch library in MHC."
<#else>

<#assign no_standby_devices = ["SAMD10","SAMD11"]>

<#assign no_standby_during_measurement = 0>
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if (DS_DEDICATED_ENABLE == true) || (DS_PLUS_ENABLE == true) || no_standby_devices?seq_contains(DEVICE_NAME)>
<#assign no_standby_during_measurement = 1>
</#if>
</#if>
#include "touch_example.h"

void touch_mainloop_example(void){

    /* call touch process function */
    touch_process();

    if(measurement_done_touch == 1u)
    {
        measurement_done_touch = 0u;
        // process touch data
    }

    <#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>
    /* perform sleep operation based on touch state */
    <#if no_standby_during_measurement == 1>
    #if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
        if ((time_to_measure_touch_var != 1u)&& 
        (measurement_mode == 1u)) {
            if(measurement_in_progress == 0u) {
                PM_StandbyModeEnter();
            } else {
                PM_IdleModeEnter();
            }
        }
    #endif
    <#else>
    #if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
            if ((time_to_measure_touch_var != 1u)&& 
        (measurement_mode == 1u)) {
                PM_StandbyModeEnter();
            }
    #endif
    </#if>
    </#if>
}

/*============================================================================
void touch_status_display(void)
------------------------------------------------------------------------------
Purpose: Sample code snippet to demonstrate how to check the status of the 
         sensors
Input  : none
Output : none
Notes  : none
============================================================================*/
void touch_status_display(void)
{
uint8_t key_status = 0u;
<#if ENABLE_SCROLLER == true>
uint8_t scroller_status = 0u;
uint16_t scroller_position = 0u;
</#if>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
    key_status = get_sensor_state(${i}) & KEY_TOUCHED_MASK;
    if (0u != key_status) {
        //Touch detect
    } else {
        //Touch No detect
    }

</#list>

<#if ENABLE_SCROLLER == true>
<#list 0..TOUCH_SCROLLER_ENABLE_CNT-1 as i>
    scroller_status = get_scroller_state(${i});
    scroller_position = get_scroller_position(${i});
    //Example: 8 bit scroller resolution. Modify as per requirement.
    scroller_position = scroller_position  >> 5u;
    //LED_OFF
    if ( 0u != scroller_status) {
        switch (scroller_position) {
        case 0:
            //LED0_ON
            break;
        case 1:
            //LED1_ON
            break;
        case 2:
            //LED2_ON
            break;
        case 3:
            //LED3_ON
            break;
        case 4:
            //LED4_ON
            break;
        case 5:
            //LED5_ON
            break;
        case 6:
            //LED6_ON
            break;
        case 7:
            //LED7_ON
            break;
        default:
            //LED_OFF
            break;
        }
    }

    </#list>
</#if>
}


</#if>