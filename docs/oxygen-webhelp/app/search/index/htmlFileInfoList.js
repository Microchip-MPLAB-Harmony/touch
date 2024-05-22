define(function () {
return ["GUID-0100245C-9970-478E-8AB7-2AB1AD122157.html@@@2.3.3.3 DEF_TOUCH_DET_INT@@@Defines the number of additional touch measurements to be performed to confirm a touch or to confirm the removal of a touch. The actual additional measurement will be DEF_TOUCH_DET_INT + 1. Parameter...","GUID-01F02DDF-C663-4830-899C-DE26504B72E3.html@@@2.3.3.8 DEF_DRIFT_HOLD_TIME@@@When a sensor is in the detect state, the drifting on all other sensors is stopped. When the finger is removed (when the sensor goes out of detect state) drifting is started. &quot;Drift Hold Time&quot; defines...","GUID-02A694CF-88A5-4ADA-8785-7EEEC62D66EA.html@@@Worldwide Sales and Service@@@AMERICAS ASIA/PACIFIC ASIA/PACIFIC EUROPE Corporate Office 2355 West Chandler Blvd. Chandler, AZ 85224-6199 Tel: 480-792-7200 Fax: 480-792-7277 Technical Support: www.microchip.com/support Web...","GUID-033278AC-5674-470E-81DD-6FDA78349B00.html@@@1.1.7 How to create Low-power sensor@@@Overview This section provides step by step information for generating Low power sensor using Touch Configurator in MCC. Note: To create a new project, follow the steps in the 1.1.2 Generate Touch...","GUID-049E8C52-A686-4EF1-8D2D-2D15A9AB51F6.html@@@2.3.6.12 PINCH_ZOOM_THRESHOLD@@@This parameter is valid only if 2 finger gesture is selected. The PINCH_ZOOM_THRESHOLD limits the allowable distance between the two fingers to detect the pinch and the zoom gestures. After crossing...","GUID-04AE07CA-7B44-4458-8CA4-4BEF531E9146.html@@@1 MCC Touch Configurator@@@...","GUID-0686327D-64D2-48B1-917C-AEFDF1E5237F.html@@@2.3.4 Frequency Hop@@@This section covers parameters that control Frequency Hop and Frequency Hop Autotune behavior (Noise counter Measure Modules)...","GUID-0717A19E-633A-4537-B38D-F19CE5C5D509.html@@@1.2.1.3 Melody Driver Dependencies@@@v4.0.0 Dependencies Table 1-6.\u2000 8-bit AVR Devices Device or Family RTC UART ATTiny 1 Series 4.2.4 1.10.0 AVR DA 4.2.4 1.10.0 ATmega328PB NA 1.10.0 ATmega324PB NA 1.10.0 Table 1-7.\u2000 8-Bit PIC Devices...","GUID-073E5924-7690-4369-82E7-054342A06C2B.html@@@2.1.4.3 Status and Output Data@@@Parameter Size Range/Options Usage module_status 1 byte N/A Module status \u2013 N/A current_freq 1 byte 0-to-15 Current frequency step *filter_buffer Pointer 2/4 bytes Pointer The pointer to the filter...","GUID-07985EED-D525-413B-AEFE-78B563328687.html@@@Quality Management System@@@For information regarding Microchip\u2019s Quality Management Systems, please visit www.microchip.com/quality...","GUID-0900C929-FAA3-46A6-946C-62D38391B95D.html@@@1.2.1 Melody Touch Release Notes@@@Release 4.0.0 \u2013 Feb 2024 Features: Added Support for PTG based touch Acquisition for dsPIC33CK devices. Improvements: Improved Matrix View for Mutual Capacitance pin assignment Added option to update...","GUID-09540563-BF8B-4F4C-B8ED-E42F775C7AAE.html@@@2.3 Touch Application Parameter Reference@@@This section provides a detailed description of the touch parameters that have been initialized within the touch.h file...","GUID-0B1AEEE9-0F88-485F-85A3-0C1A0010EEE4.html@@@2.3.6.6 TAP_AREA@@@The TAP_AREA bounds the finger to an area it must stay within to be considered a tap gesture when the finger is removed and tap and hold gesture if the finger is not removed for sometime. Unit...","GUID-0B7CD064-B26C-448E-A6E9-8B297C9F1723.html@@@2.3.4.3 DEF_FREQ_AUTOTUNE_ENABLE@@@This parameter Enables / Disables the frequency hop auto-tune. Enabling the &apos;Frequency Hop Auto-Tuning&apos; feature allows the library to automatically replace the noisy frequency from the list of...","GUID-0BBB4ACA-D241-4AB5-B8E1-A772C47D643A.html@@@2.3.4.5 FREQ_AUTOTUNE_COUNT_IN@@@This parameter acts as an integrator to confirm the noise on a measurement frequency. The measurement frequency is changed ONLY if noise levels are more than the maximum variance for tune-in count...","GUID-0D464E64-1E38-4143-A61E-BAA79400BE31.html@@@2.3.6.8 EDGE_BOUNDARY@@@With Edge Boundary defined, swipe gestures that start in an edge region will be reported as edge swipe gestures in place of normal swipe gestures. To create an edge region, the EDGE_BOUNDARY is set...","GUID-0FB3F908-88EE-45CE-94F5-E97AF9049C9B.html@@@Microchip Information@@@...","GUID-125F1A93-76CC-4BD7-BACA-01844FBD5F4F.html@@@Legal Notice@@@This publication and the information herein may be used only with Microchip products, including to design, test, and integrate Microchip products with your application. Use of this information in any...","GUID-169C0569-D42D-4C1A-B8AC-BB84F6C65EC8.html@@@2.3.4.1 NUM_FREQ_STEPS@@@Defines the number of frequencies used in touch measurement. The designated frequencies will be utilized sequentially in a cyclical manner throughout the acquisition process. If more frequencies are...","GUID-1B1234C6-25EC-4E48-84F2-06A99BE6A978.html@@@2.1.6.3 Status and Output Data@@@Table 2-14.\u2000 Group Data Parameter Size Range/Options Usage scroller_group_status 1 byte Bit field Bit 7: Reburst required Bit 0: Touch detection Reburst Required = 1 Indicates that one or more...","GUID-1B491DD1-33AA-4173-9110-2E20F6740FAA.html@@@2.3.2.2 NODE_x_PARAMS@@@The Node (channel) parameters comprise of the following configuration for each node. X-Line The bit mask of the required X-line for this channel is configured here. There could be more than 1 bit set...","GUID-1C3BE8D5-631C-4D86-8747-1E3087C1B82B.html@@@2.3.5.3.8 SURFACE_CS_MIN_CONTACT@@@This surface parameter has to be tuned based on the actual contact size of the touch when moved over the surface. The contact size of the moving touch can be observed from &quot;contact_size&quot; parameter on...","GUID-1D7A3D0E-8B8A-4479-993C-FCD6ED12DAD2.html@@@2.1.7.3 Surface CS/1T APIs@@@touch_ret_t qtm_init_surface_cs(qtm_surface_cs_control_t *qtm_surface_cs_control) Description: Initialize a Surface Module Parameter: Type Description qtm_surface_cs_control_t * Pointer to Surface...","GUID-1F66BE42-2E0D-460A-93E7-09FBBC7F84CB.html@@@2.1.2.3 Acquisition Module APIs@@@touch_ret_t qtm_ptc_init_acquisition_module(qtm_acquisition_control_t* qtm_acq_control_ptr); Description: This function initializes the Acquisition module and PTC. Parameter...","GUID-21750586-F9F2-4E33-87FB-8F2994BF4744.html@@@Trademarks@@@The Microchip name and logo, the Microchip logo, Adaptec, AVR, AVR logo, AVR Freaks, BesTime, BitCloud, CryptoMemory, CryptoRF, dsPIC, flexPWR, HELDO, IGLOO, JukeBlox, KeeLoq, Kleer, LANCheck, LinkMD...","GUID-21B54348-3E8A-406E-94B6-24CACCDB10D7.html@@@1.2.2.1 Known Issues@@@Note: This section is maintained from Release v3.14.0. Refer to release notes for other releases known issue. Issue Details Affected Version Workaround/Remarks Is fixed? Issue fixed Version For...","GUID-22EE3848-59EB-4B46-A4C3-C648BB2DB0A4.html@@@2.3.5.3.1 SURFACE_CS_NUM_KEYS_H@@@It represents the number of channels forming horizontal axis. Parameter Range SURFACE_CS_NUM_KEYS_H 1 to 255...","GUID-233ADADA-7458-4CA3-A8D6-9D9C5FEA6FD8.html@@@2.1.8 2D Surface (Two-Finger Touch) CS/2T Module@@@...","GUID-23623A51-5B32-466F-B140-D7F6757E9080.html@@@2.3.5.3.4 SURFACE_CS_NUM_KEYS_V@@@It represents the number of channels forming vertical axis. Parameter Range SURFACE_CS_NUM_KEYS_V 1 to 255...","GUID-23C3B324-C0A4-4A3E-BA00-6DF846F1D29E.html@@@2.1.3.2 Data Structures@@@Parameter Size Range/Options Usage num_sensors 1 byte 0-255 The number of sensors to buffer data for median filter num_freqs 1 byte 3-to-7 The number of frequencies to cycle/depth of median filter...","GUID-2A7D96D2-2812-4E00-AED6-13AFAAB71208.html@@@2.3.4.4 FREQ_AUTOTUNE_MAX_VARIANCE@@@Sets the maximum variance for Frequency Hop Auto tune. When the &apos;Frequency Hop Auto-tune&apos; is enabled, the touch measurement frequencies are automatically changed based on noise levels. If the noise...","GUID-31075CA0-8470-4AE2-B6C6-DEE6FE0B5336.html@@@1.2.2.2 Touch Library Module Version@@@Release v3.16.0 Module Information Acquisition Modules Module Id XC32 Compiler Version Module Version SAMD20 autotune 0x000E v4.10 1.4 SAME5x/D5x 0x000F v4.10 1.5 SAMD21/HA1/DA1 Autotune 0x0024 v2.40...","GUID-328F35DA-D6F2-42F5-B23F-EFDC2A6CDAC8.html@@@2.1.8.3 Surface CS/2T APIs@@@touch_ret_t qtm_init_surface_cs2t(qtm_surface_cs2t_control_t *qtm_surface_cs2t_control); Description: Initialize a Surface CS2T Module. Parameter: Type Description qtm_surface_cs2t_control_t * Pointer...","GUID-3559BF1F-8EA0-4D86-9EB4-B275B4E989E9.html@@@2.3.2 Node Parameters@@@This section covers parameters that control individual sensor&apos;s acquisition configuration. The node parameters for each channel are defined using the following macro definitions. Example...","GUID-3860D840-9DDA-427D-BA71-9C0AA8B1354C.html@@@2.2.3 Low Power APIs@@@The APIs defined in this sections are applicable only if low-power feature is used. Not all APIs are available for all devices. void touch_configure_pm_supc(void) Description: Additional configuration...","GUID-3AC4114C-FE60-4B5D-B490-BE805286AB9A.html@@@2.3.3.7 DEF_ANTI_TCH_DRIFT_RATE@@@This parameter works in the same way as DEF_TCH_DRIFT_RATE - but in the opposite direction. When the signal value is smaller than the reference, this value defines the rate at which the sensor...","GUID-3ADC2586-4815-4563-9F4C-2631EB9E40DB.html@@@2.3.6.2 TAP_HOLD_TIMEOUT@@@If a finger stays within the bounds set by TAP_AREA and is not removed, the firmware will report a Tap Hold gesture once the gesture timer exceeds the TAP_HOLD_TIMEOUT value. HOLD_TAP is a single...","GUID-3B7D9A65-0F1A-4F05-BAB2-9DD9ED7E3470.html@@@2.1.5.2 Data Structures@@@Table 2-8.\u2000 Group Configuration Parameter Size Range/Options Usage num_key_sensors 2 bytes 1-to-65535 The number of sensor keys in the group sensor_touch_di 1 byte 0-to-255 The number of repeat...","GUID-3BE68C58-0BB1-42E5-8DC1-EC33B4A469C2.html@@@2.3.6.1 TAP_RELEASE_TIMEOUT@@@The TAP_RELEASE_TIMEOUT parameter limits the amount of time allowed between the initial finger press and the liftoff. Exceeding this value will cause the firmware to not consider the gesture as a tap...","GUID-40A1D1B4-BE5C-4BB7-A3D3-0EBAC15C9DC0.html@@@2.3.2.1 DEF_NUM_CHANNELS@@@Defines the number of channels configured by the application. The Scroller/Wheel sensor may have more than one channel. This parameter should be configured considering each channel in the...","GUID-413BE21C-6915-4CA8-8698-4AD47177FEBB.html@@@2.1.6.4 Scroller Module API@@@touch_ret_t qtm_init_scroller_module(qtm_scroller_control_t *qtm_scroller_control) Description: Initialize a Scroller Module Parameter: Type Description qtm_scroller_control_t * Pointer to Scroller...","GUID-419F33CA-D125-44BA-85E7-6DB7EC35009F.html@@@1.1.3 Tuning Options for touch in Melody/Harmony@@@Overview This section gives an overview of how to use the tune option in the touch configurator. Details The two options in touch tuning are Touch Tuning (bidirectional, requires UART Tx and Rx) This...","GUID-43626B17-7DEC-483B-B7C5-4C4D2DF7B471.html@@@2.3.3.1 DEF_NUM_SENSORS@@@Defines the number of key sensors. Parameter Range DEF_NUM_SENSORS 1 to 65535...","GUID-438D2FF7-58FA-4CD8-AEFF-052FAAD5FB48.html@@@2.2.2 Helper APIs@@@The APIs defined in this sections are not mandatory to use. These APIs can be used to get or set touch library specific state or data. uint16_t get_sensor_node_signal(uint16_t sensor_node)...","GUID-4524F4FA-8223-44A7-AAA5-541DBF8632F9.html@@@2.2 Touch Application API Reference@@@...","GUID-45C279B6-0FBC-409A-A15F-D15F9F81F3DF.html@@@2.3.6.7 SEQ_TAP_DIST_THRESHOLD@@@The SEQ_TAP_DIST_THRESHOLD parameter limits the allowable distance of the current touch&apos;s initial press from the liftoff position of the previous touch. It is used for multiple taps (double-tap...","GUID-4802499F-E71A-4F38-B352-23AFCC5146C9.html@@@2.3.6.3 SWIPE_TIMEOUT@@@The SWIPE_TIMEOUT limits the amount of time allowed for the swipe gesture (initial finger press, moving in a particular direction crossing the distance threshold and the liftoff). Ideally...","GUID-4B08DFD5-0C4C-43F2-BD59-DE8ACF6B6FD6.html@@@2.1.6.2 Data Structures@@@Table 2-12.\u2000 Group Configuration Parameter Size Range/Options Usage *qtm_touch_key_data Pointer 2/4 bytes qtm_touch_key_data_t Pointer to touch key data for the underlying set of touch keys...","GUID-4C2FEE1D-984B-4E3D-B240-079E1019F5DB.html@@@2.1.3.4 Frequency Hop APIs@@@touch_ret_t qtm_freq_hop(qtm_freq_hop_control_t *qtm_freq_hop_control); Description: Performs Frequency Hopping Algorithm. Chose the next measurements frequency from the frequency-set and perform...","GUID-4CA2D6C2-E04B-4A58-B2E6-FDE574436F2B.html@@@2.3.6.11 WHEEL_REVERSE_QUADRANT_COUNT@@@The WHEEL_REVERSE_QUADRANT_COUNT performs a similar function as WHEEL_START_QUADRANT_COUNT except it is used when changing the direction of the wheel instead of starting it new. This is used to...","GUID-50FF11EE-162F-4638-B01E-B5544EEC2DF8.html@@@2.3.1.1 DEF_TOUCH_MEASUREMENT_PERIOD_MS@@@This parameter defines the measurement period in milliseconds. The timer interrupt service routine (ISR) will be set up according to this value. If the specified time is shorter than the measurement...","GUID-51095496-E7B8-479D-A5E7-02F076A11797.html@@@1.2.1.2 Touch Library Module Version@@@Note: The module version details are not applicable for 8-bit PIC devices as the touch libraries are provided in source form. Release v4.0.0 Module Information Table 1-1.\u2000 8-bit AVR & 16-bit dsPIC...","GUID-53597E7D-1140-4B34-9A06-9AC049B8764E.html@@@2.1.7 2D Surface (One-Finger Touch) CS Module@@@...","GUID-5453F40B-CCBD-4960-8A8E-5A353B7B7DDB.html@@@2.3.5.3.2 SURFACE_CS_START_KEY_V@@@It represents the start key of the vertical axis. Parameter Range SURFACE_CS_START_KEY_V 1 to 65535...","GUID-550D5665-F55D-46EC-990C-4097CF19711A.html@@@2.2.4 Software Driven Shield APIs@@@The APIs defined in this sections are applicable only for devices which support software drivenshield option. void drivenshield_configure(void) Description: Initializes driven shield related APIs for...","GUID-5743C75C-6878-44AE-BCE7-DB219F2D720E.html@@@2.3.1.4 DEF_PTC_INTERRUPT_PRIORITY@@@Defines the interrupt priority for the PTC ISR. There will be considerable number of interrupts when the number of sensors are more. This could affect other high priority interrupts used by...","GUID-5CD5AB69-D3C0-4E51-8ABF-16A8948214B5.html@@@2.3.5.3.5 SURFACE_CS_RESOL_DB@@@It is the combination of resolution and deadband for surface. It is defined as follows, Parameter Value SURFACE_CS_RESOL_DB SURFACE_RESOL_DEADBAND (SURFACE_RESOL_8_BIT, SURFACE_DB_1_PERCENT)...","GUID-60F1A1D6-B94E-4FA9-9C93-E05332190B1E.html@@@3 Tuning Touch Applications using MPLAB\u00AE Data Visualizer@@@...","GUID-619201BB-1704-40EB-BDDB-D7FDDDC39B85.html@@@2.3.5.2 SCROLLER_x_PARAMS@@@The individual scroller sensor configurations given below can be set in this field. Scroller type This field defines the type of scroller that is used in the project. The two types include, Slider and...","GUID-62B13394-B4C2-43F4-86D9-B5D7D467F1B2.html@@@2.1.9.2 Gesture Module APIs@@@void qtm_gestures_2d_clearGesture(void); Description: Clears the previously reported gesture. Application can clear the gesture after reading it. Otherwise the gesture will be reported continuously...","GUID-665A3769-7DDF-4A2B-AF7E-8802D37BF8C0.html@@@2.3.3.4 DEF_ANTI_TCH_DET_INT@@@Defines the number of additional touch measurements to be performed to confirm a negative delta recalibration. Usually, a continuous negative delta will be observed when the system is calibrated with...","GUID-66A9218B-E52B-4017-AE9A-8F0073A051CB.html@@@2.3.3 Key Parameters@@@This section covers parameters that control Key touch detection behavior. The Key parameters for each channel are set using the following format Example, KEY_0_PARAMS \u2192 Correspond to Channel 0...","GUID-672D14EE-CB28-4991-BD75-9F1FAC42B535.html@@@2.3.1.3 DEF_PTC_CAL_AUTO_TUNE@@@The calibration type selects which parameter should be automatically tuned for optimal charge transfer. Parameter Range DEF_PTC_CAL_AUTO_TUNE (uint8_t)((DEF_PTC_TAU_TARGET &lt;&lt; CAL_CHRG_TIME_POS) |...","GUID-693C4AFF-48E6-4858-93CF-C022220C260F.html@@@2.1.5.4 Keys Module APIs@@@touch_ret_t qtm_init_sensor_key(qtm_touch_key_control_t* qtm_lib_key_group_ptr, uint8_t which_sensor_key, qtm_acq_node_data_t* acq_lib_node_ptr) Description: Initialize a touch key sensor and assigns...","GUID-6F732935-F3D6-444E-884D-697944D5C9DD.html@@@2.3.5.3.3 SURFACE_CS_START_KEY_H@@@It represents the start key of the horizontal axis. Parameter Range SURFACE_CS_START_KEY_H 1 to 65535...","GUID-6FA13B3A-D051-4A85-9C30-154CF4B79E4D.html@@@2.1.6.1 Scroller Module Typedef@@@Table 2-11.\u2000 Name Type scroller_resolution_t enum { SCR_RESOL_2_BIT = 2, SCR_RESOL_3_BIT, SCR_RESOL_4_BIT, SCR_RESOL_5_BIT, SCR_RESOL_6_BIT, SCR_RESOL_7_BIT, SCR_RESOL_8_BIT, SCR_RESOL_9_BIT...","GUID-74A85FFC-4A77-45B5-98E9-4C2C2051F503.html@@@2.3.1 Acquisition Controls@@@This section covers parameters that control the touch measurement (also known as Acquisition) behaviors that are common for all the sensors...","GUID-7551DC67-D79D-4F0C-B56F-7B17E12400E0.html@@@The Microchip Website@@@Microchip provides online support via our website at www.microchip.com/ . This website is used to make files and information easily available to customers. Some of the content available includes...","GUID-75FDE40F-49BA-41AC-8E1A-D4291FC91905.html@@@2.3.5 Scroller Parameters@@@This section covers parameters which control Slider/Wheel behaviors. The scroller parameters for each channel is set using the following format. Example, SCROLLER_0_PARAMS \u2192 Correspond to Channel 0...","GUID-7B9D3030-2B0B-43EB-8BF4-68468BA0E9E9.html@@@1.2.1.1 Known Issues@@@Note: This section is maintained from Release v3.5.0. Refer to Melody Touch Release Notes for other releases known issue. Issue Details Issue in Version Workaround Fixed? Issue fixed Version For...","GUID-7C3C36D3-CD0F-4ED8-B50F-B467AFF76A97.html@@@2.1.5.1 Keys Typedef@@@Table 2-7.\u2000 Name Type threshold_t uint8_t sensor_id_t uint16_t touch_current_time_t uint16_t touch_delta_t int16_t touch_acq_status_t uint16_t QTM_hysteresis_t enum { HYST_50, HYST_25, HYST_12_5...","GUID-7D8DA8F3-BA9C-4E06-96E1-D15C1915F377.html@@@2.1.7.1 Surface 1T Typedef@@@Table 2-15.\u2000 Name Type scr_resolution_t enum { RESOL_2_BIT = 2, RESOL_3_BIT, RESOL_4_BIT, RESOL_5_BIT, RESOL_6_BIT, RESOL_7_BIT, RESOL_8_BIT, RESOL_9_BIT, RESOL_10_BIT, RESOL_11_BIT, RESOL_12_BIT }...","GUID-7E21BA80-E1A7-4358-8B94-97DC540A754C.html@@@2.1.2.1 Data Structures@@@The acquisition module implements all functionality required for making relative measurements of sensor capacitance. This is the only module uniquely built for an individual device, as it must access...","GUID-7E83AF07-CA81-43AE-8B14-E744A7E67A72.html@@@2.1.6 Scroller Module@@@...","GUID-817EE1CB-2056-4BD1-B30D-F8E20F136C3A.html@@@2.3.6 Gesture Parameters@@@This section covers parameters that control Gesture module behaviors. Two kinds of gesture detection are possible namely, 1 Finger 1 & 2 Finger...","GUID-844935E8-037A-4FDF-B4FF-31C40471CBAB.html@@@2.3.4.2 DEF_MEDIAN_FILTER_FREQUENCIES@@@This points to the frequencies selected for the hop. There are 16 frequencies available for selection. Parameter Range DEF_MEDIAN_FILTER_FREQUENCIES FREQ_SEL_0 to FREQ_SEL_15...","GUID-85278728-278A-4F08-A3AC-EE1EB3CD57FD.html@@@2.3.6.5 VERTICAL_SWIPE_DISTANCE_THRESHOLD@@@VERTICAL_SWIPE_DISTANCE_THRESHOLD controls the distance traveled in the vertical direction for detecting Up and Down Swipe gestures. Unit: Vertical position (i.e. y - co-ordinate) Example: If...","GUID-854AA2E5-B835-4003-9BC9-1D9438DBC327.html@@@1.1.8 How to create Lump Sensor@@@Overview This section provides step by step information for Generating Lump sensor using Touch Configurator in MCC. Note: To create a new project, follow the steps in the 1.1.2 Generate Touch Project...","GUID-8A35F250-5703-4F7A-A2A4-F2289E07C181.html@@@2.3.3.9 DEF_REBURST_MODE@@@Under various conditions (like Calibration, Detect Integration, Recalibration), additional touch measurements need to be performed to confirm an activity. This parameter defines how the re-bursting...","GUID-8F2641B0-4039-483B-9BE6-5141EE667743.html@@@3.1 Visualize Touch Data Using MPLAB\u00AE Data Visualizer@@@Overview This section provides step by step information on visualize touch data using MPLAB \u00AE Data Visualizer Installation Go to Menu &gt; Tools &gt; Plugins . Check if Installed section has MPLAB \u00AE Touch...","GUID-907D5930-9DCA-4A6C-BB43-6CB4DE0DD059.html@@@2.3.3.5 DEF_ANTI_TCH_RECAL_THRSHLD@@@This parameter is complementary to DEF_ANTI_TCH_DET_INT . Where DEF_ANTI_TCH_DET_INT acts as the confirmation, this parameter acts as the threshold. If the touch delta is more than &quot;Anti Touch Recal...","GUID-90C371A1-85D9-4761-B87C-ED24B10FBC7E.html@@@2.3.1.3.2 DEF_PTC_TAU_TARGET@@@The calibration target applies a limit to the charge transfer loss allowed, where a higher setting of a target ensures a greater proportion of full charge is transferred. The PTC_TAU_TARGET is...","GUID-916BB2DD-DDCB-4105-834C-1ADE6B7883AD.html@@@2.1.4.2 Data Structures@@@Parameter Size Range/Options Usage num_sensors 1 byte 0 \u2013 255 The number of sensors to buffer data for the median filter num_freqs 1 byte 3-to-7 The number of frequencies to cycle/depth of the median...","GUID-9314BE10-D578-4ADD-900D-74BA1F9332E7.html@@@2.1.3.1 Frequency Hop Typdef@@@Table 2-4.\u2000 Name Type qtm_freq_hop_config_t struct { uint16_t num_sensors; uint8_t num_freqs; uint8_t *freq_option_select; uint8_t *median_filter_freq; } qtm_freq_hop_data_t struct { uint8_t...","GUID-932786FA-D853-4D18-80CC-22A26D6B2701.html@@@2.3.6.10 WHEEL_START_QUADRANT_COUNT@@@The wheel gesture movement can be broken down into 90 degree arcs. The firmware watches for a certain number of arcs to occur in a circular pattern before starting to report wheel gesture information...","GUID-936F6C9B-49AB-4EF7-A7D3-DCE0DC1AD0D9.html@@@1.1.6 How to enable Driven Shield@@@Note: Driven Shield is applicable only for self capacitance sensors. Steps to enable Driven Shield Include required Self Capacitance Sensors Select Configure \u2192 Driven shield \u2192 Enable Driven Shield...","GUID-962029DB-ECD4-433F-A446-BCAD9EE1D4EB.html@@@2.1.8.1 Surface 2T Typedef@@@Table 2-16.\u2000 Name Type scr_resolution_t enum { RESOL_2_BIT = 2, RESOL_3_BIT, RESOL_4_BIT, RESOL_5_BIT, RESOL_6_BIT, RESOL_7_BIT, RESOL_8_BIT, RESOL_9_BIT, RESOL_10_BIT, RESOL_11_BIT, RESOL_12_BIT }...","GUID-9930C6EA-C5A4-4744-8A8D-15169A1E4EAF.html@@@2.3.5.1 DEF_NUM_SCROLLERS@@@Defines the number of scroller sensors. Parameter Range DEF_NUM_SCROLLERS 1 to 65535 * Note: * Theoretically the scroller module supports 65535 scrollers. But it may not be possible to realize unique...","GUID-9BFC1B7A-7C53-4E72-BA9E-C1CE99E865EB.html@@@2.3.1.5 DEF_SEL_FREQ_INIT@@@This defines the default PTC&apos;s acquisition frequency. If the Frequency Hop or Frequency Hop Autotune module is used, then the acquisition frequency will be dynamically updated by those modules...","GUID-9D717B19-006E-4723-B39B-27D89839E3ED.html@@@2.1.3 Frequency Hop Module@@@...","GUID-9E54F531-6DEB-447F-987F-7D79EC6B7BC8.html@@@2.3.1.2 DEF_SENSOR_TYPE@@@Defines the type acquisition measurement type. This also depends on the sensor design and/or layout. Self-Capacitance Sensor Requires one Y-line sense pin per button. Mutual Capacitance Sensor...","GUID-9E6F4962-F7A6-4972-844C-2D1B6E397429.html@@@2.1 Touch Modular Library API Reference@@@...","GUID-9E96FD2E-AAA2-4AF7-864B-DE1D49E68EB1.html@@@2 Touch Library API and Parameter Reference@@@...","GUID-9F536B24-DCF4-4D54-A659-CBC52A0ADF15.html@@@1.1.4 How to Enable Frequency Hop Auto tune@@@Steps to enable Frequency Hop Feature Select Configure \u2192 Frequency Hop/AFA \u2192 Enable Frequency Hop/AFA Optionally, Enable Frequency Auto Tuning...","GUID-A2AD8BD9-5A18-4451-AD99-03574C777720.html@@@2.1.5 Touch Key Module@@@...","GUID-A65E1015-8F04-4A02-861C-E11A9EC33D53.html@@@2.3.5.3.6 SURFACE_CS_FILT_CFG@@@This parameter is a combination of median filter enable/disable and IIR filter configuration. It is defined as Parameter Value SURFACE_CS_FILT_CFG SURFACE_MEDIAN_IIR(Median filter enable, IIR filter...","GUID-AA97B9B5-B019-4123-935F-7081D15693D3.html@@@2.3.6.9 WHEEL_POSTSCALER@@@The clockwise wheel is performed with 4 swipes (right-&gt;down-&gt;left-&gt;up). Similarly, the anti-clockwise wheel is performed with 4 swipes (left-&gt;down-&gt;right-&gt;up). To detect a wheel, the minimum number of...","GUID-ACA244D9-9C61-4D69-AC23-B9BEC3018030.html@@@2.1.4.4 Frequency Hop AutoTune API@@@touch_ret_t qtm_freq_hop_autotune(qtm_freq_hop_autotune_control_t *qtm_freq_hop_autotune_control); Description: Performs Frequency Hopping Autotune algorithm. Measure noise in the signal value and...","GUID-ADE751AB-6E7A-439F-92BA-FF566F108B79.html@@@2.1.2.2 Status and Output Data@@@While different target hardware requires that the configuration structure for sensor nodes varies from one device to another, all acquisition modules conform to a standard sensor node data structure...","GUID-AF635E22-2BA7-4541-BA49-B71489B1971B.html@@@2.3.1.3.1 DEF_PTC_CAL_OPTION@@@This parameter determines whether the auto-tune charge time feature is enabled or not. When enabled, the auto-tune charge time feature helps to adjust the parameters to ensure full charging of the...","GUID-B191719E-170A-4DB6-A837-E15347296AB6.html@@@2.3.5.3.7 SURFACE_CS_POS_HYST@@@Position Hysteresis is applied when the direction of the position is changed and when the surface is touched. This parameter determines the number of positions that must be moved in opposite direction...","GUID-B2CED8F1-CBBD-44A1-94E0-F8D512CFB189.html@@@2.3.3.6 DEF_TCH_DRIFT_RATE@@@When there is a touch, the signal value increases above the reference. But if such signal value does not increase beyond the threshold, then the rise in signal is not due to finger touch. Usually...","GUID-B4A434FA-7A00-48F1-91E4-B56A8059E899.html@@@2.1.8.2 Data Structures@@@qtm_surface_cs2t_control_t Top-level container for surface configuration Contains pointers to data and configuration structures Struct Contents qtm_surface_cs2t_control_t qtm_surface_cs2t_data_t...","GUID-B6D103D4-6484-45BF-B1E7-3535146B2424.html@@@1.1.2 Generate Touch Project with MCC Melody@@@Objective The following procedure shows how to create a Touch project with the MCC Melody platform where touch sensors and their parameters can be graphically added and tuned. The resulting project...","GUID-BE143985-0F6A-4E8B-AAAC-97E4E900B815.html@@@1.2 Release Information@@@This section covers release notes and known issues of Touch Confiugrator in MCC Melody and Harmony3...","GUID-BFABBDB1-3005-487B-9F57-EA1C2E827990.html@@@2.1.2 Acquisition Module@@@...","GUID-C889AFDA-2BA2-4191-A426-21B463A64260.html@@@1.1.9 How to configure timers for touch project in Melody@@@8-bit ATtiny, AVRDA Devices Note: Only RTC is supported CAUTION: Do not change the API Prefix field Include RTC from Device Resources Enable Overflow Interrupt 8-bit PIC Devices CAUTION: Do not change...","GUID-CA1C46EF-6095-4F9B-97AE-537971099B22.html@@@3.2.1 Step by Step Procedure for Touch Plugin Installation@@@This section provides a step by step procedure for touch Plugin Installation in MPLAB \u00AE Data Visualizer. Tools Required : MPLAB \u00AE Data Visualizer. Download Procedure : Step 1: Open MPLAB \u00AE Data...","GUID-CBBE3B70-E32E-42D1-A048-4F5CB6609DDD.html@@@2.1.3.3 Status and Output Data@@@Parameter Size Range/Options Usage module_status 1 byte N/A Module status \u2013 N/A current_freq 1 byte 0-to-15 Current frequency step *filter_buffer 2/4 bytes N/A The pointer to the filter buffer array...","GUID-CDA512D8-0DE4-4672-8716-04CAC681CB38.html@@@Product Change Notification Service@@@Microchip\u2019s product change notification service helps keep customers current on Microchip products. Subscribers will receive email notification whenever there are changes, updates, revisions or errata...","GUID-D6ADCAD8-85F5-4D55-92DF-CF1F668542E2.html@@@2.1.5.3 Status and Output Data@@@Table 2-10.\u2000 Group Data Parameter Size Range/Options Usage qtm_keys_status 1 byte Bit 7: Reburst required Bit 6-1: Reserved Bit 0: Touch Detection Indicates the current state of the Touch Key Group...","GUID-E142E459-FE35-47E9-BABC-803D5E3A8F08.html@@@2.3.6.4 HORIZONTAL_SWIPE_DISTANCE_THRESHOLD@@@HORIZONTAL_SWIPE_DISTANCE_THRESHOLD controls the distance traveled in the horizontal direction for detecting Left and Right Swipe gestures. Unit: Horizontal position (i.e. x- co-ordinate) Example: If...","GUID-E8251634-7B15-4073-A103-5A5F128B8699.html@@@Microchip Devices Code Protection Feature@@@Note the following details of the code protection feature on Microchip products: Microchip products meet the specifications contained in their particular Microchip Data Sheet. Microchip believes that...","GUID-E90AB64F-0444-4F82-9954-B2A4D380E3AD.html@@@1.1.1 Generate Touch Project with MCC Harmony@@@Objective The following procedure shows how to create a Touch project with the MCC Harmony platform where touch sensors and their parameters can be graphically added and tuned. The resulting project...","GUID-EB762DCC-6E56-4E86-9BC8-1E91B8FA165B.html@@@2.3.3.2 KEY_x_PARAMS@@@Defines Key Sensor settings. It includes, Sensor Threshold Defines the sensor&apos;s detect threshold. When a finger touches the sensor, the touch delta increases. The sensor will be reported as touched...","GUID-EDEAD3E0-FB69-4554-808E-33904213BB26.html@@@1.1.5 How to Enable Boost Mode@@@Note: Boost Mode is applicable only for mutual capacitance sensors. Steps to enable Boost Mode Include required Mutual Capacitance Sensors Select Configure \u2192 Boost Mode \u2192 Enable Boost Mode...","GUID-EE969261-6E3F-4194-B7D0-B796C062E18A.html@@@3.2 Guide to view Touch Tune Data using MPLAB\u00AE Data Visualizer@@@This section provides information on how to visualize touch data when Bi-directional connection is enabled in the Touch Configurator. Project Configuration and Generation For creating and configuring...","GUID-EF92052F-8166-4818-99F5-4176AB370894.html@@@2.1.9.1 Data Structures@@@qtm_gestures_2d_control_t The qtm_gestures_2d_control_t data interface is a container structure which controls the input and output of this module. Field Unit Range/Options Parameter...","GUID-EFEA493D-BA96-47B9-BF1B-F920F294C875.html@@@2.3.5.3 Surface Parameters@@@This section covers parameters that control Surface behaviors. The surface dimensions (horizontal x vertical), contact size threshold, position hysteresis, resolution, dead band percentage, and...","GUID-F05182E4-B102-4775-A746-1FF37F465312.html@@@Customer Support@@@Users of Microchip products can receive assistance through several channels: Distributor or Representative Local Sales Office Embedded Solutions Engineer (ESE) Technical Support Customers should...","GUID-F08CE02A-038A-4F60-A662-4DC3F3851ECB.html@@@2.1.4.1 Frequency Hop AutoTune Typedef@@@Table 2-6.\u2000 Name Type qtm_freq_hop_autotune_config_t struct { uint16_t num_sensors; uint8_t num_freqs; uint8_t *freq_option_select; uint8_t *median_filter_freq; uint8_t enable_freq_autotune; uint8_t...","GUID-F187FFD8-1C61-495D-B8FB-59793CE5DEE1.html@@@2.1.7.2 Data Structures@@@qtm_surface_cs_control_t Top-level container for surface configuration Contains pointers to data and configuration structures Struct Contents qtm_surface_cs_control_t qtm_surface_contact_data_t...","GUID-F553B5A5-04F6-408E-BCDB-5DD9E52D3DB4.html@@@2.1.4 Frequency Hop Auto-Tune Module@@@...","GUID-F5E91405-8393-4523-95FA-DA995AC5B816.html@@@2.3.3.10 DEF_MAX_ON_DURATION@@@Max-On-Duration (MOD) defines the maximum sensor ON time. For a system, if prolonged touch is not valid, then MOD can be configured. If a sensor is in detect for more than MOD, then the sensor will be...","GUID-F8BE2E13-3EF5-4BC1-8DF8-DCE25EDE0CB9.html@@@1.2.2 Harmony3 Touch Release Notes@@@Release notes is available in github.com/Microchip-MPLAB-Harmony/touch/blob/master/release_notes.md...","GUID-F8DDEA16-BE03-4F20-A22C-EDF7C21B3A3E.html@@@2.1.1 Common Data Structures and Enum@@@touch_ret_t enum { TOUCH_SUCCESS = 0u, TOUCH_ACQ_INCOMPLETE = 1u, TOUCH_INVALID_INPUT_PARAM = 2u, TOUCH_INVALID_LIB_STATE = 3u, TOUCH_FMEA_SUCCESS = 4u, TOUCH_FMEA_ERROR = 5u, TOUCH_PC_FUNC_MAGIC_NO_1...","GUID-FBE6D9DC-DAA0-41F2-84FC-08D645DF5734.html@@@1.1 Step by Step Guide@@@...","GUID-FD4D6F17-D993-486A-93D9-15AADCD77134.html@@@2.1.9 Gestures Module@@@...","GUID-FF9A05D0-21E2-4396-A2FB-1976362A70D1.html@@@2.2.1 General APIs@@@The APIs defined in this sections are typically found in all touch projects and applicable mostly for all devices. void touch_init(void) Description: Initializes various touch library modules and...","cshelp.html@@@Context Sensitive Help@@@..."];
});