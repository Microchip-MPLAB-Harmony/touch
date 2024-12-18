/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    driven_shield.h

  Summary:
    QTouch Modular Library

  Description:
    Provides Initialization, Processing and ISR handler of touch library,
    Simple API functions to get/set the key touch parameters from/to the
    touch library data structures
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

#ifndef DRIVEN_SHIELD_H
#define DRIVEN_SHIELD_H
<#assign data_type = "uint8_t" >
<#list ["SAMC20", "SAMC21","SAML22"] as i>
	<#if DEVICE_NAME == i>
		<#assign data_type = "uint32_t">
	</#if>
</#list>
#include <definitions.h>
extern uint16_t current_measure_channel;
/*============================================================================
void drivenshield_configure(void)
------------------------------------------------------------------------------
Purpose: Sets up the qtm_softshield_config_t qtm_softshield_config object
Input  : Users application / configuration parameters
Output : None
Notes  : This setup is very product dependent,
         users can setup the delays between the SW_Trigger event and
         PWM2 and PTC start, Select Two or Three level Shield mode
         Users also use this function to configure GPIO pins and Enable
         GCLKs and APBClocks for the peripherals associated with the shield
============================================================================*/
void drivenshield_configure(void);

/*============================================================================
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, ${data_type} volatile *dst_addr, ${data_type} value)
------------------------------------------------------------------------------
Purpose: user call back from the SAMD21 Acquisition engine
Input  : Charge Share Delay (CSD) setting from PTC Acq. engine, (Set to 0 in SAMD21)
         Sample Delay Selection (SDS) setting from PTC Acq. engine this is the Frequency Hop Value for this cycle
         Prescaler setting from the PTC Acq. Engine
Output : None
Notes  : This function uses the EVSYS to start the PTC to acquire touch
============================================================================*/
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, ${data_type} volatile *dst_addr, ${data_type} value);

/*============================================================================
void drivenshield_stop(void)
------------------------------------------------------------------------------
Purpose: Stops the softshiled timers
Input  : none
Output : none
Notes  : This function is called from the PTC EOC handler in the users application in touch.c
============================================================================*/
void drivenshield_stop(void);

#endif