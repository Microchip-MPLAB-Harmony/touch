
/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.

  File Name:
    qtm_acq_samc20_0x0020_api.h

  Summary:
    QTouch Modular Library

  Description:
    API for Acquisition module - SAMC20/PTC
	
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

/* QTouch Modular Library Configuration */

#ifndef TOUCH_API_C20_ACQ_H
#define TOUCH_API_C20_ACQ_H

/* Include files */
#include <stdint.h>
#include <stddef.h>
#include "qtm_acq_samc21_0x0020_api.h"
#define qtm_samc20_ptc_handler_eoc qtm_samc21_ptc_handler_eoc
#define qtm_samc20_acq_module_get_id qtm_samc21_acq_module_get_id
#define qtm_samc20_acq_module_get_version qtm_samc21_acq_module_get_version
#define qtm_samc20_ptc_handler_wcomp qtm_samc21_ptc_handler_wcomp
#define qtm_acq_samc20_node_config_t qtm_acq_samc21_node_config_t

#endif /* TOUCH_API_C20_ACQ_H */
