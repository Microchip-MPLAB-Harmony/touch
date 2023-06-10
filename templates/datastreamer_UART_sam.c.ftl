/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    datastreamer_UART_sam.c

  Summary:
    QTouch Modular Library

  Description:
    Provides the datastreamer protocol implementation, transmission of
          module data to data visualizer software using UART port.
	
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

/*----------------------------------------------------------------------------
  include files
----------------------------------------------------------------------------*/
#include "touch/datastreamer/datastreamer.h"
#include "definitions.h"

#if (DEF_TOUCH_DATA_STREAMER_ENABLE == 1u)

/*----------------------------------------------------------------------------
 *     defines
 *----------------------------------------------------------------------------*/
<#if TUNE_MODE_SELECTED != "CAL_AUTO_TUNE_NONE">
#define ACQ_MODULE_AUTOTUNE_OUTPUT 1
<#else>
#define ACQ_MODULE_AUTOTUNE_OUTPUT 0
</#if>
<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 1
<#else>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 0
</#if>
</#if>
<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
#define SCROLLER_MODULE_OUTPUT 1
</#if>
<#else>
#define SCROLLER_MODULE_OUTPUT 0
</#if>
<#if ENABLE_SURFACE != false>
#define SURFACE_MODULE_OUTPUT 1
<#else>
#define SURFACE_MODULE_OUTPUT 0
</#if>

/*----------------------------------------------------------------------------
  global variables
----------------------------------------------------------------------------*/
static uint8_t data[] = {
    0x5F, 0xB4, 0x00, 0x86, 0x4A, 0x03, 0xEB, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xAA, 0x55, 0x01, 0x6E, 0xA0};

/*----------------------------------------------------------------------------
  prototypes
----------------------------------------------------------------------------*/
void datastreamer_transmit(uint8_t data);

/*----------------------------------------------------------------------------
 *   function definitions
 *----------------------------------------------------------------------------*/

/*============================================================================
void datastreamer_init(void)
------------------------------------------------------------------------------
Purpose: Initialization for datastreamer module
Input  : none
Output : none
Notes  :
============================================================================*/
void datastreamer_init(void)
{
}

/*============================================================================
void datastreamer_transmit(uint8_t data_byte)
------------------------------------------------------------------------------
Purpose: Transmits the single byte through the configured UART port.
Input  : Byte to be transmitted
Output : none
Notes  :
============================================================================*/
void datastreamer_transmit(uint8_t data_byte)
{
	<#if TOUCH_SERCOM_INSTANCE != "">
	<#if DEVICE_NAME == "PIC32MZDA">
	uint32_t delay = 50000;
	while(delay--);
	</#if>
	/* Write the data bye */
   ${.vars["${TOUCH_SERCOM_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Write(&data_byte, 1);
   <#else>
   #warning "UART to send touch debug data is not defined. Connect UART to Touch library in MHC."
   </#if>
}

/*============================================================================
void datastreamer_output(void)
------------------------------------------------------------------------------
Purpose: Forms the datastreamer frame based on the configured modules, Tranmits
         the frame as single packet through UART port.
Input  : none
Output : none
Notes  :
============================================================================*/
void datastreamer_output(void)
{
	int16_t           i, temp_int_calc;
	static uint8_t    sequence = 0u;
	uint16_t          u16temp_output;
	uint8_t           u8temp_output, send_header;
	volatile uint16_t count_bytes_out;

	send_header = sequence & (0x0f);
	if (send_header == 0) {
		for (i = 0; i < sizeof(data); i++) {
			datastreamer_transmit(data[i]);
		}
	}

	// Start token
	datastreamer_transmit(0x55);

	// Frame Start
	datastreamer_transmit(sequence);

	for (count_bytes_out = 0u; count_bytes_out < DEF_NUM_SENSORS; count_bytes_out++) {
		/* Signals */
		u16temp_output = get_sensor_node_signal(count_bytes_out);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Reference */
		u16temp_output = get_sensor_node_reference(count_bytes_out);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Touch delta */
		temp_int_calc = get_sensor_node_signal(count_bytes_out);
		temp_int_calc -= get_sensor_node_reference(count_bytes_out);
		u16temp_output = (uint16_t)(temp_int_calc);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Comp Caps */
		u16temp_output = get_sensor_cc_val(count_bytes_out);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

#if (ACQ_MODULE_AUTOTUNE_OUTPUT == 1)

#if (DEF_PTC_CAL_OPTION == CAL_AUTO_TUNE_CSD)
		/* CSD */
		u8temp_output = ptc_seq_node_cfg1[count_bytes_out].node_csd;
		datastreamer_transmit(u8temp_output);
#else
		/* Prescalar */
		u8temp_output = NODE_PRSC(ptc_seq_node_cfg1[count_bytes_out].node_rsel_prsc);
		datastreamer_transmit(u8temp_output);
#endif

#endif
		/* State */
		u8temp_output = get_sensor_state(count_bytes_out);
		if (0u != (u8temp_output & 0x80)) {
			datastreamer_transmit(0x01);
		} else {
			datastreamer_transmit(0x00);
		}

		/* Threshold */
		datastreamer_transmit(qtlib_key_configs_set1[count_bytes_out].channel_threshold);
	}

#if (SCROLLER_MODULE_OUTPUT == 1)

	for (count_bytes_out = 0u; count_bytes_out < DEF_NUM_SCROLLERS; count_bytes_out++) {

		/* State */
		u8temp_output = qtm_scroller_data1[count_bytes_out].scroller_status;
		if (0u != (u8temp_output & 0x01)) {
			datastreamer_transmit(0x01);
		} else {
			datastreamer_transmit(0x00);
		}

		/* Delta */
		u16temp_output = qtm_scroller_data1[count_bytes_out].contact_size;
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Threshold */
		u16temp_output = qtm_scroller_config1[count_bytes_out].contact_min_threshold;
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* filtered position */
		u16temp_output = qtm_scroller_data1[count_bytes_out].position;
		datastreamer_transmit((uint8_t)(u16temp_output & 0x00FFu));
		datastreamer_transmit((uint8_t)((u16temp_output & 0xFF00u) >> 8u));
	}

#endif
<#if ENABLE_SURFACE != false>
#if (SURFACE_MODULE_OUTPUT == 1)
<#if ENABLE_SURFACE1T != true>
	for (count_bytes_out = 0u; count_bytes_out < 2u; count_bytes_out++) {

		/* surface contact state */
		u8temp_output = qtm_surface_contacts[count_bytes_out].qt_contact_status;
		datastreamer_transmit(u8temp_output);

		/* horizontal position */
		u16temp_output = qtm_surface_contacts[count_bytes_out].h_position;
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* vertical position */
		u16temp_output = qtm_surface_contacts[count_bytes_out].v_position;
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* filtered position */
		u16temp_output = qtm_surface_contacts[count_bytes_out].contact_size;
		datastreamer_transmit((uint8_t)(u16temp_output & 0x00FFu));
		datastreamer_transmit((uint8_t)((u16temp_output & 0xFF00u) >> 8u));
	}

	u8temp_output = qtm_surface_cs_data1.qt_surface_cs2t_status;
	datastreamer_transmit(u8temp_output);
<#else>
	/* surface contact state */
	u8temp_output = qtm_surface_cs_data1.qt_surface_status;
	datastreamer_transmit(u8temp_output);

	/* horizontal position */
	u16temp_output = qtm_surface_cs_data1.h_position;
	datastreamer_transmit((uint8_t)u16temp_output);
	datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

	/* vertical position */
	u16temp_output = qtm_surface_cs_data1.v_position;
	datastreamer_transmit((uint8_t)u16temp_output);
	datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

	/* filtered position */
	u16temp_output = qtm_surface_cs_data1.contact_size;
	datastreamer_transmit((uint8_t)(u16temp_output & 0x00FFu));
	datastreamer_transmit((uint8_t)((u16temp_output & 0xFF00u) >> 8u));
</#if>
#endif
</#if>

#if (FREQ_HOP_AUTO_MODULE_OUTPUT == 1)

	/* Frequency selection - from acq module */
	datastreamer_transmit(qtm_freq_hop_autotune_config1->freq_option_select);

	for (count_bytes_out = 0u; count_bytes_out < NUM_FREQ_STEPS; count_bytes_out++) {
		/* Frequencies */
		datastreamer_transmit(qtm_freq_hop_autotune_control1.qtm_freq_hop_autotune_config->median_filter_freq[count_bytes_out]);
	}
#endif

	/* Other Debug Parameters */
	datastreamer_transmit(module_error_code);

	/* Frame End */
	datastreamer_transmit(sequence++);

	/* End token */
	datastreamer_transmit(~0x55);
}

#endif
