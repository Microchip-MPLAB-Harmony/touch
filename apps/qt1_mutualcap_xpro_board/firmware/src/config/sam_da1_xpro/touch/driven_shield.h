/*******************************************************************************
  Touch Library v3.6.0 Release

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
Copyright (c)  2020 released Microchip Technology Inc.  All rights reserved.

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

#ifndef DRIVEN_SHIELD_H
#define DRIVEN_SHIELD_H
#include <definitions.h>

/*============================================================================
void drivenshield_configure()
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
void drivenshield_configure();

/*============================================================================
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, uint8_t volatile *dst_addr, uint8_t value)
------------------------------------------------------------------------------
Purpose: user call back from the SAMD21 Acquisition engine
Input  : Charge Share Delay (CSD) setting from PTC Acq. engine, (Set to 0 in SAMD21)
         Sample Delay Selection (SDS) setting from PTC Acq. engine this is the Frequency Hop Value for this cycle
         Prescaler setting from the PTC Acq. Engine
Output : None
Notes  : This function uses the EVSYS to start the PTC to acquire touch
============================================================================*/
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, uint8_t volatile *dst_addr, uint8_t value);

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