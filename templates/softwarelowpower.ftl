<#macro lowpwer_disableevsys_saml_no_evs>
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
	touch_timer_config();
</#macro>

<#macro lowpwer_disableevsys_samc20_c21_no_evs>
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
	touch_timer_config();
</#macro>

<#macro lowpwer_disableevsys_samd20_d21_no_evs>
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(DEF_TOUCH_MEASUREMENT_PERIOD_MS);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = DEF_TOUCH_MEASUREMENT_PERIOD_MS;
	touch_timer_config();
</#macro>


<#macro lowpwer_enableevsys_saml_no_evs>
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
	touch_timer_config();
</#macro>

<#macro lowpwer_enableevsys_samc20_c21_no_evs>
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
	touch_timer_config();
</#macro>

<#macro lowpwer_enableevsys_samd20_d21_no_evs>
	RTC_Timer32Stop();  
    RTC_Timer32CompareSet(QTM_LOWPOWER_TRIGGER_PERIOD);
    RTC_Timer32Start();
	/* Store the measurement period */
	measurement_period_store = QTM_LOWPOWER_TRIGGER_PERIOD;
	touch_timer_config();
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
#define DEF_TOUCH_LOWPOWER_ENABLE ${(LOW_POWER_KEYS!="")?then("1", "0")}

/* Lowpower Key Information 
 * Bit-mask of the keys which are enabled in low-power mode
*/
#define DEF_LOWPOWER_KEYS 	${LOW_POWER_KEYS}

/* Lowpower Touch measurement periodicity
 * defines the interval between low-power touch measurement.
 * Range : 1 to 65535
 * Default: 100
*/
#define QTM_LOWPOWER_TRIGGER_PERIOD       ${LOW_POWER_TRIGGER_PERIOD}

/* Defines the touch timeout to enable auto scan
 * Waiting time for the application to switch to low-power measurement after the last touch.
 * Range : 1 to 65535
 * Default: 5000
*/
#define DEF_TOUCH_TIMEOUT	${TCH_INACTIVE_TIME}

/* Defines drift measurement period
 * If drift period is not a multiple of Low-power measurement period,
 * then drift will happen at multiples of the Low-power period,
 * which is just above the configured drift period.
 * Range: 1 to 65535 (should be more than QTM_LOWPOWER_TRIGGER_PERIOD)
 * Default: 2000
*/
#define DEF_TOUCH_DRIFT_PERIOD_MS	${DRIFT_WAKE_UP_PERIOD}

</#macro>