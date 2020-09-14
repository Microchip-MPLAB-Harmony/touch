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
#ifndef UART_H_
#define UART_H_

#include "definitions.h"                // SYS function prototypes
#include "touch/touch.h"
#include "touch/datastreamer/kronocommadaptor.h"

void uart_init_debug_data(void);
void uart_process(void);
void krono_rx_complete_callback(uintptr_t);
void krono_tx_complete_callback(uintptr_t);
void uart_send_touch_gesture_data(void);

/* Register MAP https://microchip.app.box.com/file/139775393441 */
typedef enum {
	VADDR_CORERAM           = 0x00,
	VADDR_CORERAM_END       = 0x07,
	VADDR_TOUCHRAM          = 0x10,
	VADDR_TOUCHRAM_END      = 0x15,
	VADDR_CFGRAM            = 0x20,
	VADDR_CFGRAM_END        = 0x29,
	VADDR_GESTURECFGRAM     = 0x37,
	VADDR_GESTURECFGRAM_END = 0x42,
	VADDR_COMPRAM           = 0x5e,
	VADDR_COMPRAM_END       = 0x74,
	VADDR_SENSORMAP         = 0x75,
	VADDR_SENSORMAP_END     = 0x8B,
	VADDR_SVRAM             = 0x8c,
	VADDR_SVRAM_END         = 0xa2,
	VADDR_RAWVALUES         = 0xa3,
	VADDR_RAWVALUES_END     = 0xd0,
	VADDR_BASEVALUES        = 0xd1,
	VADDR_BASEVALUES_END    = 0xfe,
	VADDR_VERSIONINFO_T     = 0xff
} VADDR_BLOCKS;

#define UART_TX_BUF_LEN 100
#define UART_RX_BUF_LEN 20

#define HEADER_AWAITING 0
#define HEADER_RECEIVED 1

#define COMMAND_DATA_MCU_TO_PC 0x01
#define COMMAND_DATA_PC_TO_MCU 0x00
#define COMMAND_INFO_MCU_TO_PC 0x81
#define COMMAND_INFO_PC_TO_MCU 0x80

#endif /* UART_H_ */
