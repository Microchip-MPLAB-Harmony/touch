/*******************************************************************************
  Touch Library v3.7.0 Release

  Company:
    Microchip Technology Inc.

  File Name:
    touch.c

  Summary:
    QTouch Modular Library

  Description:
    Provides Initialization, Processing and ISR handler of touch library,
    Simple API functions to get/set the key touch parameters from/to the
    touch library data structures
*******************************************************************************/

/*******************************************************************************
Copyright (c)  2020 released Microchip Technology Inc.  All rights reserved.

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

/*----------------------------------------------------------------------------
 *     include files
 *----------------------------------------------------------------------------*/
#include "touch/touch.h"
#include "definitions.h" 
#include "touch/datastreamer/datastreamer.h"
/*----------------------------------------------------------------------------
 *   prototypes
 *----------------------------------------------------------------------------*/

/*! \brief configure binding layer config parameter
 */
static void build_qtm_config(qtm_control_t *qtm);

/*! \brief configure keys, wheels and sliders.
 */
static touch_ret_t touch_sensors_config(void);

/*! \brief Init complete callback function prototype.
 */
static void init_complete_callback();

/*! \brief Touch measure complete callback function example prototype.
 */
static void qtm_measure_complete_callback(void);

/*! \brief Touch post process complete callback function prototype.
 */
static void qtm_post_process_complete();

/*! \brief Touch Error callback function prototype.
 */
static void qtm_error_callback(uint8_t error);


/*----------------------------------------------------------------------------
 *     Global Variables
 *----------------------------------------------------------------------------*/

/* Binding layer control */
qtm_control_t  qtm_control;
qtm_control_t *p_qtm_control;
qtm_state_t    qstate;

/* Measurement Done Touch Flag  */
volatile uint8_t measurement_done_touch = 0;

/* Error Handling */
uint8_t module_error_code = 0;


/* Acquisition module internal data - Size to largest acquisition set */
uint16_t touch_acq_signals_raw[DEF_NUM_CHANNELS];
/* Acquisition set 1 - General settings */
qtm_acq_node_group_config_t ptc_qtlib_acq_gen1
    = {DEF_NUM_CHANNELS, DEF_SENSOR_TYPE, DEF_PTC_CAL_AUTO_TUNE, DEF_SEL_FREQ_INIT, DEF_PTC_INTERRUPT_PRIORITY};

/* Node status, signal, calibration values */
qtm_acq_node_data_t ptc_qtlib_node_stat1[DEF_NUM_CHANNELS];

/* Node configurations */
qtm_acq_saml21_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {NODE_0_PARAMS};

/* Container */
qtm_acquisition_control_t qtlib_acq_set1 = {&ptc_qtlib_acq_gen1, &ptc_seq_node_cfg1[0], &ptc_qtlib_node_stat1[0]};

/**********************************************************/
/*********** Frequency Hop Auto tune Module **********************/
/**********************************************************/

/* Buffer used with various noise filtering functions */
uint16_t noise_filter_buffer[DEF_NUM_CHANNELS * NUM_FREQ_STEPS];
uint8_t  freq_hop_delay_selection[NUM_FREQ_STEPS] = {DEF_MEDIAN_FILTER_FREQUENCIES};
uint8_t  freq_hop_autotune_counters[NUM_FREQ_STEPS];

/* Configuration */
qtm_freq_hop_autotune_config_t qtm_freq_hop_autotune_config1 = {DEF_NUM_CHANNELS,
                                                                NUM_FREQ_STEPS,
                                                                &ptc_qtlib_acq_gen1.freq_option_select,
                                                                &freq_hop_delay_selection[0],
                                                                DEF_FREQ_AUTOTUNE_ENABLE,
                                                                FREQ_AUTOTUNE_MAX_VARIANCE,
                                                                FREQ_AUTOTUNE_COUNT_IN};

/* Data */
qtm_freq_hop_autotune_data_t qtm_freq_hop_autotune_data1
    = {0, 0, &noise_filter_buffer[0], &ptc_qtlib_node_stat1[0], &freq_hop_autotune_counters[0]};

/* Container */
qtm_freq_hop_autotune_control_t qtm_freq_hop_autotune_control1
    = {&qtm_freq_hop_autotune_data1, &qtm_freq_hop_autotune_config1};

/**********************************************************/
/*********************** Keys Module **********************/
/**********************************************************/

/* Keys set 1 - General settings */
qtm_touch_key_group_config_t qtlib_key_grp_config_set1 = {DEF_NUM_SENSORS,
                                                          DEF_TOUCH_DET_INT,
                                                          DEF_MAX_ON_DURATION,
                                                          DEF_ANTI_TCH_DET_INT,
                                                          DEF_ANTI_TCH_RECAL_THRSHLD,
                                                          DEF_TCH_DRIFT_RATE,
                                                          DEF_ANTI_TCH_DRIFT_RATE,
                                                          DEF_DRIFT_HOLD_TIME,
                                                          DEF_REBURST_MODE};

qtm_touch_key_group_data_t qtlib_key_grp_data_set1;

/* Key data */
qtm_touch_key_data_t qtlib_key_data_set1[DEF_NUM_SENSORS];

/* Key Configurations */
qtm_touch_key_config_t qtlib_key_configs_set1[DEF_NUM_SENSORS] = {KEY_0_PARAMS}; 
/* Container */
qtm_touch_key_control_t qtlib_key_set1
    = {&qtlib_key_grp_data_set1, &qtlib_key_grp_config_set1, &qtlib_key_data_set1[0], &qtlib_key_configs_set1[0]};




/**********************************************************/
/****************  Binding Layer Module  ******************/
/**********************************************************/
#define LIB_MODULES_INIT_LIST                                                                                          \
    {                                                                                                                  \
        (module_init_t) & qtm_ptc_init_acquisition_module, null                                                        \
    }

#define LIB_MODULES_PROC_LIST                                                                                          \
    {                                                                                                                  \
		(module_proc_t)&qtm_freq_hop_autotune,             \
						\
		(module_proc_t)&qtm_key_sensors_process,                                                                        \
						\
	 	                               \
		                               \
		                               \
		                               \
		null                                                                                                           \
    }

#define LIB_INIT_DATA_MODELS_LIST                                                                                      \
    {                                                                                                                  \
        (void *)&qtlib_acq_set1, null                                                                                  \
    }

#define LIB_DATA_MODELS_PROC_LIST                                                                                       \
    {                                                                                                                   \
		(void *)&qtm_freq_hop_autotune_control1,               \
						\
		(void *)&qtlib_key_set1,                                                                                           \
						\
		                                         \
		                                      \
		                               \
		                               \
		null                                                                                                               \
    }

#define LIB_MODULES_ACQ_ENGINES_LIST                                                                                   \
    {                                                                                                                  \
        (module_acq_t) & qtm_ptc_start_measurement_seq, null                                                           \
    }

#define LIB_MODULES_ACQ_ENGINES_LIST_DM                                                                                \
    {                                                                                                                  \
        (void *)&qtlib_acq_set1, null                                                                                  \
    }

/* QTM run time options */
module_init_t library_modules_init[]            = LIB_MODULES_INIT_LIST;
module_proc_t library_modules_proc[]            = LIB_MODULES_PROC_LIST;
module_arg_t  library_module_init_data_models[] = LIB_INIT_DATA_MODELS_LIST;
module_acq_t  library_modules_acq_engines[]     = LIB_MODULES_ACQ_ENGINES_LIST;

module_arg_t library_module_acq_engine_data_model[] = LIB_MODULES_ACQ_ENGINES_LIST_DM;
module_arg_t library_module_proc_data_model[]       = LIB_DATA_MODELS_PROC_LIST;

/*----------------------------------------------------------------------------
 *   function definitions
 *----------------------------------------------------------------------------*/


/*============================================================================
static void build_qtm_config(qtm_control_t *qtm)
------------------------------------------------------------------------------
Purpose: Initialization of binding layer module
Input  : Pointer of binding layer container data structure
Output : none
Notes  :
============================================================================*/
static void build_qtm_config(qtm_control_t *qtm)
{
    /* Initialise the Flags by clearing them */
    qtm->binding_layer_flags = 0x00u;

    /*!< List of function pointers to acquisition sets */
    qtm->library_modules_init = library_modules_init;

    /*!< List of function pointers to post processing modules  */
    qtm->library_modules_proc = library_modules_proc;

    /*!< List of Acquisition Engines (Acq Modules one per AcqSet */
    qtm->library_modules_acq = library_modules_acq_engines;

    /*!< Data Model for Acquisition modules  */
    qtm->library_module_init_data_model = library_module_init_data_models;

    /*!< Data Model for post processing modules  */
    qtm->library_module_proc_data_model = library_module_proc_data_model;

    /*!< Data model for inline module processes  */
    qtm->library_modules_acq_dm = library_module_acq_engine_data_model;

    /*!< Post porcessing pointer */
    qtm->qtm_acq_pp = qtm_acquisition_process;

    /* Register Binding layer callbacks */
    qtm->qtm_init_complete_callback    = init_complete_callback;
    qtm->qtm_error_callback            = qtm_error_callback;
    qtm->qtm_measure_complete_callback = qtm_measure_complete_callback;
    qtm->qtm_pre_process_callback      = null;
    qtm->qtm_post_process_callback     = qtm_post_process_complete;
}

/*============================================================================
static touch_ret_t touch_sensors_config(void)
------------------------------------------------------------------------------
Purpose: Initialization of touch key sensors
Input  : none
Output : none
Notes  :
============================================================================*/
/* Touch sensors config - assign nodes to buttons / wheels / sliders / surfaces / water level / etc */
static touch_ret_t touch_sensors_config(void)
{
    uint16_t    sensor_nodes;
    touch_ret_t touch_ret = TOUCH_SUCCESS;

    /* Init pointers to DMA sequence memory */
    qtm_ptc_qtlib_assign_signal_memory(&touch_acq_signals_raw[0]);

    /* Initialize sensor nodes */
    for (sensor_nodes = 0u; sensor_nodes < DEF_NUM_CHANNELS; sensor_nodes++) {
        /* Enable each node for measurement and mark for calibration */
        qtm_enable_sensor_node(&qtlib_acq_set1, sensor_nodes);
        qtm_calibrate_sensor_node(&qtlib_acq_set1, sensor_nodes);
    }


    /* Enable sensor keys and assign nodes */
    for (sensor_nodes = 0u; sensor_nodes < DEF_NUM_SENSORS; sensor_nodes++) {
			qtm_init_sensor_key(&qtlib_key_set1, sensor_nodes, &ptc_qtlib_node_stat1[sensor_nodes]);
    }



    return (touch_ret);
}

/*============================================================================
static void init_complete_callback(void)
------------------------------------------------------------------------------
Purpose: Callback function from binding layer called after the completion of
         acquisition module initialization.
Input  : none
Output : none
Notes  :
============================================================================*/
static void init_complete_callback(void)
{
    /* Configure touch sensors with Application specific settings */
    touch_sensors_config();
}

/*============================================================================
static void qtm_measure_complete_callback( void )
------------------------------------------------------------------------------
Purpose: Callback function from binding layer called after the completion of
         measurement cycle. This function sets the post processing request
         flag to trigger the post processing.
Input  : none
Output : none
Notes  :
============================================================================*/
static void qtm_measure_complete_callback(void)
{
    qtm_control.binding_layer_flags |= (1 << node_pp_request);
}

/*============================================================================
static void qtm_post_process_complete(void)
------------------------------------------------------------------------------
Purpose: Callback function from binding layer called after the completion of
         post processing. This function sets the reburst flag based on the
         key sensor group status, calls the datastreamer output function to
         display the module data.
Input  : none
Output : none
Notes  :
============================================================================*/
static void qtm_post_process_complete(void)
{
    if ((0u != (qtlib_key_set1.qtm_touch_key_group_data->qtm_keys_status & 0x80u))) {
        p_qtm_control->binding_layer_flags |= (1u << reburst_request);
    } else {
        measurement_done_touch = 1;
    }
#if DEF_TOUCH_DATA_STREAMER_ENABLE == 1
    datastreamer_output();
#endif

}

/*============================================================================
static void qtm_error_callback(uint8_t error)
------------------------------------------------------------------------------
Purpose: Callback function from binding layer called after the completion of
         post processing. This function is called only when there is error.
Input  : error code
Output : decoded module error code
Notes  :
Error Handling supported by Binding layer module:
    Acquisition Module Error codes: 0x8<error code>
    0x81 - Qtm init
    0x82 - start acq
    0x83 - cal sensors
    0x84 - cal hardware

    Post processing Modules error codes: 0x4<process_id>
    0x40, 0x41, 0x42, ...
    process_id is the sequence of process IDs listed in #define LIB_MODULES_PROC_LIST macro.
    Process IDs start from zero and maximum is 15

    Examples:
    0x40 -> error in post processing module 1
    0x42 -> error in post processing module 3

Derived Module_error_codes:
    Acquisition module error =1
    post processing module1 error = 2
    post processing module2 error = 3
    ... and so on

============================================================================*/
static void qtm_error_callback(uint8_t error)
{
    module_error_code = 0;
    if (error & 0x80) {
        module_error_code = 1;
    } else if (error & 0x40) {
        module_error_code = (error & 0x0F) + 2;
    }

#if DEF_TOUCH_DATA_STREAMER_ENABLE == 1
    datastreamer_output();
#endif
}

/*============================================================================
void touch_init(void)
------------------------------------------------------------------------------
Purpose: Initialization of touch library. PTC, timer, binding layer and
         datastreamer modules are initialized in this function.
Input  : none
Output : none
Notes  :
============================================================================*/
void touch_init(void)
{
	    touch_timer_config();

    build_qtm_config(&qtm_control);

    qtm_binding_layer_init(&qtm_control);

    /* get a pointer to the binding layer control */
    p_qtm_control = qmt_get_binding_layer_ptr();

	
#if DEF_TOUCH_DATA_STREAMER_ENABLE == 1
    datastreamer_init();
#endif
}

/*============================================================================
void touch_process(void)
------------------------------------------------------------------------------
Purpose: Main processing function of touch library. This function initiates the
         acquisition, calls post processing after the acquistion complete and
         sets the flag for next measurement based on the sensor status.
Input  : none
Output : none
Notes  :
============================================================================*/
volatile uint8_t time_to_measure_touch_var =0;
void touch_process(void)
{
    touch_ret_t touch_ret;
    /* check the time_to_measure_touch for Touch Acquisition */
    if (time_to_measure_touch_var)
	{
        /* Do the acquisition */
        touch_ret = qtm_lib_start_acquisition(0);

        /* if the Acquistion request was successful then clear the request flag */
        if (TOUCH_SUCCESS == touch_ret) {
            /* Clear the Measure request flag */
			time_to_measure_touch_var = 0;
        }
    }

    /* check the flag for node level post processing */
    if (p_qtm_control->binding_layer_flags & (1u << node_pp_request)) {
        /* Run Acquisition module level post pocessing*/
        touch_ret = qtm_lib_acq_process();

        /* Check the return value */
        if (TOUCH_SUCCESS == touch_ret) {
            /* Returned with success: Start module level post processing */
            qtm_lib_post_process();
        } else {
            /* Acq module Eror Detected: Issue an Acq module common error code 0x80 */
            qtm_error_callback(0x80);
        }

        /* Reset the flags for node_level_post_processing */
        p_qtm_control->binding_layer_flags &= (uint8_t) ~(1u << node_pp_request);
    

    if (p_qtm_control->binding_layer_flags & (1u << reburst_request)) {
		time_to_measure_touch_var = 1;
        p_qtm_control->binding_layer_flags &= ~(1u << reburst_request);
		}
    }
#if KRONOCOMM_ENABLE == 1u
	uart_process();
#endif
}


/*============================================================================
void touch_timer_handler(void)
------------------------------------------------------------------------------
Purpose: This function updates the time elapsed to the touch key module to
         synchronize the internal time counts used by the module.
Input  : none
Output : none
Notes  :
============================================================================*/
void touch_timer_handler(void)
{
    /* Count complete - Measure touch sensors */
	time_to_measure_touch_var = 1;
    qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
}
void rtc_cb( RTC_TIMER32_INT_MASK intCause, uintptr_t context )
{
     touch_timer_handler();
}
uintptr_t rtc_context;

void touch_timer_config(void)
{  
	RTC_Timer32CallbackRegister(rtc_cb, rtc_context);
	RTC_Timer32Start();
	RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
}

uint16_t get_sensor_node_signal(uint16_t sensor_node)
{
    return (ptc_qtlib_node_stat1[sensor_node].node_acq_signals);
}

void update_sensor_node_signal(uint16_t sensor_node, uint16_t new_signal)
{
    ptc_qtlib_node_stat1[sensor_node].node_acq_signals = new_signal;
}

uint16_t get_sensor_node_reference(uint16_t sensor_node)
{
    return (qtlib_key_data_set1[sensor_node].channel_reference);
}

void update_sensor_node_reference(uint16_t sensor_node, uint16_t new_reference)
{
    qtlib_key_data_set1[sensor_node].channel_reference = new_reference;
}

uint16_t get_sensor_cc_val(uint16_t sensor_node)
{
    return (ptc_qtlib_node_stat1[sensor_node].node_comp_caps);
}

void update_sensor_cc_val(uint16_t sensor_node, uint16_t new_cc_value)
{
    ptc_qtlib_node_stat1[sensor_node].node_comp_caps = new_cc_value;
}

uint8_t get_sensor_state(uint16_t sensor_node)
{
    return (qtlib_key_set1.qtm_touch_key_data[sensor_node].sensor_state);
}

void update_sensor_state(uint16_t sensor_node, uint8_t new_state)
{
    qtlib_key_set1.qtm_touch_key_data[sensor_node].sensor_state = new_state;
}

void calibrate_node(uint16_t sensor_node)
{
    /* Calibrate Node */
    qtm_calibrate_sensor_node(&qtlib_acq_set1, sensor_node);
    /* Initialize key */
    qtm_init_sensor_key(&qtlib_key_set1, sensor_node, &ptc_qtlib_node_stat1[sensor_node]);
}



/*============================================================================
void PTC_Handler_EOC(void)
------------------------------------------------------------------------------
Purpose: Interrupt service handler for PTC EOC interrupt
Input  : none
Output : none
Notes  : none
============================================================================*/
void PTC_Handler(void)
{
	qtm_ptc_clear_interrupt();
	qtm_saml21_ptc_handler_eoc();
}
