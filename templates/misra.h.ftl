<#assign pic_devices = ["PIC32MZW","PIC32MZDA","PIC32CXBZ31","WBZ35"]>
<#assign pic32cz = ["PIC32CZCA80","PIC32CZCA90"]>
<#assign no_standby_devices = ["SAMD10","SAMD11"]>

<#macro externvariables>
/* Acquisition variables */
extern qtm_acq_node_data_t ptc_qtlib_node_stat1[DEF_NUM_CHANNELS];
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
<#if DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00" || DEVICE_NAME=="PIC32CMLS60">
extern qtm_acq_4p_pic32cm_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS >> 2];
<#elseif pic32cz?seq_contains(DEVICE_NAME)>
extern qtm_acq_pic32czca_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS >> 2];
<#else>
extern qtm_acq_4p_${DEVICE_NAME?lower_case}_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS >> 2];
</#if>
<#else>
<#if TOUCH_CHAN_ENABLE_CNT&gt;=1>
<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
extern qtm_acq_samd1x_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#elseif DEVICE_NAME== "SAML11" || DEVICE_NAME== "SAML1xE">
extern qtm_acq_saml10_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#elseif  DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00" || DEVICE_NAME=="PIC32CMLS60">
extern qtm_acq_pic32cm_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#elseif  DEVICE_NAME =="PIC32CMJH00" || DEVICE_NAME=="PIC32CMJH01">
extern qtm_acq_pic32cmjh_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#elseif  DEVICE_NAME =="PIC32CXBZ31" || DEVICE_NAME=="WBZ35">
extern qtm_acq_pic32cx_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#elseif  DEVICE_NAME =="PIC32CZCA80"||DEVICE_NAME =="PIC32CZCA90">
extern qtm_acq_pic32czca_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#else>
extern qtm_acq_${DEVICE_NAME?lower_case}_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
</#if>
<#else>
extern qtm_acq_${DEVICE_NAME?lower_case}_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
</#if>
</#if>

<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
<#if ENABLE_SURFACE == true>
/* map node to key */
extern uint8_t touch_key_node_mapping_4p[SURFACE_CS_START_KEY_V+SURFACE_CS_NUM_KEYS_V*SURFACE_CS_NUM_KEYS_H];
<#else>
/* map node to key */
extern uint8_t touch_key_node_mapping_4p[DEF_NUM_SENSORS];
</#if>
</#if>

/* Keys variables */
extern qtm_touch_key_group_config_t qtlib_key_grp_config_set1;
extern qtm_touch_key_data_t qtlib_key_data_set1[DEF_NUM_SENSORS];
extern qtm_touch_key_config_t qtlib_key_configs_set1[DEF_NUM_SENSORS];
<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
/* Scroller variables */
extern qtm_scroller_config_t qtm_scroller_config1[DEF_NUM_SCROLLERS];
extern qtm_scroller_data_t qtm_scroller_data1[DEF_NUM_SCROLLERS];
</#if>
</#if>
<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>
/* Frequency Hop Autotune variables */
extern qtm_freq_hop_autotune_config_t qtm_freq_hop_autotune_config1;
<#else>
extern qtm_freq_hop_config_t qtm_freq_hop_config1;
</#if>
</#if>
<#if ENABLE_SURFACE == true>
/* Surface variables */
<#if ENABLE_SURFACE1T == true>
extern qtm_surface_cs_config_t  qtm_surface_cs_config1;
extern qtm_surface_contact_data_t qtm_surface_cs_data1;
<#else>
extern qtm_surface_cs_config_t  qtm_surface_cs_config1;
extern qtm_surface_contact_data_t qtm_surface_contacts[2];
extern qtm_surface_cs2t_data_t qtm_surface_cs_data1;
</#if>
</#if>
<#if ENABLE_GESTURE == true>
/* Gesture variables */
extern qtm_gestures_2d_config_t qtm_gestures_2d_config;
extern qtm_gestures_2d_data_t qtm_gestures_2d_data;
</#if>
extern uint8_t module_error_code;


<#assign no_standby_during_measurement = 0>
<#if DS_DEDICATED_ENABLE??|| DS_PLUS_ENABLE??>
<#if (DS_DEDICATED_ENABLE == true) || (DS_PLUS_ENABLE == true) || no_standby_devices?seq_contains(DEVICE_NAME)>
<#assign no_standby_during_measurement = 1>
</#if>
</#if>
<#if (LOW_POWER_KEYS?exists && LOW_POWER_KEYS != "")> 
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
extern volatile uint8_t time_to_measure_touch_var;
<#if no_standby_during_measurement == 1>
extern uint8_t measurement_in_progress;
</#if>
#endif
</#if>
extern volatile uint8_t measurement_done_touch;
</#macro>

