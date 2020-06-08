
/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.

  File Name:
    qtm_acq_same51_0x000f_api.h

  Summary:
    QTouch Modular Library

  Description:
    API for Acquisition module - SAME51/PTC
	
*******************************************************************************/

/*******************************************************************************
Copyright (c) Microchip Technology Inc.  All rights reserved.

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

/*============================================================================
Filename : qtm_acq_same51_0x000f_api.h
Project : QTouch Modular Library
Purpose : API for Acquisition module - SAME51/PTC
------------------------------------------------------------------------------
Copyright (c)  Microchip Inc. All rights reserved.
------------------------------------------------------------------------------
============================================================================*/

#ifndef TOUCH_API_SAME51_ACQ_MODULE_H
#define TOUCH_API_SAME51_ACQ_MODULE_H

/* Include base API file */
#include "qtm_acq_same54_0x000f_api.h"

/* Definition of node config structure based on base API file */
#define qtm_acq_same51_node_config_t 		qtm_acq_same54_node_config_t

/* Definitions of derived API functions based on base API file */
#define qtm_same51_acq_module_get_id 		qtm_same54_acq_module_get_id
#define qtm_same51_acq_module_get_version 	qtm_same54_acq_module_get_version
#define qtm_same51_ptc_handler  			qtm_same54_ptc_handler

#endif /* TOUCH_API_SAME51_ACQ_MODULE_H */

