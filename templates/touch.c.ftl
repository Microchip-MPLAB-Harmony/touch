/*******************************************************************************
  Touch Library ${REL_VER} Release

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
Copyright (c)  ${REL_YEAR} released Microchip Technology Inc.  All rights reserved.

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

<#if TOUCH_CHAN_ENABLE_CNT == 0>
#error "Number of Touch sensor is defined as ZERO. Include atleast one touch sensor or remove Touch library in MHC."
<#else>
<#import "/eventlowpower.ftl" as eventlp>
<#import "/softwarelowpower.ftl" as softwarelp>
<#assign sam_e5x_devices = ["SAME54","SAME53","SAME51","SAMD51"]>
<#assign sam_d2x_devices = ["SAMD21","SAMDA1","SAMD20","SAMHA1"]>
<#assign sam_d1x_devices = ["SAMD10","SAMD11"]>
<#assign sam_c2x_devices = ["SAMC21","SAMC20","PIC32CMJH01","PIC32CMJH00"]>
<#assign sam_l2x_devices = ["SAML21","SAML22"]>
<#assign sam_l1x_devices = ["SAML10","SAML11","SAML1xE"]>
<#assign pic32cm_le_devices = ["PIC32CMLE00","PIC32CMLS00","PIC32CMLS60"]>
<#assign pic_devices = ["PIC32MZW","PIC32MZDA","PIC32CXBZ31","WBZ35"]>
<#assign buckland = ["PIC32CXBZ31","WBZ35"]>
<#assign pic32cz = ["PIC32CZCA80", "PIC32CZCA90"]>
<#assign supc_devices = ["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00","PIC32CMLS60","PIC32CZCA80","PIC32CZCA90"]>
<#assign no_standby_devices = ["SAMD10","SAMD11"]>
<#assign no_standby_during_measurement = 0>
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if (DS_DEDICATED_ENABLE == true) || (DS_PLUS_ENABLE == true) || no_standby_devices?seq_contains(DEVICE_NAME)>
<#assign no_standby_during_measurement = 1>
</#if>
</#if>
<#assign num_of_channel_more_than_one = 0 >
<#if (TOUCH_CHAN_ENABLE_CNT > 1) >
<#assign num_of_channel_more_than_one = 1 >
</#if>

/*----------------------------------------------------------------------------
 *     include files
 *----------------------------------------------------------------------------*/
#include "definitions.h"
#include "touch/touch.h"
<#if ENABLE_TOUCH_TUNE_WITH_PLUGIN == true>
#include "touch/touchTune.h"
</#if>
<#if ENABLE_DATA_STREAMER == true>
#include "touch/datastreamer/datastreamer.h"
</#if>
<#if ENABLE_KRONOCOMM == true>
#include "touch/datastreamer/kronocommadaptor.h"
#include "touch/datastreamer/kronocommuart_sam.h"
</#if>
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if DS_DEDICATED_ENABLE == true || DS_PLUS_ENABLE == true>
#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)
#include "driven_shield.h"
extern qtm_drivenshield_config_t qtm_drivenshield_config;
#endif
</#if>
</#if>

/*----------------------------------------------------------------------------
 *   prototypes
 *----------------------------------------------------------------------------*/

/*! \brief configure keys, wheels and sliders.
 */
static touch_ret_t touch_sensors_config(void);

/*! \brief Touch measure complete callback function example prototype.
 */
static void qtm_measure_complete_callback(void);

/*! \brief Touch Error callback function prototype.
 */
static void qtm_error_callback(uint8_t error);

<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
<#if no_standby_during_measurement == 1>
uint8_t measurement_in_progress = 0u;
</#if>
/* low power processing function */
static void touch_process_lowpower(void);
static void touch_enable_lowpower_measurement(void);
static void touch_disable_lowpower_measurement(void);
<#if supc_devices?seq_contains(DEVICE_NAME)>
/* configure pm, supc */
static void touch_configure_pm_supc(void);
</#if>
<#if ENABLE_EVENT_LP?exists>
    <#if ENABLE_EVENT_LP == true>
/* low power touch detection callback */
static void touch_measure_wcomp_match(void);
    <#elseif ENABLE_EVENT_LP == false>
<#if num_of_channel_more_than_one == 1>
static void touch_seq_lp_sensor(void);
static void touch_enable_nonlp_sensors(void);
static void touch_disable_nonlp_sensors(void);
uint16_t time_drift_wakeup_counter;
</#if>
</#if>
<#else>
<#if sam_d1x_devices?seq_contains(DEVICE_NAME) || sam_e5x_devices?seq_contains(DEVICE_NAME)>
<#if num_of_channel_more_than_one == 1>
static void touch_seq_lp_sensor(void);
static void touch_enable_nonlp_sensors(void);
static void touch_disable_nonlp_sensors(void);
uint16_t time_drift_wakeup_counter;
</#if>
<#elseif sam_e5x_devices?seq_contains(DEVICE_NAME)>
static void touch_measure_wcomp_match(void);
</#if>
</#if>
#endif
</#if>

/*----------------------------------------------------------------------------
 *     Global Variables
 *----------------------------------------------------------------------------*/
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
    <#if ENABLE_EVENT_LP?exists >
        <#if ENABLE_EVENT_LP == false>
#if DEF_TOUCH_LOWPOWER_ENABLE == 1u
static uint8_t lp_measurement = 0u;
 <#if num_of_channel_more_than_one == 1>
#define get_lowpower_mask(x) lowpower_key_mask[x>>3]
uint8_t lowpower_key_mask[(DEF_NUM_CHANNELS+7)>>3] = {DEF_LOWPOWER_KEYS};
uint8_t current_lp_sensor = 0;
</#if>
#endif
        </#if>
    <#else>
        <#if sam_d1x_devices?seq_contains(DEVICE_NAME) || sam_e5x_devices?seq_contains(DEVICE_NAME)>
#if DEF_TOUCH_LOWPOWER_ENABLE == 1u
static uint8_t lp_measurement = 0u;
<#if num_of_channel_more_than_one == 1>
uint8_t current_lp_sensor = 0;
#define get_lowpower_mask(x) lowpower_key_mask[x>>3]
uint8_t lowpower_key_mask[(DEF_NUM_CHANNELS+7)>>3] = {DEF_LOWPOWER_KEYS};
</#if>
#endif
        </#if>
    </#if> 
</#if>

/* Flag to indicate time for touch measurement */
volatile uint8_t time_to_measure_touch_var = 0;
/* post-process request flag */
volatile uint8_t touch_postprocess_request = 0;

/* Measurement Done Touch Flag  */
volatile uint8_t measurement_done_touch = 0;
<#if pic_devices?seq_contains(DEVICE_NAME)>
static uint8_t all_measure_complete = 0;
</#if>

/* Error Handling */
uint8_t module_error_code = 0;


<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>  
/* Low-power measurement variables */
uint16_t time_since_touch = 0;
/* store the drift period for comparison */
uint16_t measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
/* measurement mode; 0 - sequential, 1 - windowcomp*/
static uint8_t measurement_mode = 0u; 
</#if>

/* Acquisition module internal data - Size to largest acquisition set */
<#if pic_devices?seq_contains(DEVICE_NAME)>
uint32_t touch_acq_signals_raw[DEF_NUM_CHANNELS];
/* Acquisition set 1 - General settings */
qtm_acq_node_group_config_t ptc_qtlib_acq_gen1
    = {DEF_NUM_CHANNELS, DEF_SENSOR_TYPE, DEF_PTC_CAL_AUTO_TUNE, DEF_SEL_FREQ_INIT, 1};
<#elseif pic32cz?seq_contains(DEVICE_NAME)>
uint16_t touch_acq_signals_raw[DEF_NUM_CHANNELS];
/* Acquisition set 1 - General settings */
qtm_acq_node_group_config_t ptc_qtlib_acq_gen1
    ={DEF_NUM_CHANNELS, DEF_SENSOR_TYPE, DEF_SEL_FREQ_INIT, DEF_PTC_INTERRUPT_PRIORITY, DEF_PTC_WAKEUP_EXP};
<#else>
uint16_t touch_acq_signals_raw[DEF_NUM_CHANNELS];
/* Acquisition set 1 - General settings */
qtm_acq_node_group_config_t ptc_qtlib_acq_gen1
    = {DEF_NUM_CHANNELS, DEF_SENSOR_TYPE, DEF_PTC_CAL_AUTO_TUNE, DEF_SEL_FREQ_INIT, DEF_PTC_INTERRUPT_PRIORITY};
</#if>

/* Node status, signal, calibration values */
qtm_acq_node_data_t ptc_qtlib_node_stat1[DEF_NUM_CHANNELS];

/* Node configurations */
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
<#if DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00" || DEVICE_NAME=="PIC32CMLS60">
qtm_acq_4p_pic32cm_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS >> 2] = {<#list 0..MUTL_4P_NUM_GROUP-1 as i><#if i==MUTL_4P_NUM_GROUP-1>GRP_${i}_4P_PARAMS<#else>GRP_${i}_4P_PARAMS,</#if></#list>};
<#else>
qtm_acq_4p_${DEVICE_NAME?lower_case}_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS >> 2] = {<#list 0..MUTL_4P_NUM_GROUP-1 as i><#if i==MUTL_4P_NUM_GROUP-1>GRP_${i}_4P_PARAMS<#else>GRP_${i}_4P_PARAMS,</#if></#list>};
</#if>
<#else>
<#if TOUCH_CHAN_ENABLE_CNT&gt;=1>
<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
qtm_acq_samd1x_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
<#elseif DEVICE_NAME== "SAML11" || DEVICE_NAME== "SAML1xE">
qtm_acq_saml10_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
<#elseif  DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00" || DEVICE_NAME=="PIC32CMLS60">
qtm_acq_pic32cm_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
<#elseif  DEVICE_NAME =="PIC32CMJH00" || DEVICE_NAME=="PIC32CMJH01">
qtm_acq_pic32cmjh_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
<#elseif  DEVICE_NAME =="PIC32CXBZ31" || DEVICE_NAME=="WBZ35">
qtm_acq_pic32cx_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
<#elseif  DEVICE_NAME =="PIC32CZCA80"||DEVICE_NAME =="PIC32CZCA90">
qtm_acq_pic32czca_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
<#else>
qtm_acq_${DEVICE_NAME?lower_case}_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] = {<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i><#if i==TOUCH_CHAN_ENABLE_CNT-1>NODE_${i}_PARAMS<#else>NODE_${i}_PARAMS,</#if></#list>};
</#if>
<#else>
/* Node configurations */
qtm_acq_${DEVICE_NAME?lower_case}_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
</#if>
</#if>

/* Container */
qtm_acquisition_control_t qtlib_acq_set1 = {&ptc_qtlib_acq_gen1, &ptc_seq_node_cfg1[0], &ptc_qtlib_node_stat1[0]};

<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
<#if ENABLE_SURFACE == true>
touch_ret_t touch_surface_4p_acq_to_key(void * ptr);
touch_ret_t touch_surface_4p_key_to_acq_update(void *ptr);
/* extra array to store the consolidated row, cloumn signal and status value */
qtm_acq_node_data_t ptc_qtlib_node_stat1_4p_sur[SURFACE_CS_NUM_KEYS_H + SURFACE_CS_NUM_KEYS_V];

/* map node to key */
uint8_t touch_key_node_mapping_4p[SURFACE_CS_START_KEY_V+SURFACE_CS_NUM_KEYS_V*SURFACE_CS_NUM_KEYS_H] = {${.vars["MUTL_4P_NODE_KEY_MAP"]}};
<#else>
/* map node to key */
uint8_t touch_key_node_mapping_4p[DEF_NUM_SENSORS] = {${.vars["MUTL_4P_NODE_KEY_MAP"]}};
</#if>
</#if>
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
<#if ENABLE_EVENT_LP?exists&& ENABLE_EVENT_LP == true> 
<@eventlp.lowpower_acq_param/>
</#if>
</#if>
<#if ((ENABLE_FREQ_HOP==true) && (FREQ_AUTOTUNE!=true))>
/**********************************************************/
/*********** Frequency Hop Module **********************/
/**********************************************************/

/* Buffer used with various noise filtering functions */
uint16_t noise_filter_buffer[DEF_NUM_CHANNELS * NUM_FREQ_STEPS];
uint8_t  freq_hop_delay_selection[NUM_FREQ_STEPS] = {DEF_MEDIAN_FILTER_FREQUENCIES};

/* Configuration */
qtm_freq_hop_config_t qtm_freq_hop_config1 = {
    DEF_NUM_CHANNELS,
    NUM_FREQ_STEPS,
    &ptc_qtlib_acq_gen1.freq_option_select,
    &freq_hop_delay_selection[0],
};

/* Data */
qtm_freq_hop_data_t qtm_freq_hop_data1 = {0, 0, &noise_filter_buffer[0], &ptc_qtlib_node_stat1[0]};

/* Container */
qtm_freq_hop_control_t qtm_freq_hop_control1 = {&qtm_freq_hop_data1, &qtm_freq_hop_config1};

<#elseif ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE==true>
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

</#if>
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

<#if TOUCH_KEY_ENABLE_CNT&gt;=1>
/* Key Configurations */
qtm_touch_key_config_t qtlib_key_configs_set1[DEF_NUM_SENSORS] = {<#list 0..TOUCH_KEY_ENABLE_CNT-1 as i><#if i==TOUCH_KEY_ENABLE_CNT-1>KEY_${i}_PARAMS<#else> KEY_${i}_PARAMS,</#if></#list>}; 
<#else>
/* Key Configurations */
qtm_touch_key_config_t qtlib_key_configs_set1[DEF_NUM_SENSORS];
</#if>
/* Container */
qtm_touch_key_control_t qtlib_key_set1
    = {&qtlib_key_grp_data_set1, &qtlib_key_grp_config_set1, &qtlib_key_data_set1[0], &qtlib_key_configs_set1[0]};

<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
/**********************************************************/
/***************** Scroller Module ********************/
/**********************************************************/

/* Individual and Group Data */
qtm_scroller_data_t       qtm_scroller_data1[DEF_NUM_SCROLLERS];
qtm_scroller_group_data_t qtm_scroller_group_data1 = {0};

/* Group Configuration */
qtm_scroller_group_config_t qtm_scroller_group_config1 = {&qtlib_key_data_set1[0], DEF_NUM_SCROLLERS};

<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
/* Scroller Configurations */
qtm_scroller_config_t qtm_scroller_config1[DEF_NUM_SCROLLERS] = {<#list 0..TOUCH_SCROLLER_ENABLE_CNT-1 as i><#if i==TOUCH_SCROLLER_ENABLE_CNT-1>SCROLLER_${i}_PARAMS<#else> SCROLLER_${i}_PARAMS,</#if></#list>}; 
</#if>

/* Container */
qtm_scroller_control_t qtm_scroller_control1
    = {&qtm_scroller_group_data1, &qtm_scroller_group_config1, &qtm_scroller_data1[0], &qtm_scroller_config1[0]};
</#if>
</#if>
<#if ENABLE_SURFACE1T?exists && ENABLE_SURFACE1T== true>
/**********************************************************/
/***************** Surface 1t Module ********************/
/**********************************************************/

qtm_surface_cs_config_t qtm_surface_cs_config1 = {
    /* Config: */
    SURFACE_CS_START_KEY_H,
    SURFACE_CS_NUM_KEYS_H,
    SURFACE_CS_START_KEY_V,
    SURFACE_CS_NUM_KEYS_V,
    SURFACE_CS_RESOL_DB,
    SURFACE_CS_POS_HYST,
    SURFACE_CS_FILT_CFG,
    SURFACE_CS_MIN_CONTACT,
    &qtlib_key_data_set1[0]};

/* Surface Data */
qtm_surface_contact_data_t qtm_surface_cs_data1;

/* Container */
qtm_surface_cs_control_t qtm_surface_cs_control1 = {&qtm_surface_cs_data1, &qtm_surface_cs_config1};
</#if>

<#if ENABLE_SURFACE2T?exists && ENABLE_SURFACE2T== true>
/**********************************************************/
/***************** Surface 2t Module ********************/
/**********************************************************/

qtm_surface_cs_config_t qtm_surface_cs_config1 = {
    /* Config: */
    SURFACE_CS_START_KEY_H,
    SURFACE_CS_NUM_KEYS_H,
    SURFACE_CS_START_KEY_V,
    SURFACE_CS_NUM_KEYS_V,
    SURFACE_CS_RESOL_DB,
    SURFACE_CS_POS_HYST,
    SURFACE_CS_FILT_CFG,
    SURFACE_CS_MIN_CONTACT,
    &qtlib_key_data_set1[0]};

/* surface Configurations */
/* Surface Data */
qtm_surface_cs2t_data_t qtm_surface_cs_data1;

/* Contact Data */
qtm_surface_contact_data_t qtm_surface_contacts[2];

/* Container */
qtm_surface_cs2t_control_t qtm_surface_cs_control1
    = {&qtm_surface_cs_data1, &qtm_surface_contacts[0], &qtm_surface_cs_config1};
</#if>

<#if ENABLE_GESTURE==true>
/**********************************************************/
/***************** Gesture Module ********************/
/**********************************************************/

/* Gesture Configurations */
<#if ENABLE_SURFACE2T==true>
qtm_gestures_2d_config_t qtm_gestures_2d_config = {&qtm_surface_contacts[0].h_position,
                                                   &qtm_surface_contacts[0].v_position,
                                                   &qtm_surface_contacts[0].qt_contact_status,
                                                   &qtm_surface_contacts[1].h_position,
                                                   &qtm_surface_contacts[1].v_position,
                                                   &qtm_surface_contacts[1].qt_contact_status,
                                                   SCR_RESOLUTION(SURFACE_CS_RESOL_DB),
                                                   TAP_RELEASE_TIMEOUT,
                                                   TAP_HOLD_TIMEOUT,
                                                   SWIPE_TIMEOUT,
                                                   HORIZONTAL_SWIPE_DISTANCE_THRESHOLD,
                                                   VERTICAL_SWIPE_DISTANCE_THRESHOLD,
                                                   0,
                                                   TAP_AREA,
                                                   SEQ_TAP_DIST_THRESHOLD,
                                                   EDGE_BOUNDARY,
                                                   WHEEL_POSTSCALER,
                                                   WHEEL_START_QUADRANT_COUNT,
                                                   WHEEL_REVERSE_QUADRANT_COUNT,

                                                   PINCH_ZOOM_THRESHOLD

};
<#elseif ENABLE_SURFACE1T==true>
qtm_gestures_2d_config_t qtm_gestures_2d_config = {&qtm_surface_cs_data1.h_position,
                                                   &qtm_surface_cs_data1.v_position,
                                                   &qtm_surface_cs_data1.qt_surface_status,
                                                   0,
                                                   0,
                                                   0,
                                                   SCR_RESOLUTION(SURFACE_CS_RESOL_DB),
                                                   TAP_RELEASE_TIMEOUT,
                                                   TAP_HOLD_TIMEOUT,
                                                   SWIPE_TIMEOUT,
                                                   HORIZONTAL_SWIPE_DISTANCE_THRESHOLD,
                                                   VERTICAL_SWIPE_DISTANCE_THRESHOLD,
                                                   0,
                                                   TAP_AREA,
                                                   SEQ_TAP_DIST_THRESHOLD,
                                                   EDGE_BOUNDARY,
                                                   WHEEL_POSTSCALER,
                                                   WHEEL_START_QUADRANT_COUNT,
                                                   WHEEL_REVERSE_QUADRANT_COUNT,
                                                   0
};
</#if>
qtm_gestures_2d_data_t qtm_gestures_2d_data;

qtm_gestures_2d_control_t qtm_gestures_2d_control1 = {&qtm_gestures_2d_data, &qtm_gestures_2d_config};
</#if>

/*----------------------------------------------------------------------------
 *   function definitions
 *----------------------------------------------------------------------------*/

<#if ENABLE_BOOST?exists && ENABLE_BOOST == true && ENABLE_SURFACE == true >
/*============================================================================
touch_ret_t touch_surface_4p_acq_to_key(void * ptr)
------------------------------------------------------------------------------
Purpose: from vertical*horizontal nodes, make vertical+horizontal to make it
         compatible with surface module
Input  : none
Output : none
Notes  :
============================================================================*/
touch_ret_t touch_surface_4p_acq_to_key(void * ptr)
{
	uint32_t    sum_signal = 0, comp_cap = 0;
	uint8_t     status  = 0;
	touch_ret_t ret_var = TOUCH_SUCCESS;

	/*compute vertical node signal, compcap and status */
	for (uint16_t cnt = 0; cnt < SURFACE_CS_NUM_KEYS_V; cnt++) {
		sum_signal = 0;
		comp_cap   = 0;
		status     = 0;
		for (uint16_t cnt1 = 0; cnt1 < SURFACE_CS_NUM_KEYS_H; cnt1++) {
			sum_signal
			    += ptc_qtlib_node_stat1[touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_H + cnt1 + SURFACE_CS_START_KEY_V]].node_acq_signals;
			comp_cap
			    += ptc_qtlib_node_stat1[touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_H + cnt1 + SURFACE_CS_START_KEY_V]].node_comp_caps;
			status
			    |= ptc_qtlib_node_stat1[touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_H + cnt1 + SURFACE_CS_START_KEY_V]].node_acq_status;
		}
		ptc_qtlib_node_stat1_4p_sur[cnt].node_acq_signals = sum_signal / SURFACE_CS_NUM_KEYS_H;
		ptc_qtlib_node_stat1_4p_sur[cnt].node_comp_caps   = comp_cap;
		ptc_qtlib_node_stat1_4p_sur[cnt].node_acq_status  = status;
	}

	/*compute horizontal node signal, compcap and status */
	for (uint16_t cnt1 = 0; cnt1 < SURFACE_CS_NUM_KEYS_H; cnt1++) {
		sum_signal = 0;
		comp_cap   = 0;
		status     = 0;
		for (uint16_t cnt = 0; cnt < SURFACE_CS_NUM_KEYS_V; cnt++) {
			sum_signal
			    += ptc_qtlib_node_stat1[touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_V + cnt1 + SURFACE_CS_START_KEY_V]].node_acq_signals;
			comp_cap
			    += ptc_qtlib_node_stat1[touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_V + cnt1 + SURFACE_CS_START_KEY_V]].node_comp_caps;
			status
			    |= ptc_qtlib_node_stat1[touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_V + cnt1 + SURFACE_CS_START_KEY_V]].node_acq_status;
		}
		ptc_qtlib_node_stat1_4p_sur[cnt1 + SURFACE_CS_NUM_KEYS_V].node_acq_signals
		= sum_signal / SURFACE_CS_NUM_KEYS_V;
		ptc_qtlib_node_stat1_4p_sur[cnt1 + SURFACE_CS_NUM_KEYS_V].node_comp_caps  = comp_cap;
		ptc_qtlib_node_stat1_4p_sur[cnt1 + SURFACE_CS_NUM_KEYS_V].node_acq_status = status;
	}

	return ret_var;
}

/*============================================================================
touch_ret_t touch_surface_4p_key_to_acq_update(void * ptr)
------------------------------------------------------------------------------
Purpose: depends on key's module reburst,calibration request, update 4P nodes
Input  : none
Output : none
Notes  :
============================================================================*/
touch_ret_t touch_surface_4p_key_to_acq_update(void * ptr)
{
	uint16_t temp_cnt = 0, calib_flag = 0;
	touch_ret_t ret_var = TOUCH_SUCCESS;

	for(uint16_t cnt = 0; cnt < (SURFACE_CS_NUM_KEYS_V+SURFACE_CS_NUM_KEYS_H); cnt++)	{
		if(ptc_qtlib_node_stat1_4p_sur[cnt].node_acq_status & NODE_CAL_REQ) {
			calib_flag = 1;
			break;
		}
	}

	if(calib_flag == 1)	{
		for(uint16_t cnt = 0; cnt < (SURFACE_CS_NUM_KEYS_V+SURFACE_CS_NUM_KEYS_H); cnt++) {
			qtm_init_sensor_key(
			&qtlib_key_set1, cnt + SURFACE_CS_START_KEY_V, &ptc_qtlib_node_stat1_4p_sur[cnt]);

			if(cnt < SURFACE_CS_NUM_KEYS_V) {
				for(uint16_t hor_cnt = 0; hor_cnt < SURFACE_CS_NUM_KEYS_H; hor_cnt++){
					temp_cnt = touch_key_node_mapping_4p[cnt*SURFACE_CS_NUM_KEYS_H+hor_cnt];
					qtm_calibrate_sensor_node(&qtlib_acq_set1, temp_cnt);
				}
			}
			else {
				for(uint16_t ver_cnt = 0; ver_cnt < SURFACE_CS_NUM_KEYS_V; ver_cnt++) {
					temp_cnt = touch_key_node_mapping_4p[ver_cnt*SURFACE_CS_NUM_KEYS_V+(cnt - SURFACE_CS_NUM_KEYS_V)];
					qtm_calibrate_sensor_node(&qtlib_acq_set1, temp_cnt);
				}
			}
			ptc_qtlib_node_stat1_4p_sur[cnt].node_acq_status &= ~(NODE_CAL_REQ);
		}
	}
	return ret_var;
}
</#if>

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

    /* Init acquisition module */
<#if pic_devices?seq_contains(DEVICE_NAME)>
    qtm_cvd_init_acquisition_module(&qtlib_acq_set1);
    qtm_cvd_qtlib_assign_signal_memory(&touch_acq_signals_raw[0]);
<#else>
    qtm_ptc_init_acquisition_module(&qtlib_acq_set1);
    qtm_ptc_qtlib_assign_signal_memory(&touch_acq_signals_raw[0]);
</#if>

    /* Initialize sensor nodes */
    for (sensor_nodes = 0u; sensor_nodes < DEF_NUM_CHANNELS; sensor_nodes++) {
        /* Enable each node for measurement and mark for calibration */
        qtm_enable_sensor_node(&qtlib_acq_set1, sensor_nodes);
        qtm_calibrate_sensor_node(&qtlib_acq_set1, sensor_nodes);
    }


<#if ENABLE_BOOST?exists && ENABLE_BOOST == true && ENABLE_SURFACE == true>
		/* Enable sensor keys and assign nodes */
		for(sensor_nodes = 0u; sensor_nodes < SURFACE_CS_START_KEY_V; sensor_nodes++)
		{
			qtm_init_sensor_key(&qtlib_key_set1, sensor_nodes, &ptc_qtlib_node_stat1[touch_key_node_mapping_4p[sensor_nodes]]);
		}
		/* For surface sensor configure separately */
		for (sensor_nodes = 0u; sensor_nodes < SURFACE_CS_NUM_KEYS_V+SURFACE_CS_NUM_KEYS_H; sensor_nodes++) {
			qtm_init_sensor_key(
			&qtlib_key_set1, sensor_nodes + SURFACE_CS_START_KEY_V, &ptc_qtlib_node_stat1_4p_sur[sensor_nodes]);
		}
<#else>
    /* Enable sensor keys and assign nodes */
    for (sensor_nodes = 0u; sensor_nodes < DEF_NUM_SENSORS; sensor_nodes++) {
		<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
			qtm_init_sensor_key(&qtlib_key_set1, sensor_nodes, &ptc_qtlib_node_stat1[touch_key_node_mapping_4p[sensor_nodes]]);
    <#else>
			qtm_init_sensor_key(&qtlib_key_set1, sensor_nodes, &ptc_qtlib_node_stat1[sensor_nodes]);
		</#if>
    }
</#if>

<#if ENABLE_SCROLLER?exists && ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>	
	/* scroller init */
	touch_ret |= qtm_init_scroller_module(&qtm_scroller_control1);
</#if>
</#if>

<#if ENABLE_SURFACE1T?exists && ENABLE_SURFACE1T== true>	
	touch_ret |= qtm_init_surface_cs(&qtm_surface_cs_control1);
</#if>
<#if ENABLE_SURFACE2T?exists && ENABLE_SURFACE2T== true>	
	touch_ret |= qtm_init_surface_cs2t(&qtm_surface_cs_control1);
</#if>
<#if ENABLE_GESTURE?exists && ENABLE_GESTURE==true>	
	touch_ret |= qtm_init_gestures_2d();
</#if>

    return (touch_ret);
}

/*============================================================================
static void qtm_measure_complete_callback( void )
------------------------------------------------------------------------------
Purpose: Callback function called after the completion of
         measurement cycle. This function sets the post processing request
         flag to trigger the post processing.
Input  : none
Output : none
Notes  :
============================================================================*/
static void qtm_measure_complete_callback(void)
{
    touch_postprocess_request = 1u;
<#if pic_devices?seq_contains(DEVICE_NAME)>
	all_measure_complete = 1;
</#if>
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
<#if no_standby_during_measurement == 1>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
<#if DEVICE_NAME == "SAMD10" || DEVICE_NAME == "SAMD11" >
    qtm_autoscan_node_cancel(); /* disable PTC */
</#if>
measurement_in_progress = 0;
#endif
</#if>
</#if>
}

/*============================================================================
static void qtm_error_callback(uint8_t error)
------------------------------------------------------------------------------
Purpose: Callback function called after the completion of
         post processing. This function is called only when there is error.
Input  : error code
Output : decoded module error code
Notes  :
Derived Module_error_codes:
    Acquisition module error =1
    post processing module1 error = 2
    post processing module2 error = 3
    ... and so on

============================================================================*/
static void qtm_error_callback(uint8_t error)
{
	module_error_code = error + 1u;

<#if ENABLE_DATA_STREAMER == true>
	#if DEF_TOUCH_DATA_STREAMER_ENABLE == 1
	    datastreamer_output();
	#endif
</#if>
}

/*============================================================================
void touch_init(void)
------------------------------------------------------------------------------
Purpose: Initialization of touch library. PTC, timer, and
         datastreamer modules are initialized in this function.
Input  : none
Output : none
Notes  :
============================================================================*/
void touch_init(void)
{
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
	touch_timer_config();
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
<#if supc_devices?seq_contains(DEVICE_NAME)>
	/* configure voltage regulator to run in standby sleep mode */
	touch_configure_pm_supc();
</#if>
	touch_disable_lowpower_measurement();
#endif
<#else>
	touch_timer_config();
</#if>

	/* Configure touch sensors with Application specific settings */
	touch_sensors_config();

<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if DS_DEDICATED_ENABLE == true || DS_PLUS_ENABLE == true>
#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)
	drivenshield_configure();
#endif
</#if>
</#if>
	
<#if ENABLE_DATA_STREAMER == true>	
#if DEF_TOUCH_DATA_STREAMER_ENABLE == 1
	datastreamer_init();
#endif
</#if>

<#if ENABLE_TOUCH_TUNE_WITH_PLUGIN == true>
    #if DEF_TOUCH_TUNE_ENABLE == 1u
    touchTuneInit();
    #endif
</#if>
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
void touch_process(void)
{
    touch_ret_t touch_ret;
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == true> 
<#else>
<#if num_of_channel_more_than_one == 1>
#if DEF_TOUCH_DRIFT_PERIOD_MS != 0u && DEF_TOUCH_LOWPOWER_ENABLE == 1u
	if ((time_drift_wakeup_counter >= DEF_TOUCH_DRIFT_PERIOD_MS) && (measurement_period_store != DEF_TOUCH_MEASUREMENT_PERIOD_MS)) {
		time_drift_wakeup_counter = 0u;
		touch_enable_nonlp_sensors();
	}
#endif
</#if>
</#if>
</#if>

    /* check the time_to_measure_touch for Touch Acquisition */
    if (time_to_measure_touch_var == 1u) {

        /* Do the acquisition */
        <#if pic_devices?seq_contains(DEVICE_NAME)>
        touch_ret = qtm_cvd_start_measurement_seq(&qtlib_acq_set1, qtm_measure_complete_callback);
        <#else>
         touch_ret = qtm_ptc_start_measurement_seq(&qtlib_acq_set1, qtm_measure_complete_callback);
         </#if>

        /* if the Acquistion request was successful then clear the request flag */
        if (TOUCH_SUCCESS == touch_ret) {
            /* Clear the Measure request flag */
			time_to_measure_touch_var = 0;
            <#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
            <#if no_standby_during_measurement == 1>
            #if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
            measurement_in_progress = 1;
            #endif
            </#if>
            </#if>
<#if pic_devices?seq_contains(DEVICE_NAME)>
			all_measure_complete = 0;
</#if>
        }
    }
    /* check the flag for node level post processing */
    if (touch_postprocess_request == 1u){
        /* Reset the flags for node_level_post_processing */
        touch_postprocess_request = 0u;
        /* Run Acquisition module level post processing*/
        touch_ret = qtm_acquisition_process();
        /* Check the return value */
        if (TOUCH_SUCCESS == touch_ret) {
            /* Returned with success: Start module level post processing */
<#assign i = 1><#if ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE!=true>
            touch_ret = qtm_freq_hop(&qtm_freq_hop_control1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if><#if ENABLE_FREQ_HOP==true && FREQ_AUTOTUNE==true>
            touch_ret = qtm_freq_hop_autotune(&qtm_freq_hop_autotune_control1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
        }</#if>
            touch_ret = qtm_key_sensors_process(&qtlib_key_set1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
            <#assign i =i+1>}<#if ENABLE_BOOST?exists && ENABLE_BOOST==true && ENABLE_SURFACE == true>
            touch_ret = touch_surface_4p_acq_to_key(&qtlib_key_set1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if><#if ENABLE_BOOST?exists && ENABLE_BOOST==true && ENABLE_SURFACE == true>
            touch_ret = touch_surface_4p_key_to_acq_update(&qtlib_key_set1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if><#if ENABLE_SCROLLER?exists && ENABLE_SCROLLER == true><#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
            touch_ret = qtm_scroller_process(&qtm_scroller_control1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if></#if><#if ENABLE_SURFACE1T?exists && ENABLE_SURFACE1T== true>
            touch_ret = qtm_surface_cs_process(&qtm_surface_cs_control1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if><#if ENABLE_SURFACE2T?exists && ENABLE_SURFACE2T== true>
            touch_ret = qtm_surface_cs2t_process(&qtm_surface_cs_control1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if><#if ENABLE_GESTURE?exists && ENABLE_GESTURE==true>
            touch_ret = qtm_gestures_2d_process(&qtm_gestures_2d_control1);
            if (TOUCH_SUCCESS != touch_ret) {
                qtm_error_callback(${i});
<#assign i =i+1>
            }</#if>
<#assign i =0>
         }else {
           /* Acq module Error Detected: Issue an Acq module common error code 0x80 */
            qtm_error_callback(0);
        }

        <#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
        #if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
        if (0u != (qtlib_key_grp_data_set1.qtm_keys_status & QTM_KEY_DETECT)) {
            /* Something in detect */
            time_since_touch = 0u;
        }
        #endif
        </#if>

        <#if ENABLE_TOUCH_TUNE_WITH_PLUGIN = true>
        #if DEF_TOUCH_TUNE_ENABLE == 1u
        touchTuneNewDataAvailable();
        #endif
        </#if>

        if (0u != (qtlib_key_set1.qtm_touch_key_group_data->qtm_keys_status & QTM_KEY_REBURST)) {
            time_to_measure_touch_var = 1u;
        } else {
            measurement_done_touch =1u;
            <#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
            #if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
            /* process lowpower touch measurement */
            touch_process_lowpower();
            #endif
            </#if>
        }
        <#if ENABLE_KRONOCOMM == true>
        #if KRONOCOMM_ENABLE == 1u
            Krono_UpdateBuffer();
        #endif
        </#if>
        <#if ENABLE_DATA_STREAMER == true>
            #if DEF_TOUCH_DATA_STREAMER_ENABLE == 1
                datastreamer_output();
            #endif
        </#if>
    }
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
	if ((time_to_measure_touch_var != 1u) && 
        (measurement_mode == 1u) ){
		PM_StandbyModeEnter();   
	}
#endif
<#if ENABLE_KRONOCOMM == true>
#if KRONOCOMM_ENABLE == 1u
    uart_process();
#endif
</#if>
<#if ENABLE_TOUCH_TUNE_WITH_PLUGIN == true>
    #if DEF_TOUCH_TUNE_ENABLE == 1u
    touchTuneProcess();
    #endif
</#if>
}
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
    <#if (DEVICE_NAME == "SAML10")||(DEVICE_NAME == "SAML11")||(DEVICE_NAME == "SAML1xE")>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
static void touch_configure_pm_supc(void)
{
    /* Configure PM */
    PM_REGS->PM_STDBYCFG = PM_STDBYCFG_BBIASHS_Msk| PM_STDBYCFG_VREGSMOD(0)| PM_STDBYCFG_DPGPDSW_Msk| PM_STDBYCFG_BBIASTR_Msk;

    PM_ConfigurePerformanceLevel(PM_PLCFG_PLSEL_PL0);

    /* Configure VREG. Mask the values loaded from NVM during reset.*/
    SUPC_REGS->SUPC_VREG = SUPC_VREG_ENABLE_Msk | SUPC_VREG_SEL_BUCK | SUPC_VREG_RUNSTDBY_Msk | SUPC_VREG_VSVSTEP(0) | SUPC_VREG_VSPER(0) | SUPC_VREG_STDBYPL0_Msk;

}
#endif
    <#elseif ((DEVICE_NAME == "PIC32CMLE00")||(DEVICE_NAME == "PIC32CMLS00")|| (DEVICE_NAME=="PIC32CMLS60"))>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
static void touch_configure_pm_supc(void)
{
    /* Configure PM */
    PM_REGS->PM_STDBYCFG = PM_STDBYCFG_BBIASHS_Msk| PM_STDBYCFG_VREGSMOD(2)| PM_STDBYCFG_DPGPDSW_Msk| PM_STDBYCFG_BBIASTR_Msk;

    while(PM_ConfigurePerformanceLevel(PM_PLCFG_PLSEL_PL0) != true);

    /* Configure VREG. Mask the values loaded from NVM during reset.*/
    SUPC_REGS->SUPC_VREG = SUPC_VREG_ENABLE_Msk | SUPC_VREG_SEL_BUCK | SUPC_VREG_RUNSTDBY_Msk | SUPC_VREG_VSVSTEP(0) | SUPC_VREG_VSPER(0) | SUPC_VREG_STDBYPL0_Msk;
}
#endif
    <#elseif ((DEVICE_NAME == "PIC32CZCA80")||(DEVICE_NAME == "PIC32CZCA90"))>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
static void touch_configure_pm_supc(void)
{
    /* 
     * Enable Analog Input Charge Pump of PTC , for weak VDD 
     */
    SUPC_REGS->SUPC_VREGCTRL |= SUPC_VREGCTRL_CPEN(1u << 2u);
}
#endif
</#if>
</#if>
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 

#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
/*============================================================================
static void touch_disable_lowpower_measurement(void)
------------------------------------------------------------------------------
Purpose: 
Input  : none
Output : none
Notes  :
============================================================================*/
static void touch_disable_lowpower_measurement(void)
{
<#if sam_l1x_devices?seq_contains(DEVICE_NAME) || pic32cm_le_devices?seq_contains(DEVICE_NAME)>
    <#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
    lp_measurement = 0;
    <@softwarelp.lowpwer_disableevsys_saml_no_evs/>
    <#else>
    <@eventlp.lowpwer_disable_saml_evsys/>
    </#if>
</#if>
<#if sam_d2x_devices?seq_contains(DEVICE_NAME)>
    <#if ENABLE_EVENT_LP?exists &&ENABLE_EVENT_LP == false>
    lp_measurement = 0;
    <@softwarelp.lowpwer_disableevsys_samd20_d21_no_evs/>
    <#else>
    <@eventlp.lowpwer_disableevsys_samd20_d21/>
    </#if>
</#if>
<#if sam_c2x_devices?seq_contains(DEVICE_NAME)>
    <#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
    lp_measurement = 0;
    <@softwarelp.lowpwer_disable_samc20_c21_no_evs/>
    <#else>
    <@eventlp.lowpwer_disable_samc20_c21_evsys/>
    </#if>
</#if>
<#if sam_l2x_devices?seq_contains(DEVICE_NAME)>
	<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == true>
    <@eventlp.lowpwer_disable_saml21_l22_evsys/>
    <#else>
    lp_measurement = 0;
	<@softwarelp.lowpwer_disable_saml21_l22_no_evs/>
	</#if>
</#if>
<#if sam_d1x_devices?seq_contains(DEVICE_NAME)>
    lp_measurement = 0;
    <@softwarelp.lowpwer_disable_samd1x_no_evs/>
    </#if>
<#if sam_e5x_devices?seq_contains(DEVICE_NAME)>
    <@softwarelp.lowpwer_disable_same5x_no_evs/>
</#if>
<#if pic32cz?seq_contains(DEVICE_NAME)>
    <#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
    lp_measurement = 0;
    <@softwarelp.lowpwer_disableevsys_saml_no_evs/>
    <#else>
    <@eventlp.lowpwer_disable_pic32cz_evsys/>
    </#if>
</#if>
}

/*============================================================================
static void touch_enable_lowpower_measurement(void)
------------------------------------------------------------------------------
Purpose: 
Input  : none
Output : none
Notes  :
============================================================================*/
static void touch_enable_lowpower_measurement(void)
{
<#if sam_l1x_devices?seq_contains(DEVICE_NAME) || pic32cm_le_devices?seq_contains(DEVICE_NAME)>
	<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
    <#if num_of_channel_more_than_one == 1>
	time_drift_wakeup_counter = 0;
    </#if>
    lp_measurement = 1u;
	<@softwarelp.lowpwer_enableevsys_saml_no_evs/>
	<#else>
	<@eventlp.lowpwer_enable_saml_evsys/>
	</#if>
</#if>
<#if sam_d2x_devices?seq_contains(DEVICE_NAME)>
	<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
    lp_measurement = 1;
	<@softwarelp.lowpwer_enableevsys_samd20_d21_no_evs/>
	<#else>
	<@eventlp.lowpwer_enableevsys_samd20_d21/>
	</#if>
</#if>
<#if sam_c2x_devices?seq_contains(DEVICE_NAME)>
	<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
	    lp_measurement = 1;
	<@softwarelp.lowpwer_enable_samc20_c21_no_evs/>
	<#else>
	<@eventlp.lowpwer_enable_samc20_c21_evsys/>
	</#if>
</#if>
<#if sam_l2x_devices?seq_contains(DEVICE_NAME)>
	<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == true>
    <@eventlp.lowpwer_enable_saml21_l22_evsys />
	<#else>
    lp_measurement = 1;
	<@softwarelp.lowpwer_enable_saml21_l22_no_evs/>
    </#if>
</#if>
<#if sam_d1x_devices?seq_contains(DEVICE_NAME)>
    lp_measurement = 1;
	<@softwarelp.lowpwer_enable_samd1x_no_evs/>
    </#if>
<#if sam_e5x_devices?seq_contains(DEVICE_NAME)>
    <@softwarelp.lowpwer_enable_same5x_no_evs/>
</#if>
<#if pic32cz?seq_contains(DEVICE_NAME)>
	<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false>
    lp_measurement = 1u;
	<@softwarelp.lowpwer_enableevsys_saml_no_evs/>
	<#else>
	<@eventlp.lowpwer_enable_pic32cz_evsys/>
	</#if>
</#if>
}

<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>  
/*============================================================================
static void touch_process_lowpower(void)
------------------------------------------------------------------------------
Purpose: Processing function for low-power touch measurment.
         Monitors the touch activity and if there is not touch for longer
         duration, low-power autoscan is enabled.
Input  : none
Output : none
Notes  :
============================================================================*/
static void touch_process_lowpower(void) {
       touch_ret_t touch_ret;
<#if ENABLE_EVENT_LP?exists>
	<#if ENABLE_EVENT_LP == true>
    if (time_since_touch >= DEF_TOUCH_TIMEOUT) {
    
		/* Start Autoscan */
		touch_ret = qtm_autoscan_sensor_node(&auto_scan_setup, touch_measure_wcomp_match);

        if ((touch_ret == TOUCH_SUCCESS) && (measurement_period_store != DEF_TOUCH_DRIFT_PERIOD_MS)){

            /* Enable Event System */
            touch_enable_lowpower_measurement();
        }
    } else if (measurement_period_store != DEF_TOUCH_MEASUREMENT_PERIOD_MS) {

        /* Cancel node auto scan */
        qtm_autoscan_node_cancel();

        /* disable event system low-power measurement */
        touch_disable_lowpower_measurement();
    }
}
    <#elseif ENABLE_EVENT_LP == false>
    if (time_since_touch >= DEF_TOUCH_TIMEOUT) {
        <#if num_of_channel_more_than_one == 1>
		touch_disable_nonlp_sensors();
        </#if>
        if (measurement_period_store != QTM_LOWPOWER_TRIGGER_PERIOD) {
            touch_enable_lowpower_measurement();
        }
        <#if num_of_channel_more_than_one == 1>
        if(lp_measurement) {
            if(get_sensor_state(current_lp_sensor) == QTM_KEY_STATE_NO_DET) {
                /* change low-power sensor only when
                    the current lp sensor is not in detect*/
                touch_seq_lp_sensor();
            }
		}
        </#if>
    } 
    else if(measurement_period_store != DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
        <#if num_of_channel_more_than_one == 1>
        touch_enable_nonlp_sensors();
        </#if>
        /* disable low-power measurement */
        touch_disable_lowpower_measurement();
    }
}
        </#if>
<#else>
    <#if sam_d1x_devices?seq_contains(DEVICE_NAME) || sam_e5x_devices?seq_contains(DEVICE_NAME)>
    if (time_since_touch >= DEF_TOUCH_TIMEOUT) {
        <#if num_of_channel_more_than_one == 1>
        touch_disable_nonlp_sensors();
        </#if>
        if (measurement_period_store != QTM_LOWPOWER_TRIGGER_PERIOD) {
			touch_enable_lowpower_measurement();
        }
        <#if num_of_channel_more_than_one == 1>
        if (lp_measurement) {
            touch_seq_lp_sensor();
        }
        </#if>
	}
	else if(measurement_period_store != DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
        <#if num_of_channel_more_than_one == 1>
		touch_enable_nonlp_sensors();
        </#if>
        /* disable low-power measurement */
        touch_disable_lowpower_measurement();
    }
}    
    </#if>
	</#if>
<#else>
    if (time_since_touch >= DEF_TOUCH_TIMEOUT)
    {
        touch_enable_lowpower_measurement();
    } else {
		/* disable low-power measurement */
		touch_disable_lowpower_measurement();
	}
}
</#if>

<#if (ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false) || sam_d1x_devices?seq_contains(DEVICE_NAME) || sam_e5x_devices?seq_contains(DEVICE_NAME) >
<#if num_of_channel_more_than_one == 1>
static void touch_seq_lp_sensor(void)
{
	uint8_t lp_sensor_found = 0;
	uint8_t mbit = 0;

	qtm_key_suspend(current_lp_sensor, &qtlib_key_set1);

    for (uint16_t cnt = current_lp_sensor+1; cnt < DEF_NUM_CHANNELS; cnt++) {
        mbit = cnt % 8;
        if (get_lowpower_mask(cnt) & (1 << mbit)) {
            lp_sensor_found = 1;
            current_lp_sensor = cnt;
            break;
        }
    }
    
    if (lp_sensor_found == 0) {
        for (uint16_t cnt = 0; cnt <= current_lp_sensor; cnt++) {
            mbit = cnt % 8;
            if (get_lowpower_mask(cnt) & (1 << mbit)) {
                lp_sensor_found = 1;
                current_lp_sensor = cnt;
                break;
            }
        }
    }
	qtm_key_resume(current_lp_sensor, &qtlib_key_set1);
}

static void touch_disable_nonlp_sensors(void)
{
	for (uint16_t cnt = 0; cnt < DEF_NUM_CHANNELS; cnt++) {
		if(cnt != current_lp_sensor) {
			qtm_key_suspend(cnt, &qtlib_key_set1);
		}
	}
}

static void touch_enable_nonlp_sensors(void)
{
	for (uint16_t cnt = 0; cnt < DEF_NUM_CHANNELS; cnt++) {
		if(cnt != current_lp_sensor) {
			qtm_key_resume(cnt, &qtlib_key_set1);
		}
	}
}
</#if>
</#if>

<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == true>
/*============================================================================
static void touch_measure_wcomp_match(void)
------------------------------------------------------------------------------
Purpose: callback of autoscan function
Input  : none
Output : none
Notes  :
============================================================================*/
static void touch_measure_wcomp_match(void)
{
    if(measurement_period_store != DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
        <#if sam_c2x_devices?seq_contains(DEVICE_NAME) || sam_l2x_devices?seq_contains(DEVICE_NAME) || sam_d2x_devices?seq_contains(DEVICE_NAME)>
        qtm_autoscan_node_cancel();
        time_since_touch = 0u;
        time_to_measure_touch_var =1; 
        <#else>
        touch_disable_lowpower_measurement();
        time_to_measure_touch_var = 1u;	
        time_since_touch = 0u;
        </#if>
    }
}
    </#if>
#endif
</#if>
<#if ENABLE_GESTURE==true>
uint8_t interrupt_cnt;
uint8_t touch_gesture_time_cnt;
</#if>

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
<#if ENABLE_GESTURE==true>
	touch_gesture_time_cnt= touch_gesture_time_cnt + 2u;
	if (touch_gesture_time_cnt >= DEF_GESTURE_TIME_BASE_MS) {
		qtm_update_gesture_2d_timer(touch_gesture_time_cnt / DEF_GESTURE_TIME_BASE_MS);
		touch_gesture_time_cnt = touch_gesture_time_cnt % DEF_GESTURE_TIME_BASE_MS;
	}
	interrupt_cnt= interrupt_cnt + 2u;
	if (interrupt_cnt >= DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
		interrupt_cnt = 0;
		/* Count complete - Measure touch sensors */
		time_to_measure_touch_var = 1;
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>  
#if DEF_TOUCH_LOWPOWER_ENABLE == 1u
	if (time_since_touch < (65535u - measurement_period_store)) {
		time_since_touch += measurement_period_store;
	} else {
		time_since_touch = 65535;
	}
    qtm_update_qtlib_timer(measurement_period_store);
#else
    qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
#endif
<#else>
    qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
</#if>
	}
<#else> <#-- no gesture -->
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>
<#if ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == true > <#-- event system -->
    <#if sam_d2x_devices?seq_contains(DEVICE_NAME)>
    <@eventlp.lowpower_touch_timer_handler_samd21_evsys/>
    <#elseif sam_c2x_devices?seq_contains(DEVICE_NAME)>
    <@eventlp.lowpower_touch_timer_handler_samc20_c21_evsys/>
    <#elseif sam_l1x_devices?seq_contains(DEVICE_NAME) || pic32cm_le_devices?seq_contains(DEVICE_NAME)>
    <@eventlp.lowpower_touch_timer_handler_saml1x_evsys/>
    <#elseif sam_l2x_devices?seq_contains(DEVICE_NAME)>
    <@eventlp.lowpower_touch_timer_handler_saml2x_evsys/>
    <#elseif pic32cz?seq_contains(DEVICE_NAME)>
    <@eventlp.lowpower_touch_timer_handler_pic32cz_evsys/>  
    </#if>

<#elseif (ENABLE_EVENT_LP?exists && ENABLE_EVENT_LP == false) || (sam_e5x_devices?seq_contains(DEVICE_NAME)) || (sam_d1x_devices?seq_contains(DEVICE_NAME)) >  <#-- No event system -->
	/* Count complete - Measure touch sensors */
	time_to_measure_touch_var = 1u;

	qtm_update_qtlib_timer(measurement_period_store);
    #if DEF_TOUCH_LOWPOWER_ENABLE == 1u
	if (time_since_touch < (65535u - measurement_period_store)) {
		time_since_touch += measurement_period_store;
	}
	else
	{
		time_since_touch = 65535;
	}
    <#if num_of_channel_more_than_one == 1>
	if (time_drift_wakeup_counter < (65535u - measurement_period_store)) {
		time_drift_wakeup_counter += measurement_period_store;
		} else {
		time_drift_wakeup_counter = 65535;
	}
    </#if>
    #endif
<#else>
    <#if sam_e5x_devices?seq_contains(DEVICE_NAME)>
        <@softwarelp.lowpower_touch_timer_handler_same5x_noevs/>
    </#if>
</#if>  
<#else>  <#-- no low power -->
    time_to_measure_touch_var = 1u;
    qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
</#if>
</#if>
}
<#if pic_devices?seq_contains(DEVICE_NAME)>
<#if TOUCH_TIMER_INSTANCE != "">
void timer_handler( uint32_t intCause, uintptr_t context )
{
     touch_timer_handler();
}
uintptr_t tmr_context;
</#if>

void touch_timer_config(void)
{
	<#if TOUCH_TIMER_INSTANCE != "">
	${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].CALLBACK_API_NAME}(timer_handler,tmr_context);
	${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].TIMER_START_API_NAME}();
    <#if buckland?seq_contains(DEVICE_NAME) >
	<#if ENABLE_GESTURE==true>
	${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}(1*(${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].FREQUENCY_GET_API_NAME}()/1000));
	<#else>
	${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}(DEF_TOUCH_MEASUREMENT_PERIOD_MS*(${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].FREQUENCY_GET_API_NAME}()/1000));
	</#if>
    <#else>
	<#if ENABLE_GESTURE==true>
	${TOUCH_TIMER_INSTANCE}_PeriodSet(1*(${TOUCH_TIMER_INSTANCE}_FrequencyGet()/1000));
	<#else>
	${TOUCH_TIMER_INSTANCE}_PeriodSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS*(${TOUCH_TIMER_INSTANCE}_FrequencyGet()/1000));
	</#if>
    </#if>
	<#else>
	<#if ENABLE_GESTURE==true>
	#warning "Timer for periodic touch measurement not defined; Call touch_timer_handler() every 2 millisecond."
	<#else>
	#warning "Timer for periodic touch measurement not defined; Call touch_timer_handler() every DEF_TOUCH_MEASUREMENT_PERIOD_MS."
	</#if>
	</#if>
}
<#else>
<#if TOUCH_TIMER_INSTANCE != "">

void rtc_cb( RTC_TIMER32_INT_MASK intCause, uintptr_t context )
{
    touch_timer_handler();
}
uintptr_t rtc_context;
</#if>

void touch_timer_config(void)
{  
<#if TOUCH_TIMER_INSTANCE != "">
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].CALLBACK_API_NAME}(rtc_cb, rtc_context);

<#if (DEVICE_NAME == "SAMD20") || (DEVICE_NAME == "SAMD21") >
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
<#elseif (DEVICE_NAME == "SAMC20") || (DEVICE_NAME == "SAMC21") || (DEVICE_NAME == "SAML21") || (DEVICE_NAME == "SAML22") || (DEVICE_NAME == "SAML10")||(DEVICE_NAME == "SAML11")||(DEVICE_NAME == "SAML1xE")||(DEVICE_NAME == "PIC32CMLE00")||(DEVICE_NAME == "PIC32CMLS00")||(DEVICE_NAME == "PIC32CMLS60")|| (DEVICE_NAME == "PIC32CMJH01")|| (DEVICE_NAME == "PIC32CMJH00")>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
</#if>
    /* Wait for Synchronization after writing value to Count Register */
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0u);

<#if ENABLE_GESTURE==true>
#if ((KRONO_GESTURE_ENABLE == 1u) || (DEF_TOUCH_DATA_STREAMER_ENABLE == 1u))
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}(1);
#else
    <#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>  
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}((uint32_t) measurement_period_store);
    <#else>
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}((uint32_t) DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    </#if>    
#endif
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].TIMER_START_API_NAME}(); 
<#else>
    <#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")>  
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}((uint32_t) measurement_period_store);
    <#else>
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].COMPARE_SET_API_NAME}((uint32_t) DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    </#if>   
    ${.vars["${TOUCH_TIMER_INSTANCE?lower_case}"].TIMER_START_API_NAME}();  
</#if>
<#else>
	<#if ENABLE_GESTURE==true>
	#warning "Timer for periodic touch measurement not defined; Call touch_timer_handler() every 1 millisecond."
	<#else>
	#warning "Timer for periodic touch measurement not defined; Call touch_timer_handler() every DEF_TOUCH_MEASUREMENT_PERIOD_MS."
	</#if>
</#if>
}
</#if>

uint16_t get_sensor_node_signal(uint16_t sensor_node)
{
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
    return (qtlib_key_data_set1[sensor_node].node_data_struct_ptr->node_acq_signals);
<#else>
    return (ptc_qtlib_node_stat1[sensor_node].node_acq_signals);
</#if>
}

void update_sensor_node_signal(uint16_t sensor_node, uint16_t new_signal)
{
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
    qtlib_key_data_set1[sensor_node].node_data_struct_ptr->node_acq_signals = new_signal;
<#else>
    ptc_qtlib_node_stat1[sensor_node].node_acq_signals = new_signal;
</#if>
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
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
    return (qtlib_key_data_set1[sensor_node].node_data_struct_ptr->node_comp_caps);
<#else>
    return (ptc_qtlib_node_stat1[sensor_node].node_comp_caps);
</#if>
}

void update_sensor_cc_val(uint16_t sensor_node, uint16_t new_cc_value)
{
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
    qtlib_key_data_set1[sensor_node].node_data_struct_ptr->node_comp_caps = new_cc_value;
<#else>
    ptc_qtlib_node_stat1[sensor_node].node_comp_caps = new_cc_value;
</#if>
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
<#if ENABLE_SCROLLER?exists && ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>

uint8_t get_scroller_state(uint16_t sensor_node)
{
	return (qtm_scroller_control1.qtm_scroller_data[sensor_node].scroller_status);
}

uint16_t get_scroller_position(uint16_t sensor_node)
{
	return (qtm_scroller_control1.qtm_scroller_data[sensor_node].position);
}
</#if>
</#if>

<#if ENABLE_SURFACE1T?exists && ENABLE_SURFACE1T== true>
uint8_t get_surface_status(void)
{
  return (qtm_surface_cs_control1.qtm_surface_contact_data->qt_surface_status);
}

uint8_t get_surface_position(uint8_t ver_or_hor)
{
	uint8_t temp_pos = 0;
/*
*	ver_or_hor, 0 = hor, 1 = ver
*/
	if(ver_or_hor == VER_POS)
	{
		temp_pos = qtm_surface_cs_control1.qtm_surface_contact_data->v_position;
	}
	else
	{
		temp_pos = qtm_surface_cs_control1.qtm_surface_contact_data->h_position;
	}
  return temp_pos;
}
</#if>

<#if ENABLE_SURFACE2T?exists && ENABLE_SURFACE2T== true>
uint8_t get_surface_status(void)
{
  return (qtm_surface_cs_control1.qtm_surface_cs2t_data->qt_surface_cs2t_status);
}

uint8_t get_surface_position(uint8_t ver_or_hor, uint8_t contact)
{
	uint8_t temp_pos = 0;
	/*
	*	ver_or_hor, 0 = hor, 1 = ver
	* contact, determines which contact point,
	*	0 is for the first contact point, and 1 is for the second contact point
	*/
	if(ver_or_hor == VER_POS)
	{
		temp_pos = qtm_surface_cs_control1.qtm_surface_contact_data[contact].v_position;
	}
	else
	{
		temp_pos = qtm_surface_cs_control1.qtm_surface_contact_data[contact].h_position;
	}
  return temp_pos;
}
</#if>

<#if pic_devices?seq_contains(DEVICE_NAME)>
<#if buckland?seq_contains(DEVICE_NAME)>
void CVD_Handler(void)
{
    qtm_cvd_clear_interrupt();
    qtm_pic32_cvd_handler_eoc();
}
</#if>
<#else>
/*============================================================================
void PTC_Handler_EOC(void)
------------------------------------------------------------------------------
Purpose: Interrupt service handler for PTC EOC interrupt
Input  : none
Output : none
Notes  : none
============================================================================*/
<#if sam_e5x_devices?seq_contains(DEVICE_NAME)>
void ADC0_1_Handler(void)
{
    ADC0_REGS->ADC_INTFLAG |=1u;
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if DS_DEDICATED_ENABLE == true || DS_PLUS_ENABLE == true>
#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)
	if (qtm_drivenshield_config.flags & (1u << DRIVEN_SHIELD_DUMMY_ACQ)) {
		/* Clear the flag */
		qtm_drivenshield_config.flags &= (uint8_t) ~(1u << DRIVEN_SHIELD_DUMMY_ACQ);
	} else {
		drivenshield_stop();
    qtm_same54_ptc_handler();
}
#else
	qtm_same54_ptc_handler();
#endif
<#else>
	qtm_same54_ptc_handler();
</#if>
</#if>
}
<#else>
void PTC_Handler(void)
{
	qtm_ptc_clear_interrupt();
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if DS_DEDICATED_ENABLE == true || DS_PLUS_ENABLE == true>
#if (DEF_ENABLE_DRIVEN_SHIELD == 1u)
	if (qtm_drivenshield_config.flags & (1u << DRIVEN_SHIELD_DUMMY_ACQ)) {
		/* Clear the flag */
		qtm_drivenshield_config.flags &= (uint8_t) ~(1u << DRIVEN_SHIELD_DUMMY_ACQ);
    <#if DEVICE_NAME == "SAMD10" || DEVICE_NAME == "SAMD11" >
	EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_CHANNEL(0);
    </#if>
	} else {
		drivenshield_stop();
	qtm_${DEVICE_NAME?lower_case}_ptc_handler_eoc();
}
#else
	qtm_${DEVICE_NAME?lower_case}_ptc_handler_eoc();
#endif
<#else>
	qtm_${DEVICE_NAME?lower_case}_ptc_handler_eoc();
</#if>
<#else>
<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
	qtm_samd1x_ptc_handler_eoc();
<#elseif DEVICE_NAME=="SAML11">
    qtm_saml10_ptc_handler_eoc();
<#elseif DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00" || DEVICE_NAME=="PIC32CMLS60">
    qtm_pic32cm_ptc_handler_eoc();
<#elseif DEVICE_NAME =="PIC32CMJH00" || DEVICE_NAME=="PIC32CMJH01">
    qtm_pic32cmjh_ptc_handler_eoc();
<#elseif (DEVICE_NAME =="PIC32CZCA80" ||(DEVICE_NAME == "PIC32CZCA90"))>
    qtm_pic32cz_ptc_handler_eoc();
<#else>
	qtm_${DEVICE_NAME?lower_case}_ptc_handler_eoc();
</#if>
</#if>
}
</#if>
</#if>
</#if>