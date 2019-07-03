#ifndef UART_H_
#define UART_H_

#include "definitions.h"                // SYS function prototypes
#include "touch/touch.h"
#include "touch/datastreamer/kronocommadaptor.h"

void uart_init_debug_data(void);
void uart_process(void);
void krono_rx_complete_callback(uintptr_t);
void krono_tx_complete_callback(uintptr_t);
void uart_send_touch_gesture_data(void);

/* Register MAP https://microchip.app.box.com/file/139775393441 */
typedef enum {
	VADDR_CORERAM           = 0x00,
	VADDR_CORERAM_END       = 0x07,
	VADDR_TOUCHRAM          = 0x10,
	VADDR_TOUCHRAM_END      = 0x15,
	VADDR_CFGRAM            = 0x20,
	VADDR_CFGRAM_END        = 0x29,
	VADDR_GESTURECFGRAM     = 0x37,
	VADDR_GESTURECFGRAM_END = 0x42,
	VADDR_COMPRAM           = 0x5e,
	VADDR_COMPRAM_END       = 0x74,
	VADDR_SENSORMAP         = 0x75,
	VADDR_SENSORMAP_END     = 0x8B,
	VADDR_SVRAM             = 0x8c,
	VADDR_SVRAM_END         = 0xa2,
	VADDR_RAWVALUES         = 0xa3,
	VADDR_RAWVALUES_END     = 0xd0,
	VADDR_BASEVALUES        = 0xd1,
	VADDR_BASEVALUES_END    = 0xfe,
	VADDR_VERSIONINFO_T     = 0xff
} VADDR_BLOCKS;

#define UART_TX_BUF_LEN 100
#define UART_RX_BUF_LEN 20

#define HEADER_AWAITING 0
#define HEADER_RECEIVED 1

#define COMMAND_DATA_MCU_TO_PC 0x01
#define COMMAND_DATA_PC_TO_MCU 0x00
#define COMMAND_INFO_MCU_TO_PC 0x81
#define COMMAND_INFO_PC_TO_MCU 0x80

#endif /* UART_H_ */
