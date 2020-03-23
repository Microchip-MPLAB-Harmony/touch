/*******************************************************************************
  Touch Library v3.6.0 Release

  Company:
    Microchip Technology Inc.

  File Name:
    driven_shield.c

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

#include "definitions.h"
#include "driven_shield.h"
#include "touch.h"

#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)

/*============================================================================
void drivenshield_port_mux_config()
------------------------------------------------------------------------------
Purpose: configures pin mux to switch between timer and PTC
Input  : pin and mux position
Output : None
============================================================================*/
static void drivenshield_port_mux_config(uint8_t pin, uint8_t mux);

/*============================================================================
static void drivenshield_port_mux_config(uint8_t pin, uint8_t mux)
------------------------------------------------------------------------------
Purpose: configures pin mux to switch between timer and PTC
Input  : pin and mux position
Output : None
============================================================================*/
static void drivenshield_port_mux_config(uint8_t pin, uint8_t mux)
{
	uint8_t temp_pin = pin%32;
	uint8_t port = pin>>5; /* div by 32 */

	if(mux == 0)
	{
		PORT_REGS->GROUP[port].PORT_PINCFG[temp_pin] = 0;
	}
	else
	{
		PORT_REGS->GROUP[port].PORT_PINCFG[temp_pin] = 0x01;

		if(temp_pin%2)
		{
			/* odd */
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1] &= ~0xf0;
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1] |= (mux << 4);
		}
		else
		{
			/* even */
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1] &= ~0x0f;
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1] |= (mux);
		}
	}
}

/* extern current measure channel data from lib */
extern uint16_t current_measure_channel;


qtm_drivenshield_config_t qtm_drivenshield_config;

/*============================================================================
void drivenshield_configure()
------------------------------------------------------------------------------
Purpose: Sets up the qtm_drivenshield_config_t qtm_drivenshield_config object
Input  : Users application / configuration parameters
Output : None
Notes  : This setup is very product dependent,
         users can setup the delays between the SW_Trigger event and
         PWM2 and PTC start, Select Two or Three level Shield mode
         Users also use this function to configure GPIO pins and Enable
         GCLKs and APBClocks for the peripherals associated with the shield
============================================================================*/
void drivenshield_configure()
{
	touch_ret_t touch_ret = TOUCH_SUCCESS;
	/* Shield configuration */
	touch_ret = qtm_drivenshield_setup(&qtm_drivenshield_config);
	if (touch_ret != TOUCH_SUCCESS) {
		while (1)
			;
	}
	touch_ret = qtm_drivenshield_register_start_callback(&drivenshield_start);
	if (touch_ret != TOUCH_SUCCESS) {
		while (1)
			;
	}
	
	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER[23] = EVSYS_USER_CHANNEL(0x2);


	/* stop all the timers */
	drivenshield_stop();
}

/*============================================================================
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, uint32_t volatile *dst_addr, uint32_t value)
------------------------------------------------------------------------------
Purpose: user call back from the SAMD21 Acquisition engine
Input  : Charge Share Delay (CSD) setting from PTC Acq. engine, (Set to 0 in SAMD21)
         Sample Delay Selection (SDS) setting from PTC Acq. engine this is the Frequency Hop Value for this cycle
         Prescaler setting from the PTC Acq. Engine
Output : None
Notes  : This function uses the EVSYS to start the PTC to acquire touch
============================================================================*/
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, uint32_t volatile *dst_addr, uint32_t value)
{
	static uint32_t  filter_level = 0;
	static uint32_t *addr;
	uint16_t        period = 0, count = 0, cc = 0;

	addr         = (uint32_t *)dst_addr;
	filter_level = value;

	/* Configure DMA transfer */
	DMAC_ChannelTransfer(0, &filter_level, addr, 8);

	/* TC/TCC period value */
	period = csd+1;
	period = period * 6;
	period = period + sds + 1;
	period = period << 2;
	period = period - 1;

	/* TC/TCC compare value */
	cc = csd+1;
	cc = cc * 3;
	cc = cc << 2;
	cc = cc + (sds<<2);
	
	/* TC/TCC count value - initial offset */
	count = csd+1;
	count = count * 2;
	count = count << 2;
	count = count - 2;
	while (period > 255) {
		prescaler = prescaler + 1;
		period    = period >> 1;
		cc        = cc >> 1;
		count     = count >> 1;
	}


}

/*============================================================================
void drivenshield_stop(void)
------------------------------------------------------------------------------
Purpose: Stops the softshield timers
Input  : none
Output : none
Notes  : This function is called from the PTC EOC handler in the users application in touch.c
============================================================================*/
void drivenshield_stop(void)
{
}
#endif