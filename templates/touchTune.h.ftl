/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    touchTune.h

  Summary:
    QTouch Modular Library

  Description:
    Configuration macros for touch library

*******************************************************************************/

/*******************************************************************************
Copyright (c) ${REL_YEAR} released Microchip Technology Inc.  All rights reserved.

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

#ifndef TOUCH_TUNE_H
#define TOUCH_TUNE_H


#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include "touch.h"

#if DEF_TOUCH_TUNE_ENABLE == 1U

/* 0x00000010b - msb 5 bits - Minor version (00000b), lsb first 3 bits - Major version (010b) */
#define PROTOCOL_VERSION 0x02u

#define DV_HEADER    0x55u //0x48
#define DV_FOOTER    0xAAu //0x46

#define UART_RX_BUF_LENGTH 60u

#define HEADER_AWAITING 0u
#define HEADER_RECEIVED 1u
#define DATA_AWAITING 2u
#define DATA_RECEIVED 3u
 
#define SEND_DEBUG_DATA		 0x8000u

#define STREAMING_DEBUG_DATA     (1u)
#define STREAMING_CONFIG_DATA    (2u)

#define ZERO 0x00u

typedef enum
{
	PC_REQUEST_CONFIG_DATA_FROM_MCU		= 0x01u,//0x31, // sw read PC_REQUEST_CONFIG_DATA_FROM_MCU
	PC_SEND_CONFIG_DATA_TO_MCU		= 0x02u,//0x32, // sw write	PC_SEND_CONFIG_DATA_TO_MCU
	MCU_SEND_TUNE_DATA_TO_PC		= 0x03u,//0x33, // send debug data MCU_SEND_TUNE_DATA_TO_PC
	MCU_RESPOND_CONFIG_DATA_TO_PC = 0x04u //0x34	// sw read MCU_RESPOND_CONFIG_DATA_TO_PC
}TYPE_ID_VALUES;

typedef enum {
	tiny = 0x31u,
    avrda = 0x32u,
	samd2x_d1x_l21 = 0x33u,
	samc2x = 0x34u,
	same5x = 0x35u,
	saml1x_pic32cmle = 0x36u,
	saml22 = 0x37u,
	pic32cvd = 0x38u,
	pic32czca = 0x39u,
	pic32cmpl= 0x40u
}DEVICE_TYPE;

/***********
 * Config data mask and ids
*/

#define PROJECT_CONFIG_ID  0u
#define SENSOR_NODE_CONFIG_ID 1u
#define SENSOR_KEY_CONFIG_ID 2u
#define COMMON_SENSOR_CONFIG_ID 3u
#define SCROLLER_CONFIG_ID 4u
#define FREQ_HOPPING_AUTO_TUNE_ID 5u
#define SURFACE_CONFIG_ID 6u
#define GESTURE_CONFIG_ID 7u


#define PROJECT_CONFIG_MASK  ((uint8_t) 1<<PROJECT_CONFIG_ID)
#define SENSOR_NODE_CONFIG_MASK ((uint8_t) 1<<(SENSOR_NODE_CONFIG_ID-1))
#define SENSOR_KEY_CONFIG_MASK ((uint8_t) 1<<(SENSOR_KEY_CONFIG_ID-1))
#define COMMON_SENSOR_CONFIG_MASK ((uint8_t) 1<<(COMMON_SENSOR_CONFIG_ID-1))
#define SCROLLER_CONFIG_MASK ((uint8_t) 1<<(SCROLLER_CONFIG_ID-1))
#define FREQ_HOPPING_AUTO_TUNE_MASK ((uint8_t) 1<<(FREQ_HOPPING_AUTO_TUNE_ID-1))
#define SURFACE_CONFIG_MASK ((uint8_t) 1<<(SURFACE_CONFIG_ID-1))
#define GESTURE_CONFIG_MASK ((uint8_t) 1<<(GESTURE_CONFIG_ID-1))

/***********
 * debug data mask and ids
*/

#define DEBUG_MASK 0x80u

#define KEY_DEBUG_DATA_ID 		0u
#define SCROLLER_DEBUG_DATA_ID	1u
#define FREQ_HOP_AUTO_TUNE_DATA_ID 		2u
#define SURFACE_DEBUG_DATA_ID 		3u
#define GESTURE_DEBUG_DATA_ID 		4u

#define KEY_DEBUG_MASK ((uint8_t)1<<KEY_DEBUG_DATA_ID)
#define SCROLLER_DEBUG_MASK ((uint8_t)1<<SCROLLER_DEBUG_DATA_ID)
#define FREQ_HOP_AUTO_TUNE_DEBUG_MASK ((uint8_t)1<<FREQ_HOP_AUTO_TUNE_DATA_ID)
#define SURFACE_DEBUG_MASK ((uint8_t)1<<SURFACE_DEBUG_DATA_ID)
#define GESTURE_DEBUG_MASK ((uint8_t)1<<GESTURE_DEBUG_DATA_ID)

typedef enum
{
	SELF_CAP = 0x00u,
	MUTUAL_CAP = 0x01u
}ACQ_METHOD;

typedef enum
{
	VAL_8P = 0x30u,
	VAL_4P = 0x40u
}SUB_TYPE;

typedef enum
{
	EV_LP = 0x01u,
	SW_LP = 0x02u,
	LUMP = 0x08u
}ROW_4;

void touchTuneInit(void);
void touchTuneProcess(void);
void touchTuneNewDataAvailable(void);



#endif

#endif /* TOUCH_TUNE_H */