/*******************************************************************************
  Touch Library

  Company:
    Microchip Technology Inc.
    Filename : qtm_acq_pic32czca_0x004A_api.h 
    Project  : Touch Modular Library
    Purpose  : Acquisition module - PIC32CZ_CA80/CA90 
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
#ifndef TOUCH_API_PIC32CZCA_ACQ_H
#define TOUCH_API_PIC32CZCA_ACQ_H

/* Include files */
#include <stdint.h>
#include <stddef.h>
#include "qtm_common_components_api.h"

/* Bit mask forming */
#define TOUCH_BITMASK(np)  (uint32_t)((uint32_t) 1u << (np) )            
    
/* Touch constant definitions */
#undef X
#define X(n)        TOUCH_BITMASK((n))
#define Y(n)        TOUCH_BITMASK((n))
#define X_NONE      (0u)
#define Y_NONE      (0u)
#define CEXT_NONE   (0xFFu)

/* Extract Analog / Digital Gain */
#define NODE_GAIN_ANA(m) 		(uint8_t)(((m) & 0xF0u) >> 4u)
#define NODE_GAIN_DIG(m) 		(uint8_t)((m) & 0x0Fu)

/* Combine Analog / Digital Gain */
#define NODE_GAIN(a,d) 			(uint8_t)(((a) << 4u)|(d))

/* Extract Resistor / Prescaler */
#define NODE_RSEL(m) 			(uint8_t)(((m) & 0xF0u) >> 4u)
#define NODE_PRSC(m) 			(uint8_t)((m) & 0x0Fu)

/* Combine Resistor / Prescaler */
#define NODE_RSEL_PRSC(r,p) 	(uint8_t)(((r) << 4u)|(p))

/* Auto scan trigger Periods */
#define NODE_SCAN_8MS 			0u
#define NODE_SCAN_16MS 			1u
#define NODE_SCAN_32MS 			2u
#define NODE_SCAN_64MS 			3u
#define NODE_SCAN_128MS 		4u
#define NODE_SCAN_256MS 		5u
#define NODE_SCAN_512MS 		6u
#define NODE_SCAN_1024MS 		7u

typedef enum tag_filter_level_t 
{
  FILTER_LEVEL_1,
  FILTER_LEVEL_2,
  FILTER_LEVEL_4,
  FILTER_LEVEL_8,
  FILTER_LEVEL_16,
  FILTER_LEVEL_32,
  FILTER_LEVEL_64
}
filter_level_t;

/* Touch library GAIN setting */
typedef enum tag_gain_t 
{
  GAIN_1,
  GAIN_2,
  GAIN_4,
  GAIN_8
}
gain_t;
/* PTC clock prescale setting.
* For Example: if Generic clock input to PTC = 4MHz, then:
* PRSC_DIV_SEL_4 sets PTC Clock to 1MHz
* PRSC_DIV_SEL_8 sets PTC Clock to 500KHz
*
*/
typedef enum tag_prsc_div_sel_t 
{
  PRSC_DIV_SEL_2,
  PRSC_DIV_SEL_4,
  PRSC_DIV_SEL_8,
  PRSC_DIV_SEL_16,
  PRSC_DIV_SEL_32
}
prsc_div_sel_t;

/**
* PTC series resistor setting, only works in mutual capacitance mode
* RSEL_VAL_0 sets internal series resistor to 0ohms.
* RSEL_VAL_3 sets internal series resistor to 3Kohms.
* RSEL_VAL_6 sets internal series resistor to 6Kohms.
* RSEL_VAL_20 sets internal series resistor to 20Kohms.
* RSEL_VAL_50 sets internal series resistor to 50Kohms.
* RSEL_VAL_75 sets internal series resistor to 75Kohms.
* RSEL_VAL_100 sets internal series resistor to 100Kohms.
* RSEL_VAL_200 sets internal series resistor to 200Kohms.
*/
typedef enum tag_rsel_val_t 
{
  RSEL_VAL_0,
  RSEL_VAL_3,
  RSEL_VAL_6,
  RSEL_VAL_20,
  RSEL_VAL_50,
  RSEL_VAL_75,
  RSEL_VAL_100,
  RSEL_VAL_200
}
rsel_val_t;

/**
* PTC acquisition frequency delay setting.

* inserts "n" PTC clock cycles between consecutive measurements 
* e.g.  FREQ_HOP_SEL_14 setting inserts 14 PTC clock cycles.
OR
* FREQ_SEL_SPREAD automatically sweeps through all 15 delay values during the series of measurements.
*/
typedef enum tag_freq_config_sel_t 
{
  FREQ_SEL_0,
  FREQ_SEL_1,
  FREQ_SEL_2,
  FREQ_SEL_3,
  FREQ_SEL_4,
  FREQ_SEL_5,
  FREQ_SEL_6,
  FREQ_SEL_7,
  FREQ_SEL_8,
  FREQ_SEL_9,
  FREQ_SEL_10,
  FREQ_SEL_11,
  FREQ_SEL_12,
  FREQ_SEL_13,
  FREQ_SEL_14,
  FREQ_SEL_15,
  FREQ_SEL_SPREAD
}
freq_config_sel_t;

/*----------------------------------------------------------------------------
*     Structure Declarations
*----------------------------------------------------------------------------*/

/* Acquisition module Sequential */
typedef struct
{
  uint32_t node_xmask;		/* Selects the X Pins for this node */
  uint32_t node_ymask;		/* Selects the Y Pins for this node */
  uint8_t node_csd;             /* Charge share delay */
  uint8_t node_rsel_prsc;       /* Bits 7:4 = Resistor, Bits 3:0  Prescaler */
  uint8_t node_gain;            /* Bits 7:4 = Analog gain, Bits 3:0 = Digital gain */
  uint8_t node_oversampling;	/* Accumulator setting  */
}qtm_acq_pic32czca_node_config_t;

/* Node run-time data - Defined in common api as it will be used with all acquisition modules */

/* Node group configuration */
typedef struct
{
  uint16_t num_sensor_nodes;    /* Number of sensor node group */
  uint8_t acq_sensor_type;      /* Self or mutual sensors */
  uint8_t freq_option_select;   /* Frequency altering delay */
  uint8_t ptc_interrupt_priority;       /* Runtime priority of PTC interrupt */
  uint8_t wakeup_exp; /* wakeup exponent for the minimum prescaler of PTC(PRSC_DIV_SEL_2)  */
  
} qtm_acq_node_group_config_t;

/* Container structure for sensor group */
typedef struct
{
  qtm_acq_node_group_config_t *qtm_acq_node_group_config;
  qtm_acq_pic32czca_node_config_t *qtm_acq_node_config;
  qtm_acq_node_data_t *qtm_acq_node_data;
} qtm_acquisition_control_t;

typedef struct 
{
  qtm_acquisition_control_t* qtm_acq_control;
  uint16_t auto_scan_node_number;
  uint8_t auto_scan_node_threshold;
  uint8_t auto_scan_trigger;  
}qtm_auto_scan_config_t;


/*----------------------------------------------------------------------------
* prototypes
*----------------------------------------------------------------------------*/

/* Library prototypes */
/*============================================================================
touch_ret_t qtm_acquisition_process(void)
------------------------------------------------------------------------------
Purpose: Signal capture and processing
Input  : (Measured signals, config)
Output : touch_ret_t
Notes  : Called by application after 'touch_measure_complete_callback'
============================================================================*/
touch_ret_t qtm_acquisition_process(void);

/*============================================================================
touch_ret_t qtm_ptc_init_acquisition_module(qtm_acquisition_control_t* qtm_acq_control_ptr);
------------------------------------------------------------------------------
Purpose: Initialize the PTC & Assign pins
Input  : pointer to acquisition set
Output : touch_ret_t: TOUCH_SUCCESS or INVALID_PARAM
Notes  : ptc_init_acquisition module must be called ONLY once with a pointer to each config set
============================================================================*/
touch_ret_t qtm_ptc_init_acquisition_module(qtm_acquisition_control_t* qtm_acq_control_ptr);

/*============================================================================
touch_ret_t qtm_ptc_qtlib_assign_signal_memory(uint16_t* qtm_signal_raw_data_ptr);
------------------------------------------------------------------------------
Purpose: Assign raw signals pointer to array defined in application code
Input  : pointer to raw data array
Output : touch_ret_t: TOUCH_SUCCESS
Notes  : none
============================================================================*/
touch_ret_t qtm_ptc_qtlib_assign_signal_memory(uint16_t* qtm_signal_raw_data_ptr);

/* Scan configuration */
/*============================================================================
touch_ret_t qtm_enable_sensor_node(qtm_acquisition_control_t* qtm_acq_control_ptr, uint16_t qtm_which_node_number);
------------------------------------------------------------------------------
Purpose:  Enables a sensor node for measurement
Input  :  Node configurations pointer, node (channel) number
Output : touch_ret_t:
Notes  :
============================================================================*/
touch_ret_t qtm_enable_sensor_node(qtm_acquisition_control_t* qtm_acq_control_ptr, uint16_t qtm_which_node_number);

/*============================================================================
touch_ret_t qtm_calibrate_sensor_node(ptc_seq_acq_settings* qtm_acq_control_l_ptr, uint16_t which_node_number)
------------------------------------------------------------------------------
Purpose:  Marks a sensor node for calibration
Input  :  Node configurations pointer, node (channel) number
Output : touch_ret_t:
Notes  :
============================================================================*/
touch_ret_t qtm_calibrate_sensor_node(qtm_acquisition_control_t* qtm_acq_control_ptr, uint16_t qtm_which_node_number);

/* Measurement start - sequence or windowcomp */

/*============================================================================
touch_ret_t qtm_ptc_start_measurement_seq(qtm_acquisition_control_t* qtm_acq_control_pointer, void (*measure_complete_callback) (void));
------------------------------------------------------------------------------
Purpose:  Loads touch configurations for first channel and start,  
Input  :  Node configurations pointer, measure complete callback pointer
Output : touch_ret_t:
Notes  :
============================================================================*/
touch_ret_t qtm_ptc_start_measurement_seq(qtm_acquisition_control_t* qtm_acq_control_pointer, void (*measure_complete_callback) (void));

/*============================================================================
touch_ret_t qtm_autoscan_sensor_node(qtm_auto_scan_config_t* qtm_auto_scan_config_ptr, void (*auto_scan_callback)(void));
------------------------------------------------------------------------------
Purpose: Configures the PTC for sleep mode measurement of a single node, with window comparator wake
Input  : Acquisition set, channel number, threshold, scan trigger
Output : touch_ret_t
Notes  : none
============================================================================*/
touch_ret_t qtm_autoscan_sensor_node(qtm_auto_scan_config_t* qtm_auto_scan_config_ptr, void (*auto_scan_callback)(void));

/*============================================================================
touch_ret_t qtm_autoscan_node_cancel(void)
------------------------------------------------------------------------------
Purpose: Cancel auto-scan config
Input  : None
Output : touch_ret_t
Notes  : none
============================================================================*/
touch_ret_t qtm_autoscan_node_cancel(void);

/*============================================================================
void qtm_ptc_de_init(void)
------------------------------------------------------------------------------
Purpose: Clear PTC Pin registers, set TOUCH_STATE_NULL
Input  : none
Output : none
Notes  : none
============================================================================*/
void qtm_ptc_de_init(void);

/*============================================================================
void qtm_ptc_clear_interrupt(void)
------------------------------------------------------------------------------
Purpose:  Clears the eoc/wcomp interrupt bits
Input    :  none
Output  :  none
Notes    :  none
============================================================================*/
void qtm_ptc_clear_interrupt(void);

/*============================================================================
void qtm_pic32czca_ptc_handler_eoc(void)
------------------------------------------------------------------------------
Purpose:  Captures  the  measurement,  starts  the  next  or  End  Of  Sequence  handler
Input    :  none
Output  :  none
Notes    :  none
============================================================================*/
void qtm_pic32czca_ptc_handler_eoc(void);

/*============================================================================
uint16_t qtm_acq_module_get_id(void);
------------------------------------------------------------------------------
Purpose: Returns the module ID
Input  : none
Output : Module ID
Notes  : none
============================================================================*/
uint16_t qtm_acq_module_get_id(void);

/*============================================================================
uint8_t qtm_acq_module_get_version(void);
------------------------------------------------------------------------------
Purpose: Returns the module Firmware version
Input  : none
Output : Module ID - Upper nibble major / Lower nibble minor
Notes  : none
============================================================================*/
uint8_t qtm_acq_module_get_version(void);

#endif    /* TOUCH_API_PIC32CZCA_ACQ_H */
