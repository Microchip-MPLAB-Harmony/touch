/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

extern volatile uint8_t measurement_done_touch;
/*----------------------------------------------------------------------------
 *   Global variables
 *----------------------------------------------------------------------------*/
volatile uint8_t rotor_state = 0u;
volatile uint8_t rotor_position = 0u;
uint8_t PWM_Count = 0u;

const uint8_t PWM_RGB_values[64][3]
    = {{20, 0, 0},  {20, 0, 0}, {19, 1, 0}, {18, 2, 0},  {17, 3, 0}, {16, 4, 0},  {15, 5, 0}, {14, 6, 0},
       {13, 7, 0},  {12, 8, 0}, {11, 9, 0}, {10, 10, 0}, {9, 11, 0}, {8, 12, 0},  {7, 13, 0}, {6, 14, 0},
       {5, 15, 0},  {4, 16, 0}, {3, 17, 0}, {2, 18, 0},  {1, 19, 0}, {0, 20, 0},  {0, 20, 0}, {0, 19, 1},
       {0, 18, 2},  {0, 17, 3}, {0, 16, 4}, {0, 15, 5},  {0, 14, 6}, {0, 13, 7},  {0, 12, 8}, {0, 11, 9},
       {0, 10, 10}, {0, 9, 11}, {0, 8, 12}, {0, 7, 13},  {0, 6, 14}, {0, 5, 15},  {0, 4, 16}, {0, 3, 17},
       {0, 2, 18},  {0, 1, 19}, {0, 0, 20}, {0, 0, 20},  {1, 0, 19}, {2, 0, 18},  {3, 0, 17}, {4, 0, 16},
       {5, 0, 15},  {6, 0, 14}, {7, 0, 13}, {8, 0, 12},  {9, 0, 11}, {10, 0, 10}, {11, 0, 9}, {12, 0, 8},
       {13, 0, 7},  {14, 0, 6}, {15, 0, 5}, {16, 0, 4},  {17, 0, 3}, {18, 0, 2},  {19, 0, 1}, {19, 0, 1}};

/*----------------------------------------------------------------------------
 *   prototypes
 *----------------------------------------------------------------------------*/

static void touch_led_display_1(void);
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize(NULL);
        
    while ( true )
    {
        touch_process();
        touch_led_display_1();
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE);
}
/*============================================================================
static void touch_led_display_1(void)
------------------------------------------------------------------------------
Purpose: Sample code snippet to demonstrate sensors On/OFF status using LEDs
Input  : none
Output : none
Notes  : none
============================================================================*/

static void touch_led_display_1(void)
{
    uint8_t button1_state;
    uint8_t button2_state;
    uint8_t slider_state;
    uint8_t slider_position;

    if ((measurement_done_touch == 1u)) {

        measurement_done_touch = 0u;

        /**
         * Get touch sensor states
         */
        button1_state = get_sensor_state(0);
        button2_state = get_sensor_state(1);
        slider_state = get_scroller_state(0);

        if (button1_state == 0x03) {
            LED_BUT_0_Set();
        } else {
            LED_BUT_0_Clear();
        }

        if (button2_state == 0x03) {
            LED_BUT_1_Set();
        } else {
            LED_BUT_1_Clear();
        }

        /**
         * Clear all slider controlled LEDs
         */
        LED_0_SLIDER_Set();
        LED_1_SLIDER_Set();
        LED_2_SLIDER_Set();
        LED_3_SLIDER_Set();
        LED_4_SLIDER_Set();
        LED_5_SLIDER_Set();
        LED_6_SLIDER_Set();
        LED_7_SLIDER_Set();
        
        /**
         * If slider is activated
         */
        if (slider_state) {
            /**
             * Parse slider position
             */
            slider_position = get_scroller_position(0);
            slider_position = slider_position >> 5u;
            switch (slider_position) {
                case 0:
                    LED_0_SLIDER_Clear();
                    break;

                case 1:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    break;

                case 2:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    LED_2_SLIDER_Clear();
                    break;

                case 3:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    LED_2_SLIDER_Clear();
                    LED_3_SLIDER_Clear();
                    break;

                case 4:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    LED_2_SLIDER_Clear();
                    LED_3_SLIDER_Clear();
                    LED_4_SLIDER_Clear();
                    break;

                case 5:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    LED_2_SLIDER_Clear();
                    LED_3_SLIDER_Clear();
                    LED_4_SLIDER_Clear();
                    LED_5_SLIDER_Clear();
                    break;

                case 6:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    LED_2_SLIDER_Clear();
                    LED_3_SLIDER_Clear();
                    LED_4_SLIDER_Clear();
                    LED_5_SLIDER_Clear();
                    LED_6_SLIDER_Clear();
                    break;

                case 7:
                    LED_0_SLIDER_Clear();
                    LED_1_SLIDER_Clear();
                    LED_2_SLIDER_Clear();
                    LED_3_SLIDER_Clear();
                    LED_4_SLIDER_Clear();
                    LED_5_SLIDER_Clear();
                    LED_6_SLIDER_Clear();
                    LED_7_SLIDER_Clear();
                    break;

                default:
                    LED_0_SLIDER_Set();
                    LED_1_SLIDER_Set();
                    LED_2_SLIDER_Set();
                    LED_3_SLIDER_Set();
                    LED_4_SLIDER_Set();
                    LED_5_SLIDER_Set();
                    LED_6_SLIDER_Set();
                    LED_7_SLIDER_Set();
                    break;
            }
        }
    } /* measurement done flag */

    /* Update PWM counter */
    if (PWM_Count < 4) {
        PWM_Count++;
    } else {
        PWM_Count = 0;
    }

    rotor_state = get_scroller_state(1);
    /* If rotor is active */
    if (rotor_state) {
        rotor_position = get_scroller_position(1);
        rotor_position = rotor_position >> 2u;
        if (PWM_Count < PWM_RGB_values[rotor_position][0]) {
            LED_WHEEL_R_Clear();
        } else {
            LED_WHEEL_R_Set();
        }

        if (PWM_Count < PWM_RGB_values[rotor_position][1]) {
            LED_WHEEL_G_Clear();
        } else {
            LED_WHEEL_G_Set();
        }

        if (PWM_Count < PWM_RGB_values[rotor_position][2]) {
            LED_WHEEL_B_Clear();
        } else {
            LED_WHEEL_B_Set();
        }
    } else {
        LED_WHEEL_R_Set();
        LED_WHEEL_G_Set();
        LED_WHEEL_B_Set();
    }
}
/*******************************************************************************
 End of File
 */

