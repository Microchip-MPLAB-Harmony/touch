/* QTouch Modular Library Configuration */
/* Header file for application project - Acquisition library API */

#ifndef TOUCH_API_PIC32CMJH_ACQ_H
#define TOUCH_API_PIC32CMJH_ACQ_H

/* Include files */
#include <stdint.h>
#include <stddef.h>
#include "qtm_acq_samc21_0x0020_api.h"
#define qtm_pic32cmjh_ptc_handler_eoc qtm_samc21_ptc_handler_eoc
#define qtm_pic32cmjh_acq_module_get_id qtm_samc21_acq_module_get_id
#define qtm_pic32cmjh_acq_module_get_version qtm_samc21_acq_module_get_version
#define qtm_pic32cmjh_ptc_handler_wcomp qtm_samc21_ptc_handler_wcomp
#define qtm_acq_pic32cmjh_node_config_t qtm_acq_samc21_node_config_t


#endif    /* TOUCH_API_PIC32CMJH_ACQ_H */
