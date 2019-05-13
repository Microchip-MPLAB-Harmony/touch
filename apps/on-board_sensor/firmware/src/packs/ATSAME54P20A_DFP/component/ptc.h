/**
 * \file
 *
 * \brief Component description for PTC
 *
 * Copyright (c) 2017 Atmel Corporation,
 *                    a wholly owned subsidiary of Microchip Technology Inc.
 *
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the Licence at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef _SAME54_PTC_COMPONENT_
#define _SAME54_PTC_COMPONENT_

/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR PTC */
/* ========================================================================== */


#define PTC_U2500
#define REV_PTC                     0x100

/* -------- PTC_CTRLA : (PTC Offset: 0x00) (R/W 16) Control A -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t SWRST:1;          /*!< bit:      0  Software Reset                     */
    uint16_t ENABLE:1;         /*!< bit:      1  Enable                             */
    uint16_t PTCEN:1;          /*!< bit:      2  Touch Enable                       */
    uint16_t DUALSEL:2;        /*!< bit:  3.. 4  Dual Mode Trigger Selection        */
    uint16_t SLAVEEN:1;        /*!< bit:      5  Slave Enable                       */
    uint16_t RUNSTDBY:1;       /*!< bit:      6  Run in Standby                     */
    uint16_t ONDEMAND:1;       /*!< bit:      7  On Demand Control                  */
    uint16_t PRESCALER:3;      /*!< bit:  8..10  Prescaler Configuration            */
    uint16_t :4;               /*!< bit: 11..14  Reserved                           */
    uint16_t R2R:1;            /*!< bit:     15  Rail to Rail Operation Enable      */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_CTRLA_Type;

#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_CTRLA_OFFSET            0x00         /**< \brief (PTC_CTRLA offset) Control A */
#define PTC_CTRLA_RESETVALUE        _U_(0x0000)  /**< \brief (PTC_CTRLA reset_value) Control A */

#define PTC_CTRLA_SWRST_Pos         0            /**< \brief (PTC_CTRLA) Software Reset */
#define PTC_CTRLA_SWRST             (_U_(0x1) << PTC_CTRLA_SWRST_Pos)
#define PTC_CTRLA_ENABLE_Pos        1            /**< \brief (PTC_CTRLA) Enable */
#define PTC_CTRLA_ENABLE            (_U_(0x1) << PTC_CTRLA_ENABLE_Pos)
#define PTC_CTRLA_DUALSEL_Pos       3            /**< \brief (PTC_CTRLA) Dual Mode Trigger Selection */
#define PTC_CTRLA_DUALSEL_Msk       (_U_(0x3) << PTC_CTRLA_DUALSEL_Pos)
#define PTC_CTRLA_DUALSEL(value)    (PTC_CTRLA_DUALSEL_Msk & ((value) << PTC_CTRLA_DUALSEL_Pos))
#define   PTC_CTRLA_DUALSEL_BOTH_Val      _U_(0x0)   /**< \brief (PTC_CTRLA) Start event or software trigger will start a conversion on both PTCs */
#define   PTC_CTRLA_DUALSEL_INTERLEAVE_Val _U_(0x1)   /**< \brief (PTC_CTRLA) START event or software trigger will alternatingly start a conversion on PTC0 and PTC1 */
#define PTC_CTRLA_DUALSEL_BOTH      (PTC_CTRLA_DUALSEL_BOTH_Val    << PTC_CTRLA_DUALSEL_Pos)
#define PTC_CTRLA_DUALSEL_INTERLEAVE (PTC_CTRLA_DUALSEL_INTERLEAVE_Val << PTC_CTRLA_DUALSEL_Pos)
#define PTC_CTRLA_SLAVEEN_Pos       5            /**< \brief (PTC_CTRLA) Slave Enable */
#define PTC_CTRLA_SLAVEEN           (_U_(0x1) << PTC_CTRLA_SLAVEEN_Pos)
#define PTC_CTRLA_RUNSTDBY_Pos      6            /**< \brief (PTC_CTRLA) Run in Standby */
#define PTC_CTRLA_RUNSTDBY          (_U_(0x1) << PTC_CTRLA_RUNSTDBY_Pos)
#define PTC_CTRLA_ONDEMAND_Pos      7            /**< \brief (PTC_CTRLA) On Demand Control */
#define PTC_CTRLA_ONDEMAND          (_U_(0x1) << PTC_CTRLA_ONDEMAND_Pos)
#define PTC_CTRLA_PRESCALER_Pos     8            /**< \brief (PTC_CTRLA) Prescaler Configuration */
#define PTC_CTRLA_PRESCALER_Msk     (_U_(0x7) << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER(value)  (PTC_CTRLA_PRESCALER_Msk & ((value) << PTC_CTRLA_PRESCALER_Pos))
#define   PTC_CTRLA_PRESCALER_DIV2_Val    _U_(0x0)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 2 */
#define   PTC_CTRLA_PRESCALER_DIV4_Val    _U_(0x1)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 4 */
#define   PTC_CTRLA_PRESCALER_DIV8_Val    _U_(0x2)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 8 */
#define   PTC_CTRLA_PRESCALER_DIV16_Val   _U_(0x3)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 16 */
#define   PTC_CTRLA_PRESCALER_DIV32_Val   _U_(0x4)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 32 */
#define   PTC_CTRLA_PRESCALER_DIV64_Val   _U_(0x5)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 64 */
#define   PTC_CTRLA_PRESCALER_DIV128_Val  _U_(0x6)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 128 */
#define   PTC_CTRLA_PRESCALER_DIV256_Val  _U_(0x7)   /**< \brief (PTC_CTRLA) Peripheral clock divided by 256 */
#define PTC_CTRLA_PRESCALER_DIV2    (PTC_CTRLA_PRESCALER_DIV2_Val  << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV4    (PTC_CTRLA_PRESCALER_DIV4_Val  << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV8    (PTC_CTRLA_PRESCALER_DIV8_Val  << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV16   (PTC_CTRLA_PRESCALER_DIV16_Val << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV32   (PTC_CTRLA_PRESCALER_DIV32_Val << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV64   (PTC_CTRLA_PRESCALER_DIV64_Val << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV128  (PTC_CTRLA_PRESCALER_DIV128_Val << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_PRESCALER_DIV256  (PTC_CTRLA_PRESCALER_DIV256_Val << PTC_CTRLA_PRESCALER_Pos)
#define PTC_CTRLA_R2R_Pos           15           /**< \brief (PTC_CTRLA) Rail to Rail Operation Enable */
#define PTC_CTRLA_R2R               (_U_(0x1) << PTC_CTRLA_R2R_Pos)
#define PTC_CTRLA_MASK              _U_(0x87FB)  /**< \brief (PTC_CTRLA) MASK Register */

/* -------- PTC_EVCTRL : (PTC Offset: 0x02) (R/W  8) Event Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  FLUSHEI:1;        /*!< bit:      0  Flush Event Input Enable           */
    uint8_t  STARTEI:1;        /*!< bit:      1  Start Conversion Event Input Enable */
    uint8_t  FLUSHINV:1;       /*!< bit:      2  Flush Event Invert Enable          */
    uint8_t  STARTINV:1;       /*!< bit:      3  Start Conversion Event Invert Enable */
    uint8_t  RESRDYEO:1;       /*!< bit:      4  Result Ready Event Out             */
    uint8_t  WINMONEO:1;       /*!< bit:      5  Window Monitor Event Out           */
    uint8_t  :2;               /*!< bit:  6.. 7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_EVCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_EVCTRL_OFFSET           0x02         /**< \brief (PTC_EVCTRL offset) Event Control */
#define PTC_EVCTRL_RESETVALUE       _U_(0x00)    /**< \brief (PTC_EVCTRL reset_value) Event Control */

#define PTC_EVCTRL_FLUSHEI_Pos      0            /**< \brief (PTC_EVCTRL) Flush Event Input Enable */
#define PTC_EVCTRL_FLUSHEI          (_U_(0x1) << PTC_EVCTRL_FLUSHEI_Pos)
#define PTC_EVCTRL_STARTEI_Pos      1            /**< \brief (PTC_EVCTRL) Start Conversion Event Input Enable */
#define PTC_EVCTRL_STARTEI          (_U_(0x1) << PTC_EVCTRL_STARTEI_Pos)
#define PTC_EVCTRL_FLUSHINV_Pos     2            /**< \brief (PTC_EVCTRL) Flush Event Invert Enable */
#define PTC_EVCTRL_FLUSHINV         (_U_(0x1) << PTC_EVCTRL_FLUSHINV_Pos)
#define PTC_EVCTRL_STARTINV_Pos     3            /**< \brief (PTC_EVCTRL) Start Conversion Event Invert Enable */
#define PTC_EVCTRL_STARTINV         (_U_(0x1) << PTC_EVCTRL_STARTINV_Pos)
#define PTC_EVCTRL_RESRDYEO_Pos     4            /**< \brief (PTC_EVCTRL) Result Ready Event Out */
#define PTC_EVCTRL_RESRDYEO         (_U_(0x1) << PTC_EVCTRL_RESRDYEO_Pos)
#define PTC_EVCTRL_WINMONEO_Pos     5            /**< \brief (PTC_EVCTRL) Window Monitor Event Out */
#define PTC_EVCTRL_WINMONEO         (_U_(0x1) << PTC_EVCTRL_WINMONEO_Pos)
#define PTC_EVCTRL_MASK             _U_(0x3F)    /**< \brief (PTC_EVCTRL) MASK Register */

/* -------- PTC_DBGCTRL : (PTC Offset: 0x03) (R/W  8) Debug Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  DBGRUN:1;         /*!< bit:      0  Debug Run                          */
    uint8_t  :7;               /*!< bit:  1.. 7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_DBGCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_DBGCTRL_OFFSET          0x03         /**< \brief (PTC_DBGCTRL offset) Debug Control */
#define PTC_DBGCTRL_RESETVALUE      _U_(0x00)    /**< \brief (PTC_DBGCTRL reset_value) Debug Control */

#define PTC_DBGCTRL_DBGRUN_Pos      0            /**< \brief (PTC_DBGCTRL) Debug Run */
#define PTC_DBGCTRL_DBGRUN          (_U_(0x1) << PTC_DBGCTRL_DBGRUN_Pos)
#define PTC_DBGCTRL_MASK            _U_(0x01)    /**< \brief (PTC_DBGCTRL) MASK Register */

/* -------- PTC_INPUTCTRL : (PTC Offset: 0x04) (R/W 16) Input Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t MUXPOS:5;         /*!< bit:  0.. 4  Positive Mux Input Selection       */
    uint16_t :2;               /*!< bit:  5.. 6  Reserved                           */
    uint16_t DIFFMODE:1;       /*!< bit:      7  Differential Mode                  */
    uint16_t MUXNEG:5;         /*!< bit:  8..12  Negative Mux Input Selection       */
    uint16_t :2;               /*!< bit: 13..14  Reserved                           */
    uint16_t DSEQSTOP:1;       /*!< bit:     15  Stop DMA Sequencing                */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_INPUTCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_INPUTCTRL_OFFSET        0x04         /**< \brief (PTC_INPUTCTRL offset) Input Control */
#define PTC_INPUTCTRL_RESETVALUE    _U_(0x0000)  /**< \brief (PTC_INPUTCTRL reset_value) Input Control */

#define PTC_INPUTCTRL_MUXPOS_Pos    0            /**< \brief (PTC_INPUTCTRL) Positive Mux Input Selection */
#define PTC_INPUTCTRL_MUXPOS_Msk    (_U_(0x1F) << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS(value) (PTC_INPUTCTRL_MUXPOS_Msk & ((value) << PTC_INPUTCTRL_MUXPOS_Pos))
#define   PTC_INPUTCTRL_MUXPOS_AIN0_Val   _U_(0x0)   /**< \brief (PTC_INPUTCTRL) PTC AIN0 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN1_Val   _U_(0x1)   /**< \brief (PTC_INPUTCTRL) PTC AIN1 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN2_Val   _U_(0x2)   /**< \brief (PTC_INPUTCTRL) PTC AIN2 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN3_Val   _U_(0x3)   /**< \brief (PTC_INPUTCTRL) PTC AIN3 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN4_Val   _U_(0x4)   /**< \brief (PTC_INPUTCTRL) PTC AIN4 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN5_Val   _U_(0x5)   /**< \brief (PTC_INPUTCTRL) PTC AIN5 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN6_Val   _U_(0x6)   /**< \brief (PTC_INPUTCTRL) PTC AIN6 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN7_Val   _U_(0x7)   /**< \brief (PTC_INPUTCTRL) PTC AIN7 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN8_Val   _U_(0x8)   /**< \brief (PTC_INPUTCTRL) PTC AIN8 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN9_Val   _U_(0x9)   /**< \brief (PTC_INPUTCTRL) PTC AIN9 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN10_Val  _U_(0xA)   /**< \brief (PTC_INPUTCTRL) PTC AIN10 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN11_Val  _U_(0xB)   /**< \brief (PTC_INPUTCTRL) PTC AIN11 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN12_Val  _U_(0xC)   /**< \brief (PTC_INPUTCTRL) PTC AIN12 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN13_Val  _U_(0xD)   /**< \brief (PTC_INPUTCTRL) PTC AIN13 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN14_Val  _U_(0xE)   /**< \brief (PTC_INPUTCTRL) PTC AIN14 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN15_Val  _U_(0xF)   /**< \brief (PTC_INPUTCTRL) PTC AIN15 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN16_Val  _U_(0x10)   /**< \brief (PTC_INPUTCTRL) PTC AIN16 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN17_Val  _U_(0x11)   /**< \brief (PTC_INPUTCTRL) PTC AIN17 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN18_Val  _U_(0x12)   /**< \brief (PTC_INPUTCTRL) PTC AIN18 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN19_Val  _U_(0x13)   /**< \brief (PTC_INPUTCTRL) PTC AIN19 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN20_Val  _U_(0x14)   /**< \brief (PTC_INPUTCTRL) PTC AIN20 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN21_Val  _U_(0x15)   /**< \brief (PTC_INPUTCTRL) PTC AIN21 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN22_Val  _U_(0x16)   /**< \brief (PTC_INPUTCTRL) PTC AIN22 Pin */
#define   PTC_INPUTCTRL_MUXPOS_AIN23_Val  _U_(0x17)   /**< \brief (PTC_INPUTCTRL) PTC AIN23 Pin */
#define   PTC_INPUTCTRL_MUXPOS_SCALEDCOREVCC_Val _U_(0x18)   /**< \brief (PTC_INPUTCTRL) 1/4 Scaled Core Supply */
#define   PTC_INPUTCTRL_MUXPOS_SCALEDVBAT_Val _U_(0x19)   /**< \brief (PTC_INPUTCTRL) 1/4 Scaled VBAT Supply */
#define   PTC_INPUTCTRL_MUXPOS_SCALEDIOVCC_Val _U_(0x1A)   /**< \brief (PTC_INPUTCTRL) 1/4 Scaled I/O Supply */
#define   PTC_INPUTCTRL_MUXPOS_BANDGAP_Val _U_(0x1B)   /**< \brief (PTC_INPUTCTRL) Bandgap Voltage */
#define   PTC_INPUTCTRL_MUXPOS_PTAT_Val   _U_(0x1C)   /**< \brief (PTC_INPUTCTRL) Temperature Sensor */
#define   PTC_INPUTCTRL_MUXPOS_CTAT_Val   _U_(0x1D)   /**< \brief (PTC_INPUTCTRL) Temperature Sensor */
#define   PTC_INPUTCTRL_MUXPOS_DAC_Val    _U_(0x1E)   /**< \brief (PTC_INPUTCTRL) DAC Output */
#define   PTC_INPUTCTRL_MUXPOS_PTC_Val    _U_(0x1F)   /**< \brief (PTC_INPUTCTRL) PTC output (only on PTC0) */
#define PTC_INPUTCTRL_MUXPOS_AIN0   (PTC_INPUTCTRL_MUXPOS_AIN0_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN1   (PTC_INPUTCTRL_MUXPOS_AIN1_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN2   (PTC_INPUTCTRL_MUXPOS_AIN2_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN3   (PTC_INPUTCTRL_MUXPOS_AIN3_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN4   (PTC_INPUTCTRL_MUXPOS_AIN4_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN5   (PTC_INPUTCTRL_MUXPOS_AIN5_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN6   (PTC_INPUTCTRL_MUXPOS_AIN6_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN7   (PTC_INPUTCTRL_MUXPOS_AIN7_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN8   (PTC_INPUTCTRL_MUXPOS_AIN8_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN9   (PTC_INPUTCTRL_MUXPOS_AIN9_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN10  (PTC_INPUTCTRL_MUXPOS_AIN10_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN11  (PTC_INPUTCTRL_MUXPOS_AIN11_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN12  (PTC_INPUTCTRL_MUXPOS_AIN12_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN13  (PTC_INPUTCTRL_MUXPOS_AIN13_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN14  (PTC_INPUTCTRL_MUXPOS_AIN14_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN15  (PTC_INPUTCTRL_MUXPOS_AIN15_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN16  (PTC_INPUTCTRL_MUXPOS_AIN16_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN17  (PTC_INPUTCTRL_MUXPOS_AIN17_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN18  (PTC_INPUTCTRL_MUXPOS_AIN18_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN19  (PTC_INPUTCTRL_MUXPOS_AIN19_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN20  (PTC_INPUTCTRL_MUXPOS_AIN20_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN21  (PTC_INPUTCTRL_MUXPOS_AIN21_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN22  (PTC_INPUTCTRL_MUXPOS_AIN22_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_AIN23  (PTC_INPUTCTRL_MUXPOS_AIN23_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_SCALEDCOREVCC (PTC_INPUTCTRL_MUXPOS_SCALEDCOREVCC_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_SCALEDVBAT (PTC_INPUTCTRL_MUXPOS_SCALEDVBAT_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_SCALEDIOVCC (PTC_INPUTCTRL_MUXPOS_SCALEDIOVCC_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_BANDGAP (PTC_INPUTCTRL_MUXPOS_BANDGAP_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_PTAT   (PTC_INPUTCTRL_MUXPOS_PTAT_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_CTAT   (PTC_INPUTCTRL_MUXPOS_CTAT_Val << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_DAC    (PTC_INPUTCTRL_MUXPOS_DAC_Val  << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_MUXPOS_PTC    (PTC_INPUTCTRL_MUXPOS_PTC_Val  << PTC_INPUTCTRL_MUXPOS_Pos)
#define PTC_INPUTCTRL_DIFFMODE_Pos  7            /**< \brief (PTC_INPUTCTRL) Differential Mode */
#define PTC_INPUTCTRL_DIFFMODE      (_U_(0x1) << PTC_INPUTCTRL_DIFFMODE_Pos)
#define PTC_INPUTCTRL_MUXNEG_Pos    8            /**< \brief (PTC_INPUTCTRL) Negative Mux Input Selection */
#define PTC_INPUTCTRL_MUXNEG_Msk    (_U_(0x1F) << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG(value) (PTC_INPUTCTRL_MUXNEG_Msk & ((value) << PTC_INPUTCTRL_MUXNEG_Pos))
#define   PTC_INPUTCTRL_MUXNEG_AIN0_Val   _U_(0x0)   /**< \brief (PTC_INPUTCTRL) PTC AIN0 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN1_Val   _U_(0x1)   /**< \brief (PTC_INPUTCTRL) PTC AIN1 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN2_Val   _U_(0x2)   /**< \brief (PTC_INPUTCTRL) PTC AIN2 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN3_Val   _U_(0x3)   /**< \brief (PTC_INPUTCTRL) PTC AIN3 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN4_Val   _U_(0x4)   /**< \brief (PTC_INPUTCTRL) PTC AIN4 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN5_Val   _U_(0x5)   /**< \brief (PTC_INPUTCTRL) PTC AIN5 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN6_Val   _U_(0x6)   /**< \brief (PTC_INPUTCTRL) PTC AIN6 Pin */
#define   PTC_INPUTCTRL_MUXNEG_AIN7_Val   _U_(0x7)   /**< \brief (PTC_INPUTCTRL) PTC AIN7 Pin */
#define   PTC_INPUTCTRL_MUXNEG_GND_Val    _U_(0x18)   /**< \brief (PTC_INPUTCTRL) Internal Ground */
#define PTC_INPUTCTRL_MUXNEG_AIN0   (PTC_INPUTCTRL_MUXNEG_AIN0_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN1   (PTC_INPUTCTRL_MUXNEG_AIN1_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN2   (PTC_INPUTCTRL_MUXNEG_AIN2_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN3   (PTC_INPUTCTRL_MUXNEG_AIN3_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN4   (PTC_INPUTCTRL_MUXNEG_AIN4_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN5   (PTC_INPUTCTRL_MUXNEG_AIN5_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN6   (PTC_INPUTCTRL_MUXNEG_AIN6_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_AIN7   (PTC_INPUTCTRL_MUXNEG_AIN7_Val << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_MUXNEG_GND    (PTC_INPUTCTRL_MUXNEG_GND_Val  << PTC_INPUTCTRL_MUXNEG_Pos)
#define PTC_INPUTCTRL_DSEQSTOP_Pos  15           /**< \brief (PTC_INPUTCTRL) Stop DMA Sequencing */
#define PTC_INPUTCTRL_DSEQSTOP      (_U_(0x1) << PTC_INPUTCTRL_DSEQSTOP_Pos)
#define PTC_INPUTCTRL_MASK          _U_(0x9F9F)  /**< \brief (PTC_INPUTCTRL) MASK Register */

/* -------- PTC_CTRLB : (PTC Offset: 0x06) (R/W 16) Control B -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t LEFTADJ:1;        /*!< bit:      0  Left-Adjusted Result               */
    uint16_t FREERUN:1;        /*!< bit:      1  Free Running Mode                  */
    uint16_t CORREN:1;         /*!< bit:      2  Digital Correction Logic Enable    */
    uint16_t RESSEL:2;         /*!< bit:  3.. 4  Conversion Result Resolution       */
    uint16_t :3;               /*!< bit:  5.. 7  Reserved                           */
    uint16_t WINMODE:3;        /*!< bit:  8..10  Window Monitor Mode                */
    uint16_t WINSS:1;          /*!< bit:     11  Window Single Sample               */
    uint16_t :4;               /*!< bit: 12..15  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_CTRLB_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_CTRLB_OFFSET            0x06         /**< \brief (PTC_CTRLB offset) Control B */
#define PTC_CTRLB_RESETVALUE        _U_(0x0000)  /**< \brief (PTC_CTRLB reset_value) Control B */

#define PTC_CTRLB_LEFTADJ_Pos       0            /**< \brief (PTC_CTRLB) Left-Adjusted Result */
#define PTC_CTRLB_LEFTADJ           (_U_(0x1) << PTC_CTRLB_LEFTADJ_Pos)
#define PTC_CTRLB_FREERUN_Pos       1            /**< \brief (PTC_CTRLB) Free Running Mode */
#define PTC_CTRLB_FREERUN           (_U_(0x1) << PTC_CTRLB_FREERUN_Pos)
#define PTC_CTRLB_CORREN_Pos        2            /**< \brief (PTC_CTRLB) Digital Correction Logic Enable */
#define PTC_CTRLB_CORREN            (_U_(0x1) << PTC_CTRLB_CORREN_Pos)
#define PTC_CTRLB_RESSEL_Pos        3            /**< \brief (PTC_CTRLB) Conversion Result Resolution */
#define PTC_CTRLB_RESSEL_Msk        (_U_(0x3) << PTC_CTRLB_RESSEL_Pos)
#define PTC_CTRLB_RESSEL(value)     (PTC_CTRLB_RESSEL_Msk & ((value) << PTC_CTRLB_RESSEL_Pos))
#define   PTC_CTRLB_RESSEL_12BIT_Val      _U_(0x0)   /**< \brief (PTC_CTRLB) 12-bit result */
#define   PTC_CTRLB_RESSEL_16BIT_Val      _U_(0x1)   /**< \brief (PTC_CTRLB) For averaging mode output */
#define   PTC_CTRLB_RESSEL_10BIT_Val      _U_(0x2)   /**< \brief (PTC_CTRLB) 10-bit result */
#define   PTC_CTRLB_RESSEL_8BIT_Val       _U_(0x3)   /**< \brief (PTC_CTRLB) 8-bit result */
#define PTC_CTRLB_RESSEL_12BIT      (PTC_CTRLB_RESSEL_12BIT_Val    << PTC_CTRLB_RESSEL_Pos)
#define PTC_CTRLB_RESSEL_16BIT      (PTC_CTRLB_RESSEL_16BIT_Val    << PTC_CTRLB_RESSEL_Pos)
#define PTC_CTRLB_RESSEL_10BIT      (PTC_CTRLB_RESSEL_10BIT_Val    << PTC_CTRLB_RESSEL_Pos)
#define PTC_CTRLB_RESSEL_8BIT       (PTC_CTRLB_RESSEL_8BIT_Val     << PTC_CTRLB_RESSEL_Pos)
#define PTC_CTRLB_WINMODE_Pos       8            /**< \brief (PTC_CTRLB) Window Monitor Mode */
#define PTC_CTRLB_WINMODE_Msk       (_U_(0x7) << PTC_CTRLB_WINMODE_Pos)
#define PTC_CTRLB_WINMODE(value)    (PTC_CTRLB_WINMODE_Msk & ((value) << PTC_CTRLB_WINMODE_Pos))
#define   PTC_CTRLB_WINMODE_DISABLE_Val   _U_(0x0)   /**< \brief (PTC_CTRLB) No window mode (default) */
#define   PTC_CTRLB_WINMODE_MODE1_Val     _U_(0x1)   /**< \brief (PTC_CTRLB) RESULT > WINLT */
#define   PTC_CTRLB_WINMODE_MODE2_Val     _U_(0x2)   /**< \brief (PTC_CTRLB) RESULT < WINUT */
#define   PTC_CTRLB_WINMODE_MODE3_Val     _U_(0x3)   /**< \brief (PTC_CTRLB) WINLT < RESULT < WINUT */
#define   PTC_CTRLB_WINMODE_MODE4_Val     _U_(0x4)   /**< \brief (PTC_CTRLB) !(WINLT < RESULT < WINUT) */
#define PTC_CTRLB_WINMODE_DISABLE   (PTC_CTRLB_WINMODE_DISABLE_Val << PTC_CTRLB_WINMODE_Pos)
#define PTC_CTRLB_WINMODE_MODE1     (PTC_CTRLB_WINMODE_MODE1_Val   << PTC_CTRLB_WINMODE_Pos)
#define PTC_CTRLB_WINMODE_MODE2     (PTC_CTRLB_WINMODE_MODE2_Val   << PTC_CTRLB_WINMODE_Pos)
#define PTC_CTRLB_WINMODE_MODE3     (PTC_CTRLB_WINMODE_MODE3_Val   << PTC_CTRLB_WINMODE_Pos)
#define PTC_CTRLB_WINMODE_MODE4     (PTC_CTRLB_WINMODE_MODE4_Val   << PTC_CTRLB_WINMODE_Pos)
#define PTC_CTRLB_WINSS_Pos         11           /**< \brief (PTC_CTRLB) Window Single Sample */
#define PTC_CTRLB_WINSS             (_U_(0x1) << PTC_CTRLB_WINSS_Pos)
#define PTC_CTRLB_MASK              _U_(0x0F1F)  /**< \brief (PTC_CTRLB) MASK Register */

/* -------- PTC_REFCTRL : (PTC Offset: 0x08) (R/W  8) Reference Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  REFSEL:4;         /*!< bit:  0.. 3  Reference Selection                */
    uint8_t  :3;               /*!< bit:  4.. 6  Reserved                           */
    uint8_t  REFCOMP:1;        /*!< bit:      7  Reference Buffer Offset Compensation Enable */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_REFCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_REFCTRL_OFFSET          0x08         /**< \brief (PTC_REFCTRL offset) Reference Control */
#define PTC_REFCTRL_RESETVALUE      _U_(0x00)    /**< \brief (PTC_REFCTRL reset_value) Reference Control */

#define PTC_REFCTRL_REFSEL_Pos      0            /**< \brief (PTC_REFCTRL) Reference Selection */
#define PTC_REFCTRL_REFSEL_Msk      (_U_(0xF) << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFSEL(value)   (PTC_REFCTRL_REFSEL_Msk & ((value) << PTC_REFCTRL_REFSEL_Pos))
#define   PTC_REFCTRL_REFSEL_INTREF_Val   _U_(0x0)   /**< \brief (PTC_REFCTRL) Internal Bandgap Reference */
#define   PTC_REFCTRL_REFSEL_INTVCC0_Val  _U_(0x2)   /**< \brief (PTC_REFCTRL) 1/2 VDDANA */
#define   PTC_REFCTRL_REFSEL_INTVCC1_Val  _U_(0x3)   /**< \brief (PTC_REFCTRL) VDDANA */
#define   PTC_REFCTRL_REFSEL_AREFA_Val    _U_(0x4)   /**< \brief (PTC_REFCTRL) External Reference */
#define   PTC_REFCTRL_REFSEL_AREFB_Val    _U_(0x5)   /**< \brief (PTC_REFCTRL) External Reference */
#define   PTC_REFCTRL_REFSEL_AREFC_Val    _U_(0x6)   /**< \brief (PTC_REFCTRL) External Reference (only on PTC1) */
#define PTC_REFCTRL_REFSEL_INTREF   (PTC_REFCTRL_REFSEL_INTREF_Val << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFSEL_INTVCC0  (PTC_REFCTRL_REFSEL_INTVCC0_Val << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFSEL_INTVCC1  (PTC_REFCTRL_REFSEL_INTVCC1_Val << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFSEL_AREFA    (PTC_REFCTRL_REFSEL_AREFA_Val  << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFSEL_AREFB    (PTC_REFCTRL_REFSEL_AREFB_Val  << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFSEL_AREFC    (PTC_REFCTRL_REFSEL_AREFC_Val  << PTC_REFCTRL_REFSEL_Pos)
#define PTC_REFCTRL_REFCOMP_Pos     7            /**< \brief (PTC_REFCTRL) Reference Buffer Offset Compensation Enable */
#define PTC_REFCTRL_REFCOMP         (_U_(0x1) << PTC_REFCTRL_REFCOMP_Pos)
#define PTC_REFCTRL_MASK            _U_(0x8F)    /**< \brief (PTC_REFCTRL) MASK Register */

/* -------- PTC_AVGCTRL : (PTC Offset: 0x0A) (R/W  8) Average Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  SAMPLENUM:4;      /*!< bit:  0.. 3  Number of Samples to be Collected  */
    uint8_t  ADJRES:3;         /*!< bit:  4.. 6  Adjusting Result / Division Coefficient */
    uint8_t  :1;               /*!< bit:      7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_AVGCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_AVGCTRL_OFFSET          0x0A         /**< \brief (PTC_AVGCTRL offset) Average Control */
#define PTC_AVGCTRL_RESETVALUE      _U_(0x00)    /**< \brief (PTC_AVGCTRL reset_value) Average Control */

#define PTC_AVGCTRL_SAMPLENUM_Pos   0            /**< \brief (PTC_AVGCTRL) Number of Samples to be Collected */
#define PTC_AVGCTRL_SAMPLENUM_Msk   (_U_(0xF) << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM(value) (PTC_AVGCTRL_SAMPLENUM_Msk & ((value) << PTC_AVGCTRL_SAMPLENUM_Pos))
#define   PTC_AVGCTRL_SAMPLENUM_1_Val     _U_(0x0)   /**< \brief (PTC_AVGCTRL) 1 sample */
#define   PTC_AVGCTRL_SAMPLENUM_2_Val     _U_(0x1)   /**< \brief (PTC_AVGCTRL) 2 samples */
#define   PTC_AVGCTRL_SAMPLENUM_4_Val     _U_(0x2)   /**< \brief (PTC_AVGCTRL) 4 samples */
#define   PTC_AVGCTRL_SAMPLENUM_8_Val     _U_(0x3)   /**< \brief (PTC_AVGCTRL) 8 samples */
#define   PTC_AVGCTRL_SAMPLENUM_16_Val    _U_(0x4)   /**< \brief (PTC_AVGCTRL) 16 samples */
#define   PTC_AVGCTRL_SAMPLENUM_32_Val    _U_(0x5)   /**< \brief (PTC_AVGCTRL) 32 samples */
#define   PTC_AVGCTRL_SAMPLENUM_64_Val    _U_(0x6)   /**< \brief (PTC_AVGCTRL) 64 samples */
#define   PTC_AVGCTRL_SAMPLENUM_128_Val   _U_(0x7)   /**< \brief (PTC_AVGCTRL) 128 samples */
#define   PTC_AVGCTRL_SAMPLENUM_256_Val   _U_(0x8)   /**< \brief (PTC_AVGCTRL) 256 samples */
#define   PTC_AVGCTRL_SAMPLENUM_512_Val   _U_(0x9)   /**< \brief (PTC_AVGCTRL) 512 samples */
#define   PTC_AVGCTRL_SAMPLENUM_1024_Val  _U_(0xA)   /**< \brief (PTC_AVGCTRL) 1024 samples */
#define PTC_AVGCTRL_SAMPLENUM_1     (PTC_AVGCTRL_SAMPLENUM_1_Val   << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_2     (PTC_AVGCTRL_SAMPLENUM_2_Val   << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_4     (PTC_AVGCTRL_SAMPLENUM_4_Val   << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_8     (PTC_AVGCTRL_SAMPLENUM_8_Val   << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_16    (PTC_AVGCTRL_SAMPLENUM_16_Val  << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_32    (PTC_AVGCTRL_SAMPLENUM_32_Val  << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_64    (PTC_AVGCTRL_SAMPLENUM_64_Val  << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_128   (PTC_AVGCTRL_SAMPLENUM_128_Val << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_256   (PTC_AVGCTRL_SAMPLENUM_256_Val << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_512   (PTC_AVGCTRL_SAMPLENUM_512_Val << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_SAMPLENUM_1024  (PTC_AVGCTRL_SAMPLENUM_1024_Val << PTC_AVGCTRL_SAMPLENUM_Pos)
#define PTC_AVGCTRL_ADJRES_Pos      4            /**< \brief (PTC_AVGCTRL) Adjusting Result / Division Coefficient */
#define PTC_AVGCTRL_ADJRES_Msk      (_U_(0x7) << PTC_AVGCTRL_ADJRES_Pos)
#define PTC_AVGCTRL_ADJRES(value)   (PTC_AVGCTRL_ADJRES_Msk & ((value) << PTC_AVGCTRL_ADJRES_Pos))
#define PTC_AVGCTRL_MASK            _U_(0x7F)    /**< \brief (PTC_AVGCTRL) MASK Register */

/* -------- PTC_SAMPCTRL : (PTC Offset: 0x0B) (R/W  8) Sample Time Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  SAMPLEN:6;        /*!< bit:  0.. 5  Sampling Time Length               */
    uint8_t  :1;               /*!< bit:      6  Reserved                           */
    uint8_t  OFFCOMP:1;        /*!< bit:      7  Comparator Offset Compensation Enable */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_SAMPCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_SAMPCTRL_OFFSET         0x0B         /**< \brief (PTC_SAMPCTRL offset) Sample Time Control */
#define PTC_SAMPCTRL_RESETVALUE     _U_(0x00)    /**< \brief (PTC_SAMPCTRL reset_value) Sample Time Control */

#define PTC_SAMPCTRL_SAMPLEN_Pos    0            /**< \brief (PTC_SAMPCTRL) Sampling Time Length */
#define PTC_SAMPCTRL_SAMPLEN_Msk    (_U_(0x3F) << PTC_SAMPCTRL_SAMPLEN_Pos)
#define PTC_SAMPCTRL_SAMPLEN(value) (PTC_SAMPCTRL_SAMPLEN_Msk & ((value) << PTC_SAMPCTRL_SAMPLEN_Pos))
#define PTC_SAMPCTRL_OFFCOMP_Pos    7            /**< \brief (PTC_SAMPCTRL) Comparator Offset Compensation Enable */
#define PTC_SAMPCTRL_OFFCOMP        (_U_(0x1) << PTC_SAMPCTRL_OFFCOMP_Pos)
#define PTC_SAMPCTRL_MASK           _U_(0xBF)    /**< \brief (PTC_SAMPCTRL) MASK Register */

/* -------- PTC_WINLT : (PTC Offset: 0x0C) (R/W 16) Window Monitor Lower Threshold -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t WINLT:16;         /*!< bit:  0..15  Window Lower Threshold             */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_WINLT_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_WINLT_OFFSET            0x0C         /**< \brief (PTC_WINLT offset) Window Monitor Lower Threshold */
#define PTC_WINLT_RESETVALUE        _U_(0x0000)  /**< \brief (PTC_WINLT reset_value) Window Monitor Lower Threshold */

#define PTC_WINLT_WINLT_Pos         0            /**< \brief (PTC_WINLT) Window Lower Threshold */
#define PTC_WINLT_WINLT_Msk         (_U_(0xFFFF) << PTC_WINLT_WINLT_Pos)
#define PTC_WINLT_WINLT(value)      (PTC_WINLT_WINLT_Msk & ((value) << PTC_WINLT_WINLT_Pos))
#define PTC_WINLT_MASK              _U_(0xFFFF)  /**< \brief (PTC_WINLT) MASK Register */

/* -------- PTC_WINUT : (PTC Offset: 0x0E) (R/W 16) Window Monitor Upper Threshold -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t WINUT:16;         /*!< bit:  0..15  Window Upper Threshold             */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_WINUT_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_WINUT_OFFSET            0x0E         /**< \brief (PTC_WINUT offset) Window Monitor Upper Threshold */
#define PTC_WINUT_RESETVALUE        _U_(0x0000)  /**< \brief (PTC_WINUT reset_value) Window Monitor Upper Threshold */

#define PTC_WINUT_WINUT_Pos         0            /**< \brief (PTC_WINUT) Window Upper Threshold */
#define PTC_WINUT_WINUT_Msk         (_U_(0xFFFF) << PTC_WINUT_WINUT_Pos)
#define PTC_WINUT_WINUT(value)      (PTC_WINUT_WINUT_Msk & ((value) << PTC_WINUT_WINUT_Pos))
#define PTC_WINUT_MASK              _U_(0xFFFF)  /**< \brief (PTC_WINUT) MASK Register */

/* -------- PTC_GAINCORR : (PTC Offset: 0x10) (R/W 16) Gain Correction -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t GAINCORR:12;      /*!< bit:  0..11  Gain Correction Value              */
    uint16_t :4;               /*!< bit: 12..15  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_GAINCORR_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_GAINCORR_OFFSET         0x10         /**< \brief (PTC_GAINCORR offset) Gain Correction */
#define PTC_GAINCORR_RESETVALUE     _U_(0x0000)  /**< \brief (PTC_GAINCORR reset_value) Gain Correction */

#define PTC_GAINCORR_GAINCORR_Pos   0            /**< \brief (PTC_GAINCORR) Gain Correction Value */
#define PTC_GAINCORR_GAINCORR_Msk   (_U_(0xFFF) << PTC_GAINCORR_GAINCORR_Pos)
#define PTC_GAINCORR_GAINCORR(value) (PTC_GAINCORR_GAINCORR_Msk & ((value) << PTC_GAINCORR_GAINCORR_Pos))
#define PTC_GAINCORR_MASK           _U_(0x0FFF)  /**< \brief (PTC_GAINCORR) MASK Register */

/* -------- PTC_OFFSETCORR : (PTC Offset: 0x12) (R/W 16) Offset Correction -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t OFFSETCORR:12;    /*!< bit:  0..11  Offset Correction Value            */
    uint16_t :4;               /*!< bit: 12..15  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_OFFSETCORR_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_OFFSETCORR_OFFSET       0x12         /**< \brief (PTC_OFFSETCORR offset) Offset Correction */
#define PTC_OFFSETCORR_RESETVALUE   _U_(0x0000)  /**< \brief (PTC_OFFSETCORR reset_value) Offset Correction */

#define PTC_OFFSETCORR_OFFSETCORR_Pos 0            /**< \brief (PTC_OFFSETCORR) Offset Correction Value */
#define PTC_OFFSETCORR_OFFSETCORR_Msk (_U_(0xFFF) << PTC_OFFSETCORR_OFFSETCORR_Pos)
#define PTC_OFFSETCORR_OFFSETCORR(value) (PTC_OFFSETCORR_OFFSETCORR_Msk & ((value) << PTC_OFFSETCORR_OFFSETCORR_Pos))
#define PTC_OFFSETCORR_MASK         _U_(0x0FFF)  /**< \brief (PTC_OFFSETCORR) MASK Register */

/* -------- PTC_SWTRIG : (PTC Offset: 0x14) (R/W  8) Software Trigger -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  FLUSH:1;          /*!< bit:      0  PTC Conversion Flush               */
    uint8_t  START:1;          /*!< bit:      1  Start PTC Conversion               */
    uint8_t  :6;               /*!< bit:  2.. 7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_SWTRIG_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_SWTRIG_OFFSET           0x14         /**< \brief (PTC_SWTRIG offset) Software Trigger */
#define PTC_SWTRIG_RESETVALUE       _U_(0x00)    /**< \brief (PTC_SWTRIG reset_value) Software Trigger */

#define PTC_SWTRIG_FLUSH_Pos        0            /**< \brief (PTC_SWTRIG) PTC Conversion Flush */
#define PTC_SWTRIG_FLUSH            (_U_(0x1) << PTC_SWTRIG_FLUSH_Pos)
#define PTC_SWTRIG_START_Pos        1            /**< \brief (PTC_SWTRIG) Start PTC Conversion */
#define PTC_SWTRIG_START            (_U_(0x1) << PTC_SWTRIG_START_Pos)
#define PTC_SWTRIG_MASK             _U_(0x03)    /**< \brief (PTC_SWTRIG) MASK Register */
/* -------- PTC_CTRLC : (PTC Offset: 0x18) (R/W 32) Control C -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
	struct {
		uint32_t CTSM:4;           /*!< bit:  0.. 3  Capacitive Touch Sensing Mode      */
		uint32_t DRIVERSEL:2;      /*!< bit:  4.. 5  Driver Selection                   */
		uint32_t RSCEN:1;          /*!< bit:      6  Reduced Self-Cap Enable            */
		uint32_t :1;               /*!< bit:      7  Reserved                           */
		uint32_t SDS:4;            /*!< bit:  8..11  Sampling Delay Selection           */
		uint32_t ASDV:1;           /*!< bit:     12  Automatic Sampling Delay Variation */
		uint32_t CCDS:2;           /*!< bit: 13..14  Channel Change Delay Selection     */
		uint32_t :5;               /*!< bit: 15..19  Reserved                           */
		uint32_t RSEL:3;           /*!< bit: 20..22  Resistor Selection                 */
		uint32_t :9;               /*!< bit: 23..31  Reserved                           */
		} bit;                       /*!< Structure used for bit  access                  */
		uint32_t reg;                /*!< Type      used for register access              */
	} PTC_CTRLC_Type;
	#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

	#define PTC_CTRLC_OFFSET            0x18         /**< \brief (PTC_CTRLC offset) Control C */
	#define PTC_CTRLC_RESETVALUE        _U(0x00000000); /**< \brief (PTC_CTRLC reset_value) Control C */

	#define PTC_CTRLC_CTSM_Pos          0            /**< \brief (PTC_CTRLC) Capacitive Touch Sensing Mode */
	#define PTC_CTRLC_CTSM_Msk          (_U(0xF) << PTC_CTRLC_CTSM_Pos)
	#define PTC_CTRLC_CTSM(value)       (PTC_CTRLC_CTSM_Msk & ((value) << PTC_CTRLC_CTSM_Pos))
	#define PTC_CTRLC_DRIVERSEL_Pos     4            /**< \brief (PTC_CTRLC) Driver Selection */
	#define PTC_CTRLC_DRIVERSEL_Msk     (_U(0x3) << PTC_CTRLC_DRIVERSEL_Pos)
	#define PTC_CTRLC_DRIVERSEL(value)  (PTC_CTRLC_DRIVERSEL_Msk & ((value) << PTC_CTRLC_DRIVERSEL_Pos))
	#define   PTC_CTRLC_DRIVERSEL_LINEDRV_Val _U(0x0)   /**< \brief (PTC_CTRLC) Individual digital drivers */
	#define   PTC_CTRLC_DRIVERSEL_LARGEDRV_Val _U(0x1)   /**< \brief (PTC_CTRLC) Large digital driver (selfcap mode only) */
	#define   PTC_CTRLC_DRIVERSEL_PADDRV_Val  _U(0x3)   /**< \brief (PTC_CTRLC) Pads drivers */
	#define PTC_CTRLC_DRIVERSEL_LINEDRV (PTC_CTRLC_DRIVERSEL_LINEDRV_Val << PTC_CTRLC_DRIVERSEL_Pos)
	#define PTC_CTRLC_DRIVERSEL_LARGEDRV (PTC_CTRLC_DRIVERSEL_LARGEDRV_Val << PTC_CTRLC_DRIVERSEL_Pos)
	#define PTC_CTRLC_DRIVERSEL_PADDRV  (PTC_CTRLC_DRIVERSEL_PADDRV_Val << PTC_CTRLC_DRIVERSEL_Pos)
	#define PTC_CTRLC_RSCEN_Pos         6            /**< \brief (PTC_CTRLC) Reduced Self-Cap Enable */
	#define PTC_CTRLC_RSCEN             (_U(0x1) << PTC_CTRLC_RSCEN_Pos)
	#define PTC_CTRLC_SDS_Pos           8            /**< \brief (PTC_CTRLC) Sampling Delay Selection */
	#define PTC_CTRLC_SDS_Msk           (_U(0xF) << PTC_CTRLC_SDS_Pos)
	#define PTC_CTRLC_SDS(value)        (PTC_CTRLC_SDS_Msk & ((value) << PTC_CTRLC_SDS_Pos))
	#define PTC_CTRLC_ASDV_Pos          12           /**< \brief (PTC_CTRLC) Automatic Sampling Delay Variation */
	#define PTC_CTRLC_ASDV              (_U(0x1) << PTC_CTRLC_ASDV_Pos)
	#define PTC_CTRLC_CCDS_Pos          13           /**< \brief (PTC_CTRLC) Channel Change Delay Selection */
	#define PTC_CTRLC_CCDS_Msk          (_U(0x3) << PTC_CTRLC_CCDS_Pos)
	#define PTC_CTRLC_CCDS(value)       (PTC_CTRLC_CCDS_Msk & ((value) << PTC_CTRLC_CCDS_Pos))
	#define PTC_CTRLC_RSEL_Pos          20           /**< \brief (PTC_CTRLC) Resistor Selection */
	#define PTC_CTRLC_RSEL_Msk          (_U(0x7) << PTC_CTRLC_RSEL_Pos)
	#define PTC_CTRLC_RSEL(value)       (PTC_CTRLC_RSEL_Msk & ((value) << PTC_CTRLC_RSEL_Pos))
	#define PTC_CTRLC_MASK              _U(0x00707F7F) /**< \brief (PTC_CTRLC) MASK Register */

	/* -------- PTC_CTRLD : (PTC Offset: 0x1C) (R/W 32) Control D -------- */
	#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
	typedef union {
		struct {
			uint32_t CCA:4;            /*!< bit:  0.. 3  Compensation Capacitor Accurate Value */
			uint32_t CCF:4;            /*!< bit:  4.. 7  Compensation Capacitor Fine Value  */
			uint32_t CCC:4;            /*!< bit:  8..11  Compensation Capacitor Coarse Value */
			uint32_t CCR:2;            /*!< bit: 12..13  Compensation Capacitor Rough Value */
			uint32_t :2;               /*!< bit: 14..15  Reserved                           */
			uint32_t CIF:4;            /*!< bit: 16..19  Integration Capacitor Fine Value   */
			uint32_t CIC:2;            /*!< bit: 20..21  Integration Capacitor Coarse Value */
			uint32_t :10;              /*!< bit: 22..31  Reserved                           */
			} bit;                       /*!< Structure used for bit  access                  */
			uint32_t reg;                /*!< Type      used for register access              */
		} PTC_CTRLD_Type;
		#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

		#define PTC_CTRLD_OFFSET            0x1C         /**< \brief (PTC_CTRLD offset) Control D */
		#define PTC_CTRLD_RESETVALUE        _U(0x00000000); /**< \brief (PTC_CTRLD reset_value) Control D */

		#define PTC_CTRLD_CCA_Pos           0            /**< \brief (PTC_CTRLD) Compensation Capacitor Accurate Value */
		#define PTC_CTRLD_CCA_Msk           (_U(0xF) << PTC_CTRLD_CCA_Pos)
		#define PTC_CTRLD_CCA(value)        (PTC_CTRLD_CCA_Msk & ((value) << PTC_CTRLD_CCA_Pos))
		#define PTC_CTRLD_CCF_Pos           4            /**< \brief (PTC_CTRLD) Compensation Capacitor Fine Value */
		#define PTC_CTRLD_CCF_Msk           (_U(0xF) << PTC_CTRLD_CCF_Pos)
		#define PTC_CTRLD_CCF(value)        (PTC_CTRLD_CCF_Msk & ((value) << PTC_CTRLD_CCF_Pos))
		#define PTC_CTRLD_CCC_Pos           8            /**< \brief (PTC_CTRLD) Compensation Capacitor Coarse Value */
		#define PTC_CTRLD_CCC_Msk           (_U(0xF) << PTC_CTRLD_CCC_Pos)
		#define PTC_CTRLD_CCC(value)        (PTC_CTRLD_CCC_Msk & ((value) << PTC_CTRLD_CCC_Pos))
		#define PTC_CTRLD_CCR_Pos           12           /**< \brief (PTC_CTRLD) Compensation Capacitor Rough Value */
		#define PTC_CTRLD_CCR_Msk           (_U(0x3) << PTC_CTRLD_CCR_Pos)
		#define PTC_CTRLD_CCR(value)        (PTC_CTRLD_CCR_Msk & ((value) << PTC_CTRLD_CCR_Pos))
		#define PTC_CTRLD_CIF_Pos           16           /**< \brief (PTC_CTRLD) Integration Capacitor Fine Value */
		#define PTC_CTRLD_CIF_Msk           (_U(0xF) << PTC_CTRLD_CIF_Pos)
		#define PTC_CTRLD_CIF(value)        (PTC_CTRLD_CIF_Msk & ((value) << PTC_CTRLD_CIF_Pos))
		#define PTC_CTRLD_CIC_Pos           20           /**< \brief (PTC_CTRLD) Integration Capacitor Coarse Value */
		#define PTC_CTRLD_CIC_Msk           (_U(0x3) << PTC_CTRLD_CIC_Pos)
		#define PTC_CTRLD_CIC(value)        (PTC_CTRLD_CIC_Msk & ((value) << PTC_CTRLD_CIC_Pos))
		#define PTC_CTRLD_MASK              _U(0x003F3FFF) /**< \brief (PTC_CTRLD) MASK Register */

		/* -------- PTC_PINEN : (PTC Offset: 0x20) (R/W 32) Pin Touch Enable -------- */
		#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
		typedef union {
			struct {
				uint32_t PINEN:32;         /*!< bit:  0..31  Touch line Enable                  */
				} bit;                       /*!< Structure used for bit  access                  */
				uint32_t reg;                /*!< Type      used for register access              */
			} PTC_PINEN_Type;
			#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

			#define PTC_PINEN_OFFSET            0x20         /**< \brief (PTC_PINEN offset) Pin Touch Enable */
			#define PTC_PINEN_RESETVALUE        _U(0x00000000); /**< \brief (PTC_PINEN reset_value) Pin Touch Enable */

			#define PTC_PINEN_PINEN_Pos         0            /**< \brief (PTC_PINEN) Touch line Enable */
			#define PTC_PINEN_PINEN_Msk         (_U(0xFFFFFFFF) << PTC_PINEN_PINEN_Pos)
			#define PTC_PINEN_PINEN(value)      (PTC_PINEN_PINEN_Msk & ((value) << PTC_PINEN_PINEN_Pos))
			#define PTC_PINEN_MASK              _U(0xFFFFFFFF) /**< \brief (PTC_PINEN) MASK Register */

			/* -------- PTC_XSEL : (PTC Offset: 0x24) (R/W 32) X-lines Selection -------- */
			#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
			typedef union {
				struct {
					uint32_t XSEL:32;          /*!< bit:  0..31  X-lines Selection                  */
					} bit;                       /*!< Structure used for bit  access                  */
					uint32_t reg;                /*!< Type      used for register access              */
				} PTC_XSEL_Type;
				#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

				#define PTC_XSEL_OFFSET             0x24         /**< \brief (PTC_XSEL offset) X-lines Selection */
				#define PTC_XSEL_RESETVALUE         _U(0x00000000); /**< \brief (PTC_XSEL reset_value) X-lines Selection */

				#define PTC_XSEL_XSEL_Pos           0            /**< \brief (PTC_XSEL) X-lines Selection */
				#define PTC_XSEL_XSEL_Msk           (_U(0xFFFFFFFF) << PTC_XSEL_XSEL_Pos)
				#define PTC_XSEL_XSEL(value)        (PTC_XSEL_XSEL_Msk & ((value) << PTC_XSEL_XSEL_Pos))
				#define PTC_XSEL_MASK               _U(0xFFFFFFFF) /**< \brief (PTC_XSEL) MASK Register */

				/* -------- PTC_YSEL : (PTC Offset: 0x28) (R/W 32) Y-lines Selection -------- */
				#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
				typedef union {
					struct {
						uint32_t YSEL:32;          /*!< bit:  0..31  Y-line Selection                   */
						} bit;                       /*!< Structure used for bit  access                  */
						uint32_t reg;                /*!< Type      used for register access              */
					} PTC_YSEL_Type;
					#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

					#define PTC_YSEL_OFFSET             0x28         /**< \brief (PTC_YSEL offset) Y-lines Selection */
					#define PTC_YSEL_RESETVALUE         _U(0x00000000); /**< \brief (PTC_YSEL reset_value) Y-lines Selection */

					#define PTC_YSEL_YSEL_Pos           0            /**< \brief (PTC_YSEL) Y-line Selection */
					#define PTC_YSEL_YSEL_Msk           (_U(0xFFFFFFFF) << PTC_YSEL_YSEL_Pos)
					#define PTC_YSEL_YSEL(value)        (PTC_YSEL_YSEL_Msk & ((value) << PTC_YSEL_YSEL_Pos))
					#define PTC_YSEL_MASK               _U(0xFFFFFFFF) /**< \brief (PTC_YSEL) MASK Register */
/* -------- PTC_INTENCLR : (PTC Offset: 0x2C) (R/W  8) Interrupt Enable Clear -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  RESRDY:1;         /*!< bit:      0  Result Ready Interrupt Disable     */
    uint8_t  OVERRUN:1;        /*!< bit:      1  Overrun Interrupt Disable          */
    uint8_t  WINMON:1;         /*!< bit:      2  Window Monitor Interrupt Disable   */
    uint8_t  :5;               /*!< bit:  3.. 7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_INTENCLR_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_INTENCLR_OFFSET         0x2C         /**< \brief (PTC_INTENCLR offset) Interrupt Enable Clear */
#define PTC_INTENCLR_RESETVALUE     _U_(0x00)    /**< \brief (PTC_INTENCLR reset_value) Interrupt Enable Clear */

#define PTC_INTENCLR_RESRDY_Pos     0            /**< \brief (PTC_INTENCLR) Result Ready Interrupt Disable */
#define PTC_INTENCLR_RESRDY         (_U_(0x1) << PTC_INTENCLR_RESRDY_Pos)
#define PTC_INTENCLR_OVERRUN_Pos    1            /**< \brief (PTC_INTENCLR) Overrun Interrupt Disable */
#define PTC_INTENCLR_OVERRUN        (_U_(0x1) << PTC_INTENCLR_OVERRUN_Pos)
#define PTC_INTENCLR_WINMON_Pos     2            /**< \brief (PTC_INTENCLR) Window Monitor Interrupt Disable */
#define PTC_INTENCLR_WINMON         (_U_(0x1) << PTC_INTENCLR_WINMON_Pos)
#define PTC_INTENCLR_MASK           _U_(0x07)    /**< \brief (PTC_INTENCLR) MASK Register */

/* -------- PTC_INTENSET : (PTC Offset: 0x2D) (R/W  8) Interrupt Enable Set -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  RESRDY:1;         /*!< bit:      0  Result Ready Interrupt Enable      */
    uint8_t  OVERRUN:1;        /*!< bit:      1  Overrun Interrupt Enable           */
    uint8_t  WINMON:1;         /*!< bit:      2  Window Monitor Interrupt Enable    */
    uint8_t  :5;               /*!< bit:  3.. 7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_INTENSET_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_INTENSET_OFFSET         0x2D         /**< \brief (PTC_INTENSET offset) Interrupt Enable Set */
#define PTC_INTENSET_RESETVALUE     _U_(0x00)    /**< \brief (PTC_INTENSET reset_value) Interrupt Enable Set */

#define PTC_INTENSET_RESRDY_Pos     0            /**< \brief (PTC_INTENSET) Result Ready Interrupt Enable */
#define PTC_INTENSET_RESRDY         (_U_(0x1) << PTC_INTENSET_RESRDY_Pos)
#define PTC_INTENSET_OVERRUN_Pos    1            /**< \brief (PTC_INTENSET) Overrun Interrupt Enable */
#define PTC_INTENSET_OVERRUN        (_U_(0x1) << PTC_INTENSET_OVERRUN_Pos)
#define PTC_INTENSET_WINMON_Pos     2            /**< \brief (PTC_INTENSET) Window Monitor Interrupt Enable */
#define PTC_INTENSET_WINMON         (_U_(0x1) << PTC_INTENSET_WINMON_Pos)
#define PTC_INTENSET_MASK           _U_(0x07)    /**< \brief (PTC_INTENSET) MASK Register */

/* -------- PTC_INTFLAG : (PTC Offset: 0x2E) (R/W  8) Interrupt Flag Status and Clear -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union { // __I to avoid read-modify-write on write-to-clear register
  struct {
    __I uint8_t  RESRDY:1;         /*!< bit:      0  Result Ready Interrupt Flag        */
    __I uint8_t  OVERRUN:1;        /*!< bit:      1  Overrun Interrupt Flag             */
    __I uint8_t  WINMON:1;         /*!< bit:      2  Window Monitor Interrupt Flag      */
    __I uint8_t  :5;               /*!< bit:  3.. 7  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_INTFLAG_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_INTFLAG_OFFSET          0x2E         /**< \brief (PTC_INTFLAG offset) Interrupt Flag Status and Clear */
#define PTC_INTFLAG_RESETVALUE      _U_(0x00)    /**< \brief (PTC_INTFLAG reset_value) Interrupt Flag Status and Clear */

#define PTC_INTFLAG_RESRDY_Pos      0            /**< \brief (PTC_INTFLAG) Result Ready Interrupt Flag */
#define PTC_INTFLAG_RESRDY          (_U_(0x1) << PTC_INTFLAG_RESRDY_Pos)
#define PTC_INTFLAG_OVERRUN_Pos     1            /**< \brief (PTC_INTFLAG) Overrun Interrupt Flag */
#define PTC_INTFLAG_OVERRUN         (_U_(0x1) << PTC_INTFLAG_OVERRUN_Pos)
#define PTC_INTFLAG_WINMON_Pos      2            /**< \brief (PTC_INTFLAG) Window Monitor Interrupt Flag */
#define PTC_INTFLAG_WINMON          (_U_(0x1) << PTC_INTFLAG_WINMON_Pos)
#define PTC_INTFLAG_MASK            _U_(0x07)    /**< \brief (PTC_INTFLAG) MASK Register */

/* -------- PTC_STATUS : (PTC Offset: 0x2F) (R/   8) Status -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint8_t  PTCBUSY:1;        /*!< bit:      0  PTC Busy Status                    */
    uint8_t  :1;               /*!< bit:      1  Reserved                           */
    uint8_t  WCC:6;            /*!< bit:  2.. 7  Window Comparator Counter          */
  } bit;                       /*!< Structure used for bit  access                  */
  uint8_t reg;                 /*!< Type      used for register access              */
} PTC_STATUS_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_STATUS_OFFSET           0x2F         /**< \brief (PTC_STATUS offset) Status */
#define PTC_STATUS_RESETVALUE       _U_(0x00)    /**< \brief (PTC_STATUS reset_value) Status */

#define PTC_STATUS_PTCBUSY_Pos      0            /**< \brief (PTC_STATUS) PTC Busy Status */
#define PTC_STATUS_PTCBUSY          (_U_(0x1) << PTC_STATUS_PTCBUSY_Pos)
#define PTC_STATUS_WCC_Pos          2            /**< \brief (PTC_STATUS) Window Comparator Counter */
#define PTC_STATUS_WCC_Msk          (_U_(0x3F) << PTC_STATUS_WCC_Pos)
#define PTC_STATUS_WCC(value)       (PTC_STATUS_WCC_Msk & ((value) << PTC_STATUS_WCC_Pos))
#define PTC_STATUS_MASK             _U_(0xFD)    /**< \brief (PTC_STATUS) MASK Register */

/* -------- PTC_SYNCBUSY : (PTC Offset: 0x30) (R/  32) Synchronization Busy -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint32_t SWRST:1;          /*!< bit:      0  SWRST Synchronization Busy         */
    uint32_t ENABLE:1;         /*!< bit:      1  ENABLE Synchronization Busy        */
    uint32_t INPUTCTRL:1;      /*!< bit:      2  Input Control Synchronization Busy */
    uint32_t CTRLB:1;          /*!< bit:      3  Control B Synchronization Busy     */
    uint32_t REFCTRL:1;        /*!< bit:      4  Reference Control Synchronization Busy */
    uint32_t AVGCTRL:1;        /*!< bit:      5  Average Control Synchronization Busy */
    uint32_t SAMPCTRL:1;       /*!< bit:      6  Sampling Time Control Synchronization Busy */
    uint32_t WINLT:1;          /*!< bit:      7  Window Monitor Lower Threshold Synchronization Busy */
    uint32_t WINUT:1;          /*!< bit:      8  Window Monitor Upper Threshold Synchronization Busy */
    uint32_t GAINCORR:1;       /*!< bit:      9  Gain Correction Synchronization Busy */
    uint32_t OFFSETCORR:1;     /*!< bit:     10  Offset Correction Synchronization Busy */
    uint32_t SWTRIG:1;         /*!< bit:     11  Software Trigger Synchronization Busy */
    uint32_t :20;              /*!< bit: 12..31  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint32_t reg;                /*!< Type      used for register access              */
} PTC_SYNCBUSY_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_SYNCBUSY_OFFSET         0x30         /**< \brief (PTC_SYNCBUSY offset) Synchronization Busy */
#define PTC_SYNCBUSY_RESETVALUE     _U_(0x00000000) /**< \brief (PTC_SYNCBUSY reset_value) Synchronization Busy */

#define PTC_SYNCBUSY_SWRST_Pos      0            /**< \brief (PTC_SYNCBUSY) SWRST Synchronization Busy */
#define PTC_SYNCBUSY_SWRST          (_U_(0x1) << PTC_SYNCBUSY_SWRST_Pos)
#define PTC_SYNCBUSY_ENABLE_Pos     1            /**< \brief (PTC_SYNCBUSY) ENABLE Synchronization Busy */
#define PTC_SYNCBUSY_ENABLE         (_U_(0x1) << PTC_SYNCBUSY_ENABLE_Pos)
#define PTC_SYNCBUSY_INPUTCTRL_Pos  2            /**< \brief (PTC_SYNCBUSY) Input Control Synchronization Busy */
#define PTC_SYNCBUSY_INPUTCTRL      (_U_(0x1) << PTC_SYNCBUSY_INPUTCTRL_Pos)
#define PTC_SYNCBUSY_CTRLB_Pos      3            /**< \brief (PTC_SYNCBUSY) Control B Synchronization Busy */
#define PTC_SYNCBUSY_CTRLB          (_U_(0x1) << PTC_SYNCBUSY_CTRLB_Pos)
#define PTC_SYNCBUSY_REFCTRL_Pos    4            /**< \brief (PTC_SYNCBUSY) Reference Control Synchronization Busy */
#define PTC_SYNCBUSY_REFCTRL        (_U_(0x1) << PTC_SYNCBUSY_REFCTRL_Pos)
#define PTC_SYNCBUSY_AVGCTRL_Pos    5            /**< \brief (PTC_SYNCBUSY) Average Control Synchronization Busy */
#define PTC_SYNCBUSY_AVGCTRL        (_U_(0x1) << PTC_SYNCBUSY_AVGCTRL_Pos)
#define PTC_SYNCBUSY_SAMPCTRL_Pos   6            /**< \brief (PTC_SYNCBUSY) Sampling Time Control Synchronization Busy */
#define PTC_SYNCBUSY_SAMPCTRL       (_U_(0x1) << PTC_SYNCBUSY_SAMPCTRL_Pos)
#define PTC_SYNCBUSY_WINLT_Pos      7            /**< \brief (PTC_SYNCBUSY) Window Monitor Lower Threshold Synchronization Busy */
#define PTC_SYNCBUSY_WINLT          (_U_(0x1) << PTC_SYNCBUSY_WINLT_Pos)
#define PTC_SYNCBUSY_WINUT_Pos      8            /**< \brief (PTC_SYNCBUSY) Window Monitor Upper Threshold Synchronization Busy */
#define PTC_SYNCBUSY_WINUT          (_U_(0x1) << PTC_SYNCBUSY_WINUT_Pos)
#define PTC_SYNCBUSY_GAINCORR_Pos   9            /**< \brief (PTC_SYNCBUSY) Gain Correction Synchronization Busy */
#define PTC_SYNCBUSY_GAINCORR       (_U_(0x1) << PTC_SYNCBUSY_GAINCORR_Pos)
#define PTC_SYNCBUSY_OFFSETCORR_Pos 10           /**< \brief (PTC_SYNCBUSY) Offset Correction Synchronization Busy */
#define PTC_SYNCBUSY_OFFSETCORR     (_U_(0x1) << PTC_SYNCBUSY_OFFSETCORR_Pos)
#define PTC_SYNCBUSY_SWTRIG_Pos     11           /**< \brief (PTC_SYNCBUSY) Software Trigger Synchronization Busy */
#define PTC_SYNCBUSY_SWTRIG         (_U_(0x1) << PTC_SYNCBUSY_SWTRIG_Pos)
#define PTC_SYNCBUSY_MASK           _U_(0x00000FFF) /**< \brief (PTC_SYNCBUSY) MASK Register */

/* -------- PTC_DSEQDATA : (PTC Offset: 0x34) ( /W 32) DMA Sequencial Data -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint32_t DATA:32;          /*!< bit:  0..31  DMA Sequential Data                */
  } bit;                       /*!< Structure used for bit  access                  */
  uint32_t reg;                /*!< Type      used for register access              */
} PTC_DSEQDATA_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_DSEQDATA_OFFSET         0x34         /**< \brief (PTC_DSEQDATA offset) DMA Sequencial Data */
#define PTC_DSEQDATA_RESETVALUE     _U_(0x00000000) /**< \brief (PTC_DSEQDATA reset_value) DMA Sequencial Data */

#define PTC_DSEQDATA_DATA_Pos       0            /**< \brief (PTC_DSEQDATA) DMA Sequential Data */
#define PTC_DSEQDATA_DATA_Msk       (_U_(0xFFFFFFFF) << PTC_DSEQDATA_DATA_Pos)
#define PTC_DSEQDATA_DATA(value)    (PTC_DSEQDATA_DATA_Msk & ((value) << PTC_DSEQDATA_DATA_Pos))
#define PTC_DSEQDATA_MASK           _U_(0xFFFFFFFF) /**< \brief (PTC_DSEQDATA) MASK Register */

/* -------- PTC_DSEQCTRL : (PTC Offset: 0x38) (R/W 32) DMA Sequential Control -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint32_t INPUTCTRL:1;      /*!< bit:      0  Input Control                      */
    uint32_t CTRLB:1;          /*!< bit:      1  Control B                          */
    uint32_t REFCTRL:1;        /*!< bit:      2  Reference Control                  */
    uint32_t AVGCTRL:1;        /*!< bit:      3  Average Control                    */
    uint32_t SAMPCTRL:1;       /*!< bit:      4  Sampling Time Control              */
    uint32_t WINLT:1;          /*!< bit:      5  Window Monitor Lower Threshold     */
    uint32_t WINUT:1;          /*!< bit:      6  Window Monitor Upper Threshold     */
    uint32_t GAINCORR:1;       /*!< bit:      7  Gain Correction                    */
    uint32_t OFFSETCORR:1;     /*!< bit:      8  Offset Correction                  */
    uint32_t :22;              /*!< bit:  9..30  Reserved                           */
    uint32_t AUTOSTART:1;      /*!< bit:     31  PTC Auto-Start Conversion          */
  } bit;                       /*!< Structure used for bit  access                  */
  uint32_t reg;                /*!< Type      used for register access              */
} PTC_DSEQCTRL_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_DSEQCTRL_OFFSET         0x38         /**< \brief (PTC_DSEQCTRL offset) DMA Sequential Control */
#define PTC_DSEQCTRL_RESETVALUE     _U_(0x00000000) /**< \brief (PTC_DSEQCTRL reset_value) DMA Sequential Control */

#define PTC_DSEQCTRL_INPUTCTRL_Pos  0            /**< \brief (PTC_DSEQCTRL) Input Control */
#define PTC_DSEQCTRL_INPUTCTRL      (_U_(0x1) << PTC_DSEQCTRL_INPUTCTRL_Pos)
#define PTC_DSEQCTRL_CTRLB_Pos      1            /**< \brief (PTC_DSEQCTRL) Control B */
#define PTC_DSEQCTRL_CTRLB          (_U_(0x1) << PTC_DSEQCTRL_CTRLB_Pos)
#define PTC_DSEQCTRL_REFCTRL_Pos    2            /**< \brief (PTC_DSEQCTRL) Reference Control */
#define PTC_DSEQCTRL_REFCTRL        (_U_(0x1) << PTC_DSEQCTRL_REFCTRL_Pos)
#define PTC_DSEQCTRL_AVGCTRL_Pos    3            /**< \brief (PTC_DSEQCTRL) Average Control */
#define PTC_DSEQCTRL_AVGCTRL        (_U_(0x1) << PTC_DSEQCTRL_AVGCTRL_Pos)
#define PTC_DSEQCTRL_SAMPCTRL_Pos   4            /**< \brief (PTC_DSEQCTRL) Sampling Time Control */
#define PTC_DSEQCTRL_SAMPCTRL       (_U_(0x1) << PTC_DSEQCTRL_SAMPCTRL_Pos)
#define PTC_DSEQCTRL_WINLT_Pos      5            /**< \brief (PTC_DSEQCTRL) Window Monitor Lower Threshold */
#define PTC_DSEQCTRL_WINLT          (_U_(0x1) << PTC_DSEQCTRL_WINLT_Pos)
#define PTC_DSEQCTRL_WINUT_Pos      6            /**< \brief (PTC_DSEQCTRL) Window Monitor Upper Threshold */
#define PTC_DSEQCTRL_WINUT          (_U_(0x1) << PTC_DSEQCTRL_WINUT_Pos)
#define PTC_DSEQCTRL_GAINCORR_Pos   7            /**< \brief (PTC_DSEQCTRL) Gain Correction */
#define PTC_DSEQCTRL_GAINCORR       (_U_(0x1) << PTC_DSEQCTRL_GAINCORR_Pos)
#define PTC_DSEQCTRL_OFFSETCORR_Pos 8            /**< \brief (PTC_DSEQCTRL) Offset Correction */
#define PTC_DSEQCTRL_OFFSETCORR     (_U_(0x1) << PTC_DSEQCTRL_OFFSETCORR_Pos)
#define PTC_DSEQCTRL_AUTOSTART_Pos  31           /**< \brief (PTC_DSEQCTRL) PTC Auto-Start Conversion */
#define PTC_DSEQCTRL_AUTOSTART      (_U_(0x1) << PTC_DSEQCTRL_AUTOSTART_Pos)
#define PTC_DSEQCTRL_MASK           _U_(0x800001FF) /**< \brief (PTC_DSEQCTRL) MASK Register */

/* -------- PTC_DSEQSTAT : (PTC Offset: 0x3C) (R/  32) DMA Sequencial Status -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint32_t INPUTCTRL:1;      /*!< bit:      0  Input Control                      */
    uint32_t CTRLB:1;          /*!< bit:      1  Control B                          */
    uint32_t REFCTRL:1;        /*!< bit:      2  Reference Control                  */
    uint32_t AVGCTRL:1;        /*!< bit:      3  Average Control                    */
    uint32_t SAMPCTRL:1;       /*!< bit:      4  Sampling Time Control              */
    uint32_t WINLT:1;          /*!< bit:      5  Window Monitor Lower Threshold     */
    uint32_t WINUT:1;          /*!< bit:      6  Window Monitor Upper Threshold     */
    uint32_t GAINCORR:1;       /*!< bit:      7  Gain Correction                    */
    uint32_t OFFSETCORR:1;     /*!< bit:      8  Offset Correction                  */
    uint32_t :22;              /*!< bit:  9..30  Reserved                           */
    uint32_t BUSY:1;           /*!< bit:     31  DMA Sequencing Busy                */
  } bit;                       /*!< Structure used for bit  access                  */
  uint32_t reg;                /*!< Type      used for register access              */
} PTC_DSEQSTAT_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_DSEQSTAT_OFFSET         0x3C         /**< \brief (PTC_DSEQSTAT offset) DMA Sequencial Status */
#define PTC_DSEQSTAT_RESETVALUE     _U_(0x00000000) /**< \brief (PTC_DSEQSTAT reset_value) DMA Sequencial Status */

#define PTC_DSEQSTAT_INPUTCTRL_Pos  0            /**< \brief (PTC_DSEQSTAT) Input Control */
#define PTC_DSEQSTAT_INPUTCTRL      (_U_(0x1) << PTC_DSEQSTAT_INPUTCTRL_Pos)
#define PTC_DSEQSTAT_CTRLB_Pos      1            /**< \brief (PTC_DSEQSTAT) Control B */
#define PTC_DSEQSTAT_CTRLB          (_U_(0x1) << PTC_DSEQSTAT_CTRLB_Pos)
#define PTC_DSEQSTAT_REFCTRL_Pos    2            /**< \brief (PTC_DSEQSTAT) Reference Control */
#define PTC_DSEQSTAT_REFCTRL        (_U_(0x1) << PTC_DSEQSTAT_REFCTRL_Pos)
#define PTC_DSEQSTAT_AVGCTRL_Pos    3            /**< \brief (PTC_DSEQSTAT) Average Control */
#define PTC_DSEQSTAT_AVGCTRL        (_U_(0x1) << PTC_DSEQSTAT_AVGCTRL_Pos)
#define PTC_DSEQSTAT_SAMPCTRL_Pos   4            /**< \brief (PTC_DSEQSTAT) Sampling Time Control */
#define PTC_DSEQSTAT_SAMPCTRL       (_U_(0x1) << PTC_DSEQSTAT_SAMPCTRL_Pos)
#define PTC_DSEQSTAT_WINLT_Pos      5            /**< \brief (PTC_DSEQSTAT) Window Monitor Lower Threshold */
#define PTC_DSEQSTAT_WINLT          (_U_(0x1) << PTC_DSEQSTAT_WINLT_Pos)
#define PTC_DSEQSTAT_WINUT_Pos      6            /**< \brief (PTC_DSEQSTAT) Window Monitor Upper Threshold */
#define PTC_DSEQSTAT_WINUT          (_U_(0x1) << PTC_DSEQSTAT_WINUT_Pos)
#define PTC_DSEQSTAT_GAINCORR_Pos   7            /**< \brief (PTC_DSEQSTAT) Gain Correction */
#define PTC_DSEQSTAT_GAINCORR       (_U_(0x1) << PTC_DSEQSTAT_GAINCORR_Pos)
#define PTC_DSEQSTAT_OFFSETCORR_Pos 8            /**< \brief (PTC_DSEQSTAT) Offset Correction */
#define PTC_DSEQSTAT_OFFSETCORR     (_U_(0x1) << PTC_DSEQSTAT_OFFSETCORR_Pos)
#define PTC_DSEQSTAT_BUSY_Pos       31           /**< \brief (PTC_DSEQSTAT) DMA Sequencing Busy */
#define PTC_DSEQSTAT_BUSY           (_U_(0x1) << PTC_DSEQSTAT_BUSY_Pos)
#define PTC_DSEQSTAT_MASK           _U_(0x800001FF) /**< \brief (PTC_DSEQSTAT) MASK Register */

/* -------- PTC_RESULT : (PTC Offset: 0x40) (R/  16) Result Conversion Value -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t RESULT:16;        /*!< bit:  0..15  Result Conversion Value            */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_RESULT_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_RESULT_OFFSET           0x40         /**< \brief (PTC_RESULT offset) Result Conversion Value */
#define PTC_RESULT_RESETVALUE       _U_(0x0000)  /**< \brief (PTC_RESULT reset_value) Result Conversion Value */

#define PTC_RESULT_RESULT_Pos       0            /**< \brief (PTC_RESULT) Result Conversion Value */
#define PTC_RESULT_RESULT_Msk       (_U_(0xFFFF) << PTC_RESULT_RESULT_Pos)
#define PTC_RESULT_RESULT(value)    (PTC_RESULT_RESULT_Msk & ((value) << PTC_RESULT_RESULT_Pos))
#define PTC_RESULT_MASK             _U_(0xFFFF)  /**< \brief (PTC_RESULT) MASK Register */

/* -------- PTC_RESS : (PTC Offset: 0x44) (R/  16) Last Sample Result -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t RESS:16;          /*!< bit:  0..15  Last PTC conversion result         */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_RESS_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_RESS_OFFSET             0x44         /**< \brief (PTC_RESS offset) Last Sample Result */
#define PTC_RESS_RESETVALUE         _U_(0x0000)  /**< \brief (PTC_RESS reset_value) Last Sample Result */

#define PTC_RESS_RESS_Pos           0            /**< \brief (PTC_RESS) Last PTC conversion result */
#define PTC_RESS_RESS_Msk           (_U_(0xFFFF) << PTC_RESS_RESS_Pos)
#define PTC_RESS_RESS(value)        (PTC_RESS_RESS_Msk & ((value) << PTC_RESS_RESS_Pos))
#define PTC_RESS_MASK               _U_(0xFFFF)  /**< \brief (PTC_RESS) MASK Register */

/* -------- PTC_CALIB : (PTC Offset: 0x48) (R/W 16) Calibration -------- */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef union {
  struct {
    uint16_t BIASCOMP:3;       /*!< bit:  0.. 2  Bias Comparator Scaling            */
    uint16_t :1;               /*!< bit:      3  Reserved                           */
    uint16_t BIASR2R:3;        /*!< bit:  4.. 6  Bias R2R Ampli scaling             */
    uint16_t :1;               /*!< bit:      7  Reserved                           */
    uint16_t BIASREFBUF:3;     /*!< bit:  8..10  Bias  Reference Buffer Scaling     */
    uint16_t :5;               /*!< bit: 11..15  Reserved                           */
  } bit;                       /*!< Structure used for bit  access                  */
  uint16_t reg;                /*!< Type      used for register access              */
} PTC_CALIB_Type;
#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

#define PTC_CALIB_OFFSET            0x48         /**< \brief (PTC_CALIB offset) Calibration */
#define PTC_CALIB_RESETVALUE        _U_(0x0000)  /**< \brief (PTC_CALIB reset_value) Calibration */

#define PTC_CALIB_BIASCOMP_Pos      0            /**< \brief (PTC_CALIB) Bias Comparator Scaling */
#define PTC_CALIB_BIASCOMP_Msk      (_U_(0x7) << PTC_CALIB_BIASCOMP_Pos)
#define PTC_CALIB_BIASCOMP(value)   (PTC_CALIB_BIASCOMP_Msk & ((value) << PTC_CALIB_BIASCOMP_Pos))
#define PTC_CALIB_BIASR2R_Pos       4            /**< \brief (PTC_CALIB) Bias R2R Ampli scaling */
#define PTC_CALIB_BIASR2R_Msk       (_U_(0x7) << PTC_CALIB_BIASR2R_Pos)
#define PTC_CALIB_BIASR2R(value)    (PTC_CALIB_BIASR2R_Msk & ((value) << PTC_CALIB_BIASR2R_Pos))
#define PTC_CALIB_BIASREFBUF_Pos    8            /**< \brief (PTC_CALIB) Bias  Reference Buffer Scaling */
#define PTC_CALIB_BIASREFBUF_Msk    (_U_(0x7) << PTC_CALIB_BIASREFBUF_Pos)
#define PTC_CALIB_BIASREFBUF(value) (PTC_CALIB_BIASREFBUF_Msk & ((value) << PTC_CALIB_BIASREFBUF_Pos))
#define PTC_CALIB_MASK              _U_(0x0777)  /**< \brief (PTC_CALIB) MASK Register */

/** \brief PTC hardware registers */
#if !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__))
typedef struct {
  __IO PTC_CTRLA_Type            CTRLA;       /**< \brief Offset: 0x00 (R/W 16) Control A */
  __IO PTC_EVCTRL_Type           EVCTRL;      /**< \brief Offset: 0x02 (R/W  8) Event Control */
  __IO PTC_DBGCTRL_Type          DBGCTRL;     /**< \brief Offset: 0x03 (R/W  8) Debug Control */
  __IO PTC_INPUTCTRL_Type        INPUTCTRL;   /**< \brief Offset: 0x04 (R/W 16) Input Control */
  __IO PTC_CTRLB_Type            CTRLB;       /**< \brief Offset: 0x06 (R/W 16) Control B */
  __IO PTC_REFCTRL_Type          REFCTRL;     /**< \brief Offset: 0x08 (R/W  8) Reference Control */
       RoReg8                    Reserved1[0x1];
  __IO PTC_AVGCTRL_Type          AVGCTRL;     /**< \brief Offset: 0x0A (R/W  8) Average Control */
  __IO PTC_SAMPCTRL_Type         SAMPCTRL;    /**< \brief Offset: 0x0B (R/W  8) Sample Time Control */
  __IO PTC_WINLT_Type            WINLT;       /**< \brief Offset: 0x0C (R/W 16) Window Monitor Lower Threshold */
  __IO PTC_WINUT_Type            WINUT;       /**< \brief Offset: 0x0E (R/W 16) Window Monitor Upper Threshold */
  __IO PTC_GAINCORR_Type         GAINCORR;    /**< \brief Offset: 0x10 (R/W 16) Gain Correction */
  __IO PTC_OFFSETCORR_Type       OFFSETCORR;  /**< \brief Offset: 0x12 (R/W 16) Offset Correction */
  __IO PTC_SWTRIG_Type           SWTRIG;      /**< \brief Offset: 0x14 (R/W  8) Software Trigger */
       RoReg8                    Reserved2[0x3];
  __IO PTC_CTRLC_Type            CTRLC;       /**< \brief Offset: 0x18 (R/W 32) Control C */
  __IO PTC_CTRLD_Type            CTRLD;       /**< \brief Offset: 0x1C (R/W 32) Control D */
  __IO PTC_PINEN_Type            PINEN;       /**< \brief Offset: 0x20 (R/W 32) Pin Touch Enable */
  __IO PTC_XSEL_Type             XSEL;        /**< \brief Offset: 0x24 (R/W 32) X-lines Selection */
  __IO PTC_YSEL_Type             YSEL;        /**< \brief Offset: 0x28 (R/W 32) Y-lines Selection */
  __IO PTC_INTENCLR_Type         INTENCLR;    /**< \brief Offset: 0x2C (R/W  8) Interrupt Enable Clear */
  __IO PTC_INTENSET_Type         INTENSET;    /**< \brief Offset: 0x2D (R/W  8) Interrupt Enable Set */
  __IO PTC_INTFLAG_Type          INTFLAG;     /**< \brief Offset: 0x2E (R/W  8) Interrupt Flag Status and Clear */
  __I  PTC_STATUS_Type           STATUS;      /**< \brief Offset: 0x2F (R/   8) Status */
  __I  PTC_SYNCBUSY_Type         SYNCBUSY;    /**< \brief Offset: 0x30 (R/  32) Synchronization Busy */
  __O  PTC_DSEQDATA_Type         DSEQDATA;    /**< \brief Offset: 0x34 ( /W 32) DMA Sequencial Data */
  __IO PTC_DSEQCTRL_Type         DSEQCTRL;    /**< \brief Offset: 0x38 (R/W 32) DMA Sequential Control */
  __I  PTC_DSEQSTAT_Type         DSEQSTAT;    /**< \brief Offset: 0x3C (R/  32) DMA Sequencial Status */
  __I  PTC_RESULT_Type           RESULT;      /**< \brief Offset: 0x40 (R/  16) Result Conversion Value */
       RoReg8                    Reserved3[0x2];
  __I  PTC_RESS_Type             RESS;        /**< \brief Offset: 0x44 (R/  16) Last Sample Result */
       RoReg8                    Reserved4[0x2];
  __IO PTC_CALIB_Type            CALIB;       /**< \brief Offset: 0x48 (R/W 16) Calibration */
} QTML_Ptc;



#define QTML_PTC              ((QTML_Ptc      *)0x43001C00UL) /**< \brief (ADC0) APB Base Address */
#define QTML_PTC_0_IRQn        ADC0_OTHER_IRQn
#define QTML_PTC_1_IRQn        ADC0_RESRDY_IRQn


#endif /* !(defined(__ASSEMBLY__) || defined(__IAR_SYSTEMS_ASM__)) */

/*@}*/

#endif /* _SAME54_PTC_COMPONENT_ */
