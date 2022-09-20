/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    touchTune.c

  Summary:
    QTouch Modular Library

  Description:
    Configuration macros for touch library

*******************************************************************************/

/*******************************************************************************
Copyright (c) ${REL_YEAR} released Microchip Technology Inc.  All rights reserved.

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
 
#include "touchTune.h"

<#if TOUCH_SERCOM_KRONO_INSTANCE == "">
#warning "UART to send touch debug data is not defined. Connect UART to Touch library in MHC."
<#else>
#if DEF_TOUCH_TUNE_ENABLE == 1U

#if ((DEF_SENSOR_TYPE == NODE_SELFCAP) || (DEF_SENSOR_TYPE == NODE_SELFCAP_SHIELD) )
#define TECH SELF_CAP
#elif (DEF_SENSOR_TYPE == NODE_MUTUAL)
#define TECH MUTUAL_CAP
#endif

<#assign csdDevices = 0 />
<#list ["PIC32CMLS60","PIC32CMLS00","PIC32CMLE00","SAML10","SAML11","SAML1xE","SAML22","SAMC20","SAMC21","SAME54","SAME53","SAME51","SAMD51","PIC32MZW","PIC32MZDA", "PIC32CMJH01","PIC32CMJH00","PIC32CXBZ31","WBZ35"] as csdSupported>
    <#if DEVICE_NAME == csdSupported>
        <#assign csdDevices = 1>
    </#if>
</#list>
<#assign outputModuleCnt = 3 >
<#assign configModuleCnt = 7 >
<#assign runtimeDataFunctions = ["copy_run_time_data"] />
<#assign availableData = ["KEYS_MODULE"] />
<#assign availableConfig = ["SENSOR_NODE_CONFIG_ID","SENSOR_KEY_CONFIG_ID","COMMON_SENSOR_CONFIG_ID"] />
<#assign familyname = "" />
<#assign samd2x_d1x_l21 = ["SAMD11", "SAMD10", "SAMD20", "SAMD21", "SAMDA1","SAMHA1", "SAML21" ] />
<#assign samc2x = ["SAMC20", "SAMC21","PIC32CMJH00","PIC32CMJH01"] />
<#assign saml22 = ["SAML22"] />
<#assign same5x = ["SAME51","SAME53","SAME54","SAMD51"] />
<#assign saml1x_pic32cmle = ["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00","PIC32CMLS60"] />
<#assign pic32cvd = ["PIC32MZW","PIC32MZDA","PIC32CXBZ31","WBZ35"] />
<#if samd2x_d1x_l21?seq_contains(DEVICE_NAME)>
<#assign familyname = "samd2x_d1x_l21" />
<#elseif samc2x?seq_contains(DEVICE_NAME)>
<#assign familyname = "samc2x" />
<#elseif same5x?seq_contains(DEVICE_NAME)>
<#assign familyname = "same5x" />
<#elseif saml1x_pic32cmle?seq_contains(DEVICE_NAME)>
<#assign familyname = "saml1x_pic32cmle" />
<#elseif pic32cvd?seq_contains(DEVICE_NAME)>
<#assign familyname = "pic32cvd" />
<#elseif saml22?seq_contains(DEVICE_NAME)>
<#assign familyname = "saml22" />
</#if>

<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
<#-- assign outputModuleCnt = outputModuleCnt + 1 -->
<#assign runtimeDataFunctions = runtimeDataFunctions + ["copy_scroller_run_time_data"] />
<#assign availableData = availableData + ["SCROLLER_MODULE"] />
<#assign availableConfig = availableConfig + ["SCROLLER_CONFIG_ID"] />
#define SCROLLER_MODULE_OUTPUT 1u
<#else>
<#assign runtimeDataFunctions = runtimeDataFunctions + ["NULL"] />
#define SCROLLER_MODULE_OUTPUT 0u
</#if>
<#else>
<#assign runtimeDataFunctions = runtimeDataFunctions + ["NULL"] />
#define SCROLLER_MODULE_OUTPUT 0u
</#if>

<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 1u
<#-- <#assign outputModuleCnt = outputModuleCnt + 1 > -->
<#assign runtimeDataFunctions =  runtimeDataFunctions + ["copy_freq_hop_auto_runtime_data"] />
<#assign availableData = availableData + ["FREQ_HOP_AUTO_TUNE_MODULE"] />
<#assign availableConfig = availableConfig + ["FREQ_HOPPING_AUTO_TUNE_ID"] />
<#else>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 0u
<#assign runtimeDataFunctions = runtimeDataFunctions + ["NULL"] />
</#if>
<#else>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 0u
<#assign runtimeDataFunctions = runtimeDataFunctions + ["NULL"] />
</#if>
#define OUTPUT_MODULE_CNT ${outputModuleCnt}u

typedef struct __attribute__((packed)) {
	uint16_t signal;
	uint16_t reference;
	int16_t delta;
	uint8_t state;
	uint16_t ccvalue;
}sensorData_t;

typedef struct __attribute__((packed)) {
	uint8_t status;
	uint16_t contactSize;
	uint16_t position;
}tuneScrollerData_t;

typedef struct __attribute__((packed))  {
	uint8_t  type;  // wheel or slider
	uint16_t start_key;
	uint8_t  number_of_keys; // key count
	uint8_t  res_deadband;
	uint8_t  position_hysteresis;
	uint16_t threhsold;//THRESHOLD_MSB
}scroll_config_param;// __attribute__((packed));
typedef struct __attribute__((packed)) {
	uint16_t node_xmask;
	uint16_t node_ymask;
	<#if csdDevices == 1 >
	uint8_t csd;
	</#if>
	uint8_t  prsc_res;     /* Bits 7:4 of node_resel_prsc = Resistor */
	uint8_t  gain;		/* Bits 3:0 of node_gain = Digital gain */
	uint8_t  node_oversampling; /* Accumulator setting */
}channel_acq_param;

#define NO_OF_CONFIG_FRAME_ID	 7u//(8U)
#define STREAMING_DEBUG_DATA     (1u)
#define STREAMING_CONFIG_DATA    (2u)
#define PROJECT_CONFIG_DATA_LEN	 (10u)
#define COMMON_KEY_CONFIG_I_LEN  sizeof(qtm_touch_key_group_config_t)
#define COMMON_KEY_CONFIG_II_LEN (2u)
#define SENSOR_ACQ_CONFIG_LEN	 sizeof(channel_acq_param)
#define SENSOR_KEY_CONFIG_LEN	 sizeof(qtm_touch_key_config_t)
#define DEBUG_DATA_PER_CH_LEN	 sizeof(sensorData_t)
#define TOTAL_RUN_TIME_DATA_LEN	 (DEBUG_DATA_PER_CH_LEN * DEF_NUM_CHANNELS)

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
typedef struct  __attribute__((packed)) {
	uint8_t currentFreq;
	uint8_t freqList[16];
}tuneFreqData_t;
#define FREQ_HOP_AUTOTUNE_PARAM_LEN		(3U)
#define DEBUG_DATA_FREQ_HOP_LEN (sizeof(tuneFreqData_t))
#endif

<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
extern qtm_acq_samd1x_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] ;
<#elseif DEVICE_NAME=="SAML11" || DEVICE_NAME=="SAML1xE">
extern qtm_acq_saml10_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] ;
<#elseif  DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00" || DEVICE_NAME=="PIC32CMLS60">
extern qtm_acq_pic32cm_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] ;
<#elseif  DEVICE_NAME =="PIC32CMJH00" || DEVICE_NAME=="PIC32CMJH01">
extern qtm_acq_pic32cmjh_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS] ;
<#else>
extern qtm_acq_${DEVICE_NAME?lower_case}_node_config_t  ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
</#if>
extern qtm_touch_key_data_t         qtlib_key_data_set1[DEF_NUM_CHANNELS];
extern qtm_touch_key_config_t       qtlib_key_configs_set1[DEF_NUM_CHANNELS];
extern qtm_touch_key_group_config_t qtlib_key_grp_config_set1;
extern qtm_acq_node_data_t			ptc_qtlib_node_stat1[DEF_NUM_CHANNELS];

#if SCROLLER_MODULE_OUTPUT == 1u
extern qtm_scroller_data_t			qtm_scroller_data1[DEF_NUM_SCROLLERS];
extern qtm_scroller_control_t		qtm_scroller_control1;
extern qtm_scroller_config_t		qtm_scroller_config1[DEF_NUM_SCROLLERS];
#endif

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
extern qtm_freq_hop_autotune_config_t qtm_freq_hop_autotune_config1;
extern qtm_acquisition_control_t qtlib_acq_set1;
#endif

void uart_send_frame_header(uint8_t trans_type, uint8_t frame,uint16_t frame_len);
void uart_recv_frame_data(uint8_t frame_id,uint16_t len);
void copy_Channel_Data(uint8_t channel_num);
void uart_send_data(uint8_t con_or_debug, uint8_t *data_ptr,  uint16_t data_len);
void copy_run_time_data(uint8_t channel_num);

typedef struct tag_uart_command_info_t {
	uint8_t transaction_type;
	uint8_t frame_id;
	uint16_t num_of_bytes;
	uint8_t header_status;
} uart_command_info_t;
uart_command_info_t volatile uart_command_info;

uint16_t tx_data_len = 0;
uint8_t *tx_data_ptr ;

volatile uint8_t  current_debug_data;
volatile uint8_t  uart_tx_in_progress = 0;
volatile uint8_t  uart_frame_header_flag = 1;
volatile uint8_t  config_or_debug = 0;
volatile uint8_t  write_buf_channel_num;
volatile uint8_t  write_buf_read_ptr;
volatile uint16_t command_flags = 0x0000;
volatile uint16_t max_channels_or_scrollers;


#if UART_RX_BUF_LENGTH <= 255 
typedef uint8_t rx_buff_ptr_t;
#else 
typedef uint16_t rx_buff_ptr_t;
#endif
volatile rx_buff_ptr_t read_buf_read_ptr;
volatile rx_buff_ptr_t read_buf_write_ptr;

static volatile uint8_t rxData;
uintptr_t touchUart;
void touchUartTxComplete(uintptr_t lTouchUart);
void touchUartRxComplete(uintptr_t lTouchUart);

#if SCROLLER_MODULE_OUTPUT == 1u
tuneScrollerData_t runtime_scroller_data_arr;
#define DEBUG_DATA_PER_SCROLLER_LEN sizeof(tuneScrollerData_t)
#define TOTAL_SCROLLER_RUN_TIME_DATA_LEN (DEBUG_DATA_PER_SCROLLER_LEN * DEF_NUM_SCROLLERS)
#define SCROLLER_CONFIG_LEN sizeof(qtm_scroller_config_t)
void copy_scroller_run_time_data(uint8_t channel_num);
#endif

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
tuneFreqData_t runtime_freq_hop_auto_data_arr;
void copy_freq_hop_auto_runtime_data(uint8_t channel_num);
#endif

uint8_t read_buffer[UART_RX_BUF_LENGTH];  
uint8_t common_parameters_arr[COMMON_KEY_CONFIG_II_LEN] = {(uint8_t)DEF_TOUCH_MEASUREMENT_PERIOD_MS,DEF_SEL_FREQ_INIT};

sensorData_t runtime_data_arr;

#define CONFIG_0_PTR ((uint8_t*) &proj_config[0])
#define CONFIG_0_LEN ((uint8_t)  PROJECT_CONFIG_DATA_LEN)

#define CONFIG_1_PTR ((uint8_t*) (&ptc_seq_node_cfg1[0].node_xmask))
#define CONFIG_1_LEN ((uint8_t)  (sizeof(channel_acq_param) * DEF_NUM_CHANNELS))

#define CONFIG_2_PTR ((uint8_t*) (&(qtlib_key_configs_set1[0].channel_threshold)))
#define CONFIG_2_LEN ((uint8_t)  (sizeof(qtm_touch_key_config_t) * DEF_NUM_CHANNELS))

#define CONFIG_3_PTR ((uint8_t*) (&qtlib_key_grp_config_set1.sensor_touch_di))
#define CONFIG_3_LEN ((uint8_t)  (sizeof(qtm_touch_key_group_config_t))-(2U))

#if SCROLLER_MODULE_OUTPUT == 1u
#define CONFIG_4_PTR ((uint8_t*) (&qtm_scroller_config1[0]))
#define CONFIG_4_LEN ((uint8_t) (sizeof(scroll_config_param) * DEF_NUM_SCROLLERS))
#else
#define CONFIG_4_PTR ((uint8_t*) 0u)//(&qtm_scroller_config1[0]))
#define CONFIG_4_LEN ((uint8_t) 0u)//(sizeof(scroll_config_param) * DEF_NUM_SCROLLERS))
#endif

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
#define CONFIG_5_PTR ((uint8_t*) (&qtm_freq_hop_autotune_config1.enable_freq_autotune))
#define CONFIG_5_LEN ((uint8_t)  FREQ_HOP_AUTOTUNE_PARAM_LEN)
#else
#define CONFIG_5_PTR ((uint8_t*) 0u)//(&qtm_scroller_config1[0]))
#define CONFIG_5_LEN ((uint8_t) 0u)//(sizeof(scroll_config_param) * DEF_NUM_SCROLLERS))
#endif

#define CONFIG_6_PTR ((uint8_t*) (&common_parameters_arr[0]))
#define CONFIG_6_LEN ((uint8_t)  (COMMON_KEY_CONFIG_II_LEN))

#define DATA_0_PTR 			((uint8_t*)&runtime_data_arr.signal)
#define DATA_0_ID 			KEY_DEBUG_DATA_ID
#define DATA_0_LEN			sizeof(sensorData_t)
#define DATA_0_REPEAT 		DEF_NUM_CHANNELS
#define DATA_0_FRAME_LEN 	(DATA_0_LEN * DATA_0_REPEAT)

#if SCROLLER_MODULE_OUTPUT == 1u
#define DATA_1_PTR 			((uint8_t*)&runtime_scroller_data_arr.status)
#define DATA_1_ID 			SCROLLER_DEBUG_DATA_ID
#define DATA_1_LEN			DEBUG_DATA_PER_SCROLLER_LEN
#define DATA_1_REPEAT 		DEF_NUM_SCROLLERS
#define DATA_1_FRAME_LEN 	(DATA_1_LEN * DATA_1_REPEAT)
#else
#define DATA_1_PTR 			0u
#define DATA_1_ID 			0u
#define DATA_1_LEN			0u
#define DATA_1_REPEAT 		0u
#define DATA_1_FRAME_LEN 	0u
#endif

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
#define DATA_2_PTR 			((uint8_t*)&runtime_freq_hop_auto_data_arr.currentFreq)
#define DATA_2_ID 			FREQ_HOP_AUTO_TUNE_DATA_ID
#define DATA_2_LEN			(sizeof(tuneFreqData_t))
#define DATA_2_REPEAT 		1u
#define DATA_2_FRAME_LEN 	(DATA_2_LEN * DATA_2_REPEAT)
#else
#define DATA_2_PTR 			0u
#define DATA_2_ID 			0u
#define DATA_2_LEN			0u
#define DATA_2_REPEAT 		0u
#define DATA_2_FRAME_LEN 	0u
#endif	

/* configuration details */
uint8_t proj_config[PROJECT_CONFIG_DATA_LEN] = {PROTOCOL_VERSION, ${familyname}, TECH, (DEF_NUM_CHANNELS),
									(${availableConfig?join("|")}), (0u), (0u),
									(${availableData?join("|")}), (0u),(0u)};

uint16_t frame_len_lookup[NO_OF_CONFIG_FRAME_ID]  = {<#list 0..configModuleCnt-1 as i><#if i==configModuleCnt-1>CONFIG_${i}_LEN<#else>CONFIG_${i}_LEN,</#if></#list>};
uint8_t *ptr_arr[NO_OF_CONFIG_FRAME_ID]	= {<#list 0..configModuleCnt-1 as i><#if i==configModuleCnt-1>CONFIG_${i}_PTR<#else>CONFIG_${i}_PTR,</#if></#list>};

/* output data details */
uint8_t *debug_frame_ptr_arr[OUTPUT_MODULE_CNT]  = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_PTR<#else>DATA_${i}_PTR,</#if></#list>};
uint8_t debug_frame_id[OUTPUT_MODULE_CNT]		  = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_ID<#else>DATA_${i}_ID,</#if></#list>};
uint16_t debug_frame_data_len[OUTPUT_MODULE_CNT]  = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_LEN<#else>DATA_${i}_LEN,</#if></#list>};
uint16_t debug_frame_total_len[OUTPUT_MODULE_CNT] = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_FRAME_LEN<#else>DATA_${i}_FRAME_LEN,</#if></#list>};
uint8_t debug_num_ch_scroller[OUTPUT_MODULE_CNT] = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_REPEAT<#else>DATA_${i}_REPEAT,</#if></#list>};
void (*debug_func_ptr[OUTPUT_MODULE_CNT])(uint8_t ch) = {<#list 0..(runtimeDataFunctions?size-1) as i><#if i==(runtimeDataFunctions?size-1)>${runtimeDataFunctions[i]}<#else>${runtimeDataFunctions[i]},</#if></#list>};

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
void copy_freq_hop_auto_runtime_data(uint8_t channel_num)
{
	uint8_t * temp = &runtime_freq_hop_auto_data_arr.currentFreq;
	*temp++ = (qtm_freq_hop_autotune_config1.num_freqs); 
	
	for (uint8_t count = 0u; count < NUM_FREQ_STEPS; count++) {
		/* Frequencies */
		*temp++ = qtm_freq_hop_autotune_config1.median_filter_freq[count]; //qtm_freq_hop_autotune_control1.qtm_freq_hop_autotune_config->median_filter_freq[count];
	}
}
#endif
#if SCROLLER_MODULE_OUTPUT == 1u
void copy_scroller_run_time_data(uint8_t channel_num)
{
	uint16_t position_temp; //, ref_temp ; 
	uint16_t delta_temp ;	
	uint8_t *temp_ptr = &runtime_scroller_data_arr.status;
 	/* Slider State */	
	
	if(qtm_scroller_control1.qtm_scroller_data[channel_num].scroller_status & 0x01)
		*temp_ptr++ = 1;
	else
		*temp_ptr++ = 0;
			
	/* Slider Delta */
	delta_temp = qtm_scroller_control1.qtm_scroller_data[channel_num].contact_size;
	*temp_ptr++ = delta_temp;
	*temp_ptr++ = (delta_temp >> 8);
	 
	/* filtered position */
	position_temp = (qtm_scroller_control1.qtm_scroller_data[channel_num].position);//get_scroller_position(channel_num);
	*temp_ptr++ =  position_temp;
	*temp_ptr++ = (position_temp >> 8);
	
}


scroll_config_param scroll_config_data;
void copy_scroller_config(uint8_t scroller_num)
{
    max_channels_or_scrollers = DEF_NUM_SCROLLERS;
	scroll_config_data.type							= qtm_scroller_config1[scroller_num].type;
	scroll_config_data.start_key				= (qtm_scroller_config1[scroller_num].start_key);
	scroll_config_data.number_of_keys				= qtm_scroller_config1[scroller_num].number_of_keys;
	scroll_config_data.res_deadband					= qtm_scroller_config1[scroller_num].resol_deadband;
	scroll_config_data.position_hysteresis			= qtm_scroller_config1[scroller_num].position_hysteresis;
	scroll_config_data.threhsold = ((qtm_scroller_config1[scroller_num].contact_min_threshold));
	if(scroller_num == 0) {
		uart_send_frame_header(MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,(sizeof(scroll_config_param) * DEF_NUM_SCROLLERS));
		uart_send_data(STREAMING_CONFIG_DATA,(uint8_t *) &scroll_config_data.type, sizeof(scroll_config_param));
	} else {
		tx_data_ptr	= (uint8_t *) &scroll_config_data.type;
		tx_data_len = sizeof(scroll_config_param);
	}
}

void update_scroller_config(uint8_t scroller_num) {
	qtm_scroller_config1[scroller_num].resol_deadband = scroll_config_data.res_deadband;
	qtm_scroller_config1[scroller_num].position_hysteresis = scroll_config_data.position_hysteresis;
	qtm_scroller_config1[scroller_num].contact_min_threshold = scroll_config_data.threhsold;
}

#endif

channel_acq_param acq_data;
void copy_acq_config(uint8_t channel)
{
<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
qtm_acq_samd1x_node_config_t *ptr = &ptc_seq_node_cfg1[channel];
<#elseif DEVICE_NAME=="SAML11" || DEVICE_NAME=="SAML1xE">
qtm_acq_saml10_node_config_t *ptr = &ptc_seq_node_cfg1[channel];
<#elseif DEVICE_NAME =="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00"|| DEVICE_NAME=="PIC32CMLS60">
qtm_acq_pic32cm_node_config_t *ptr = &ptc_seq_node_cfg1[channel];
<#elseif DEVICE_NAME =="PIC32CMJH00" || DEVICE_NAME=="PIC32CMJH01">
qtm_acq_pic32cmjh_node_config_t *ptr = &ptc_seq_node_cfg1[channel];
<#else>
qtm_acq_${DEVICE_NAME?lower_case}_node_config_t *ptr = &ptc_seq_node_cfg1[channel];
</#if>
    max_channels_or_scrollers = DEF_NUM_CHANNELS;
	//acq_data.node_xmask	= ptr->node_xmask;
	//acq_data.node_ymask	= ptr->node_ymask;
	<#if csdDevices == 1 >
    acq_data.csd	= ptr->node_csd;
	</#if>
	acq_data.prsc_res	= ptr->node_rsel_prsc;
	acq_data.gain	= ptr->node_gain;
	acq_data.node_oversampling	= ptr->node_oversampling;
	if(channel == 0) {
		uart_send_frame_header(MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,(sizeof(channel_acq_param) * DEF_NUM_CHANNELS));
		uart_send_data(STREAMING_CONFIG_DATA,(uint8_t *) &acq_data.node_xmask, sizeof(channel_acq_param));
	} else {
		tx_data_ptr	= (uint8_t *) &acq_data.node_xmask;
		tx_data_len = sizeof(channel_acq_param);
	}
}

void update_acq_config(uint8_t channel) {
	ptc_seq_node_cfg1[channel].node_rsel_prsc = acq_data.prsc_res;
	ptc_seq_node_cfg1[channel].node_gain = acq_data.gain;
	<#if csdDevices == 1 >
    ptc_seq_node_cfg1[channel].node_csd	= acq_data.csd;
	</#if>
	ptc_seq_node_cfg1[channel].node_oversampling = acq_data.node_oversampling;
    calibrate_node(channel);
}


void copy_channel_config_data(uint8_t id, uint8_t channel) {
    switch(id) {
		case 1: // acquisiton
		copy_acq_config(channel);
		break;
		#if SCROLLER_MODULE_OUTPUT == 1u
		case 4:
		copy_scroller_config(channel);
		break;
		#endif
		default:
		max_channels_or_scrollers = 1;
		uart_send_frame_header(MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,frame_len_lookup[uart_command_info.frame_id]);
		uart_send_data(STREAMING_CONFIG_DATA,ptr_arr[uart_command_info.frame_id],frame_len_lookup[uart_command_info.frame_id]);
		break;
	}
}


void copy_run_time_data(uint8_t channel_num)
{
	uint16_t signal_temp, ref_temp ; int16_t delta_temp ;
	uint8_t *temp_ptr = (uint8_t *) &runtime_data_arr.signal;
	
	signal_temp = ptc_qtlib_node_stat1[channel_num].node_acq_signals;
	*temp_ptr++ =  signal_temp;
	*temp_ptr++ = (signal_temp >> 8);
	
	ref_temp = qtlib_key_data_set1[channel_num].channel_reference;
	*temp_ptr++ = ref_temp;
	*temp_ptr++ = (ref_temp >> 8);
	
	delta_temp = signal_temp - ref_temp;
	*temp_ptr++ = delta_temp;
	*temp_ptr++ = (delta_temp >> 8);

	if(qtlib_key_data_set1[channel_num].sensor_state & 0x80) {
		*temp_ptr++ = 1;
	}
	else {
		*temp_ptr++ = 0;
	}

	*temp_ptr++ = ptc_qtlib_node_stat1[channel_num].node_comp_caps;
	*temp_ptr++ = ptc_qtlib_node_stat1[channel_num].node_comp_caps>>8;
}

uint8_t uart_get_char(void)
{
	uint8_t data = read_buffer[read_buf_read_ptr];
	read_buf_read_ptr++;
	if (read_buf_read_ptr == UART_RX_BUF_LENGTH) {
		read_buf_read_ptr = 0;
	}
	return data;
}

void uart_get_string(uint8_t *data_recv, uint16_t len)
{
	for(uint16_t idx = 0; idx < len; idx++)
	{
		*data_recv = uart_get_char();
		data_recv++;		
	}
}


void touchTuneNewDataAvailable(void) {
	command_flags |= SEND_DEBUG_DATA;
}

void UART_Write(uint8_t data) {
	static uint8_t txData;
	txData = data;
	${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Write(&txData, 1); // sam devices
}

void uart_send_data_wait(uint8_t data)
{
	uart_tx_in_progress = 1;
	UART_Write(data);
	while (uart_tx_in_progress == 1)
	;
}

void uart_send_data(uint8_t con_or_debug, uint8_t *data_ptr,  uint16_t data_len) {
	if (uart_tx_in_progress == 0) {
		config_or_debug           = con_or_debug;
		uart_tx_in_progress       = 1;
		write_buf_channel_num	  = 1;
		write_buf_read_ptr        = 1;
		tx_data_ptr			      = data_ptr;
		tx_data_len			      = data_len;
		UART_Write(tx_data_ptr[0]);
	}
}

rx_buff_ptr_t uart_min_num_bytes_received(void)
{
	int16_t retvar =  (read_buf_write_ptr - read_buf_read_ptr);
	if (retvar < 0) 
	{
		retvar = retvar + UART_RX_BUF_LENGTH;
	}
	return (rx_buff_ptr_t)(retvar);
}

void uart_send_frame_header(uint8_t trans_type, uint8_t frame,uint16_t frame_len)
{
	uart_frame_header_flag = 0;
	uart_send_data_wait(DV_HEADER);
 	uart_send_data_wait(trans_type);
 	uart_send_data_wait(frame);
	uart_send_data_wait((uint8_t)(frame_len & 0xFF));
	uart_send_data_wait((uint8_t)(frame_len>>8));
	uart_frame_header_flag = 1;
}

void uart_recv_frame_data(uint8_t frame_id, uint16_t len)
{
    static uint8_t ch_num;
    uint8_t num_data;
    num_data = uart_min_num_bytes_received();
    switch(frame_id)
    {
        case 1:
            while(num_data > sizeof(channel_acq_param)) {

                uint8_t *ptr = (uint8_t *) &acq_data.node_xmask;
                for(uint8_t cnt = 0; cnt < sizeof(channel_acq_param); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                update_acq_config(ch_num);
                ch_num++;
                num_data -= sizeof(channel_acq_param);

                if(ch_num == DEF_NUM_CHANNELS) {
                    ch_num = 0;
                    uart_command_info.header_status = HEADER_AWAITING;
                    command_flags &= ~(1<<uart_command_info.frame_id);
                    uart_get_char(); // reading footer
                    break;
                }
            }
        break;
        
        case 2:
            while(num_data > sizeof(qtm_touch_key_config_t)) {

                uint8_t *ptr = (uint8_t *) &qtlib_key_configs_set1[ch_num].channel_threshold;
                for(uint8_t cnt = 0; cnt < sizeof(qtm_touch_key_config_t); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                ch_num++;
                num_data -= sizeof(qtm_touch_key_config_t);

                if(ch_num == DEF_NUM_CHANNELS) {
                    ch_num = 0;
                    uart_command_info.header_status = HEADER_AWAITING;
                    command_flags &= ~(1<<uart_command_info.frame_id);
                    uart_get_char();
                    break;
                }
            }
        break;
#if SCROLLER_MODULE_OUTPUT == 1u
        case 4:
            while(num_data > sizeof(scroll_config_param)) {

                uint8_t *ptr = (uint8_t *) &scroll_config_data.type;
                for(uint8_t cnt = 0; cnt < sizeof(scroll_config_param); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                update_scroller_config(ch_num);
                ch_num++;
                num_data -= sizeof(scroll_config_param);

                if(ch_num == DEF_NUM_SCROLLERS) {
                    ch_num = 0;
                    uart_command_info.header_status = HEADER_AWAITING;
                    command_flags &= ~(1<<uart_command_info.frame_id);
                    uart_get_char(); // reading footer
                    break;
                }
            }
        break;
#endif
        default:
            uart_get_string(ptr_arr[uart_command_info.frame_id],uart_command_info.num_of_bytes);//frame_len_lookup[uart_command_info.frame_id]);
            uart_get_char();// receiving footer
        break;

    }
}


void touchTuneInit(void) {

    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_WriteCallbackRegister(touchUartTxComplete, touchUart);
    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_ReadCallbackRegister(touchUartRxComplete, touchUart);

    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Read((void *) &rxData, 1);
}


void touchTuneProcess(void)
{
	static uint8_t debug_index = 0;

	switch (uart_command_info.header_status) {
		case HEADER_AWAITING:
			if (uart_min_num_bytes_received() > 5)
			{
				if (uart_get_char() == DV_HEADER)
				{
					uart_get_string( (uint8_t *) &uart_command_info.transaction_type, 4); // uart_command_info.transaction_type ,uart_command_info.frame_id,uart_command_info.num_of_bytes
					uart_command_info.header_status		= DATA_AWAITING;
				}
			}
			break;
		case DATA_AWAITING:
			if(uart_command_info.transaction_type == PC_SEND_CONFIG_DATA_TO_MCU) // user has pressed write to kit
			{
                if(uart_command_info.num_of_bytes >= UART_RX_BUF_LENGTH) {
                    uart_recv_frame_data(uart_command_info.frame_id,uart_command_info.num_of_bytes);
                }else if (uart_min_num_bytes_received() > uart_command_info.num_of_bytes) //total length of bytes + footer
				{
					command_flags |= (1 << (uart_command_info.frame_id )); // (uart_command_info.frame_id - CONFIG_INFO)
					uart_command_info.header_status	= DATA_RECEIVED;
				}
			}
			else if (uart_command_info.transaction_type == PC_REQUEST_CONFIG_DATA_FROM_MCU) // read from kit
			{
				if(uart_min_num_bytes_received() > 1) // Data length = 1 + footer
				{
					if ((uart_get_char() == ZERO) && (uart_get_char() == DV_FOOTER) ) // requesting configuration
					{
						command_flags |= (1 << (uart_command_info.frame_id )); // (uart_command_info.frame_id - CONFIG_INFO)
						uart_command_info.header_status	= DATA_RECEIVED;
					}
				}
			}
		break;
		case DATA_RECEIVED:
			if((command_flags & 0x0FFF) && (uart_tx_in_progress == 0)) {
				if (uart_command_info.transaction_type == PC_REQUEST_CONFIG_DATA_FROM_MCU) // requesting configuration
				{
					copy_channel_config_data(uart_command_info.frame_id, 0);
					uart_command_info.header_status = HEADER_AWAITING;
				}
				else if(uart_command_info.transaction_type == PC_SEND_CONFIG_DATA_TO_MCU)// PC Updating parameters.
				{
					uart_recv_frame_data(uart_command_info.frame_id,uart_command_info.num_of_bytes);//frame_len_lookup[uart_command_info.frame_id]);
					// uart_get_string(ptr_arr[uart_command_info.frame_id],uart_command_info.num_of_bytes);//frame_len_lookup[uart_command_info.frame_id]);
					// uart_get_char();// receiving footer
					uart_command_info.header_status = HEADER_AWAITING;
					command_flags &= ~(1<<uart_command_info.frame_id);
				}
			}
		break;
		default:
			uart_command_info.header_status = HEADER_AWAITING;
		break;
	}

	/* to send periodic data */
	if((command_flags & SEND_DEBUG_DATA) && (uart_tx_in_progress == 0)) {
		
        while(debug_func_ptr[debug_index] == NULL) {
            debug_index++;
            if(debug_index == OUTPUT_MODULE_CNT) {
                debug_index = 0;
            }
        }
		current_debug_data = debug_frame_id[debug_index];
		
		uart_send_frame_header(MCU_SEND_TUNE_DATA_TO_PC, current_debug_data, debug_frame_total_len[debug_index]);
								
		(debug_func_ptr[debug_index])(0);
		
		max_channels_or_scrollers = debug_num_ch_scroller[debug_index];
		
		uart_send_data(STREAMING_DEBUG_DATA, (uint8_t *)debug_frame_ptr_arr[debug_index], debug_frame_data_len[debug_index]);
		
		debug_index++;
		
		if(debug_index == OUTPUT_MODULE_CNT) {
			debug_index = 0;
		}
	}
}

#endif

void touchUartTxComplete(uintptr_t lTouchUart)
{
	#if (DEF_TOUCH_TUNE_ENABLE == 1u)

	if (uart_frame_header_flag != 1)
	{
		uart_tx_in_progress = 0;
	} 
	else 
	{
		if (write_buf_read_ptr < tx_data_len )
		{
			UART_Write(tx_data_ptr[write_buf_read_ptr]);
			write_buf_read_ptr++;
		} else {
			if(config_or_debug == STREAMING_CONFIG_DATA) {
				/* per channel data are sent channel by channel to reduce RAM requirements */
				if (write_buf_channel_num < max_channels_or_scrollers)
				{
                    copy_channel_config_data(uart_command_info.frame_id, write_buf_channel_num);
					write_buf_read_ptr = 1;
					write_buf_channel_num++;
					UART_Write(tx_data_ptr[0]);
				}
				else if(write_buf_channel_num == max_channels_or_scrollers)
				{
					write_buf_channel_num++;
					command_flags &= ~(1<<uart_command_info.frame_id);
					UART_Write(DV_FOOTER);
				}
				else
				{
					uart_tx_in_progress = 0;
				}
			} else if(config_or_debug == STREAMING_DEBUG_DATA) {
				/* per channel data are sent channel by channel to reduce RAM requirements */
				if (write_buf_channel_num < max_channels_or_scrollers)
				{
					(*debug_func_ptr[current_debug_data & 0x0F])(write_buf_channel_num);  
					write_buf_read_ptr = 1;
					write_buf_channel_num++;
					UART_Write(tx_data_ptr[0]);
				}
				else if(write_buf_channel_num == max_channels_or_scrollers)
				{
					write_buf_channel_num++;
					command_flags &= ~(SEND_DEBUG_DATA); // clearing off debug data
					UART_Write(DV_FOOTER);
				}
				else
				{
					uart_tx_in_progress = 0;
				}
			}
		}
	}
	#endif
}

void touchUartRxComplete(uintptr_t lTouchUart)
{
	#if (DEF_TOUCH_TUNE_ENABLE == 1u)
	read_buffer[read_buf_write_ptr] = rxData;
	read_buf_write_ptr++;
	if (read_buf_write_ptr == UART_RX_BUF_LENGTH) {
		read_buf_write_ptr = 0;
	}
	${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Read((void *) &rxData,1);
	#endif
}
</#if>