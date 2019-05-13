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

uint8_t       PWM_Count;
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
 *   			Prototypes
 *----------------------------------------------------------------------------*/
static void touch_led_status_display_1(void);

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while ( true )
    {
        touch_process();
		if (measurement_done_touch == 1)
        {
			touch_led_status_display_1();
		}
    }
    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
/*============================================================================
static void touch_led_status_display_1(void)
------------------------------------------------------------------------------
Purpose: Sample code snippet to demonstrate sensors On/OFF status using LEDs
Input  : none
Output : none
Notes  : none
============================================================================*/
static void touch_led_status_display_1(void)
{
	volatile uint8_t button1_state;
	volatile uint8_t button2_state;
	volatile uint8_t rotor_state    = 0u;
	volatile uint8_t rotor_position = 0u;

	/**
	 * Get touch sensor states
	 */
	button1_state = get_sensor_state(0) & 0x80;
	button2_state = get_sensor_state(1) & 0x80;
	rotor_state   = get_scroller_state(0);

	if (0u != button1_state) {
	   	PORT_PinClear(LED_BUT1_PIN);
	} else {
        PORT_PinSet(LED_BUT1_PIN);
	}

	if (0u != button2_state) {
		PORT_PinClear(LED_BUT2_PIN);
	} else {
		PORT_PinSet(LED_BUT2_PIN);
	}

	/* Update PWM counter */
	if (PWM_Count < 20) {
		PWM_Count++;
	} else {
		PWM_Count = 0;
	}

	/* If rotor is active */
	if (rotor_state) {
		rotor_position = get_scroller_position(0);
		rotor_position = rotor_position >> 2u;
		if (PWM_Count < PWM_RGB_values[rotor_position][0]) {
			PORT_PinClear(LED_WHEEL_R_PIN);
		} else {
			PORT_PinSet(LED_WHEEL_R_PIN);
		}

		if (PWM_Count < PWM_RGB_values[rotor_position][1]) {
			PORT_PinClear(LED_WHEEL_G_PIN);
		} else {
			PORT_PinSet(LED_WHEEL_G_PIN);
		}

		if (PWM_Count < PWM_RGB_values[rotor_position][2]) {
			PORT_PinClear(LED_WHEEL_B_PIN);
		} else {
			PORT_PinSet(LED_WHEEL_B_PIN);
		}
	} else {
		PORT_PinSet(LED_WHEEL_R_PIN);
        PORT_PinSet(LED_WHEEL_G_PIN);
		PORT_PinSet(LED_WHEEL_B_PIN);
	}
}

/*******************************************************************************
 End of File
*/

