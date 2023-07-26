
/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.

  File Name:
    datastreamer.h

  Summary:
    QTouch Modular Library

  Description:
    Header file for datastreamer.
	
*******************************************************************************/

/*******************************************************************************
Copyright (C) [2023], Microchip Technology Inc., and its subsidiaries. All rights reserved.

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

#ifndef DATASTREAMER_H
#define DATASTREAMER_H

/*----------------------------------------------------------------------------
 *     include files
 *----------------------------------------------------------------------------*/
#include "touch/touch.h"

#if (DEF_TOUCH_DATA_STREAMER_ENABLE == 1u)

/*----------------------------------------------------------------------------
 *     defines
 *----------------------------------------------------------------------------*/
#define USER_BOARD 0x0000
#define TINY_XPLAINED_MINI 0xF012
#define TINY_XPLAINED_PRO 0xF013
#define TINY_MOISTURE_DEMO 0xF014
#define MEGA_328PB_XPLAINED_MINI 0xF015
#define MEGA_324PB_XPLAINED_PRO 0xF016

/*----------------------------------------------------------------------------
 *   prototypes
 *----------------------------------------------------------------------------*/
void datastreamer_init(void);
void datastreamer_output(void);

#endif

#endif
