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

int main(void) {
    uint8_t key_status0 = 0;
    /* Initialize all modules */
    SYS_Initialize(NULL);
    LED_Clear();
    
    while (true) {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks();
        touch_process();
        key_status0 = get_sensor_state(0) & 0x80;

        if (0u != key_status0)
            LED_Clear();
        else
            LED_Set();
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE);
}


/*******************************************************************************
 End of File
 */

