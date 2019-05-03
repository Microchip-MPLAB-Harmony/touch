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

