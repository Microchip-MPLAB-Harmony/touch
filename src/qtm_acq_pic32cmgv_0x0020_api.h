/* QTouch Modular Library Configuration */
/* Header file for application project - Acquisition library API */

#ifndef TOUCH_API_PIC32CMGV_ACQ_H
#define TOUCH_API_PIC32CMGV_ACQ_H

/* Include files */
#include <stdint.h>
#include <stddef.h>
#include "qtm_acq_samd20_0x000e_api.h"
#define qtm_pic32cmgv_ptc_handler_eoc qtm_samd20_ptc_handler_eoc
#define qtm_pic32cmgv_acq_module_get_id qtm_samd20_acq_module_get_id
#define qtm_pic32cmgv_acq_module_get_version qtm_samd20_acq_module_get_version
#define qtm_pic32cmgv_ptc_handler_wcomp qtm_samd20_ptc_handler_wcomp
#define qtm_acq_pic32cmgv_node_config_t qtm_acq_samd20_node_config_t


#endif    /* TOUCH_API_PIC32CMGV_ACQ_H */
