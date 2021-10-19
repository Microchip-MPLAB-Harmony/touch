/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    touchTune.c

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


#ifndef _TOUCHTUNE_H_
#define _TOUCHTUNE_H_


#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include "touch.h"

#if DEF_TOUCH_TUNE_ENABLE == 1U

#define DV_HEADER    0x55 //0x48
#define DV_FOOTER    0xAA //0x46

#define UART_RX_BUF_LENGTH 60

#define HEADER_AWAITING 0
#define HEADER_RECEIVED 1
#define DATA_AWAITING 2
#define DATA_RECEIVED 3
 

#define SEND_DEBUG_DATA		 0x8000

#define ZERO 0x00 // 0x30 

typedef enum
{
	NO_FRAME = 0xFF,
	CONFIG_INFO =  0x00, // 0x41
	SENSOR_ACQ_KEY_CONFIG ,
	COMMON_KEY_CONFIG_I ,
	COMMON_KEY_CONFIG_II,
	SCROLLER_CONFIG ,
	FREQ_HOPPING_AUTO_TUNE ,
	FREQ_HOPPING_MANUAL_TUNE,
	SURFACE_CONFIG ,
	LUMP_CONFIG,
	KEY_DEBUG_DATA_ID = 0xF0,
	SCROLLER_DEBUG_DATA_ID = 0xF1,
	FREQ_HOP_AUTO_TUNE_DATA_ID = 0xF2
}FRAME_ID_VALUES;

typedef enum
{
	PC_REQUEST_CONFIG_DATA_FROM_MCU		= 0x01,//0x31, // sw read PC_REQUEST_CONFIG_DATA_FROM_MCU
	PC_SEND_CONFIG_DATA_TO_MCU		= 0x02,//0x32, // sw write	PC_SEND_CONFIG_DATA_TO_MCU
	MCU_SEND_TUNE_DATA_TO_PC		= 0x03,//0x33, // send debug data MCU_SEND_TUNE_DATA_TO_PC
	MCU_RESPOND_CONFIG_DATA_TO_PC = 0x04 //0x34	// sw read MCU_RESPOND_CONFIG_DATA_TO_PC
}TYPE_ID_VALUES;

typedef enum {
	tiny = 0x31,
    avrda = 0x32,
	samd2x_d1x_l21 = 0x33,
	samc2x = 0x34,
	same5x = 0x35,
	saml1x_pic32cmle = 0x36,
	saml22 = 0x37,
	pic32cvd = 0x38
}DEVICE_TYPE;

typedef enum
{
	FREQ_HOP_MODULE           = 0x01,
	FREQ_HOP_AUTO_TUNE_MODULE = 0x02,
	KEYS_MODULE               = 0x04,
	SCROLLER_MODULE           = 0x08,
	SURFACE_1T_MODULE         = 0x10,
	SURFACE_2T_MODULE         = 0x20
}LIBRARY_MODULES;

typedef enum
{
	SELF_CAP = 0x03,
	MUTUAL_CAP = 0x04
}ACQ_METHOD;

typedef enum
{
	VAL_8P = 0x30,
	VAL_4P = 0x40
}SUB_TYPE;

typedef enum
{
	EV_LP = 0x01,
	SW_LP = 0x02,
	LUMP = 0x08	
}ROW_4;

typedef enum
{
	PROTOCOL_VERSION = 0x36
}ROW_5;

void touchTuneInit(void);
void touchTuneProcess(void);
void touchTuneNewDataAvailable(void);

extern volatile uint16_t command_flags;



#endif

#endif /* _TOUCHTUNE_H_ */