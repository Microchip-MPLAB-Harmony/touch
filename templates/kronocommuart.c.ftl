#include "KronoCommuart_sam.h"

#if KRONOCOMM_UART == 1u

extern struct io_descriptor *uart_io_ptr;

volatile uint8_t write_buffer[UART_TX_BUF_LEN];
uint8_t          write_buf_read_ptr;
uint8_t          write_buf_write_ptr;
uint8_t          read_buffer[UART_RX_BUF_LEN];
uint8_t          read_buf_read_ptr;
uint8_t          read_buf_write_ptr;
volatile uint8_t uart_tx_in_progress;

volatile uint8_t uart_send_ges_data_flag = 1;
volatile uint8_t transmit_completed      = 0;
uint8_t          uart_new_data_available = 0;

typedef struct tag_uart_command_info_t {
	uint8_t header_status;
	uint8_t transaction_id;
	uint8_t command_id;
	uint8_t read_write;
	uint8_t address;
	uint8_t num_of_bytes;
} uart_command_info_t;

uart_command_info_t uart_command_info;

#define UART_FIXED (5 + 2)

#define UART_GES_POS (0)
#define UART_GES_DATA_POS (UART_GES_POS + UART_FIXED - 1)
#define UART_GES_LEN (6)
#define UART_GES_END (UART_GES_POS + UART_GES_LEN + UART_FIXED - 1)
#define UART_GES_ADDR 0x10
#define UART_GES_ID 0x00

#define UART_SIG_POS (UART_GES_END + 1)
#define UART_SIG_DATA_POS (UART_SIG_POS + UART_FIXED - 1)
#define UART_SIG_LEN ((SURFACE_CS_NUM_KEYS_H + SURFACE_CS_NUM_KEYS_V) * 2)
#define UART_SIG_END (UART_SIG_POS + UART_SIG_LEN + UART_FIXED - 1)
#define UART_SIG_ADDR 0xa3
#define UART_SIG_ID 0x01

#define UART_DELTA_POS (UART_SIG_END + 1)
#define UART_DELTA_DATA_POS (UART_DELTA_POS + UART_FIXED - 1)
#define UART_DELTA_LEN ((SURFACE_CS_NUM_KEYS_H + SURFACE_CS_NUM_KEYS_V))
#define UART_DELTA_END (UART_DELTA_POS + UART_DELTA_LEN + UART_FIXED - 1)
#define UART_DELTA_ADDR 0x8c
#define UART_DELTA_ID 0x05

#define UART_HEADER 0xAD
#define UART_FOOTER 0xDA

uint8_t uart_runtime_data[UART_GES_LEN + UART_SIG_LEN + UART_DELTA_LEN + (UART_FIXED)*3];

uint8_t uart_get_char(void)
{
	uint8_t data = read_buffer[read_buf_read_ptr];
	read_buf_read_ptr++;
	if (read_buf_read_ptr == UART_RX_BUF_LEN) {
		read_buf_read_ptr = 0;
	}
	return data;
}

void uart_send_data_wait(uint8_t data)
{
	uart_tx_in_progress = 1;
	io_write(uart_io_ptr, &data, 1);
	while (uart_tx_in_progress == 1)
		;
}

void uart_send_data(void)
{
	if (uart_tx_in_progress == 0) {
		uart_tx_in_progress = 1;

		write_buf_read_ptr = 0;
		io_write(uart_io_ptr, &uart_runtime_data[write_buf_read_ptr++], 1);
	}
}

void uart_init_debug_data(void)
{
	uart_runtime_data[0]            = UART_HEADER;
	uart_runtime_data[1]            = UART_GES_LEN - 1 + UART_FIXED - 2;
	uart_runtime_data[2]            = UART_GES_ID;
	uart_runtime_data[3]            = 0x01;
	uart_runtime_data[4]            = 0x00;
	uart_runtime_data[5]            = UART_GES_ADDR;
	uart_runtime_data[UART_GES_END] = UART_FOOTER;

	uart_runtime_data[UART_SIG_POS + 0] = UART_HEADER;
	uart_runtime_data[UART_SIG_POS + 1] = UART_SIG_LEN - 1 + UART_FIXED - 2;
	uart_runtime_data[UART_SIG_POS + 2] = UART_SIG_ID;
	uart_runtime_data[UART_SIG_POS + 3] = 0x01;
	uart_runtime_data[UART_SIG_POS + 4] = 0x00;
	uart_runtime_data[UART_SIG_POS + 5] = UART_SIG_ADDR;
	uart_runtime_data[UART_SIG_END]     = UART_FOOTER;

	uart_runtime_data[UART_DELTA_POS + 0] = UART_HEADER;
	uart_runtime_data[UART_DELTA_POS + 1] = UART_DELTA_LEN - 1 + UART_FIXED - 2;
	uart_runtime_data[UART_DELTA_POS + 2] = UART_DELTA_ID;
	uart_runtime_data[UART_DELTA_POS + 3] = 0x01;
	uart_runtime_data[UART_DELTA_POS + 4] = 0x00;
	uart_runtime_data[UART_DELTA_POS + 5] = UART_DELTA_ADDR;
	uart_runtime_data[UART_DELTA_END]     = UART_FOOTER;
}

void uart_send_touch_gesture_data(void)
{
	uint8_t *dest_ptr;

	if (uart_runtime_data[0] == 0) {
		uart_init_debug_data();
	}

	if (uart_send_ges_data_flag == 1 && uart_tx_in_progress == 0) {
		dest_ptr = &uart_runtime_data[UART_GES_DATA_POS];
		for (uint8_t cnt = 0; cnt < UART_GES_LEN; cnt++) {
			*dest_ptr++ = Krono_memory_map_read(VADDR_TOUCHRAM + cnt);
		}

		dest_ptr = &uart_runtime_data[UART_SIG_DATA_POS];
		for (uint8_t cnt = 0; cnt < UART_SIG_LEN; cnt++) {
			*dest_ptr++ = Krono_memory_map_read(VADDR_RAWVALUES + cnt);
		}

		dest_ptr = &uart_runtime_data[UART_DELTA_DATA_POS];
		for (uint8_t cnt = 0; cnt < UART_DELTA_LEN; cnt++) {
			*dest_ptr++ = Krono_memory_map_read(VADDR_SVRAM + cnt);
		}

		if (uart_command_info.header_status != HEADER_RECEIVED) {
			uart_new_data_available = 1;
		}

#if (KRONO_GESTURE_ENABLE == 1u)
		qtm_gestures_2d_clearGesture();
#endif
	}
}

uint8_t uart_min_num_bytes_received(void)
{
	if (read_buf_write_ptr >= read_buf_read_ptr) {
		return (read_buf_write_ptr - read_buf_read_ptr);
	} else {
		return ((read_buf_write_ptr + UART_RX_BUF_LEN) - read_buf_read_ptr);
	}
}

uint8_t uart_tx_len = 0;

void uart_send_header(uint8_t len, uint8_t id, uint8_t address)
{
	write_buf_write_ptr = 0;
	uart_tx_len         = len + 5;

	uart_send_data_wait(UART_HEADER);
	uart_send_data_wait(len + 4);
	uart_send_data_wait(id);
	uart_send_data_wait(0x01); // fixed
	uart_send_data_wait(0x00); // fixed
	uart_send_data_wait(address);
}

void uart_process(void)
{
	uint8_t l_trans_id = 0, l_addr = 0, l_len = 0;

	if (uart_new_data_available == 1) {
		uart_new_data_available = 0;
		uart_send_data();
	}

	if (uart_min_num_bytes_received() > 4) {
		if (uart_get_char() == UART_HEADER) {
			// received some data process it
			if (uart_command_info.header_status == HEADER_AWAITING) {
				if (uart_min_num_bytes_received() > 3) {
					l_trans_id                      = uart_get_char();
					uart_command_info.command_id    = uart_get_char();
					l_addr                          = uart_get_char();
					l_len                           = uart_get_char();
					uart_command_info.header_status = HEADER_RECEIVED;
				}
			}

			if (uart_command_info.header_status == HEADER_RECEIVED) {
				read_buf_write_ptr = 0;
				read_buf_read_ptr  = 0;
				if (uart_command_info.command_id != COMMAND_INFO_PC_TO_MCU) {
					if (uart_command_info.command_id == COMMAND_INFO_MCU_TO_PC) // 0x81
					{
						while (uart_tx_in_progress == 1)
							;
						uart_send_ges_data_flag = 0;
						uart_send_header(l_len, l_trans_id, l_addr);
						for (uint8_t cnt = 0; cnt < l_len; cnt++) {
							uart_send_data_wait(Krono_memory_map_read(l_addr + cnt));
						}
						uart_send_data_wait(UART_FOOTER);
						uart_send_ges_data_flag = 1;
					} else if (uart_command_info.command_id == COMMAND_DATA_MCU_TO_PC) // 0x01
					{
						while (uart_tx_in_progress == 1)
							;
						uart_send_ges_data_flag = 0;
						uart_send_header(l_len, l_trans_id, l_addr);
						if (l_addr != 0) {
							for (uint8_t cnt = 0; cnt < l_len; cnt++) {
								uart_send_data_wait(Krono_memory_map_read(l_addr + cnt));
							}
						} else {
							uart_send_data_wait(0x00);
							uart_send_data_wait(0x00);
							uart_send_data_wait(0x00);
							uart_send_data_wait(0x50); // FIRMWARE INFORMATION
						}
						uart_send_data_wait(UART_FOOTER);
						uart_send_ges_data_flag = 1;
					} else if (uart_command_info.command_id == COMMAND_DATA_PC_TO_MCU) // 0x00
					{
						while (uart_tx_in_progress == 1)
							;
						uart_send_ges_data_flag = 0;
						uint8_t value           = l_len;
						Krono_memory_map_write(l_addr, value);
						l_len = 1;
						uart_send_header(l_len, l_trans_id, l_addr);
						uart_send_data_wait(value);
						uart_send_data_wait(UART_FOOTER);
						uart_send_ges_data_flag = 1;
					}

					uart_command_info.header_status = HEADER_AWAITING;
				} else {
					uart_command_info.header_status = HEADER_AWAITING;
				}
			}
		}
	}
}

void krono_tx_complete_callback(struct usart_async_descriptor *data)
{
	// USART TX complete interrupt
	if (uart_send_ges_data_flag != 1) {
		uart_tx_in_progress = 0;
	} else {

		if (write_buf_read_ptr < (UART_GES_LEN + UART_SIG_LEN + UART_DELTA_LEN + UART_FIXED * 3)) {
			io_write(uart_io_ptr, &uart_runtime_data[write_buf_read_ptr], 1);
			write_buf_read_ptr++;
		} else {
			uart_tx_in_progress = 0;
		}
	}
}

void krono_rx_complete_callback(struct usart_async_descriptor *data)
{
	io_read(uart_io_ptr, &read_buffer[read_buf_write_ptr], 1);

	read_buf_write_ptr++;
	if (read_buf_write_ptr == UART_RX_BUF_LEN) {
		read_buf_write_ptr = 0;
	}
}

#endif
