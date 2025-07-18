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

#include "definitions.h"
#include "driven_shield.h"
#include "touch.h"

<#assign noDmaDevice = ["SAMD11", "SAMD10", "SAMD20", "PIC32CMGV00"] >

#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)
<#assign prescaler_value = "0, 0, 0, 0" >
<#assign block_transfer_count = "1" >
<#assign data_type = "uint8_t" >
<#assign uniqueTimersDSP = []>
<#if DS_PLUS_ENABLE == true>
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
<#if (i = 0) && (.vars["DSPLUS_TIMER_PIN"+0] != "---")>
        <#assign uniqueTimersDSP = uniqueTimersDSP + [ .vars["DSPLUS_TIMER_PIN"+0] ] >
<#else>
  <#list 0..i as j>
    <#if .vars["DSPLUS_TIMER_PIN"+i] == .vars["DSPLUS_TIMER_PIN"+j]&& i!=j>
        <#break>
    <#elseif .vars["DSPLUS_TIMER_PIN"+i] != "---" && i==j>
        <#assign uniqueTimersDSP = uniqueTimersDSP + [ .vars["DSPLUS_TIMER_PIN"+i] ] >
         <#break>
    </#if>
  </#list>
</#if>
</#list>
</#if>
<#if DEVICE_NAME == "SAML22">
	<#assign prescaler_value = "4, 3, 3, 4" >
	<#assign block_transfer_count = "8" >
	<#assign data_type = "uint32_t" >
<#elseif DEVICE_NAME == "SAML21">
	<#assign prescaler_value = "0, 3, 2, 3" >
<#else>
<#list ["SAME54","SAME53","SAME51","SAMD51","PIC32CXSG41", "PIC32CXSG60", "PIC32CXSG61"] as i>
	<#if DEVICE_NAME == i>
		<#assign prescaler_value = "1, 1, 1, 1" >
		<#assign block_transfer_count = "3" >
		<#break>
	</#if>
</#list>

<#list ["SAMC20", "SAMC21", "PIC32CMJH00"] as i>
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
		<#if DEVICE_NAME_SPECIFIC?ends_with("D") >
		<#assign prescaler_value = "1, 2, 3, 4" >
		<#else>
		<#assign prescaler_value = "4, 2, 3, 4" >
		</#if>
		<#assign block_transfer_count = "1" >
		<#assign data_type = "uint8_t" >
	</#if>
</#list>

<#if noDmaDevice?seq_contains(DEVICE_NAME) >
		<#assign prescaler_value = "0, 2, 3, 3" >
		<#assign block_transfer_count = "1" >
		<#assign data_type = "uint8_t" >
</#if>
</#if>

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
	uint8_t temp_pin =(uint8_t) pin%32u;
	uint8_t port = (uint8_t)pin>>5u; /* div by 32 */

	if(mux == 0u)
	{
		PORT_REGS->GROUP[port].PORT_PINCFG[temp_pin] = 0;
	}
	else
	{
		PORT_REGS->GROUP[port].PORT_PINCFG[temp_pin] = 0x01;

		if(temp_pin%2u !=0u)
		{
			/* odd */
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1u] &= ~(uint8_t)0xf0;
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1u] |= (mux << 4u);
		}
		else
		{
			/* even */
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1u] &= ~(uint8_t)0x0f;
			PORT_REGS->GROUP[port].PORT_PMUX[temp_pin>>1u] |= (uint8_t)(mux);
		}
	}
}

<#if DS_PLUS_ENABLE == true && uniqueTimersDSP?size != 0>
/* PTC pin's TC/TCC pinmux settings */
static uint32_t driven_shield_pin[DEF_NUM_CHANNELS][2] = {
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

<#if DEVICE_NAME != "SAML22" && DEVICE_NAME != "SAMC20" && DEVICE_NAME != "SAMC21" && (DEVICE_NAME != "PIC32CMJH00")>
static const uint8_t offset_vs_prescaler[4] = { ${prescaler_value} };
</#if>
/*============================================================================
void drivenshield_configure(void)
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
void drivenshield_configure(void)
{
	touch_ret_t touch_ret = TOUCH_SUCCESS;
	/* Shield configuration */
	touch_ret = qtm_drivenshield_setup(&qtm_drivenshield_config);
	if (touch_ret != TOUCH_SUCCESS) {
		while (true){}
			;
	}
	touch_ret = qtm_drivenshield_register_start_callback(&drivenshield_start);
	if (touch_ret != TOUCH_SUCCESS) {
		while (true){}
			;
	}
	
<#if DEVICE_NAME == "SAML22">
	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER[23] = EVSYS_USER_CHANNEL(0x2);
<#elseif DEVICE_NAME == "SAMC21" || DEVICE_NAME == "SAMC20" || (DEVICE_NAME == "PIC32CMJH00")>
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
<#elseif (DEVICE_NAME == "SAMD20")||(DEVICE_NAME == "PIC32CMGV00")>

	EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0x3A) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_CHANNEL(0);

	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0x1)|EVSYS_USER_USER(0x0D);
<#elseif (DEVICE_NAME == "SAMD10")||(DEVICE_NAME == "SAMD11")>
	EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0x2B) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_CHANNEL(0);

	/* Map DMA Transfer complete Event
		output to PTC Start of convertion Event Inuput */
	EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0x1)|EVSYS_USER_USER(0x11);
</#if>

<#if DS_DEDICATED_ENABLE ==true>
	/* Dedicated Shield Timer pin mux setting */
	drivenshield_port_mux_config((uint8_t)PIN_${.vars["DS_DEDICATED_TIMER_PIN"]}, (uint8_t)MUX_${.vars["DS_DEDICATED_TIMER_PIN"]});
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
	<#if (DEVICE_NAME != "SAMD11") && (DEVICE_NAME != "SAMD10") && (DEVICE_NAME != "SAMD20") && (DEVICE_NAME != "PIC32CMGV00")>
	static ${data_type}  filter_level = 0;
	static uint32_t addr;
	</#if>
	uint16_t        period = 0, count = 0, cc = 0;

<#if noDmaDevice?seq_contains(DEVICE_NAME) == false>
    bool check;
	addr = (uint32_t)dst_addr;
	filter_level = value;

	/* Configure DMA transfer */
	check = DMAC_ChannelTransfer((DMAC_CHANNEL)0, &filter_level, (uint32_t *) addr, ${block_transfer_count}u);
	if (check != true) {
		/* error condition. During normal operation control shouldn't come here */
	}
<#else>
	<#if (DEVICE_NAME == "SAMD20")||(DEVICE_NAME == "PIC32CMGV00")>
	EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0x1)|EVSYS_USER_USER(0x0D);
	<#else>
	EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0x1)|EVSYS_USER_USER(0x11);
	</#if>
</#if>

<#list ["SAME54", "SAME53", "SAME51", "SAMD51", "PIC32CXSG41", "PIC32CXSG60", "PIC32CXSG61"] as i>
<#if DEVICE_NAME == i>
	/* TC/TCC period value */
	period = (uint16_t) ((uint16_t)csd + 1u);
	period = (uint16_t) (period << 2);
	period = period + sds;
	period = (uint16_t) (period << 1);
	period = (uint16_t) (period - 1u);

	/* TC/TCC compare value */
	cc = (uint16_t) ((uint16_t)csd + 1u);
	cc = (uint16_t) (cc << 1);
	cc = (uint16_t) (cc + sds);
	cc = (uint16_t) (cc << 1);

	/* TC/TCC count value - initial offset */
	count = (uint16_t) ((uint16_t)csd + 1u);
	count = (uint16_t) (count << 1);
	if (prescaler <= 3u) {
		count = count - offset_vs_prescaler[prescaler];
	} else {
		/* Using Prescaler value greater than PRSC_DIV_SEL_8
		is not recommended with Driven Shield */
	}
	<#break>
</#if>
</#list>
<#list ["SAMD11", "SAMD10","SAMD20","PIC32CMGV00"] as i>
<#if DEVICE_NAME == i>

	<#if DEVICE_NAME == "SAMD20" || DEVICE_NAME == "PIC32CMGV00">
	EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0x3A) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_CHANNEL(0);
	<#else>
	EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0x2B) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_CHANNEL(0);
	</#if>
	/* TC/TCC period value */
    period = (uint16_t)csd + 15u + (uint16_t)sds;
    period = (uint16_t) (period << 2u);
    period = (uint16_t) (period - 1u);

    /* TC/TCC compare value */
    cc = (uint16_t)(9u + (uint16_t)sds);
    cc = (uint16_t) (cc << 2u);
 

    /* TC/TCC count value - initial offset */
    count = 6u;
    count = (uint16_t) (count << 2u);
    count = (uint16_t) (count - offset_vs_prescaler[prescaler]);
</#if>
</#list>
<#list ["SAML22", "SAMC20", "SAMC21", "PIC32CMJH00"] as i>
<#if DEVICE_NAME == i>
	/* TC/TCC period value */
	period = (uint16_t)csd+1u;
	period = (uint16_t) (period * 6u);
	period = (uint16_t)period + sds + 1u;
	period = (uint16_t) (period << 2u);
	period = (uint16_t) (period - 1u);

	/* TC/TCC compare value */
	cc = (uint16_t)((uint16_t)csd+1u);
	cc = (uint16_t)(cc * 3u);
	cc = (uint16_t)(cc << 2u);
	cc = (uint16_t)(cc + (uint16_t)((uint16_t)sds<<2u));
	
	/* TC/TCC count value - initial offset */
	count = (uint16_t)csd+1u;
	count = (uint16_t)count * 2u;
	count = (uint16_t)count << 2u;
	<#if DEVICE_NAME == "SAML22">
	count = (uint16_t)count - 2u;
	<#else>
	<#if DEVICE_VARIANT == "SAMC21N">
	period = (uint16_t)period - 4u;
	count = (uint16_t)count - 2u;
	<#elseif (DEVICE_NAME == "SAMC21") || (DEVICE_NAME == "SAMC20") || (DEVICE_NAME == "PIC32CMJH00")>
	cc = (uint16_t)cc + 3u;
	</#if>
	</#if>
	<#break>
</#if>
</#list>
<#list ["SAML21"] as i>
<#if DEVICE_NAME == i>
	/* TC/TCC period value */
	period = (uint16_t)csd + 15u + (uint16_t)sds;
	period = (uint16_t)period << 2u;
	period = (uint16_t)period - 1u;

	/* TC/TCC compare value */
	cc = (uint16_t)(9u + (uint16_t)sds);
	cc = (uint16_t)cc << 2u;

	/* TC/TCC count value - initial offset */
	count = 6u;
	count = (uint16_t)count << 2u;
	count = (uint16_t)count - offset_vs_prescaler[prescaler];
	<#break>
</#if>
</#list>
<#list ["SAMD21", "SAMDA1","SAMHA1"] as i>
<#if DEVICE_NAME == i>
 /* TC/TCC period value */
    period = (uint16_t)csd + 15u + (uint16_t)sds;
    period = (uint16_t)period << 2u;
    period = (uint16_t)period - 1u; 

    /* TC/TCC compare value */
    cc = (uint16_t)(9u + (uint16_t)sds);
    cc = (uint16_t)cc << 2u;
 

    /* TC/TCC count value - initial offset */
    count = 6u;
    count = (uint16_t)count << 2u;
    count = (uint16_t)count - offset_vs_prescaler[prescaler];
</#if>
</#list>
	while (period > 255u) {
		prescaler = prescaler + 1u;
		period    = period >> 1u;
		cc        = cc >> 1u;
		count     = count >> 1u;
	}

<#if DS_PLUS_ENABLE == true && uniqueTimersDSP?size != 0>
	/* configure the pins as timer or analog based on current channel being measured */
	for (uint16_t cnt = 0; cnt < DEF_NUM_CHANNELS; cnt++) {
		if ((driven_shield_pin[cnt][0] != 0u) && (driven_shield_pin[cnt][1] != 0u)) {
			if (current_measure_channel != cnt) {
				drivenshield_port_mux_config((uint8_t)driven_shield_pin[cnt][0], (uint8_t)driven_shield_pin[cnt][1]);
			} else {
				drivenshield_port_mux_config((uint8_t)driven_shield_pin[cnt][0], 1u);
			}
		}
	}
</#if>

<#if DS_PLUS_ENABLE == true && uniqueTimersDSP?size != 0>
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
<#assign dsPartOfDsp = 0>
<#list uniqueTimersDSP as i>
	<#if i == .vars["DS_DEDICATED_TIMER"]>
			<#assign dsPartOfDsp = 1>
			<#break>
	</#if>
</#list>
<#if dsPartOfDsp == 0>
<#assign uniqueTimers = uniqueTimers + [ .vars["DS_DEDICATED_TIMER"] ] >
</#if>
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
	${x}_REGS->TCC_CC[${DediTimerWo1}u%${x}_NUM_CHANNELS] = cc;
	while (${x}_REGS->TCC_SYNCBUSY != 0U)
    {
        /* Wait for sync */
    }
	</#if>
</#list>
	<#if DS_DEDICATED_ENABLE ==true>
		<#if .vars["DS_DEDICATED_TIMER"]?contains(x) >
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	${x}_REGS->TCC_CC[${DediTimerWo1}u%${x}_NUM_CHANNELS] = cc;
		</#if>
	</#if>
	${x}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER(prescaler);
	${x}_PWMStart();
	<#else>
	${x}_REGS->COUNT8.TC_PER = (uint8_t)period;
	${x}_REGS->COUNT8.TC_COUNT = (uint8_t)count;
<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i>
	<#if .vars["DSPLUS_TIMER_PINMUX"+i]?contains(x) && .vars["DSPLUS_TIMER_PINMUX"+i] != "---">
<#assign DediTimerWo = .vars["DSPLUS_TIMER_PINMUX"+i]>
<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	${x}_REGS->COUNT8.TC_CC[${DediTimerWo1}] =(uint8_t) cc;
	</#if>
</#list>
	<#if DS_DEDICATED_ENABLE ==true>
		<#if .vars["DS_DEDICATED_TIMER"]?contains(x) >
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	${x}_REGS->COUNT8.TC_CC[${DediTimerWo1}] = (uint8_t)cc;
		</#if>
	</#if>
	<#if ((DEVICE_NAME == "SAMD21")||(DEVICE_NAME == "SAMDA1")||(DEVICE_NAME == "SAMHA1"))>	
	${x}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler)| TC_CTRLA_WAVEGEN_NPWM | TC_CTRLA_RUNSTDBY_Msk ;
	<#elseif ((DEVICE_NAME == "SAMD11")||(DEVICE_NAME == "SAMD10"))>
	${x}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler) | TC_CTRLA_WAVEGEN_NPWM | TC_CTRLA_RUNSTDBY_Msk ;
	<#elseif ((DEVICE_NAME == "SAMD20")||(DEVICE_NAME == "PIC32CMGV00"))>
	${x}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler) | TC_CTRLA_WAVEGEN_NPWM;
	<#else>
	${x}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler);
	</#if>
	${x}_CompareStart();
</#if>
</#list>
<#elseif DS_DEDICATED_ENABLE ==true>
		<#assign DediTimerWo = .vars["DS_DEDICATED_TIMER_PIN"]>
		<#assign DediTimerWo1 = DediTimerWo?split("WO")[1]>
	/* Dedicated Shield */
	<#if .vars["DS_DEDICATED_TIMER"]?contains("TCC") >
	${DS_DEDICATED_TIMER}_REGS->TCC_EVCTRL = TCC_EVCTRL_EVACT0_START | TCC_EVCTRL_TCEI0(1);
	${DS_DEDICATED_TIMER}_REGS->TCC_PER = (uint8_t)period;
	${DS_DEDICATED_TIMER}_REGS->TCC_COUNT = (uint8_t)count;
	${DS_DEDICATED_TIMER}_REGS->TCC_CC[${DediTimerWo1}%${DS_DEDICATED_TIMER}_NUM_CHANNELS] = (uint8_t)cc;
	${DS_DEDICATED_TIMER}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER(prescaler);
	${DS_DEDICATED_TIMER}_PWMStart();
	<#else>
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_PER = (uint8_t)period;
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_COUNT = (uint8_t)count;
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CC[${DediTimerWo1}] = (uint8_t)cc;
<#if ((DEVICE_NAME == "SAMD21")||(DEVICE_NAME == "SAMDA1")||(DEVICE_NAME == "SAMHA1"))>
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler) | TC_CTRLA_WAVEGEN_NPWM | TC_CTRLA_RUNSTDBY_Msk ;
<#elseif ((DEVICE_NAME == "SAMD11")||(DEVICE_NAME == "SAMD10")||(DEVICE_NAME == "SAMD20")||(DEVICE_NAME == "PIC32CMGV00"))>	
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler) | TC_CTRLA_WAVEGEN_NPWM;
<#else>
	${DS_DEDICATED_TIMER}_REGS->COUNT8.TC_CTRLA = TC_CTRLA_MODE_COUNT8 | TC_CTRLA_PRESCALER(prescaler);
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
<#if DS_PLUS_ENABLE == true && uniqueTimersDSP?size != 0 >
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