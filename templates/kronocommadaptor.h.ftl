/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    kronocommadaptor.h

  Summary:
    QTouch Modular Library

  Description:
    Enables communication between device and Microchip 2D Touch Surface Utility.
	
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

#ifndef KRONOCOMMADAPTOR_H_
#define KRONOCOMMADAPTOR_H_

#include <stdint.h>
#include "touch/touch.h"

#define GESTURECFGRAM_SIZE 14u

#define CORERAM_SIZE 8u
typedef struct _CORERAM {
	uint8_t fwMajor;
	uint8_t fwMinor;
	uint8_t appIDhigh;
	uint8_t appIDlow;
	uint8_t cmd;
	uint8_t mode;
	uint8_t modeCon;
	uint8_t powerState;
} CORERAM;

#define CORERAM_CMD_ADDR 4u

#define CFGRAM_SIZE 10u
typedef struct _CFGRAM {
	uint8_t numberOfXChannels;
	uint8_t numberOfYChannels;
	uint8_t scanCount;
	uint8_t touchThreshX;
	uint8_t touchThreshY;
	uint8_t ActivePeriodL;
	uint8_t ActivePeriodH;
	uint8_t IdleperiodL;
	uint8_t IdlePeriodH;
	uint8_t resolution;
} CFGRAM;

#define CFGGRAM_OVRSMPLS_ADDR 2u
#define CFGGRAM_THRESH_X_ADDR 3u
#define CFGGRAM_THRESH_Y_ADDR 4u
#define CFGGRAM_RESOL_ADDR 9u

/* Gesture config - no struct definition */
#define GESTCFGRAM_TAP_RELEASE_TIMEOUT_ADDR 0u
#define GESTCFGRAM_TAP_HOLD_TIMEOUT_ADDR 1u
#define GESTCFGRAM_SWIPE_TIMEOUT_ADDR 2u
#define GESTCFGRAM_XSWIPE_DIST_ADDR 3u
#define GESTCFGRAM_YSWIPE_DIST_ADDR 4u
#define GESTCFGRAM_EDGSWIPE_DIST_ADDR 5u
#define GESTCFGRAM_TAP_DIST_ADDR 6u
#define GESTCFGRAM_MULTI_TAP_DIST_ADDR 7u
#define GESTCFGRAM_EDGE_BOUND_ADDR 8u
#define GESTCFGRAM_WHEEL_POSTSCAL_ADDR 9u
#define GESTCFGRAM_WHEEL_STARTQUAD_ADDR 10u
#define GESTCFGRAM_WHEEL_REVQUAD_ADDR 11u
#define GESTCFGRAM_PINCHZOOM_THRS_ADDR 12u
#define GESTCFGRAM_PALMDETECTION_THRS_ADDR 13u

typedef struct _VersionInfo {
	uint8_t fwVersion_H; // Offset: 0
	uint8_t fwVersion_L; // Offset: 1
	uint8_t appID_H;     // Offset: 2
	uint8_t appID_L;     // Offset: 3
} VersionInfo;

#define TOUCHRAM_SIZE 6u
typedef struct _TOUCHRAM {
	uint8_t touchStatus;
	uint8_t touchX;
	uint8_t touchY;
	uint8_t touchLSB;
	uint8_t gestureState;
	uint8_t gestureDiag;
} TOUCHRAM;

// maks for operating modes (used by coreRam.mode)
#define MODE_STANDBY 0b0000
#define MODE_FULL 0b0011
#define MODE_TOUCH 0x02u
#define MODE_GESTURE 0x01u
#define MODE_RAWADC 0b0100

#define VERSION_HI 2
#define VERSION_LO 0
#define ID_HI 0
#define ID_LO 0x30

// bit masks for touch flags (used by touchRam.touchState)

#define TOUCHSTATE_TCH 0x01
#define TOUCHSTAT_TCH_DUAL 0x04
#define TOUCHSTATE_nTCH 0xfe
#define TOUCHSTATE_GES 0x02
#define TOUCHSTATE_nGES 0xfd

#endif /* KRONOCOMMADAPTOR_H_ */

uint8_t *Adaptor_QueryCoreValues(uint8_t addressOffset);
uint8_t *Adaptor_QueryCFGValues(uint8_t addressOffset);
uint8_t *Adaptor_QueryTouchValues(uint8_t addressOffset);
uint8_t *Adaptor_QuerySensorDelta(uint8_t addressOffset);
uint8_t *Adaptor_QuerySensorRaw(uint8_t addressOffset);
uint8_t *Adaptor_QuerySensorRef(uint8_t addressOffset);
uint8_t *Adaptor_QueryGestureCFGValues(uint8_t addressOffset);

uint8_t Krono_memory_map_read(uint8_t mem_map_address);
uint8_t Krono_memory_map_write(uint8_t mem_map_address, uint8_t write_what);

void Krono_UpdateBuffer(void);
void InitIRQPin(void);
void SetIRQPin(void);
void ClearIRQPin(void);
