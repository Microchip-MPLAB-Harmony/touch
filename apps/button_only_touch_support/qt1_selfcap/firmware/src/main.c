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
uint8_t key_status1 = 0;
uint8_t key_status2 = 0;
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while ( true )
    {
        touch_process();
         if (measurement_done_touch == 1) {
             
             /*Get the touch status of configured buttons */
				key_status1 = get_sensor_state(0) & 0x80;
                key_status2 = get_sensor_state(1) & 0x80;
                
             /* LED indication for touch. */   
				if (0u != key_status1) {
                    PORT_PinClear(LED_BUT1_PIN);
					} else {
					PORT_PinSet(LED_BUT1_PIN);
				}
                if (0u != key_status2) {
                    PORT_PinClear(LED_BUT2_PIN);
					} else {
					PORT_PinSet(LED_BUT2_PIN);
				}
			}
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

