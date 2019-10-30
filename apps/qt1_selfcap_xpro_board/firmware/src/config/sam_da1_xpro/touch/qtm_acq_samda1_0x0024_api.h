/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.

  File Name:
    qtm_acq_samda1_0x0024_api.h

  Summary:
    QTouch Modular Library

  Description:
    API for Acquisition module - SAMDA1/PTC
	
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

#ifndef TOUCH_API_DA1_ACQ_H
#define TOUCH_API_DA1_ACQ_H

/* Include files */
#include <stdint.h>
#include <stddef.h>
#include "qtm_acq_samd21_0x0024_api.h"
#define qtm_samda1_ptc_handler_eoc qtm_samd21_ptc_handler_eoc 
#define qtm_samda1_acq_module_get_id qtm_samd21_acq_module_get_id 
#define qtm_samda1_acq_module_get_version qtm_samd21_acq_module_get_version 
#define qtm_samda1_ptc_handler_wcomp qtm_samd21_ptc_handler_wcomp 
#define qtm_acq_samda1_node_config_t qtm_acq_samd21_node_config_t 


#endif    /* TOUCH_API_DA1_ACQ_H */
