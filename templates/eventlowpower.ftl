
<#-- =======================================COMMON============================================= -->

<#macro lowpower_acq_param>
	/* Low-power autoscan related parameters */
static qtm_auto_scan_config_t auto_scan_setup 
        = {&qtlib_acq_set1, QTM_AUTOSCAN_NODE, QTM_AUTOSCAN_THRESHOLD, QTM_AUTOSCAN_TRIGGER_PERIOD};
</#macro>

<#macro lowpower_period_lookup_param>
    <#switch LOW_POWER_PERIOD>
        <#case "NODE_SCAN_8MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 8
        <#break>
        <#case "NODE_SCAN_16MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 16
        <#break>
        <#case "NODE_SCAN_32MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 32
        <#break>
        <#case "NODE_SCAN_64MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 64
        <#break>
        <#case "NODE_SCAN_128MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 128
        <#break>
        <#case "NODE_SCAN_256MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 256
        <#break>
        <#case "NODE_SCAN_512MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 512
        <#break>
        <#case "NODE_SCAN_1024MS">
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 1024
        <#break>
        <#default>
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 64
        <#break>
    </#switch>
</#macro>

<#macro lowpower_params_common>

/**********************************************************/
/******************* Low-power parameters *****************/
/**********************************************************/
/* Enable or disable low-power scan 
* Range: 0 or 1
* Default value: 1
*/
#define DEF_TOUCH_LOWPOWER_ENABLE ${(LOW_POWER_KEYS!="")?then("1u", "0u")}

/* Node selection for Low-power scan. 
* Range: 0 to (DEF_NUM_CHANNELS-1).
* Default value: 0
*/
#define QTM_AUTOSCAN_NODE			 ${LOW_POWER_KEYS}

/* Touch detection threshold for Low-power node. 
* Range: 10 to 255
* Default value: 10
*/
#define QTM_AUTOSCAN_THRESHOLD		 ${LOW_POWER_DET_THRESHOLD}u

/* Defines the Auto scan trigger period.
 * The Low-power measurement period determine the interval between low-power touch measurement.
 * Range: NODE_SCAN_4MS to NODE_SCAN_512MS 
 * Check API file to get the actual range. For certain devices, range is NODE_SCAN_8MS to NODE_SCAN_1024MS 
 * Default value: NODE_SCAN_64MS
*/
#define QTM_AUTOSCAN_TRIGGER_PERIOD	 ${LOW_POWER_PERIOD}

/* Waiting time (in millisecond) for the application to switch to low-power measurement after the last touch.
* Range: 1 to 65535
* Default value: 5000
*/
#define DEF_TOUCH_TIMEOUT                       ${TCH_INACTIVE_TIME}u

/* Defines drift measurement period
* During low-power measurement, it is recommended to perform periodic active measurement to perform drifting.
* This parameter defines the measurement interval to perform drifting.
* Range: 1 to 65535 ( should be more than QTM_AUTOSCAN_TRIGGER_PERIOD)
* Default value: 2000
*/
#define DEF_TOUCH_DRIFT_PERIOD_MS               ${DRIFT_WAKE_UP_PERIOD}u
</#macro>


<#-- ========================================================================================== -->
<#-- =======================================SAMD21============================================= -->

<#macro lowpower_touch_timer_handler_samd21_evsys>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
    time_to_measure_touch_var = 1u;
        if (time_since_touch < (65535u - measurement_period_store)) {
            time_since_touch += measurement_period_store;
        } else {
            time_since_touch = 65535;
        }
        qtm_update_qtlib_timer(measurement_period_store);
#else
        qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
#endif
</#macro>

<#macro lowpwer_enableevsys_samd20_d21>
	/* Enable event trigger */
    EVSYS_REGS->EVSYS_CTRL = EVSYS_CTRL_GCLKREQ_Msk;
    EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL) | EVSYS_CHANNEL_EVGEN((uint32_t)QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0);
    EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL+1UL) | EVSYS_USER_USER(QTM_AUTOSCAN_STCONV_USER);
    
    /* Set up timer with periodic event output and drift period */
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
    measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>

<#macro lowpwer_disableevsys_samd20_d21>
	/* Disable RTC to PTC event system */

	EVSYS_REGS->EVSYS_CTRL = EVSYS_CTRL_GCLKREQ_Msk;
 	EVSYS_REGS->EVSYS_CHANNEL =  EVSYS_CHANNEL_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL) | EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0);
    EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(0) | EVSYS_USER_USER(QTM_AUTOSCAN_STCONV_USER);
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAME5x============================================= -->

<#macro lowpwer_enable_same5x_evsys>
    /* Enable event trigger */
    EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN((uint32_t)QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1UL;

    /* Set up timer with periodic event output and drift period */
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32Compare0Set(DEF_TOUCH_DRIFT_PERIOD_MS);
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
    RTC_Timer32Start();
</#macro>

<#macro lowpwer_disable_same5x_evsys>
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;
    EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32Compare0Set(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    RTC_Timer32Start();
</#macro>

<#macro lowpower_SAME5x>
/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u


/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD+4UL)
#define QTM_AUTOSCAN_STCONV_USER				19u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>


<#-- ========================================================================================== -->
<#-- =======================================SAMC2x============================================= -->
<#macro lowpower_touch_timer_handler_samc20_c21_evsys>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
    time_to_measure_touch_var = 1u;
        if (time_since_touch < (65535u - measurement_period_store)) {
            time_since_touch += measurement_period_store;
        } else {
            time_since_touch = 65535;
        }
        qtm_update_qtlib_timer(measurement_period_store);
#else
        qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
#endif
</#macro>
<#macro lowpwer_enable_samc20_c21_evsys>
	/* Enable event trigger */
	EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN((uint32_t)QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1UL;

    /* Set up timer with periodic event output and drift period */
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>

<#macro lowpwer_disable_samc20_c21_evsys>
	/* Disable RTC to PTC event system */
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;
 	EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
</#macro>

<#macro lowpower_samc20_c21>
/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u

/* Event system parameters */
<#if  DEVICE_NAME == "PIC32CMJH01"|| DEVICE_NAME=="PIC32CMJH00">
#define QTM_AUTOSCAN_TRIGGER_GENERATOR          ((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD + 8UL)
#define QTM_AUTOSCAN_STCONV_USER                37u
<#elseif  DEVICE_NAME == "PIC32CMPL10">
#define QTM_AUTOSCAN_TRIGGER_GENERATOR          ((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD + 7UL)
#define QTM_AUTOSCAN_STCONV_USER                15u
<#else>
#define QTM_AUTOSCAN_TRIGGER_GENERATOR          ((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD + 6UL)
#define QTM_AUTOSCAN_STCONV_USER                39u
</#if>
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL            0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAMD1x============================================= -->


<#macro lowpwer_enable_samd1x_evsys>
/*Events not supported with d1x device*/
</#macro>

<#macro lowpwer_disable_samd1x_evsys>
/*Events not supported with d1x device*/
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAML2x============================================= -->

<#macro lowpwer_enable_saml21_l22_evsys>
    /* Enable event trigger */
    EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN((uint32_t)QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1UL;

    /* Set up timer with periodic event output and drift period */
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization before Disabling RTC */
    }
    RTC_Timer32Stop();
    RTC_REGS->MODE0.RTC_CTRLA &= ~RTC_MODE0_CTRLA_COUNTSYNC_Msk;
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
    /* Store the measurement period */
    measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>

<#macro lowpwer_disable_saml21_l22_evsys>
    /* Disable RTC to PTC event system */
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;
    EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);

    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization before Disabling RTC */
    }
    RTC_Timer32Stop();
    RTC_REGS->MODE0.RTC_CTRLA &= ~RTC_MODE0_CTRLA_COUNTSYNC_Msk;
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
    /* Store the measurement period */
    measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
</#macro>

<#-- ========================================================================================== -->

<#macro lowpwer_enable_saml_evsys>
    /* Enable event trigger */
    EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN((uint32_t)QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;

    /* Set up timer with periodic event output and drift period */
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
</#macro>

<#macro lowpwer_disable_saml_evsys>
    /* Disable RTC to PTC event */
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;
    EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;

</#macro>

<#macro lowpower_SAML>
/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD+4UL)
#define QTM_AUTOSCAN_STCONV_USER				19u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAML2x============================================= -->

<#macro lowpower_SAML22>
/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD+7UL)
#define QTM_AUTOSCAN_STCONV_USER				23u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>


<#macro lowpower_SAML21>
/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD+4UL)
#define QTM_AUTOSCAN_STCONV_USER				37u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>
<#-- ========================================================================================== -->

<#macro lowpower_PIC32CM>
/* Sleep Modes */
#define PM_SLEEP_IDLE			2u
#define PM_SLEEP_STANDBY		4u
#define PM_SLEEP_OFF			6u

/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD+4UL)
#define QTM_AUTOSCAN_STCONV_USER				46u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>
<#-- ========================================================================================== -->

<#macro lowpower_samd21_da1_ha1>
/* Auto scan trigger Periods */
#define NODE_SCAN_4MS		0u
#define NODE_SCAN_8MS		1u
#define NODE_SCAN_16MS		2u
#define NODE_SCAN_32MS		3u
#define NODE_SCAN_64MS		4u
#define NODE_SCAN_128MS		5u
#define NODE_SCAN_256MS		6u
#define NODE_SCAN_512MS		7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR ((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD + 4UL)
#define QTM_AUTOSCAN_STCONV_USER 28u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL 0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>

<#macro lowpower_samd20>
/* Auto scan trigger Periods */
#define NODE_SCAN_4MS		0u
#define NODE_SCAN_8MS		1u
#define NODE_SCAN_16MS		2u
#define NODE_SCAN_32MS		3u
#define NODE_SCAN_64MS		4u
#define NODE_SCAN_128MS		5u
#define NODE_SCAN_256MS		6u
#define NODE_SCAN_512MS		7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR ((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD + 4UL)
#define QTM_AUTOSCAN_STCONV_USER 13u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL 0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>

<#-- ========================================================================================== -->
<#macro lowpwer_enable_pic32cz_evsys>
	/* Enable event trigger */
    EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN((uint32_t)QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(0u) | EVSYS_CHANNEL_EDGSEL(0u) \
                                        | EVSYS_CHANNEL_ONDEMAND(1) | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1UL;

    /* Set up timer with periodic event output and drift period */
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32Compare0Set(DEF_TOUCH_DRIFT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
    
</#macro>

<#macro lowpwer_disable_pic32cz_evsys>
	 /* Disable RTC to PTC event */
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;
    EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(0) | EVSYS_CHANNEL_EDGSEL(0) \
                                        | EVSYS_CHANNEL_ONDEMAND(0) | EVSYS_CHANNEL_RUNSTDBY(0);
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = 0;
    RTC_Timer32Compare0Set(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    
</#macro>

<#macro lowpower_touch_timer_handler_pic32cz_evsys>
	time_to_measure_touch_var = 1u;
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
	qtm_update_qtlib_timer(measurement_period_store);
	if (time_since_touch < (65535u - measurement_period_store)) {
		time_since_touch += measurement_period_store;
	} else {
		time_since_touch = 65535;
	}
#else
	qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
#endif
</#macro>

<#macro lowpower_PIC32CZ>
/* Auto scan trigger Periods */
#define NODE_SCAN_8MS		0u
#define NODE_SCAN_16MS		1u
#define NODE_SCAN_32MS		2u
#define NODE_SCAN_64MS		3u
#define NODE_SCAN_128MS		4u
#define NODE_SCAN_256MS		5u
#define NODE_SCAN_512MS		6u
#define NODE_SCAN_1024MS	7u

/* Event system parameters */
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			((uint32_t)QTM_AUTOSCAN_TRIGGER_PERIOD + 6UL)
#define QTM_AUTOSCAN_STCONV_USER				 EVENT_ID_USER_PTC_STCONV
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			 0UL
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << QTM_AUTOSCAN_TRIGGER_PERIOD)
</#macro>
<#-- ========================================================================================== -->

<#macro lowpower_touch_timer_handler_saml1x_evsys>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
    time_to_measure_touch_var = 1u;
        if (time_since_touch < (65535u - measurement_period_store)) {
            time_since_touch += measurement_period_store;
        } else {
            time_since_touch = 65535;
        }
        qtm_update_qtlib_timer(measurement_period_store);
#else
        qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
#endif
</#macro>

<#macro lowpower_touch_timer_handler_saml2x_evsys>
#if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
    time_to_measure_touch_var = 1u;
        if (time_since_touch < (65535u - measurement_period_store)) {
            time_since_touch += measurement_period_store;
        } else {
            time_since_touch = 65535;
        }
        qtm_update_qtlib_timer(measurement_period_store);
#else
        qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
#endif
</#macro>