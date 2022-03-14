
/*******************************************************************************
  Touch Library ${REL_VER} Release

  Company:
    Microchip Technology Inc.

  File Name:
    kronocommadaptor.c

  Summary:
    QTouch Modular Library

  Description:
    Enables communication between device and Microchip 2D Touch Surface Utility.
	
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

/*----------------------------------------------------------------------------
  include files
----------------------------------------------------------------------------*/
#include "touch/touch.h"

#if KRONOCOMM_ENABLE == 1u
#include "touch/datastreamer/kronocommadaptor.h"
#if KRONOCOMM_UART == 1u
 
#include "touch/datastreamer/KronoCommuart_sam.h"

#endif

static uint8_t                   writeback_req = 0u;
extern qtm_acquisition_control_t qtlib_acq_set1;
extern qtm_touch_key_control_t qtlib_key_set1;
<#if (ENABLE_SURFACE1T == true)>
extern qtm_surface_cs_control_t qtm_surface_cs_control1;
extern qtm_surface_contact_data_t qtm_surface_cs_data1;
<#else>
extern qtm_surface_cs2t_control_t qtm_surface_cs_control1;
extern qtm_surface_cs2t_data_t qtm_surface_cs_data1;
</#if>
#if (KRONO_GESTURE_ENABLE == 1u)
extern qtm_gestures_2d_control_t qtm_gestures_2d_control1;
extern qtm_gestures_2d_config_t  qtm_gestures_2d_config;
extern qtm_gestures_2d_data_t    qtm_gestures_2d_data;
#endif
extern qtm_touch_key_data_t qtlib_key_data_set1[DEF_NUM_SENSORS];

<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
extern qtm_acq_4p_${DEVICE_NAME?lower_case}_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS >> 2];
extern uint8_t touch_key_node_mapping_4p[SURFACE_CS_START_KEY_V + (SURFACE_CS_NUM_KEYS_V * SURFACE_CS_NUM_KEYS_H)];
<#else>
<#if DEVICE_NAME=="SAMD10" || DEVICE_NAME=="SAMD11">
extern qtm_acq_samd1x_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#elseif DEVICE_NAME=="PIC32CMLE00" || DEVICE_NAME=="PIC32CMLS00"|| DEVICE_NAME=="PIC32CMLS60">
extern qtm_acq_pic32cm_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
<#else>
extern qtm_acq_${DEVICE_NAME?lower_case}_node_config_t ptc_seq_node_cfg1[DEF_NUM_CHANNELS];
</#if>
</#if>

extern qtm_touch_key_config_t qtlib_key_configs_set1[DEF_NUM_SENSORS];
<#if (ENABLE_GESTURE == true)>
static uint8_t cfgRam[CFGRAM_SIZE] = 
{
	SURFACE_CS_NUM_KEYS_H,		//X
	SURFACE_CS_NUM_KEYS_V,		//Y		
	64,	//oversampling
	20,		//X threshold
	20,		//Y threshold
	(uint8_t)(DEF_GESTURE_TIME_BASE_MS),
	(uint8_t)(DEF_GESTURE_TIME_BASE_MS >> 8),
	(uint8_t)(DEF_GESTURE_TIME_BASE_MS),
	(uint8_t)(DEF_GESTURE_TIME_BASE_MS >> 8),
	(uint8_t)SCR_RESOLUTION(SURFACE_CS_RESOL_DB)
};
<#else>
static uint8_t cfgRam[CFGRAM_SIZE] = 
{
	SURFACE_CS_NUM_KEYS_H,		//X
	SURFACE_CS_NUM_KEYS_V,		//Y		
	64,	//oversampling
	20,		//X threshold
	20,		//Y threshold
	0,
	0,
	0,
	0,
	(uint8_t)SCR_RESOLUTION(SURFACE_CS_RESOL_DB)
};
</#if>
#if (KRONO_GESTURE_ENABLE == 1u)
static uint8_t gestureCfgRam[GESTURECFGRAM_SIZE] = {TAP_RELEASE_TIMEOUT,
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
						<#if (ENABLE_SURFACE2T == true)>
                                                    PINCH_ZOOM_THRESHOLD,
						    <#else>
						    0,
						    </#if>

                                                    150};
#endif
static uint8_t coreRam[CORERAM_SIZE] = {VERSION_HI, VERSION_LO, ID_HI, ID_LO, 0u, (MODE_TOUCH | MODE_GESTURE), 1u, 0u};

static uint8_t  touchRam[6];
static uint8_t  touchDelta[SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H];
static uint16_t touchRaw[SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H];
static uint16_t touchRef[SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H];

uint8_t isPowerOfTwo(uint8_t x)
{
	return ((x != 0) && ((x & (~x + 1)) == x));
}

void Krono_UpdateBuffer(void)
{
	static uint8_t initialized           = 0;
	static uint8_t frameCount            = 0;
	static uint8_t previousSurfaceStatus = 0;

	uint8_t new_setting;

	uint8_t temp_i_var, temp_j_var = 0u;

	/* CfGRam update */
	if (initialized == 0) {
		cfgRam[CFGGRAM_OVRSMPLS_ADDR] = 1 << (ptc_seq_node_cfg1[SURFACE_CS_START_KEY_H].node_oversampling);
		cfgRam[CFGGRAM_THRESH_X_ADDR] = qtlib_key_configs_set1[SURFACE_CS_START_KEY_H].channel_threshold;
		cfgRam[CFGGRAM_THRESH_Y_ADDR] = qtlib_key_configs_set1[SURFACE_CS_START_KEY_V].channel_threshold;
		initialized                   = 1;
	} else if (0u != writeback_req) {
		/* Check if any valid parameters have been written to RAM Buffer */
		/* Oversampling */
		new_setting = cfgRam[CFGGRAM_OVRSMPLS_ADDR];
		if (new_setting != (uint8_t)(1u << (ptc_seq_node_cfg1[SURFACE_CS_START_KEY_H].node_oversampling))) {
			/* Find the highest bit of the new oversampling setting */
			for (temp_i_var = 0u; temp_i_var < 8u; temp_i_var++) {
				temp_j_var = (1u << (7u - temp_i_var));
				temp_j_var &= new_setting;
				if (0u != temp_j_var) {
					/* This bit set */
					new_setting = (7u - temp_i_var);
					temp_i_var  = 99u;
				}
			}
			/* Check max for device */
			if (new_setting > 6u) {
				new_setting = 6u;
			}
			/* Write actual setting back to RAM Buffer */
			cfgRam[CFGGRAM_OVRSMPLS_ADDR] = (uint8_t)(1u << new_setting);
			/* Write oversampling to each node in config */
<#if ENABLE_BOOST?exists && ENABLE_BOOST == true>
			for (uint16_t cnt = 0; cnt < (SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H); cnt++) {
				if (cnt < SURFACE_CS_NUM_KEYS_V) {
					for (uint16_t hor_cnt = 0; hor_cnt < SURFACE_CS_NUM_KEYS_H; hor_cnt++) {
						uint8_t temp_cnt = touch_key_node_mapping_4p[cnt * SURFACE_CS_NUM_KEYS_H + hor_cnt + SURFACE_CS_START_KEY_V];
						ptc_seq_node_cfg1[(SURFACE_CS_START_KEY_V + temp_cnt)>>2].node_oversampling = new_setting;
					}
					} else {
					for (uint16_t ver_cnt = 0; ver_cnt < SURFACE_CS_NUM_KEYS_V; ver_cnt++) {
						uint8_t temp_cnt
						= touch_key_node_mapping_4p[ver_cnt * SURFACE_CS_NUM_KEYS_V + (cnt - SURFACE_CS_NUM_KEYS_V) + SURFACE_CS_START_KEY_V];
						ptc_seq_node_cfg1[(SURFACE_CS_START_KEY_V + temp_cnt)>>2].node_oversampling = new_setting;
					}
				}
			}
<#else>
			for (temp_i_var = 0; temp_i_var < SURFACE_CS_NUM_KEYS_H; temp_i_var++) {
				ptc_seq_node_cfg1[SURFACE_CS_START_KEY_H + temp_i_var].node_oversampling = new_setting;
			}

			for (temp_i_var = 0; temp_i_var < SURFACE_CS_NUM_KEYS_V; temp_i_var++) {
				ptc_seq_node_cfg1[SURFACE_CS_START_KEY_V + temp_i_var].node_oversampling = new_setting;
			}
</#if>
			touch_init(); /* Re-initialize the touch library */
		}
		/* X Threshold */
		if (cfgRam[CFGGRAM_THRESH_X_ADDR] != qtlib_key_configs_set1[SURFACE_CS_START_KEY_H].channel_threshold) {
			for (temp_i_var = 0; temp_i_var < SURFACE_CS_NUM_KEYS_H; temp_i_var++) {
				qtlib_key_configs_set1[SURFACE_CS_START_KEY_H + temp_i_var].channel_threshold = cfgRam[3];
			}
		}
		/* Y Threshold */
		if (cfgRam[CFGGRAM_THRESH_Y_ADDR] != qtlib_key_configs_set1[SURFACE_CS_START_KEY_V].channel_threshold) {
			for (temp_i_var = 0; temp_i_var < SURFACE_CS_NUM_KEYS_V; temp_i_var++) {
				qtlib_key_configs_set1[SURFACE_CS_START_KEY_V + temp_i_var].channel_threshold = cfgRam[4];
			}
		}
		/* Resolution */
		if (cfgRam[CFGGRAM_RESOL_ADDR]
		    != SCR_RESOLUTION(qtm_surface_cs_control1.qtm_surface_cs_config->resol_deadband)) {
			qtm_surface_cs_control1.qtm_surface_cs_config->resol_deadband &= 0x0Fu;
			qtm_surface_cs_control1.qtm_surface_cs_config->resol_deadband
			    |= ((cfgRam[CFGGRAM_RESOL_ADDR] & 0x0Fu) << 4u);
		}
#if (KRONO_GESTURE_ENABLE == 1u)
		/* Gesture Config */
		qtm_gestures_2d_control1.qtm_gestures_2d_config->tapReleaseTimeout
		    = gestureCfgRam[GESTCFGRAM_TAP_RELEASE_TIMEOUT_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->tapHoldTimeout
		    = gestureCfgRam[GESTCFGRAM_TAP_HOLD_TIMEOUT_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->swipeTimeout = gestureCfgRam[GESTCFGRAM_SWIPE_TIMEOUT_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->xSwipeDistanceThreshold
		    = gestureCfgRam[GESTCFGRAM_XSWIPE_DIST_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->ySwipeDistanceThreshold
		    = gestureCfgRam[GESTCFGRAM_YSWIPE_DIST_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->edgeSwipeDistanceThreshold
		    = gestureCfgRam[GESTCFGRAM_EDGSWIPE_DIST_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->tapDistanceThreshold = gestureCfgRam[GESTCFGRAM_TAP_DIST_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->seqTapDistanceThreshold
		    = gestureCfgRam[GESTCFGRAM_MULTI_TAP_DIST_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->edgeBoundary = gestureCfgRam[GESTCFGRAM_EDGE_BOUND_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->wheelPostscaler
		    = gestureCfgRam[GESTCFGRAM_WHEEL_POSTSCAL_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->wheelStartQuadrantCount
		    = gestureCfgRam[GESTCFGRAM_WHEEL_STARTQUAD_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->wheelReverseQuadrantCount
		    = gestureCfgRam[GESTCFGRAM_WHEEL_REVQUAD_ADDR];
		qtm_gestures_2d_control1.qtm_gestures_2d_config->pinchZoomThreshold
		    = gestureCfgRam[GESTCFGRAM_PINCHZOOM_THRS_ADDR];
		// qtlib_key_configs_set1[16].channel_threshold = gestureCfgRam[GESTCFGRAM_PALMDETECTION_THRS_ADDR]; // the palm
		// detection threshold will be moved into the gesture parameter in the future

#endif
		writeback_req = 0u;
	}

		/* Write to RAM buffers */

		/* Update TouchRam */
#if (KRONO_GESTURE_ENABLE == 1u)
	touchRam[5] = qtm_gestures_2d_data.gestures_info;

	touchRam[4] = qtm_gestures_2d_data.gestures_which_gesture;
#endif
	touchRam[0] = 0x00;

#if (KRONO_GESTURE_ENABLE == 1u)
	if (qtm_gestures_2d_data.gestures_status) {
		touchRam[0] |= TOUCHSTATE_GES;
		SetIRQPin();
	}
#endif
<#if (ENABLE_SURFACE1T == true)>	
        {
			if(qtm_surface_cs_control1.qtm_surface_contact_data[0].qt_surface_status & TOUCH_ACTIVE) 
			{
				touchRam[0] |= TOUCHSTATE_TCH;
				SetIRQPin();
			}
			
	    	else
		    	touchRam[0] &= TOUCHSTATE_nTCH;

		}
<#else>
	if (qtm_surface_cs_data1.qt_surface_cs2t_status & TOUCH_ACTIVE) {
		if ((qtm_surface_cs_control1.qtm_surface_contact_data[0].qt_contact_status & TOUCH_ACTIVE)
		    && (qtm_surface_cs_control1.qtm_surface_contact_data[1].qt_contact_status & TOUCH_ACTIVE))

			touchRam[0] |= TOUCHSTAT_TCH_DUAL;
		else
			touchRam[0] |= TOUCHSTATE_TCH;
		SetIRQPin();
	} else {
		touchRam[0] &= TOUCHSTATE_nTCH;
	}
</#if>

	touchRam[0] |= frameCount;
	frameCount += 0x10;
<#if (ENABLE_SURFACE2T == true)>	

	/* dual finger touch*/
	if (touchRam[0] & 0x04) {
#if (KRONO_GESTURE_ENABLE == 1u)
		uint16_t x_position = (uint16_t)((*(qtm_gestures_2d_config.horiz_position0)) >> 1)
		                      + (uint16_t)((*(qtm_gestures_2d_config.horiz_position1)) >> 1);

		uint16_t y_position = (uint16_t)((*(qtm_gestures_2d_config.vertical_position0)) >> 1)
		                      + (uint16_t)((*(qtm_gestures_2d_config.vertical_position1)) >> 1);
#else
		uint16_t x_position = (uint16_t)((qtm_surface_cs_control1.qtm_surface_contact_data[0].h_position) >> 1)
		                      + (uint16_t)((qtm_surface_cs_control1.qtm_surface_contact_data[1].h_position) >> 1);

		uint16_t y_position = (uint16_t)((qtm_surface_cs_control1.qtm_surface_contact_data[0].v_position) >> 1)
		                      + (uint16_t)((qtm_surface_cs_control1.qtm_surface_contact_data[1].v_position) >> 1);
#endif
		touchRam[1] = (uint8_t)(x_position >> 4);
		touchRam[2] = (uint8_t)(y_position >> 4);
		touchRam[3] = 0;
		touchRam[3] = (uint8_t)((x_position & 0x000F) << 4);
		touchRam[3] |= (uint8_t)((y_position & 0x000F));
	} else
</#if>

#if (KRONO_GESTURE_ENABLE == 1u)
	{
		touchRam[1] = (uint8_t)((*(qtm_gestures_2d_config.horiz_position0) >> 4) & 0x00FF);
		touchRam[2] = (uint8_t)((*(qtm_gestures_2d_config.vertical_position0) >> 4) & 0x00FF);
		touchRam[3] = 0;
		touchRam[3] = (uint8_t)((*(qtm_gestures_2d_config.horiz_position0) & 0x000F) << 4); /* Append LSB for X */
		touchRam[3] |= (uint8_t)((*(qtm_gestures_2d_config.vertical_position0) & 0x000F));  /* Append MSB for Y */
	}
#else
	{
		touchRam[1] = (uint8_t)((qtm_surface_cs_control1.qtm_surface_contact_data->h_position >> 4) & 0x00FF);
		touchRam[2] = (uint8_t)((qtm_surface_cs_control1.qtm_surface_contact_data->v_position >> 4) & 0x00FF);
		touchRam[3] = 0;
		touchRam[3] = (uint8_t)((qtm_surface_cs_control1.qtm_surface_contact_data->h_position & 0x000F)
		                        << 4); /* Append LSB for X */
		touchRam[3] |= (uint8_t)(
		    (qtm_surface_cs_control1.qtm_surface_contact_data->v_position & 0x000F)); /* Append MSB for Y */
	}
#endif
	/* Update Touch Raw Reference and Delta */
	/* QTM start with vertical axis */
	for (uint8_t i = 0; i < SURFACE_CS_NUM_KEYS_H + SURFACE_CS_NUM_KEYS_V; i++) {
		if (i < SURFACE_CS_NUM_KEYS_H) {
			touchRaw[i]   = qtlib_key_data_set1[SURFACE_CS_START_KEY_H + i].node_data_struct_ptr->node_acq_signals;
			touchRef[i]   = qtlib_key_data_set1[SURFACE_CS_START_KEY_H + i].channel_reference;
			touchDelta[i] = (touchRaw[i] > touchRef[i]) ? (touchRaw[i] - touchRef[i]) : 0;
		} else {
			touchRaw[i]   = qtlib_key_data_set1[SURFACE_CS_START_KEY_V + i - SURFACE_CS_NUM_KEYS_H].node_data_struct_ptr->node_acq_signals;
			touchRef[i]   = qtlib_key_data_set1[SURFACE_CS_START_KEY_V + i - SURFACE_CS_NUM_KEYS_H].channel_reference;
			touchDelta[i] = (touchRaw[i] > touchRef[i]) ? (touchRaw[i] - touchRef[i]) : 0;
		}
	}

	/* Force re-calibration of the whole system */
	if (coreRam[CORERAM_CMD_ADDR] & 0x01) {
		touch_init();
		coreRam[CORERAM_CMD_ADDR] &= 0xFE;
	}
<#if (ENABLE_SURFACE1T == true)>	
	if(qtm_surface_cs_data1.qt_surface_status != previousSurfaceStatus )
<#else>	
	if(qtm_surface_cs_data1.qt_surface_cs2t_status != previousSurfaceStatus )
</#if>		
	{
		SetIRQPin();
	}

	{
		uart_send_touch_gesture_data();
	}

<#if (ENABLE_SURFACE1T == true)>	
	previousSurfaceStatus = qtm_surface_cs_data1.qt_surface_status;
<#else>
	previousSurfaceStatus = qtm_surface_cs_data1.qt_surface_cs2t_status;
</#if>	

}

void InitIRQPin(void)
{
}

void SetIRQPin(void)
{
}

void ClearIRQPin(void)
{
}

uint8_t Krono_memory_map_read(uint8_t mem_map_address)
{
	uint16_t temp_read_16bit;
	uint8_t  temp_addr_calc;
	uint8_t  return_this_byte = 0u;

	if (mem_map_address < (VADDR_CORERAM + CORERAM_SIZE)) {
		return_this_byte = coreRam[mem_map_address];
	} else if ((mem_map_address >= VADDR_TOUCHRAM) && (mem_map_address < (VADDR_TOUCHRAM + TOUCHRAM_SIZE))) {
		return_this_byte = touchRam[mem_map_address - VADDR_TOUCHRAM];
	} else if ((mem_map_address >= VADDR_CFGRAM) && (mem_map_address < (VADDR_CFGRAM + CFGRAM_SIZE))) {
		return_this_byte = cfgRam[mem_map_address - VADDR_CFGRAM];
	}
#if (KRONO_GESTURE_ENABLE == 1u)
	else if ((mem_map_address >= VADDR_GESTURECFGRAM)
	         && (mem_map_address < (VADDR_GESTURECFGRAM + GESTURECFGRAM_SIZE))) {
		return_this_byte = gestureCfgRam[mem_map_address - VADDR_GESTURECFGRAM];
	}
#endif
	else if ((mem_map_address >= VADDR_SVRAM)
	         && (mem_map_address < (VADDR_SVRAM + (SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H)))) {
		return_this_byte = touchDelta[mem_map_address - VADDR_SVRAM];
	} else if ((mem_map_address >= VADDR_RAWVALUES)
	           && (mem_map_address < (VADDR_RAWVALUES + ((SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H) << 1u)))) {
		temp_addr_calc  = mem_map_address - VADDR_RAWVALUES;
		temp_read_16bit = touchRaw[temp_addr_calc >> 1u];
		if (0u == (temp_addr_calc % 2)) {
			/* Even number -> LSB */
			return_this_byte = (uint8_t)(temp_read_16bit & 0x00FFu);
		} else {
			/* Odd number -> MSB */
			return_this_byte = (uint8_t)((temp_read_16bit & 0xFF00u) >> 8u);
		}
	} else if ((mem_map_address >= VADDR_BASEVALUES)
	           && (mem_map_address < (VADDR_BASEVALUES + ((SURFACE_CS_NUM_KEYS_V + SURFACE_CS_NUM_KEYS_H) << 1u)))) {
		temp_addr_calc  = mem_map_address - VADDR_BASEVALUES;
		temp_read_16bit = touchRef[temp_addr_calc >> 1u];
		if (0u == (temp_addr_calc % 2)) {
			/* Even number -> LSB */
			return_this_byte = (uint8_t)(temp_read_16bit & 0x00FFu);
		} else {
			/* Odd number -> MSB */
			return_this_byte = (uint8_t)((temp_read_16bit & 0xFF00u) >> 8u);
		}
	} else {
		/* Address not valid */
	}

	return return_this_byte;
}

uint8_t Krono_memory_map_write(uint8_t mem_map_address, uint8_t write_what)
{
	uint8_t return_this_byte = 0u;

	/* CMD Byte */
	if (mem_map_address == 4u) {
		coreRam[mem_map_address] = write_what;
	}
	/* Touch Config - No access to NUM_KEYS_V or NUM_KEYS_H */
	else if ((mem_map_address >= (VADDR_CFGRAM + 2u)) && (mem_map_address < (VADDR_CFGRAM + CFGRAM_SIZE))) {
		cfgRam[mem_map_address - VADDR_CFGRAM] = write_what;
	}
#if (KRONO_GESTURE_ENABLE == 1u)
	/* Gesture Config - All access */
	else if ((mem_map_address >= VADDR_GESTURECFGRAM)
	         && (mem_map_address < (VADDR_GESTURECFGRAM + GESTURECFGRAM_SIZE))) {
		gestureCfgRam[mem_map_address - VADDR_GESTURECFGRAM] = write_what;
	}
#endif
	else {
		/* Address not valid */
		return_this_byte = 1u;
	}

	if (0u == return_this_byte) {
		writeback_req = 1u;
	}

	return return_this_byte;
}

#endif
