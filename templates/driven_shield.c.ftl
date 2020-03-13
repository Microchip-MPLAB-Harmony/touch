/*******************************************************************************
  Touch Library ${REL_VER} Release

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

#include "definitions.h"
#include "driven_shield.h"
#include "touch.h"

#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)
<#assign prescaler_value = "0, 0, 0, 0" >
<#assign block_transfer_count = "1" >
<#assign data_type = "uint8_t" >

<#if DEVICE_NAME == "SAML22">
	<#assign prescaler_value = "4, 3, 3, 4" >
	<#assign block_transfer_count = "4" >
	<#assign data_type = "uint32_t" >
<#elseif DEVICE_NAME == "SAML21">
	<#assign prescaler_value = "3, 4, 4, 4" >
<#else>
<#list ["SAME54","SAME53","SAME51","SAMD51"] as i>
	<#if DEVICE_NAME == i>
		<#assign prescaler_value = "0, 0, 0, 0" >
		<#assign block_transfer_count = "3" >
		<#break>
	</#if>
</#list>

<#list ["SAMC20", "SAMC21"] as i>
	<#if DEVICE_NAME == i>
	<#if DEVICE_VARIANT == "SAMC21N">
		<#assign prescaler_value = "4, 3, 3, 4" >
	<#else>
		<#assign prescaler_value = "1, 3, 4, 3" >
	</#if>
	<#assign data_type = "uint32_t">
	<#assign block_transfer_count = "4" >
		<#break>
	</#if>
</#list>

<#list ["SAMD21", "SAMDA1","SAMHA1"] as i>
	<#if DEVICE_NAME == i>
		<#assign prescaler_value = "4, 2, 3, 4" >
		<#assign block_transfer_count = "1" >
		<#assign data_type = "uint8_t" >
	</#if>
</#list>

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

/* DMA channel used to confiugre filter level */
#define SHIELD_DMA_CHANNEL 0u

/* extern current measure channel data from lib */
extern uint16_t current_measure_channel;

<#if DS_PLUS_ENABLE == true>
/* PTC pin's TC/TCC pinmux settings */
uint32_t driven_shield_pin[DEF_NUM_CHANNELS][2] = {
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#assign DSPLUS_TIMER_PINMUX = "DSPLUS_TIMER_PINMUX" + i>
<#if .vars[DSPLUS_TIMER_PINMUX] != "---">
		{PIN_${.vars[DSPLUS_TIMER_PINMUX]}, MUX_${.vars[DSPLUS_TIMER_PINMUX]} },
<#else>
		{0,0},
</#if>
</#list>
};
</#if>

qtm_drivenshield_config_t qtm_drivenshield_config;


static const uint8_t offset_vs_prescaler[4] = { ${prescaler_value} };
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
	
<#if DEVICE_NAME == "SAML22">
	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER[23] = EVSYS_USER_CHANNEL(0x2);
<#elseif DEVICE_NAME == "SAMC21" || DEVICE_NAME == "SAMC20">
	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER[39] = EVSYS_USER_CHANNEL(0x2);
<#elseif DEVICE_NAME == "SAML21">

	/* Map PTC EOC Event to DMA */
	EVSYS_REGS->EVSYS_CHANNEL[0] = EVSYS_CHANNEL_EVGEN(0x4B) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 ;

	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER[37] = EVSYS_USER_CHANNEL(0x2);

<#elseif (DEVICE_NAME == "SAMD21")||(DEVICE_NAME == "SAMDA1")||(DEVICE_NAME == "SAMHA1")>

	EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0x48) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 ;

	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0x2)|EVSYS_USER_USER(0x1C);
</#if>

<#if DS_DEDICATED_ENABLE ==true>
	/* Dedicated Shield Timer pin mux setting */
	drivenshield_port_mux_config(PIN_${.vars["DS_DEDICATED_TIMER_PIN"]}, MUX_${.vars["DS_DEDICATED_TIMER_PIN"]});
</#if>

	/* stop all the timers */
	drivenshield_stop();
}

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
void drivenshield_start(uint8_t csd, uint8_t sds, uint8_t prescaler, ${data_type} volatile *dst_addr, ${data_type} value)
{
	static ${data_type}  filter_level = 0;
	static ${data_type} *addr;
	uint16_t        period = 0, count = 0, cc = 0;

	addr         = (${data_type} *)dst_addr;
	filter_level = value;

	/* Configure DMA transfer */
	DMAC_ChannelTransfer(0, &filter_level, addr, ${block_transfer_count});

<#list ["SAME54", "SAME53", "SAME51", "SAMD51"] as i>
<#if DEVICE_NAME == i>
	/* TC/TCC period value */
	period = csd + 1;
	period = period << 2;
	period = period + sds;
	period = period << 1;
	period = period - 1;

	/* TC/TCC compare value */
	cc = csd + 1;
	cc = cc << 1;
	cc = cc + sds;
	cc = cc << 1;

	/* TC/TCC count value - initial offset */
	count = csd + 1;
	count = count << 1;
	if (prescaler <= 3) {
		count = count - offset_vs_prescaler[prescaler];
	} else {
		/* Using Prescaler value greater than PRSC_DIV_SEL_8
		is not recommended with Driven Shield */
	}
	<#break>
</#if>
</#list>
<#list ["SAML22", "SAMC20", "SAMC21"] as i>
<#if DEVICE_NAME == i>
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
	<#if DEVICE_VARIANT == "SAMC21N">
	period = period - 4;
	cc = cc - 2;
	</#if>
	
	<#break>
</#if>
</#list>
<#list ["SAML21"] as i>
<#if DEVICE_NAME == i>
	/* TC/TCC period value */
	period = csd + 15 + sds;
	period = period << 2;
	period = period - 1;

	/* TC/TCC compare value */
	cc = 9 + sds;
	cc = cc << 2;

	/* TC/TCC count value - initial offset */
	count = 6;
	count = count << 2;
	count = count - offset_vs_prescaler[prescaler];
	<#break>
</#if>
</#list>
<#list ["SAMD21", "SAMDA1","SAMHA1"] as i>
<#if DEVICE_NAME == i>
 /* TC/TCC period value */
    period = csd + 15 + sds;
    period = period << 2;
    period = period - 1; 

    /* TC/TCC compare value */
    cc = 9 + sds;
    cc = cc << 2;
 

    /* TC/TCC count value - initial offset */
    count = 6;
    count = count << 2;
    count = count - offset_vs_prescaler[prescaler];
</#if>
</#list>
	while (period > 255) {
		prescaler = prescaler + 1;
		period    = period >> 1;
		cc        = cc >> 1;
		count     = count >> 1;
	}

<#if DS_PLUS_ENABLE == true>
	/* configure the pins as timer or analog based on current channel being measured */
	for (uint16_t cnt = 0; cnt < DEF_NUM_CHANNELS; cnt++) {
		if ((driven_shield_pin[cnt][0] != 0) && (driven_shield_pin[cnt][1] != 0)) {
			if (current_measure_channel != cnt) {
				drivenshield_port_mux_config(driven_shield_pin[cnt][0], driven_shield_pin[cnt][1]);
			} else {
				drivenshield_port_mux_config(driven_shield_pin[cnt][0], 1);
			}
		}
	}
</#if>

<#if DS_PLUS_ENABLE == true>
	/* Shield plus configuration */
<#assign uniqueTimers = []>
<#if DS_PLUS_ENABLE == true>
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
<#if (i = 0) && (.vars["DSPLUS_TIMER_PIN"+0] != "---")>
        <#assign uniqueTimers = uniqueTimers + [ .vars["DSPLUS_TIMER_PIN"+0] ] >
<#else>
  <#list 0..i as j>
    <#if .vars["DSPLUS_TIMER_PIN"+i] == .vars["DSPLUS_TIMER_PIN"+j]&& i!=j>
        <#break>
    <#elseif .vars["DSPLUS_TIMER_PIN"+i] != "---" && i==j>
        <#assign uniqueTimers = uniqueTimers + [ .vars["DSPLUS_TIMER_PIN"+i] ] >
         <#break>
    </#if>
  </#list>
</#if>
</#list>
</#if>
<#if DS_DEDICATED_ENABLE ==true>
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#if .vars["DSPLUS_TIMER_PIN"+i] == .vars["DS_DEDICATED_TIMER"]>
			<#break>
	<#elseif .vars["DSPLUS_TIMER_PIN"+i] != "---" && i==TOUCH_KEY_ENABLE_CNT-1>
			<#assign uniqueTimers = uniqueTimers + [ .vars["DS_DEDICATED_TIMER"] ] >
		 <#break>
	</#if>
</#list>
</#if>
<#list uniqueTimers as x>
	<#if x?contains("TCC") >
	${x}_REGS->TCC_EVCTRL = TCC_EVCTRL_EVACT0_START | TCC_EVCTRL_TCEI0(1);
	${x}_REGS->TCC_PER = period;
	${x}_REGS->TCC_COUNT = count;
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#if .vars["DSPLUS_TIMER_PINMUX"+i]?contains(x) && .vars["DSPLUS_TIMER_PINMUX"+i] != "---">
<#assign DediTimerWo = .vars["DSPLUS_TIMER_PINMUX"+i]>
<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	${x}_REGS->TCC_CC[${DediTimerWo1}%${x}_NUM_CHANNELS] = cc;
	</#if>
</#list>
	<#if DS_DEDICATED_ENABLE ==true>
		<#if .vars["DS_DEDICATED_TIMER"]?contains(x) >
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	${x}_REGS->TCC_CC[${DediTimerWo1}%${x}_NUM_CHANNELS] = cc;
		</#if>
	</#if>
	${x}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER(prescaler);
	${x}_PWMStart();
	<#else>
	${x}_REGS->COUNT8.TC_PER = period;
	${x}_REGS->COUNT8.TC_COUNT = count;
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#if .vars["DSPLUS_TIMER_PINMUX"+i]?contains(x) && .vars["DSPLUS_TIMER_PINMUX"+i] != "---">
<#assign DediTimerWo = .vars["DSPLUS_TIMER_PINMUX"+i]>
<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	${x}_REGS->COUNT8.TC_CC[${DediTimerWo1}] = cc;
	</#if>
</#list>
	<#if DS_DEDICATED_ENABLE ==true>
		<#if .vars["DS_DEDICATED_TIMER"]?contains(x) >
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	${x}_REGS->COUNT8.TC_CC[${DediTimerWo1}] = cc;
		</#if>
	</#if>
	${x}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler) | TC_CTRLA_RUNSTDBY_Msk ;
	${x}_CompareStart();
</#if>
</#list>
<#elseif DS_DEDICATED_ENABLE ==true>
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	<#if .vars["DS_DEDICATED_TIMER"]?contains("TCC") >
	${DS_DEDICATED_TIMER}_REGS->TCC_EVCTRL = TCC_EVCTRL_EVACT0_START | TCC_EVCTRL_TCEI0(1);
	${DS_DEDICATED_TIMER}_REGS->TCC_PER = period;
	${DS_DEDICATED_TIMER}_REGS->TCC_COUNT = count;
	${DS_DEDICATED_TIMER}_REGS->TCC_CC[${DediTimerWo1}%${DS_DEDICATED_TIMER}_NUM_CHANNELS] = cc;
	${DS_DEDICATED_TIMER}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER(prescaler);
	${DS_DEDICATED_TIMER}_PWMStart();
	<#else>
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_PER = period;
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_COUNT = count;
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CC[${DediTimerWo1}] = cc;
<#if (DEVICE_NAME == "SAMD21")||(DEVICE_NAME == "SAMDA1")||(DEVICE_NAME == "SAMHA1")>	
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler) | TC_CTRLA_RUNSTDBY_Msk ;
<#else>
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler);
</#if>
	
</#if>
	${DS_DEDICATED_TIMER}_CompareStart();
	</#if>
</#if>

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
<#if DS_PLUS_ENABLE == true>
<#list uniqueTimers as x>
	<#if x?contains("TCC") >
	${x}_PWMStop();
	<#else>
	${x}_CompareStop();
	</#if>
</#list>
<#elseif DS_DEDICATED_ENABLE ==true>
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	<#if .vars["DS_DEDICATED_TIMER"]?contains("TCC") >
	${DS_DEDICATED_TIMER}_PWMStop();
	<#else>
	${DS_DEDICATED_TIMER}_CompareStop();
	</#if>
</#if>
}
#endif