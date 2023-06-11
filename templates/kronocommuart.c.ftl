/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    kronocommuart.c

  Summary:
    QTouch Modular Library

  Description:
    UART functions/structs to enable communication between SAM device and 
	Microchip 2D Touch Surface Utility.
	
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

#include "touch/datastreamer/KronoCommuart_sam.h"
#include "definitions.h"

<#if TOUCH_SERCOM_KRONO_INSTANCE == "">
#warning "UART to send touch debug data is not defined. Connect UART to Touch library in MHC."
<#else>
#if KRONOCOMM_UART == 1u

static volatile uint8_t write_buffer[UART_TX_BUF_LEN];
static uint8_t          write_buf_read_ptr;
static uint8_t          write_buf_write_ptr;
static uint8_t          read_buffer[UART_RX_BUF_LEN];
static uint8_t          read_buf_read_ptr;
static uint8_t          read_buf_write_ptr;
static volatile uint8_t uart_tx_in_progress;

static volatile uint8_t uart_send_ges_data_flag = 1;
static volatile uint8_t transmit_completed      = 0;
static uint8_t uart_new_data_available = 0;

typedef struct tag_uart_command_info_t {
	uint8_t header_status;
	uint8_t transaction_id;
	uint8_t command_id;
	uint8_t read_write;
	uint8_t address;
	uint8_t num_of_bytes;
} uart_command_info_t;

static uart_command_info_t uart_command_info;

#define UART_FIXED (5u + 2u)

#define UART_GES_POS (0u)
#define UART_GES_DATA_POS (uint8_t) (UART_GES_POS + UART_FIXED - 1u)
#define UART_GES_LEN (6u)
#define UART_GES_END (uint8_t) (UART_GES_POS + UART_GES_LEN + UART_FIXED - 1u)
#define UART_GES_ADDR 0x10u
#define UART_GES_ID 0x00u

#define UART_SIG_POS (uint8_t) (UART_GES_END + 1u)
#define UART_SIG_DATA_POS (uint8_t) (UART_SIG_POS + UART_FIXED - 1u)
#define UART_SIG_LEN (uint8_t) ((SURFACE_CS_NUM_KEYS_H + SURFACE_CS_NUM_KEYS_V) * 2u)
#define UART_SIG_END (uint8_t) (UART_SIG_POS + UART_SIG_LEN + UART_FIXED - 1u)
#define UART_SIG_ADDR 0xa3u
#define UART_SIG_ID 0x01u

#define UART_DELTA_POS (uint8_t) (UART_SIG_END + 1u)
#define UART_DELTA_DATA_POS (uint8_t) (UART_DELTA_POS + UART_FIXED - 1u)
#define UART_DELTA_LEN ((uint8_t) (SURFACE_CS_NUM_KEYS_H + SURFACE_CS_NUM_KEYS_V))
#define UART_DELTA_END (uint8_t) (UART_DELTA_POS + UART_DELTA_LEN + UART_FIXED - 1u)
#define UART_DELTA_ADDR 0x8cu
#define UART_DELTA_ID 0x05u

#define UART_HEADER 0xADu
#define UART_FOOTER 0xDAu

static uint8_t uart_runtime_data[UART_GES_LEN + UART_SIG_LEN + UART_DELTA_LEN + (UART_FIXED)*3];

uint8_t uart_get_char(void)
{
	uint8_t data = read_buffer[read_buf_read_ptr];
	read_buf_read_ptr++;
	if (read_buf_read_ptr == UART_RX_BUF_LEN) {
		read_buf_read_ptr = 0u;
	}
	return data;
}

void uart_send_data_wait(uint8_t data)
{
	static uint8_t uartTxData = data;
	uart_tx_in_progress = 1u;
    if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Write(&uartTxData, 1)) {

	}
	while (uart_tx_in_progress == 1u) {

	}
}

void uart_send_data(void)
{
	if (uart_tx_in_progress == 0u) {
		uart_tx_in_progress = 1u;

		write_buf_read_ptr = 0u;
        if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Write(&uart_runtime_data[write_buf_read_ptr++], 1)) {
			
		}
	}
}

static uintptr_t usart_ptr;

void uart_init_debug_data(void)
{
	uint8_t arrayIndex;

	arrayIndex = 0u;
	uart_runtime_data[arrayIndex++]            = UART_HEADER;
	uart_runtime_data[arrayIndex++]            = (uint8_t) (UART_GES_LEN - 1u + UART_FIXED - 2u);
	uart_runtime_data[arrayIndex++]            = UART_GES_ID;
	uart_runtime_data[arrayIndex++]            = 0x01u;
	uart_runtime_data[arrayIndex++]            = 0x00u;
	uart_runtime_data[arrayIndex++]            = UART_GES_ADDR;
	uart_runtime_data[UART_GES_END] = UART_FOOTER;

	arrayIndex = UART_SIG_POS;
	uart_runtime_data[arrayIndex++] = UART_HEADER;
	uart_runtime_data[arrayIndex++] = (uint8_t) (UART_SIG_LEN - 1u + UART_FIXED - 2u);
	uart_runtime_data[arrayIndex++] = UART_SIG_ID;
	uart_runtime_data[arrayIndex++] = 0x01u;
	uart_runtime_data[arrayIndex++] = 0x00u;
	uart_runtime_data[arrayIndex++] = UART_SIG_ADDR;
	uart_runtime_data[UART_SIG_END]     = UART_FOOTER;

	arrayIndex = UART_DELTA_POS;
	uart_runtime_data[arrayIndex++] = UART_HEADER;
	uart_runtime_data[arrayIndex++] = (uint8_t) (UART_DELTA_LEN - 1u + UART_FIXED - 2u);
	uart_runtime_data[arrayIndex++] = UART_DELTA_ID;
	uart_runtime_data[arrayIndex++] = 0x01u;
	uart_runtime_data[arrayIndex++] = 0x00u;
	uart_runtime_data[arrayIndex++] = UART_DELTA_ADDR;
	uart_runtime_data[UART_DELTA_END]     = UART_FOOTER;

    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_WriteCallbackRegister(krono_tx_complete_callback, usart_ptr);
    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_ReadCallbackRegister(krono_rx_complete_callback, usart_ptr);

    if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Read(&read_buffer[read_buf_write_ptr], 1)) {

	}

}

void uart_send_touch_gesture_data(void)
{
	uint8_t *dest_ptr;

	if (uart_runtime_data[0] == 0u) {
		uart_init_debug_data();
	}

	if(uart_tx_in_progress == 0u) {
		if (uart_send_ges_data_flag == 1u) {
			dest_ptr = &uart_runtime_data[UART_GES_DATA_POS];
			for (uint8_t cnt = 0u; cnt < UART_GES_LEN; cnt++) {
				*dest_ptr++ = Krono_memory_map_read(VADDR_TOUCHRAM + cnt);
			}

			dest_ptr = &uart_runtime_data[UART_SIG_DATA_POS];
			for (uint8_t cnt = 0u; cnt < UART_SIG_LEN; cnt++) {
				*dest_ptr++ = Krono_memory_map_read(VADDR_RAWVALUES + cnt);
			}

			dest_ptr = &uart_runtime_data[UART_DELTA_DATA_POS];
			for (uint8_t cnt = 0u; cnt < UART_DELTA_LEN; cnt++) {
				*dest_ptr++ = Krono_memory_map_read(VADDR_SVRAM + cnt);
			}

			if(uart_command_info.header_status != HEADER_RECEIVED) {
				uart_new_data_available = 1u;
			}

	#if (KRONO_GESTURE_ENABLE == 1u)
			qtm_gestures_2d_clearGesture();
	#endif
		}
	}
}

uint8_t uart_min_num_bytes_received(void)
{
	if (read_buf_write_ptr >= read_buf_read_ptr) {
		return (read_buf_write_ptr - read_buf_read_ptr);
	} else {
		return ((read_buf_write_ptr + UART_RX_BUF_LEN) - read_buf_read_ptr);
	}
}

static uint8_t uart_tx_len = 0u;

void uart_send_header(uint8_t len, uint8_t id, uint8_t address)
{
	write_buf_write_ptr = 0u;
	uart_tx_len         = len + 5u;

	uart_send_data_wait(UART_HEADER);
	uart_send_data_wait(len + 4u);
	uart_send_data_wait(id);
	uart_send_data_wait(0x01u); // fixed
	uart_send_data_wait(0x00u); // fixed
	uart_send_data_wait(address);
}

void uart_process(void)
{
	uint8_t l_trans_id = 0u, l_addr = 0u, l_len = 0u;
    

	if (uart_new_data_available == 1u) {
		uart_new_data_available = 0u;
		uart_send_data();
	}

	if (uart_min_num_bytes_received() > 4u) {
		if (uart_get_char() == UART_HEADER) {
			/*received some data process it*/
			if (uart_command_info.header_status == HEADER_AWAITING) {
				l_trans_id                      = uart_get_char();
				uart_command_info.command_id    = uart_get_char();
				l_addr                          = uart_get_char();
				l_len                           = uart_get_char();
				uart_command_info.header_status = HEADER_RECEIVED;
			}

			if (uart_command_info.header_status == HEADER_RECEIVED) {
				read_buf_write_ptr = 0u;
				read_buf_read_ptr  = 0u;
				if (uart_command_info.command_id != COMMAND_INFO_PC_TO_MCU) {
					if (uart_command_info.command_id == COMMAND_INFO_MCU_TO_PC) // 0x81
					{
						while (uart_tx_in_progress == 1u) {

						}
						uart_send_ges_data_flag = 0u;
						uart_send_header(l_len, l_trans_id, l_addr);
						for (uint8_t cnt = 0u; cnt < l_len; cnt++) {
							uart_send_data_wait(Krono_memory_map_read(l_addr + cnt));
						}
						uart_send_data_wait(UART_FOOTER);
						uart_send_ges_data_flag = 1u;
					} else if (uart_command_info.command_id == COMMAND_DATA_MCU_TO_PC) // 0x01
					{
						while (uart_tx_in_progress == 1u) {

						}
						uart_send_ges_data_flag = 0u;
						uart_send_header(l_len, l_trans_id, l_addr);
						if (l_addr != 0u) {
							for (uint8_t cnt = 0u; cnt < l_len; cnt++) {
								uart_send_data_wait(Krono_memory_map_read(l_addr + cnt));
							}
						} else {
							uart_send_data_wait(0x00u);
							uart_send_data_wait(0x00u);
							uart_send_data_wait(0x00u);
							uart_send_data_wait(0x50u); // FIRMWARE INFORMATION
						}
						uart_send_data_wait(UART_FOOTER);
						uart_send_ges_data_flag = 1u;
					} else if (uart_command_info.command_id == COMMAND_DATA_PC_TO_MCU) // 0x00
					{
						while (uart_tx_in_progress == 1u) {

						}
						uart_send_ges_data_flag = 0u;
						uint8_t value           = l_len;
						if(Krono_memory_map_write(l_addr, value) != 0u) {
							/* error condition */
						}
						l_len = 1u;
						uart_send_header(l_len, l_trans_id, l_addr);
						uart_send_data_wait(value);
						uart_send_data_wait(UART_FOOTER);
						uart_send_ges_data_flag = 1u;
					} else {
						/* not expected to come here */
					}

					uart_command_info.header_status = HEADER_AWAITING;
				} else {
					uart_command_info.header_status = HEADER_AWAITING;
				}
			}
		}
	}
}

void krono_tx_complete_callback(uintptr_t usart_pt)
{
	/* USART TX complete interrupt */
	if (uart_send_ges_data_flag != 1u) {
		uart_tx_in_progress = 0u;
	} else {

		if (write_buf_read_ptr < (uint8_t) (UART_GES_LEN + UART_SIG_LEN + UART_DELTA_LEN + UART_FIXED * 3u)) {
			if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Write(&uart_runtime_data[write_buf_read_ptr], 1)) {

			}
			write_buf_read_ptr++;
		} else {
			uart_tx_in_progress = 0u;
		}
	}
}

void krono_rx_complete_callback(uintptr_t usart_pt)
{
    read_buf_write_ptr++;
    if (read_buf_write_ptr == UART_RX_BUF_LEN) {
        read_buf_write_ptr = 0u;
    }

    if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Read(&read_buffer[read_buf_write_ptr], 1)) {

	}
}

#endif

</#if>
