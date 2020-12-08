
<#-- =======================================COMMON============================================= -->

<#macro lowpower_acq_param>
	/* Low-power autoscan related parameters */
	qtm_auto_scan_config_t auto_scan_setup 
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
<@lowpower_period_lookup_param/>

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


<#-- ========================================================================================== -->
<#-- =======================================SAMD21============================================= -->

<#macro lowpower_touch_timer_handler_samd21_evsys>
    if (measurement_period_store == DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
        /* Count complete - Measure touch sensors */
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
    } else {
        count_timeout += measurement_period_store;
        if (count_timeout >= DEF_TOUCH_DRIFT_PERIOD_MS) {
            count_timeout = 0;
            qtm_autoscan_node_cancel();
            time_to_measure_touch_var = 1;
        } else {
            qtm_autoscan_sensor_node(&auto_scan_setup, touch_measure_wcomp_match);
        }
    }
</#macro>

<#macro lowpwer_enableevsys_samd20_d21>
	/* Enable event trigger during startup */
	/* Disable RTC to PTC event system for now */
    EVSYS_REGS->EVSYS_CTRL = EVSYS_CTRL_GCLKREQ_Msk;
    EVSYS_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL) | EVSYS_CHANNEL_EVGEN(QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0);
    EVSYS_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u) | EVSYS_USER_USER(QTM_AUTOSCAN_STCONV_USER);
    /* Set up timer with periodic event output and drift period */
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_REGS->MODE0.RTC_INTENSET = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(QTM_AUTOSCAN_TRIGGER_PERIOD);
    RTC_Timer32Start();
	/* Store the measurement period */
    measurement_period_store = QTM_AUTOSCAN_TRIGGER_PERIOD;
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

<#macro lowpower_samd21_da1_ha1>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR          (QTM_AUTOSCAN_TRIGGER_PERIOD + 4u)
#define QTM_AUTOSCAN_STCONV_USER                28u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL            0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << ${LOW_POWER_PERIOD})
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAME5x============================================= -->

<#macro lowpwer_enable_same5x_evsys>
	/* Enable event trigger during startup */
	/* Disable RTC to PTC event system for now */
 	EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;

    /* Set up timer with periodic event output and drift period */
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32Compare0Set(DEF_TOUCH_DRIFT_PERIOD_MS);
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_DRIFT_PERIOD_MS;
    RTC_Timer32Start();
</#macro>

<#macro lowpwer_disable_same5x_evsys>
	EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = 0;//QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;
 	EVSYS_REGS->CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(0) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);

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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4)
#define QTM_AUTOSCAN_STCONV_USER				19u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << ${LOW_POWER_PERIOD})
</#macro>


<#-- ========================================================================================== -->
<#-- =======================================SAMC2x============================================= -->
<#macro lowpower_touch_timer_handler_samc20_c21_evsys>
    if (measurement_period_store == DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
        /* Count complete - Measure touch sensors */
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
    } else {
        count_timeout += measurement_period_store;
        if (count_timeout >= DEF_TOUCH_DRIFT_PERIOD_MS) {
            count_timeout = 0;
            qtm_autoscan_node_cancel();
        } else {
            qtm_autoscan_sensor_node(&auto_scan_setup, touch_measure_wcomp_match);
        }
    }
</#macro>
<#macro lowpwer_enable_samc20_c21_evsys>
	/* Enable event trigger during startup */
	EVSYS_REGS->EVSYS_CHANNEL[QTM_RTC_TO_PTC_EVSYS_CHANNEL] = EVSYS_CHANNEL_EVGEN(QTM_AUTOSCAN_TRIGGER_GENERATOR) | EVSYS_CHANNEL_PATH(2) | EVSYS_CHANNEL_EDGSEL(0) \
									 | EVSYS_CHANNEL_ONDEMAND_Msk | EVSYS_CHANNEL_RUNSTDBY(1);
    EVSYS_REGS->EVSYS_USER[QTM_AUTOSCAN_STCONV_USER] = QTM_RTC_TO_PTC_EVSYS_CHANNEL+1u;

    /* Set up timer with periodic event output and drift period */
	RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_REGS->MODE0.RTC_EVCTRL = QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT;
    RTC_Timer32CompareSet(QTM_AUTOSCAN_TRIGGER_PERIOD);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = QTM_AUTOSCAN_TRIGGER_PERIOD;
</#macro>

<#macro lowpwer_disable_samc20_c21_evsys>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR          (QTM_AUTOSCAN_TRIGGER_PERIOD + 6u)
#define QTM_AUTOSCAN_STCONV_USER                39u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL            0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << ${LOW_POWER_PERIOD})
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

<#macro lowpwer_disable_saml21_l22_evsys>
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

<#-- ========================================================================================== -->

<#macro lowpwer_enable_saml_evsys>
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

<#macro lowpwer_disable_saml_evsys>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4u)
#define QTM_AUTOSCAN_STCONV_USER				19u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << ${LOW_POWER_PERIOD})
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAML2x============================================= -->

<#macro lowpower_SAML21_SAML22>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4u)
#define QTM_AUTOSCAN_STCONV_USER				37u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << ${LOW_POWER_PERIOD})
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4u)
#define QTM_AUTOSCAN_STCONV_USER				46u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << ${LOW_POWER_PERIOD})
</#macro>

<#macro lowpower_SAMD1x>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR			(QTM_AUTOSCAN_TRIGGER_PERIOD+4u)
#define QTM_AUTOSCAN_STCONV_USER				46u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL			0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT		(1u << ${LOW_POWER_PERIOD})
</#macro>



<#macro lowpower_samd21_da1_ha1>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR (QTM_AUTOSCAN_TRIGGER_PERIOD + 4u)
#define QTM_AUTOSCAN_STCONV_USER 28u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL 0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << ${LOW_POWER_PERIOD})
</#macro>

<#macro lowpower_samd20>
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
#define QTM_AUTOSCAN_TRIGGER_GENERATOR (QTM_AUTOSCAN_TRIGGER_PERIOD + 4u)
#define QTM_AUTOSCAN_STCONV_USER 13u
#define QTM_RTC_TO_PTC_EVSYS_CHANNEL 0u
#define QTM_AUTOSCAN_TRIGGER_PERIOD_EVENT       (1u << ${LOW_POWER_PERIOD})
</#macro>


<#macro lowpower_touch_timer_handler_samdl1x_evsys>
if (measurement_period_store == DEF_TOUCH_MEASUREMENT_PERIOD_MS) {
        /* Count complete - Measure touch sensors */
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
    } else {
        count_timeout += measurement_period_store;
        if (count_timeout >= DEF_TOUCH_DRIFT_PERIOD_MS) {
            count_timeout = 0;
            qtm_autoscan_node_cancel();
        } else {
            qtm_autoscan_sensor_node(&auto_scan_setup, touch_measure_wcomp_match);

        }
    }
</#macro>