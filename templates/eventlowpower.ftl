<#macro lowpower_acq_param>
	/* Low-power autoscan related parameters */
	qtm_auto_scan_config_t auto_scan_setup = 
	{
	&qtlib_acq_set1,
	QTM_AUTOSCAN_NODE,
	QTM_AUTOSCAN_THRESHOLD,
	QTM_AUTOSCAN_TRIGGER_PERIOD
	};
</#macro>


<#macro lowpwer_enableevsys_saml>
	/* Enable event trigger during startup */
	/* Disable RTC to PTC event system for now */
 	EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;

    /* Set up timer with periodic event output and drift period */
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>


<#macro lowpwer_enableevsys_samd20_d21>
	/* Enable event trigger during startup */
	/* Disable RTC to PTC event system for now */
    EVSYS_REGS->EVSYS_CTRL = EVSYS_CTRL_GCLKREQ_Msk;
 	EVSYS_REGS->EVSYS_CHANNEL =  EVSYS_CHANNEL_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL) | EVSYS_CHANNEL_EVGEN(QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0);
    EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u) | EVSYS_USER_USER(QTM_AUTOSCAN_STCONV_USER);

    /* Set up timer with periodic event output and drift period */
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>

<#macro lowpwer_enableevsys_samc20_c21>
	/* Enable event trigger during startup */
	EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN(QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;

    /* Set up timer with periodic event output and drift period */
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>

<#macro lowpwer_disableevsys_saml>
	/* Disable RTC to PTC event system for now */
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;//QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;
 	EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);

    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;

</#macro>

<#macro lowpwer_disableevsys_samc20_c21>
	/* Disable RTC to PTC event system for now */
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;//QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;
 	EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);

    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
</#macro>

<#macro lowpwer_disableevsys_samd20_d21>
	/* Disable RTC to PTC event system for now */

	EVSYS_REGS->EVSYS_CTRL = EVSYS_CTRL_GCLKREQ_Msk;
 	EVSYS_REGS->EVSYS_CHANNEL =  EVSYS_CHANNEL_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL) | EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0);
    EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0) | EVSYS_USER_USER(QTM_AUTOSCAN_STCONV_USER);
	
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
</#macro>

<#macro lowpower_SAML>
/* Sleep Modes */
#define PM_SLEEP_IDLE			2u
#define PM_SLEEP_STANDBY		4u
#define PM_SLEEP_OFF			6u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4u)
#define QTM_AUTOSCAN_STCONV_USER				19u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>

<#macro lowpower_PIC32CM>
/* Sleep Modes */
#define PM_SLEEP_IDLE			2u
#define PM_SLEEP_STANDBY		4u
#define PM_SLEEP_OFF			6u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4u)
#define QTM_AUTOSCAN_STCONV_USER				46u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>

<#macro lowpower_params_saml>
/**********************************************************/
/******************* Low-power parameters *****************/
/**********************************************************/
/* Enable or disable low-power scan 
 * Range: 0 or 1.
 * Default value: 1
*/
#define DEF_TOUCH_LOWPOWER_ENABLE ${(LOW_POWER_KEYS!="")?then("1", "0")}

/* Node selection for Low-power scan. 
 * Range: 0 to (DEF_NUM_CHANNELS-1).
 * Default value: 0
*/
#define QTM_AUTOSCAN_NODE			 ${LOW_POWER_KEYS}

/* Touch detection threshold for Low-power node. 
 * Range: 0 to 255.
 * Default value:
*/
#define QTM_AUTOSCAN_THRESHOLD		 ${LOW_POWER_DET_THRESHOLD}

/* Defines the Auto scan trigger period.
 * The Low-power measurement period determine the interval between low-power touch measurement.
 * Range: NODE_SCAN_8MS to NODE_SCAN_1024MS
 * Default value: NODE_SCAN_64MS
*/
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 ${LOW_POWER_PERIOD}

/* Waiting time (in millisecond) for the application to switch to low-power measurement after the last touch.
 * Range: 1 to 65535
 * Default value: 5000
 */
#define DEF_TOUCH_TIMEOUT                       ${TCH_INACTIVE_TIME}

/* Defines drift measurement period
 * During low-power measurement, it is recommended to perform periodic active measurement to perform drifting.
 * This parameter defines the measurement interval to perform drifting.
 * Range: 1 to 65535 ( should be more than QTM_AUTOSCAN_TRIGGER_PERIOD)
 * Default value: 2000
 */
#define DEF_TOUCH_DRIFT_PERIOD_MS               ${DRIFT_WAKE_UP_PERIOD}
</#macro>

<#macro lowpower_params_samdx>
/**********************************************************/
/******************* Low-power parameters *****************/
/**********************************************************/
/* Enable or disable low-power scan 
 * Range: 0 or 1
 * Default value: 1
*/
    #define DEF_TOUCH_LOWPOWER_ENABLE ${(LOW_POWER_KEYS!="")?then("1", "0")}

/* Node selection for Low-power scan. 
 * Range: 0 to (DEF_NUM_CHANNELS-1).
 * Default value: 0
*/
	#define QTM_AUTOSCAN_NODE			 ${LOW_POWER_KEYS}

/* Touch detection threshold for Low-power node. 
 * Range: 10 to 255
 * Default value: 10
*/
#define QTM_AUTOSCAN_THRESHOLD		 ${LOW_POWER_DET_THRESHOLD}

/* Defines the Auto scan trigger period.
 * The Low-power measurement period determine the interval between low-power touch measurement.
 * Range: NODE_SCAN_4MS to NODE_SCAN_512MS
 * Default value: NODE_SCAN_64MS
*/
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 ${LOW_POWER_PERIOD}

/* Waiting time (in millisecond) for the application to switch to low-power measurement after the last touch.
 * Range: 1 to 65535
 * Default value: 5000
 */
#define DEF_TOUCH_TIMEOUT                       ${TCH_INACTIVE_TIME}

/* Defines drift measurement period
 * During low-power measurement, it is recommended to perform periodic active measurement to perform drifting.
 * This parameter defines the measurement interval to perform drifting.
 * Range: 1 to 65535 ( should be more than QTM_AUTOSCAN_TRIGGER_PERIOD)
 * Default value: 2000
 */
#define DEF_TOUCH_DRIFT_PERIOD_MS               ${DRIFT_WAKE_UP_PERIOD}
</#macro>
