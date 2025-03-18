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

void touchUartTxComplete(uintptr_t lTouchUart);
void touchUartRxComplete(uintptr_t lTouchUart);

<#if TOUCH_SERCOM_KRONO_INSTANCE == "">
#warning "UART to send touch debug data is not defined. Connect UART to Touch library in MCC."
<#else>
#if DEF_TOUCH_TUNE_ENABLE == 1U

#if ((DEF_SENSOR_TYPE == NODE_SELFCAP) || (DEF_SENSOR_TYPE == NODE_SELFCAP_SHIELD) )
#define TECH SELF_CAP
#elif (DEF_SENSOR_TYPE == NODE_MUTUAL)
#define TECH MUTUAL_CAP
#endif

<#assign outputModuleCnt = 1 >
<#assign configModuleCnt = 4 >
<#assign configIdToPositionMap = ["PROJECT_CONFIG_ID"] />
<#assign runtimeDataFunctions = ["copy_run_time_data"] />
<#assign availableData = ["KEY_DEBUG_MASK"] />
<#assign availableConfig = ["SENSOR_NODE_CONFIG_MASK","SENSOR_KEY_CONFIG_MASK","COMMON_SENSOR_CONFIG_MASK"] />
<#assign configIdToPositionMap = configIdToPositionMap + ["SENSOR_NODE_CONFIG_ID", "SENSOR_KEY_CONFIG_ID", "COMMON_SENSOR_CONFIG_ID"] />
<#assign familyname = "" />
<#assign samd2x_d1x_l21 = ["SAMD11", "SAMD10", "SAMD20", "SAMD21", "SAMDA1","SAMHA1", "SAML21" ] />
<#assign samc2x = ["SAMC20", "SAMC21","PIC32CMJH00","PIC32CMJH01"] />
<#assign saml22 = ["SAML22"] />
<#assign same5x = ["SAME51","SAME53","SAME54","SAMD51"] />
<#assign saml1x_pic32cmle = ["SAML10","SAML11","SAML1xE","PIC32CMLE00","PIC32CMLS00","PIC32CMLS60"] />

<#assign pic32czca = ["PIC32CZCA80","PIC32CZCA90"] />
<#assign pic32cmgc = ["PIC32CMGC00","PIC32CMSG00"] />
<#assign pic32ck = ["PIC32CKSG00","PIC32CKSG01", "PIC32CKGC00","PIC32CKGC01"]/>
<#if samd2x_d1x_l21?seq_contains(DEVICE_NAME)>
<#assign familyname = "samd2x_d1x_l21" />
<#elseif samc2x?seq_contains(DEVICE_NAME)>
<#assign familyname = "samc2x" />
<#elseif same5x?seq_contains(DEVICE_NAME)>
<#assign familyname = "same5x" />
<#elseif saml1x_pic32cmle?seq_contains(DEVICE_NAME)>
<#assign familyname = "saml1x_pic32cmle" />
<#elseif JSONDATA?eval.features.core == "CVD">
<#assign familyname = "pic32cvd" />
<#elseif saml22?seq_contains(DEVICE_NAME)>
<#assign familyname = "saml22" />
<#elseif pic32czca?seq_contains(DEVICE_NAME) || pic32ck?seq_contains(DEVICE_NAME)  || pic32cmgc?seq_contains(DEVICE_NAME)>
<#assign familyname = "pic32czca" />
</#if>

<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
<#assign outputModuleCnt = outputModuleCnt + 1 >
<#assign configModuleCnt = configModuleCnt + 1 >
<#assign runtimeDataFunctions = runtimeDataFunctions + ["copy_scroller_run_time_data"] />
<#assign availableData = availableData + ["SCROLLER_DEBUG_MASK"] />
<#assign availableConfig = availableConfig + ["SCROLLER_CONFIG_MASK"] />
<#assign configIdToPositionMap = configIdToPositionMap + ["SCROLLER_CONFIG_ID"] />
#define SCROLLER_MODULE_OUTPUT 1u
<#else>
#define SCROLLER_MODULE_OUTPUT 0u
</#if>
<#else>
#define SCROLLER_MODULE_OUTPUT 0u
</#if>


<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 1u
<#assign outputModuleCnt = outputModuleCnt + 1 >
<#assign configModuleCnt = configModuleCnt + 1 >
<#assign runtimeDataFunctions =  runtimeDataFunctions + ["copy_freq_hop_auto_runtime_data"] />
<#assign availableData = availableData + ["FREQ_HOP_AUTO_TUNE_DEBUG_MASK"] />
<#assign availableConfig = availableConfig + ["FREQ_HOPPING_AUTO_TUNE_MASK"] />
<#assign configIdToPositionMap = configIdToPositionMap + ["FREQ_HOPPING_AUTO_TUNE_ID"] />
<#else>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 0u
</#if>
<#else>
#define FREQ_HOP_AUTO_MODULE_OUTPUT 0u
</#if>


<#if ENABLE_SURFACE == true>
<#assign outputModuleCnt = outputModuleCnt + 1 >
<#assign configModuleCnt = configModuleCnt + 1 >
<#assign runtimeDataFunctions = runtimeDataFunctions + ["copy_surface_run_time_data"] />
<#assign availableData = availableData + ["SURFACE_DEBUG_MASK"] />
<#assign availableConfig = availableConfig + ["SURFACE_CONFIG_MASK"] />
<#assign configIdToPositionMap = configIdToPositionMap + ["SURFACE_CONFIG_ID"] />
#define SURFACE_MODULE_OUTPUT 1u
</#if>

<#if ENABLE_GESTURE == true>
<#assign outputModuleCnt = outputModuleCnt + 1 >
<#assign configModuleCnt = configModuleCnt + 1 >
<#assign runtimeDataFunctions = runtimeDataFunctions + ["copy_gesture_run_time_data"] />
<#assign availableData = availableData + ["GESTURE_DEBUG_MASK"] />
<#assign availableConfig = availableConfig + ["GESTURE_CONFIG_MASK"] />
<#assign configIdToPositionMap = configIdToPositionMap + ["GESTURE_CONFIG_ID"] />
#define GESTURE_MODULE_OUTPUT 1u
</#if>

/*******************************************************************************
 * Acqusition Parameters
*******************************************************************************/
typedef struct __attribute__((packed)) {
	uint16_t node_xmask;
	uint16_t node_ymask;
	<#if JSONDATA?eval.features.csd == true>
	uint8_t csd;
	</#if>
	uint8_t  prsc_res;
	uint8_t  gain;
	uint8_t  node_oversampling;
}channel_acq_param;
typedef struct __attribute__((packed)) {
	uint16_t acq_signal;
	uint16_t reference;
	int16_t delta;
	uint8_t sensor_state;
	uint16_t ccvalue;
}sensorData_t;
void copy_channel_config_data(uint8_t id, uint8_t channel);
void update_acq_config(uint8_t channel);
void copy_acq_config(uint8_t channel);

/*******************************************************************************
 * Keys' Module Parameters
*******************************************************************************/

<#if ENABLE_SCROLLER == true>
<#if TOUCH_SCROLLER_ENABLE_CNT&gt;=1>
/*******************************************************************************
 * Scroller Parameters
*******************************************************************************/
typedef struct __attribute__((packed)) {
	uint8_t status;
	uint16_t contactSize;
	uint16_t position;
}tuneScrollerData_t;

typedef struct __attribute__((packed))  {
	uint8_t  type;
	uint16_t start_key;
	uint8_t  number_of_keys;
	uint8_t  res_deadband;
	uint8_t  position_hysteresis;
	uint16_t threhsold;
}scroll_config_param;

static tuneScrollerData_t runtime_scroller_data_arr;
#define DEBUG_DATA_PER_SCROLLER_LEN sizeof(tuneScrollerData_t)
#define SCROLLER_CONFIG_LEN sizeof(qtm_scroller_config_t)
void copy_scroller_run_time_data(uint8_t channel_num);
void update_scroller_config(uint8_t scroller_num);
void copy_scroller_config(uint8_t scroller_num);
</#if>
</#if>

<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>
/*******************************************************************************
 * Frequency Hop Autotune Parameters
*******************************************************************************/
#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
typedef struct  __attribute__((packed)) {
	uint8_t numFreq;
	uint8_t freqList[16];
}tuneFreqData_t;
#define FREQ_HOP_AUTOTUNE_PARAM_LEN		(3U)
#define DEBUG_DATA_FREQ_HOP_LEN (sizeof(tuneFreqData_t))
static tuneFreqData_t runtime_freq_hop_auto_data_arr;
void copy_freq_hop_auto_runtime_data(uint8_t channel_num);
#endif
</#if>
</#if>

<#if ENABLE_SURFACE == true>
/*******************************************************************************
 * Surface Parameters
*******************************************************************************/
#if (SURFACE_MODULE_OUTPUT == 1u)
typedef struct __attribute__((packed))  {
  uint16_t start_key_h;
  uint8_t number_of_keys_h;
  uint16_t start_key_v;
  uint8_t number_of_keys_v;
  uint8_t resol_deadband;
  uint8_t position_hysteresis;
  uint8_t position_filter;
  uint16_t contact_min_threshold;
}surface_config_param;
typedef struct __attribute__((packed)){
	uint8_t status;
	uint16_t contact_size;
	uint16_t h_position;
	uint16_t v_position;
	uint8_t resolution;
}tuneSurfaceData_t;
static tuneSurfaceData_t runtime_surface_data_arr;
void copy_surface_run_time_data(uint8_t contact_num);
void copy_surface_config(uint8_t channel_num);
void update_surface_config(uint8_t channel_num);
#endif
</#if>

<#if ENABLE_GESTURE == true>
/*******************************************************************************
 * Gesture Parameters
*******************************************************************************/
#if (GESTURE_MODULE_OUTPUT == 1u)
typedef struct  __attribute__((packed)) {
	uint8_t gestures_status;
	uint8_t gestures_which_gesture;
	uint8_t gestures_info;
}tuneGestureData_t;
static tuneGestureData_t runtime_gesture_data_arr;
void copy_gesture_run_time_data(uint8_t channel_num);
#endif
</#if>

/*******************************************************************************
 * UART Related function prototypes
*******************************************************************************/
void uart_send_frame_header(uint8_t trans_type, uint8_t frame,uint16_t frame_len);
void uart_recv_frame_data(uint8_t frame_id,uint16_t len);
void uart_send_data(uint8_t con_or_debug, uint8_t *data_ptr,  uint16_t data_len);
void copy_run_time_data(uint8_t channel_num);
void uart_send_data_wait(uint8_t data);
void UART_Write(uint8_t data);
void uart_get_string(uint8_t *data_recv, uint16_t len);
uint8_t uart_get_char(void);

typedef struct tag_uart_command_info_t {
	uint8_t transaction_type;
	uint8_t frame_id;
	uint16_t num_of_bytes;
	uint8_t header_status;
} uart_command_info_t;
static uart_command_info_t uart_command_info;

static uint16_t tx_data_len = 0;
static uint8_t *tx_data_ptr ;
static volatile uint8_t  current_debug_data;
static volatile uint8_t  uart_tx_in_progress = 0;
static volatile uint8_t  uart_frame_header_flag = 1;
static volatile uint8_t  config_or_debug = 0;
static volatile uint8_t  write_buf_channel_num;
static volatile uint8_t  write_buf_read_ptr;
static volatile uint16_t command_flags = 0x0000;
static uint16_t max_channels_or_scrollers;

#if UART_RX_BUF_LENGTH <= 255 
typedef uint8_t rx_buff_ptr_t;
#else 
typedef uint16_t rx_buff_ptr_t;
#endif
static volatile rx_buff_ptr_t read_buf_read_ptr;
static volatile rx_buff_ptr_t read_buf_write_ptr;

static uint8_t rxData;
static uintptr_t touchUart;
rx_buff_ptr_t uart_min_num_bytes_received(void);
uint8_t getDebugIndex(uint8_t debugFramId);
uint8_t getConfigIndex(uint8_t frameid);

static uint8_t read_buffer[UART_RX_BUF_LENGTH];  

static sensorData_t runtime_data_arr;

/*******************************************************************************
 * Configuration Macros Parameters
*******************************************************************************/
#define NO_OF_CONFIG_FRAME_ID	 (${configModuleCnt}u)

#define PROJECT_CONFIG_DATA_LEN	 (10u)
#define CONFIG_0_PTR ((uint8_t*) &proj_config[0])
#define CONFIG_0_LEN ((uint16_t)  PROJECT_CONFIG_DATA_LEN)

#define CONFIG_1_PTR ((uint8_t*) (&ptc_seq_node_cfg1[0].node_xmask))
#define CONFIG_1_LEN ((uint16_t)  (sizeof(channel_acq_param) * DEF_NUM_CHANNELS))

#define CONFIG_2_PTR ((uint8_t*) (&(qtlib_key_configs_set1[0].channel_threshold)))
#define CONFIG_2_LEN ((uint16_t)  (sizeof(qtm_touch_key_config_t) * DEF_NUM_CHANNELS))

#define CONFIG_3_PTR ((uint8_t*) (&qtlib_key_grp_config_set1.sensor_touch_di))
#define CONFIG_3_LEN ((uint16_t)  (sizeof(qtm_touch_key_group_config_t))-(2U))
<#assign configPos = 4 />
<#if ENABLE_SCROLLER == true>

#if SCROLLER_MODULE_OUTPUT == 1u
#define CONFIG_${configPos}_PTR ((uint8_t*) (&qtm_scroller_config1[0]))
#define CONFIG_${configPos}_LEN ((uint16_t) (sizeof(scroll_config_param) * DEF_NUM_SCROLLERS))
<#assign configPos = configPos + 1 />
#endif
</#if>
<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
#define CONFIG_${configPos}_PTR ((uint8_t*) (&qtm_freq_hop_autotune_config1.enable_freq_autotune))
#define CONFIG_${configPos}_LEN ((uint16_t)  FREQ_HOP_AUTOTUNE_PARAM_LEN)
<#assign configPos = configPos + 1 />
#endif
</#if>
</#if>
<#if ENABLE_SURFACE == true>

#if SURFACE_MODULE_OUTPUT == 1u
#define CONFIG_${configPos}_PTR ((uint8_t*) (&qtm_surface_cs_config1.start_key_h))
#define CONFIG_${configPos}_LEN ((uint16_t)  11u)
<#assign configPos = configPos + 1 />
#endif
</#if>
<#if ENABLE_GESTURE == true>

#if GESTURE_MODULE_OUTPUT == 1u
#define CONFIG_${configPos}_PTR ((uint8_t*) (&qtm_gestures_2d_config.tapReleaseTimeout))
#define CONFIG_${configPos}_LEN ((uint16_t)  13u)
<#assign configPos = configPos + 1 />
#endif
</#if>

/*******************************************************************************
 * Debug Data Configuration
*******************************************************************************/
#define OUTPUT_MODULE_CNT ${outputModuleCnt}u

#define DATA_0_PTR 			((uint8_t*)&runtime_data_arr.acq_signal)
#define DATA_0_ID 			(DEBUG_MASK + KEY_DEBUG_DATA_ID)
#define DATA_0_LEN			(uint16_t) sizeof(sensorData_t)
#define DATA_0_REPEAT 		DEF_NUM_CHANNELS
#define DATA_0_FRAME_LEN 	(uint16_t) (DATA_0_LEN * DATA_0_REPEAT)
<#assign debugPos = 1 />
<#if ENABLE_SCROLLER == true>

#if SCROLLER_MODULE_OUTPUT == 1u
#define DATA_${debugPos}_PTR 			((uint8_t*)&runtime_scroller_data_arr.status)
#define DATA_${debugPos}_ID 			(DEBUG_MASK + SCROLLER_DEBUG_DATA_ID)
#define DATA_${debugPos}_LEN			(uint16_t) DEBUG_DATA_PER_SCROLLER_LEN
#define DATA_${debugPos}_REPEAT 		DEF_NUM_SCROLLERS
#define DATA_${debugPos}_FRAME_LEN 	(uint16_t) (DATA_${debugPos}_LEN * DATA_${debugPos}_REPEAT)
#endif
<#assign debugPos = debugPos + 1 />
</#if>
<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>

#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
#define DATA_${debugPos}_PTR 			((uint8_t*)&runtime_freq_hop_auto_data_arr.numFreq)
#define DATA_${debugPos}_ID 			(DEBUG_MASK + FREQ_HOP_AUTO_TUNE_DATA_ID)
#define DATA_${debugPos}_LEN			(uint16_t) (sizeof(tuneFreqData_t))
#define DATA_${debugPos}_REPEAT 		1u
#define DATA_${debugPos}_FRAME_LEN 	(uint16_t) (DATA_${debugPos}_LEN * DATA_${debugPos}_REPEAT)
#endif
<#assign debugPos = debugPos + 1 />
</#if>
</#if>
<#if ENABLE_SURFACE == true>

#if SURFACE_MODULE_OUTPUT == 1u
#define DATA_${debugPos}_PTR 			((uint8_t*)&runtime_surface_data_arr.status)
#define DATA_${debugPos}_ID 			(DEBUG_MASK + SURFACE_DEBUG_DATA_ID)
#define DATA_${debugPos}_LEN			(uint16_t) (sizeof(tuneSurfaceData_t))
<#if ENABLE_SURFACE1T == true>
#define DATA_${debugPos}_REPEAT 		1u
<#else>
#define DATA_${debugPos}_REPEAT 		2u
</#if>
#define DATA_${debugPos}_FRAME_LEN 	(uint16_t) (DATA_${debugPos}_LEN * DATA_${debugPos}_REPEAT)
#endif
<#assign debugPos = debugPos + 1 />
</#if>
<#if ENABLE_GESTURE == true>

#if GESTURE_MODULE_OUTPUT == 1u
#define DATA_${debugPos}_PTR 			((uint8_t*)&runtime_gesture_data_arr.gestures_status)
#define DATA_${debugPos}_ID 			(DEBUG_MASK + GESTURE_DEBUG_DATA_ID)
#define DATA_${debugPos}_LEN			(uint16_t) (sizeof(tuneGestureData_t))
#define DATA_${debugPos}_REPEAT 		1u
#define DATA_${debugPos}_FRAME_LEN 	(uint16_t) (DATA_${debugPos}_LEN * DATA_${debugPos}_REPEAT)
#endif
<#assign debugPos = debugPos + 1 />
</#if>

/* configuration details */
static uint8_t proj_config[PROJECT_CONFIG_DATA_LEN] = {PROTOCOL_VERSION, (uint8_t) ${JSONDATA?eval.acquisition.file_names.bidirectionalTune_name}, (uint8_t) TECH, (DEF_NUM_CHANNELS),
									(uint8_t) (${availableConfig?join("|")}), (0u), (0u),
									(uint8_t) (${availableData?join("|")}), (0u),(0u)};

static uint16_t frame_len_lookup[NO_OF_CONFIG_FRAME_ID]  = {<#list 0..configModuleCnt-1 as i><#if i==configModuleCnt-1>CONFIG_${i}_LEN<#else>CONFIG_${i}_LEN,</#if></#list>};
static uint8_t *configPointerArray[NO_OF_CONFIG_FRAME_ID]	= {<#list 0..configModuleCnt-1 as i><#if i==configModuleCnt-1>CONFIG_${i}_PTR<#else>CONFIG_${i}_PTR,</#if></#list>};

/* output data details */
static uint8_t *debug_frame_PointerArray[OUTPUT_MODULE_CNT]  = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_PTR<#else>DATA_${i}_PTR,</#if></#list>};
static uint8_t debug_frame_id[OUTPUT_MODULE_CNT]		  = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_ID<#else>DATA_${i}_ID,</#if></#list>};
static uint16_t debug_frame_data_len[OUTPUT_MODULE_CNT]  = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_LEN<#else>DATA_${i}_LEN,</#if></#list>};
static uint16_t debug_frame_total_len[OUTPUT_MODULE_CNT] = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_FRAME_LEN<#else>DATA_${i}_FRAME_LEN,</#if></#list>};
static uint8_t debug_num_ch_scroller[OUTPUT_MODULE_CNT] = {<#list 0..outputModuleCnt-1 as i><#if i==outputModuleCnt-1>DATA_${i}_REPEAT<#else>DATA_${i}_REPEAT,</#if></#list>};
static void (*debug_func_ptr[OUTPUT_MODULE_CNT])(uint8_t ch) = {<#list 0..(runtimeDataFunctions?size-1) as i><#if i==(runtimeDataFunctions?size-1)>${runtimeDataFunctions[i]}<#else>${runtimeDataFunctions[i]},</#if></#list>};

static uint8_t frameIdToConfigID[NO_OF_CONFIG_FRAME_ID] = {${configIdToPositionMap?join(",")}};

uint8_t getDebugIndex(uint8_t debugFramId) {
	uint8_t arrayIndex = 0u;
	for(uint8_t cnt = 0u; cnt < OUTPUT_MODULE_CNT; cnt++) {
		if(debug_frame_id[cnt] == debugFramId){
			arrayIndex = cnt;
			break;
		}
	}
	return arrayIndex;
}

uint8_t getConfigIndex(uint8_t frameid) {
	uint8_t arrayIndex = 0u;
	for(uint8_t cnt = 0u; cnt < NO_OF_CONFIG_FRAME_ID; cnt++) {
		if(frameIdToConfigID[cnt] == frameid){
			arrayIndex = cnt;
			break;
		}
	}
	return arrayIndex;
}

<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE != false>
#if FREQ_HOP_AUTO_MODULE_OUTPUT == 1u
void copy_freq_hop_auto_runtime_data(uint8_t channel_num)
{
	runtime_freq_hop_auto_data_arr.numFreq = (qtm_freq_hop_autotune_config1.num_freqs);	
	for (uint8_t count = 0u; count < (uint8_t) NUM_FREQ_STEPS; count++) {
		/* Frequencies */
		runtime_freq_hop_auto_data_arr.freqList[count] = qtm_freq_hop_autotune_config1.median_filter_freq[count];
	}
}
#endif
</#if>
</#if>

<#if ENABLE_SCROLLER == true>
#if SCROLLER_MODULE_OUTPUT == 1u
void copy_scroller_run_time_data(uint8_t channel_num)
{
 	/* Slider State */		
	runtime_scroller_data_arr.status = (uint8_t) (qtm_scroller_data1[channel_num].scroller_status & 0x01u);
	/* Slider Delta */
	runtime_scroller_data_arr.contactSize = qtm_scroller_data1[channel_num].contact_size;
	/* filtered position */
	runtime_scroller_data_arr.position = (qtm_scroller_data1[channel_num].position);
}


static scroll_config_param scroll_config_data;
void copy_scroller_config(uint8_t scroller_num)
{
    max_channels_or_scrollers = DEF_NUM_SCROLLERS;
	scroll_config_data.type							= qtm_scroller_config1[scroller_num].type;
	scroll_config_data.start_key				= (qtm_scroller_config1[scroller_num].start_key);
	scroll_config_data.number_of_keys				= qtm_scroller_config1[scroller_num].number_of_keys;
	scroll_config_data.res_deadband					= qtm_scroller_config1[scroller_num].resol_deadband;
	scroll_config_data.position_hysteresis			= qtm_scroller_config1[scroller_num].position_hysteresis;
	scroll_config_data.threhsold = ((qtm_scroller_config1[scroller_num].contact_min_threshold));
	if(scroller_num == 0u) {
		uart_send_frame_header((uint8_t)MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,((uint16_t) sizeof(scroll_config_param) * (uint8_t) DEF_NUM_SCROLLERS));
		uart_send_data(STREAMING_CONFIG_DATA,(uint8_t *) &scroll_config_data.type, (uint16_t) sizeof(scroll_config_param));
	} else {
		tx_data_ptr	= (uint8_t *) &scroll_config_data;
		tx_data_len = (uint16_t) sizeof(scroll_config_param);
	}
}

void update_scroller_config(uint8_t scroller_num) {
	qtm_scroller_config1[scroller_num].resol_deadband = scroll_config_data.res_deadband;
	qtm_scroller_config1[scroller_num].position_hysteresis = scroll_config_data.position_hysteresis;
	qtm_scroller_config1[scroller_num].contact_min_threshold = scroll_config_data.threhsold;
}
#endif
</#if>

<#if ENABLE_SURFACE == true>
#if (SURFACE_MODULE_OUTPUT == 1U)
<#if ENABLE_SURFACE1T == true>
void copy_surface_run_time_data(uint8_t contact_num)
{
	runtime_surface_data_arr.status = qtm_surface_cs_data1.qt_surface_status & 0x01u;
	runtime_surface_data_arr.contact_size = qtm_surface_cs_data1.contact_size;
	runtime_surface_data_arr.h_position = qtm_surface_cs_data1.h_position;
	runtime_surface_data_arr.v_position = qtm_surface_cs_data1.v_position;
	runtime_surface_data_arr.resolution = (uint8_t) qtm_surface_cs_config1.resol_deadband >> 4;
}
<#else>
void copy_surface_run_time_data(uint8_t contact_num)
{
	runtime_surface_data_arr.status = qtm_surface_contacts[contact_num].qt_contact_status & 0x01u;
	runtime_surface_data_arr.contact_size = qtm_surface_contacts[contact_num].contact_size;
	runtime_surface_data_arr.h_position = qtm_surface_contacts[contact_num].h_position;
	runtime_surface_data_arr.v_position = qtm_surface_contacts[contact_num].v_position;
}
</#if>

static surface_config_param surface_config_data;
void copy_surface_config(uint8_t channel_num) {
	surface_config_data.start_key_h = qtm_surface_cs_config1.start_key_h;
	surface_config_data.number_of_keys_h = qtm_surface_cs_config1.number_of_keys_h;
	surface_config_data.start_key_v = qtm_surface_cs_config1.start_key_v;
	surface_config_data.number_of_keys_v = qtm_surface_cs_config1.number_of_keys_v;
	surface_config_data.resol_deadband = qtm_surface_cs_config1.resol_deadband;
	surface_config_data.position_hysteresis = qtm_surface_cs_config1.position_hysteresis;
	surface_config_data.position_filter = qtm_surface_cs_config1.position_filter;
	surface_config_data.contact_min_threshold = qtm_surface_cs_config1.contact_min_threshold;
	max_channels_or_scrollers = 1u;
	if(channel_num == 0u) {
		uart_send_frame_header((uint8_t)MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,(uint16_t) (sizeof(surface_config_param) * 1u));
		uart_send_data((uint8_t) STREAMING_CONFIG_DATA,(uint8_t *) &surface_config_data.start_key_h, (uint16_t) sizeof(surface_config_param));
	} else {
		tx_data_ptr	= (uint8_t *) &surface_config_data.start_key_h;
		tx_data_len = (uint16_t) sizeof(surface_config_param);
	}
}

void update_surface_config(uint8_t channel_num) {

	qtm_surface_cs_config1.resol_deadband = surface_config_data.resol_deadband;
	qtm_surface_cs_config1.position_hysteresis = surface_config_data.position_hysteresis;
	qtm_surface_cs_config1.position_filter = surface_config_data.position_filter;
	qtm_surface_cs_config1.contact_min_threshold = surface_config_data.contact_min_threshold;
}
#endif
</#if>

<#if ENABLE_GESTURE == true>
#if (GESTURE_MODULE_OUTPUT == 1U)
void copy_gesture_run_time_data(uint8_t channel_num)
{
	runtime_gesture_data_arr.gestures_status = qtm_gestures_2d_data.gestures_status;
	runtime_gesture_data_arr.gestures_which_gesture = qtm_gestures_2d_data.gestures_which_gesture;
	runtime_gesture_data_arr.gestures_info = qtm_gestures_2d_data.gestures_info;

	qtm_gestures_2d_clearGesture();
}
#endif
</#if>

static channel_acq_param acq_data;
void copy_acq_config(uint8_t channel)
{
qtm_acq_${JSONDATA?eval.acquisition.file_names.node_name}_node_config_t *ptr = &ptc_seq_node_cfg1[channel];
    max_channels_or_scrollers = DEF_NUM_CHANNELS;
	<#if JSONDATA?eval.features.csd == true>
    acq_data.csd	= ptr->node_csd;
	</#if>
	acq_data.prsc_res	= ptr->node_rsel_prsc;
	acq_data.gain	= ptr->node_gain;
	acq_data.node_oversampling	= ptr->node_oversampling;
	if(channel == 0u) {
		uart_send_frame_header((uint8_t)MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,((uint16_t) sizeof(channel_acq_param) * (uint8_t) DEF_NUM_CHANNELS));
		uart_send_data(STREAMING_CONFIG_DATA,(uint8_t *) &acq_data.node_xmask, (uint16_t) sizeof(channel_acq_param));
	} else {
		tx_data_ptr	= (uint8_t *) &acq_data.node_xmask;
		tx_data_len = (uint16_t) sizeof(channel_acq_param);
	}
}

void update_acq_config(uint8_t channel) {
	ptc_seq_node_cfg1[channel].node_rsel_prsc = acq_data.prsc_res;
	ptc_seq_node_cfg1[channel].node_gain = acq_data.gain;
	<#if JSONDATA?eval.features.csd == true>
    ptc_seq_node_cfg1[channel].node_csd	= acq_data.csd;
	</#if>
	ptc_seq_node_cfg1[channel].node_oversampling = acq_data.node_oversampling;
    calibrate_node(channel);
}


void copy_channel_config_data(uint8_t id, uint8_t channel) {
	uint8_t arrayIndex = getConfigIndex(id);
    switch(id) {
		case SENSOR_NODE_CONFIG_ID:
		copy_acq_config(channel);
		break;
<#if ENABLE_SCROLLER == true>
		#if SCROLLER_MODULE_OUTPUT == 1u
		case SCROLLER_CONFIG_ID:
		copy_scroller_config(channel);
		break;		
		#endif
</#if>
<#if ENABLE_SURFACE == true>
		#if SURFACE_MODULE_OUTPUT == 1u
		case SURFACE_CONFIG_ID:
		copy_surface_config(channel);
		break;
		#endif
</#if>
		default:
		max_channels_or_scrollers = 1;
		uart_send_frame_header((uint8_t)MCU_RESPOND_CONFIG_DATA_TO_PC, uart_command_info.frame_id,frame_len_lookup[arrayIndex]);
		uart_send_data(STREAMING_CONFIG_DATA,configPointerArray[arrayIndex],frame_len_lookup[arrayIndex]);
		break;
	}
}


void copy_run_time_data(uint8_t channel_num)
{
	int16_t delta_temp ;	
	runtime_data_arr.acq_signal = ptc_qtlib_node_stat1[channel_num].node_acq_signals;
	runtime_data_arr.reference = qtlib_key_data_set1[channel_num].channel_reference;
	
	delta_temp = (int16_t) (ptc_qtlib_node_stat1[channel_num].node_acq_signals);
	delta_temp -= (int16_t) qtlib_key_data_set1[channel_num].channel_reference;
	runtime_data_arr.delta = delta_temp;

	runtime_data_arr.sensor_state = (uint8_t) ((qtlib_key_data_set1[channel_num].sensor_state & 0x80u) >> 7);
	runtime_data_arr.ccvalue = ptc_qtlib_node_stat1[channel_num].node_comp_caps;

}

uint8_t uart_get_char(void)
{
	uint8_t data = read_buffer[read_buf_read_ptr];
	read_buf_read_ptr++;
	if (read_buf_read_ptr == UART_RX_BUF_LENGTH) {
		read_buf_read_ptr = 0u;
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
	if (${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Write(&txData, 1)) {

	}
}

void uart_send_data_wait(uint8_t data)
{
	uart_tx_in_progress = 1u;
	UART_Write(data);
	while (uart_tx_in_progress == 1u) {

	}
}

void uart_send_data(uint8_t con_or_debug, uint8_t *data_ptr,  uint16_t data_len) {
	if (uart_tx_in_progress == 0u) {
		config_or_debug           = con_or_debug;
		uart_tx_in_progress       = 1u;
		write_buf_channel_num	  = 1u;
		write_buf_read_ptr        = 1u;
		tx_data_ptr			      = data_ptr;
		tx_data_len			      = data_len;
		UART_Write(tx_data_ptr[0]);
	}
}

rx_buff_ptr_t uart_min_num_bytes_received(void)
{
	int16_t retvar = (int16_t) read_buf_write_ptr;
	retvar -= (int16_t) read_buf_read_ptr;
	if (retvar < 0)
	{
		retvar = retvar + (int16_t) UART_RX_BUF_LENGTH;
	}
	return (rx_buff_ptr_t)(retvar);
}

void uart_send_frame_header(uint8_t trans_type, uint8_t frame,uint16_t frame_len)
{
	uart_frame_header_flag = 0;
	uart_send_data_wait(DV_HEADER);
 	uart_send_data_wait(trans_type);
 	uart_send_data_wait(frame);
	uart_send_data_wait((uint8_t)(frame_len));
	uart_send_data_wait((uint8_t)(frame_len>>8));
	uart_frame_header_flag = 1;
}

void uart_recv_frame_data(uint8_t frame_id, uint16_t len)
{
    static uint8_t ch_num;
    uint16_t num_data;
	uint8_t tempData;
	uint8_t arrayIndex = getConfigIndex(frame_id);
    num_data = uart_min_num_bytes_received();
    switch(frame_id)
    {
		case 0u:
		break;
        case SENSOR_NODE_CONFIG_ID:
            while(num_data > (uint16_t) sizeof(channel_acq_param)) {

                uint8_t *ptr = (uint8_t *) &acq_data.node_xmask;
                for(uint16_t cnt = 0u; cnt < (uint16_t) sizeof(channel_acq_param); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                update_acq_config(ch_num);
                ch_num++;
                num_data -= (uint16_t) sizeof(channel_acq_param);

                if(ch_num == (uint8_t) DEF_NUM_CHANNELS) {
                    ch_num = 0u;
                    uart_command_info.header_status = HEADER_AWAITING;
                    command_flags = command_flags & (uint16_t) (~((uint16_t)1<<uart_command_info.frame_id));
                    tempData = uart_get_char();
					if(tempData != DV_FOOTER) {
						/* Error condition */
					}
                    break;
                }
            }
        break;
        
        case SENSOR_KEY_CONFIG_ID:
            while(num_data > (uint16_t) sizeof(qtm_touch_key_config_t)) {

                uint8_t *ptr = (uint8_t *) &qtlib_key_configs_set1[ch_num].channel_threshold;
                for(uint16_t cnt = 0u; cnt < (uint16_t) sizeof(qtm_touch_key_config_t); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                ch_num++;
                num_data -= (uint16_t) sizeof(qtm_touch_key_config_t);

                if(ch_num == (uint8_t) DEF_NUM_CHANNELS) {
                    ch_num = 0u;
                    uart_command_info.header_status = HEADER_AWAITING;
                    command_flags = command_flags & (uint16_t) (~((uint16_t)1<<uart_command_info.frame_id));
                    tempData = uart_get_char();
					if(tempData != DV_FOOTER) {
						/* Error condition */
					}
                    break;
                }
            }
        break;
<#if ENABLE_SCROLLER == true>
#if SCROLLER_MODULE_OUTPUT == 1u
        case SCROLLER_CONFIG_ID:
            while(num_data > (uint16_t) sizeof(scroll_config_param)) {

                uint8_t *ptr = (uint8_t *) &scroll_config_data;
                for(uint16_t cnt = 0u; cnt < (uint16_t) sizeof(scroll_config_param); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                update_scroller_config(ch_num);
                ch_num++;
                num_data -= (uint16_t) sizeof(scroll_config_param);

                if(ch_num == (uint8_t) DEF_NUM_SCROLLERS) {
                    ch_num = 0u;
                    uart_command_info.header_status = HEADER_AWAITING;
                    command_flags = command_flags & (uint16_t) (~((uint16_t)1<<uart_command_info.frame_id));
                    tempData = uart_get_char();
					if(tempData != DV_FOOTER) {
						/* Error condition */
					}
                    break;
                }
            }
        break;
#endif
</#if>

<#if ENABLE_SURFACE == true>
#if SURFACE_MODULE_OUTPUT == 1u
		case SURFACE_CONFIG_ID:
            while(num_data > (uint16_t) sizeof(surface_config_param)) {

                uint8_t *ptr = (uint8_t *) &surface_config_data.start_key_h;
                for(uint16_t cnt = 0; cnt < (uint16_t) sizeof(surface_config_param); cnt++) {
                    ptr[cnt] = uart_get_char();
                }
                update_surface_config(ch_num);
				num_data -= (uint16_t) sizeof(surface_config_param);
                ch_num = 0u;
                uart_command_info.header_status = HEADER_AWAITING;
                command_flags = command_flags & (uint16_t) (~((uint16_t)1<<uart_command_info.frame_id));
                tempData = uart_get_char();
				if(tempData != DV_FOOTER) {
					/* Error condition */
				}
            }
		break;
#endif
</#if>

        default:
            uart_get_string(configPointerArray[arrayIndex],uart_command_info.num_of_bytes);
            tempData = uart_get_char();
        break;
    }
}


void touchTuneInit(void) {

    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_WriteCallbackRegister(touchUartTxComplete, touchUart);
    ${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_ReadCallbackRegister(touchUartRxComplete, touchUart);

    if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Read((void *) &rxData, 1)) {
	
	}
}


void touchTuneProcess(void)
{
	static uint8_t debug_index = 0;

	switch (uart_command_info.header_status) {
		case HEADER_AWAITING:
			if (uart_min_num_bytes_received() > 5u)
			{
				if (uart_get_char() == DV_HEADER)
				{
					uart_get_string((uint8_t *) &uart_command_info, 4);
					uart_command_info.header_status = DATA_AWAITING;
				}
			} else {

			}
			break;
		case DATA_AWAITING:
			if(uart_command_info.transaction_type == (uint8_t) PC_SEND_CONFIG_DATA_TO_MCU)
			{
                if(uart_command_info.num_of_bytes >= UART_RX_BUF_LENGTH) {
                    uart_recv_frame_data(uart_command_info.frame_id,uart_command_info.num_of_bytes);
                }else if (uart_min_num_bytes_received() > uart_command_info.num_of_bytes)
				{
					command_flags = command_flags | (uint16_t) ((uint16_t)1 << (uart_command_info.frame_id ));
					uart_command_info.header_status	= DATA_RECEIVED;
				} else {
					/* not enough data to process */
				}
			}
			else if (uart_command_info.transaction_type == (uint8_t) PC_REQUEST_CONFIG_DATA_FROM_MCU)
			{
				if(uart_min_num_bytes_received() > 1u)
				{
					uint8_t data1 = uart_get_char();
					uint8_t data2 = uart_get_char();
					if((data1 == ZERO) && (data2 == DV_FOOTER)) {
						command_flags = command_flags | (uint16_t) ((uint16_t)1 << (uart_command_info.frame_id ));
						uart_command_info.header_status	= DATA_RECEIVED;
					}
				}
			} else {
				/* error condition */
			}
		break;
		case DATA_RECEIVED:
			if(uart_tx_in_progress == 0u) {
				if((command_flags & 0x0FFFu) != 0u) {
					if (uart_command_info.transaction_type == (uint8_t) PC_REQUEST_CONFIG_DATA_FROM_MCU)
					{
						copy_channel_config_data(uart_command_info.frame_id, 0);
						uart_command_info.header_status = HEADER_AWAITING;
					}
					else if(uart_command_info.transaction_type == (uint8_t) PC_SEND_CONFIG_DATA_TO_MCU)
					{
						uart_recv_frame_data(uart_command_info.frame_id,uart_command_info.num_of_bytes);
						uart_command_info.header_status = HEADER_AWAITING;
						command_flags = command_flags & (uint16_t) (~((uint16_t)1<<uart_command_info.frame_id));
					} else {
						/* error condition */
					}
				} else {
					/* Data received - but command flag not set - error condition */
				}
			} else {
				/* transmission is in progress */
			}
		break;
		default:
			uart_command_info.header_status = HEADER_AWAITING;
		break;
	}

	if(uart_tx_in_progress == 0u) {
	 	/* to send periodic data */
		if((command_flags & SEND_DEBUG_DATA) == SEND_DEBUG_DATA) {

			current_debug_data = debug_frame_id[debug_index];
			
			uart_send_frame_header((uint8_t)MCU_SEND_TUNE_DATA_TO_PC, current_debug_data, debug_frame_total_len[debug_index]);
									
			(debug_func_ptr[debug_index])(0);
			
			max_channels_or_scrollers = debug_num_ch_scroller[debug_index];
			
			uart_send_data(STREAMING_DEBUG_DATA, (uint8_t *)debug_frame_PointerArray[debug_index], debug_frame_data_len[debug_index]);
			
			debug_index++;
			
			if(debug_index == OUTPUT_MODULE_CNT) {
				debug_index = 0;
			}
		}
	}
}

#endif

void touchUartTxComplete(uintptr_t lTouchUart)
{
	#if (DEF_TOUCH_TUNE_ENABLE == 1u)

	uint8_t arrayIndex = 0u;

	if (uart_frame_header_flag != 1u)
	{
		uart_tx_in_progress = 0u;
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
					command_flags = command_flags & (uint16_t) (~((uint16_t)1<<uart_command_info.frame_id));
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
					arrayIndex = getDebugIndex(current_debug_data);
					(*debug_func_ptr[arrayIndex])(write_buf_channel_num);  
					write_buf_read_ptr = 1;
					write_buf_channel_num++;
					UART_Write(tx_data_ptr[0]);
				}
				else if(write_buf_channel_num == max_channels_or_scrollers)
				{
					write_buf_channel_num++;
					command_flags = command_flags & (uint16_t) (~SEND_DEBUG_DATA);
					UART_Write(DV_FOOTER);
				}
				else
				{
					uart_tx_in_progress = 0;
				}
			} else {
				/* error condition - control should not reach here*/
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
		read_buf_write_ptr = 0u;
	}
	if(${.vars["${TOUCH_SERCOM_KRONO_INSTANCE?lower_case}"].USART_PLIB_API_PREFIX}_Read((void *) &rxData,1)) {
	}
	#endif
}
</#if>