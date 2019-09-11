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
/*******************************************************************************
	Copyright (c) Microchip Technology Inc.  All rights reserved.

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
        LED_BUT_0_Clear();
    } else {		
        LED_BUT_0_Set();
    }

    if (0u != button2_state) {
        LED_BUT_1_Clear();
    } else {
        LED_BUT_1_Set();
    }

	/* Update PWM counter */
	if (PWM_Count < 20) {
		PWM_Count++;
	} else {
		PWM_Count = 0;
	}

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

