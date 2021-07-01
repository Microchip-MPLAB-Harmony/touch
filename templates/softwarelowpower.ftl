<#macro lowpwer_disableevsys_saml_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
	touch_timer_config();
</#macro>

<#macro lowpwer_enableevsys_saml_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();  
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
	touch_timer_config();
</#macro>

<#macro lowpwer_disable_samc20_c21_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
    /* Store the measurement period */
    measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    touch_timer_config();
</#macro>

<#macro lowpwer_enable_samc20_c21_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();  
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    /* Store the measurement period */
    measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
    touch_timer_config();
</#macro>

<#-- ========================================================================================== -->
<#-- =======================================SAMD21============================================= -->

<#macro lowpwer_disableevsys_samd20_d21_no_evs>
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop(); 
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
    /* Store the measurement period */
    measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    touch_timer_config();
</#macro>

<#macro lowpwer_enableevsys_samd20_d21_no_evs>
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();  
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    RTC_Timer32Start();
    /* Store the measurement period */
    measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
    touch_timer_config();
</#macro>



<#macro lowpwer_disable_samd1x_no_evs>
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_MODE0_COUNT_COUNT_Msk) == RTC_MODE0_COUNT_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    /* Store the measurement period */
    measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    RTC_Timer32Start();
</#macro>

<#macro lowpwer_enable_samd1x_no_evs>
    while((RTC_REGS->MODE0.RTC_STATUS & RTC_MODE0_COUNT_COUNT_Msk) == RTC_MODE0_COUNT_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
    RTC_Timer32Stop();
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    /* Store the measurement period */
    measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
    RTC_Timer32Start();
</#macro>

<#macro lowpwer_disable_saml21_l22_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization before Disabling RTC */
    }
	RTC_Timer32Stop();
    RTC_REGS->MODE0.RTC_CTRLA &= ~RTC_MODE0_CTRLA_COUNTSYNC_Msk;
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    RTC_Timer32Start();
</#macro>

<#macro lowpwer_enable_saml21_l22_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization before Disabling RTC */
    }
	RTC_Timer32Stop();
    RTC_REGS->MODE0.RTC_CTRLA &= ~RTC_MODE0_CTRLA_COUNTSYNC_Msk;
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
	/* Store the measurement period */
	measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
    RTC_Timer32Start();
</#macro>

<#macro lowpwer_disable_same5x_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization before reading value from Count Register */
    }
	RTC_Timer32Stop();
    RTC_Timer32Compare0Set(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
    lp_measurement = 0;
	RTC_Timer32Start();
</#macro>

<#macro lowpwer_enable_same5x_no_evs>
    while((RTC_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization before reading value from Count Register */
    }
	RTC_Timer32Stop();  
    RTC_Timer32Compare0Set(QTM_LOWPOWER_TRIGGER_PERIOD);
	/* Store the measurement period */
	measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
    lp_measurement = 1;
    RTC_Timer32Start();
</#macro>

<#macro lowpower_touch_timer_handler_same5x_noevs>
    if (lp_measurement == 1) {
            cnt_tmr += RTC_Timer32CounterGet();
            if (cnt_tmr >= DEF_TOUCH_DRIFT_PERIOD_MS) {
                qtm_update_qtlib_timer(cnt_tmr);
                cnt_tmr = 0;
                time_to_measure_touch_var = 1u;
            } else {
                qtm_autoscan_trigger();
            }
        } else {
            
            time_to_measure_touch_var = 1u;
    #if (DEF_TOUCH_LOWPOWER_ENABLE == 1u)
            if (time_since_touch < (65535u - measurement_period_store)) {
                time_since_touch += measurement_period_store;
            } else {
                time_since_touch = 65535;
            }        
            qtm_update_qtlib_timer(measurement_period_store);
    #else
            qtm_update_qtlib_timer(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    #endif
        } /* Count complete - Measure touch sensors */
</#macro>

<#macro lowpower_SAML>
/* Sleep Modes */
#define PM_SLEEP_IDLE			2u
#define PM_SLEEP_STANDBY		4u
#define PM_SLEEP_OFF			6u
</#macro>

<#macro lowpower_params_noevs>
/**********************************************************/
/******************* Low-power parameters *****************/
/**********************************************************/
/* Enable or disable low-power scan 
 * Range: 0 or 1.
 * Default value: 1
*/
#define DEF_TOUCH_LOWPOWER_ENABLE ${(LOW_POWER_KEYS!="")?then("1u", "0u")}

/* Lowpower Key Information 
 * Bit-mask of the keys which are enabled in low-power mode
*/
#define DEF_LOWPOWER_KEYS 	${LOW_POWER_KEYS_MASK}

/* Lowpower Touch measurement periodicity
 * defines the interval between low-power touch measurement.
 * Range : 1 to 65535
 * Default: 100
*/
#define QTM_LOWPOWER_TRIGGER_PERIOD       ${LOW_POWER_TRIGGER_PERIOD}u

/* Defines the touch timeout to enable auto scan
 * Waiting time for the application to switch to low-power measurement after the last touch.
 * Range : 1 to 65535
 * Default: 5000
*/
#define DEF_TOUCH_TIMEOUT	${TCH_INACTIVE_TIME}u

/* Defines drift measurement period
 * If drift period is not a multiple of Low-power measurement period,
 * then drift will happen at multiples of the Low-power period,
 * which is just above the configured drift period.
 * Range: 1 to 65535 (should be more than QTM_LOWPOWER_TRIGGER_PERIOD)
 * Default: 2000
*/
#define DEF_TOUCH_DRIFT_PERIOD_MS	${DRIFT_WAKE_UP_PERIOD}u

</#macro>
<#macro lowpower_params_autoscan>
#define QTM_AUTOSCAN_NODE ${LOW_POWER_KEYS}

#define QTM_AUTOSCAN_THRESHOLD ${LOW_POWER_DET_THRESHOLD}

#define QTM_AUTOSCAN_TRIGGER_PERIOD QTM_LOWPOWER_TRIGGER_PERIOD

</#macro>
