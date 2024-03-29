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

#ifndef KRONOCOMMADAPTOR_H
#define KRONOCOMMADAPTOR_H

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
#define MODE_STANDBY 0b0000u
#define MODE_FULL 0b0011
#define MODE_TOUCH 0x02u
#define MODE_GESTURE 0x01u
#define MODE_RAWADC 0b0100u

#define VERSION_HI 2u
#define VERSION_LO 0u
#define ID_HI 0u
#define ID_LO 0x30u

// bit masks for touch flags (used by touchRam.touchState)

#define TOUCHSTATE_TCH 0x01u
#define TOUCHSTAT_TCH_DUAL 0x04u
#define TOUCHSTATE_nTCH 0xfeu
#define TOUCHSTATE_GES 0x02u
#define TOUCHSTATE_nGES 0xfdu

uint8_t Krono_memory_map_read(uint8_t mem_map_address);
uint8_t Krono_memory_map_write(uint8_t mem_map_address, uint8_t write_what);

void Krono_UpdateBuffer(void);

#endif /* KRONOCOMMADAPTOR_H */
