/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    kronocommuart_sam.h

  Summary:
    QTouch Modular Library

  Description:
    UART functions/macros to enable communication between SAM device and 
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
#ifndef KRONOCOMM_UART_H_
#define KRONOCOMM_UART_H_

<#if TOUCH_SERCOM_KRONO_INSTANCE == "">
#warning "UART to send touch debug data is not defined. Connect UART to Touch library in MHC."
<#else>
#include "definitions.h"                // SYS function prototypes
#include "touch/touch.h"
#include "touch/datastreamer/kronocommadaptor.h"

void uart_init_debug_data(void);
void uart_process(void);
void krono_rx_complete_callback(uintptr_t usart_pt);
void krono_tx_complete_callback(uintptr_t usart_pt);
void uart_send_touch_gesture_data(void);
void uart_send_header(uint8_t len, uint8_t id, uint8_t address);
uint8_t uart_min_num_bytes_received(void);
void uart_send_data(void);
void uart_send_data_wait(uint8_t data);
uint8_t uart_get_char(void);

#define VADDR_CORERAM           0x00u
#define VADDR_CORERAM_END       0x07u
#define VADDR_TOUCHRAM          0x10u
#define VADDR_TOUCHRAM_END      0x15u
#define VADDR_CFGRAM            0x20u
#define VADDR_CFGRAM_END        0x29u
#define VADDR_GESTURECFGRAM     0x37u
#define VADDR_GESTURECFGRAM_END 0x42u
#define VADDR_COMPRAM           0x5eu
#define VADDR_COMPRAM_END       0x74u
#define VADDR_SENSORMAP         0x75u
#define VADDR_SENSORMAP_END     0x8Bu
#define VADDR_SVRAM             0x8cu
#define VADDR_SVRAM_END         0xa2u
#define VADDR_RAWVALUES         0xa3u
#define VADDR_RAWVALUES_END     0xd0u
#define VADDR_BASEVALUES        0xd1u
#define VADDR_BASEVALUES_END    0xfeu
#define VADDR_VERSIONINFO_T     0xffu

#define UART_TX_BUF_LEN 100u
#define UART_RX_BUF_LEN 20u

#define HEADER_AWAITING 0u
#define HEADER_RECEIVED 1u

#define COMMAND_DATA_MCU_TO_PC 0x01u
#define COMMAND_DATA_PC_TO_MCU 0x00u
#define COMMAND_INFO_MCU_TO_PC 0x81u
#define COMMAND_INFO_PC_TO_MCU 0x80u

#endif /* UART_H_ */
</#if>