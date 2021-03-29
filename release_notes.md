![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

#  Microchip MPLAB� Harmony 3 Touch Library Release Notes

## Touch Library v3.9.2 Release

### BUG FIXES
* Touch configuration panel cannot open when MHC upgrades to 3.7.0
* Gesture disables timer start
* SAMD5x-E5x driven shield prescaler offset value
* Keys module for boost mode calibration issue
  
### DEVELOPMENT TOOLS 

* [MPLAB X IDE v5.45](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.50](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.6.5 

### Required MPLAB Harmony v3.x.x Modules 

* csp v3.9.0
* bsp v3.9.0
* dev_packs v3.9.0
* mhc v3.7.0

### KNOWN ISSUES
* None.
## Touch Library v3.9.1 Release

### BUG FIXES
* Event system low-power support added for SAML2x.
* Project generation for PIC32MZW fixed.
* Updating RTC period value halts the CPU due to count sync. Count sync is disabled.
* Optimzied low-power touch code for one button project.
  
### DEVELOPMENT TOOLS 

* [MPLAB X IDE v5.45](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.50](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.6.5 

### Required MPLAB Harmony v3.x.x Modules 

* csp v3.8.3
* bsp v3.8.2
* dev_packs v3.8.0
* mhc v3.6.5

### KNOWN ISSUES
* None.

## Touch Library v3.9.0 Release

### NEW FEATURES SUPPORTED
* Low Power Support extended for - SAMC2x, SAM D1x, SAM E5x, SAM D5x, SAM L2x.

### BUG FIXES
* Driven shield waveform for C2x was not in sync - Corrected.
* Calibration trigger does not automatically trigger corresponding button's calibration in boost mode - Corrected.
  
  
### DEVELOPMENT TOOLS 

* [MPLAB X IDE v5.45](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.50](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.6.4 

### Required MPLAB Harmony v3.x.x Modules 

* csp v3.8.3
* bsp v3.8.2
* dev_packs v3.8.0
* mhc v3.6.4

### KNOWN ISSUES
* SAM L2x - Event system based low-power support in later release. 

#  Microchip MPLAB� Harmony 3 Touch Library Release Notes
## Touch Library v3.8.0 Release

### NEW FEATURES SUPPORTED

* Low Power Support
* Lump Support
* Binding Layer is disabled 
  
### DEVELOPMENT TOOLS 

* [MPLAB X IDE v5.40](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.41](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.6.0 

### Required MPLAB Harmony v3.x.x Modules 

* csp v3.8.0
* bsp v3.8.0
* dev_packs v3.8.0
* mhc v3.5.1 

### KNOWN ISSUES
* Lump mode mouse drag operation in Touch configurator GUI only operates from top left to bottom right.

## Touch Library v3.7.0 Release

### NEW DEVICES SUPPORTED

* Device Support for SAM L11.

### NEW FEATURE SUPPORTED
* Boost mode support (parallel acquisition) added for SAML10 and SAML11 devices.
* Graphical representation of the input clock, available prescaler values, and PTC clock frequencies are displayed in the parameter tab.
* The clock-change warning message, which appears when a new sensor is added, now lists the changes which happen in the background when the user selects Yes.
* The minimum and maximum PTC clock frequency details are added.
### DEVELOPMENT TOOLS 

* [MPLAB X IDE v5.40](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.41](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.5 

### Required MPLAB Harmony v3.x.x Modules 

* csp v3.7.1
* bsp v3.7.0
* dev_packs v3.4.1
* mhc v3.4.0 

### KNOWN ISSUES
* none 



## Touch Library v3.6.0 Release

### NEW DEVICES SUPPORTED

* Device Support for SAM HA1
* Device Support for PIC32MZ1025W104132 (HCVD)

### NEW FEATURE SUPPORTED

* Driven Shield support for SAM D21 
* Driven Shield support for SAM DA1
* Driven Shield support for SAM HA1
* Driven Shield support for SAM L2x 
* Driven Shield support for SAM C2x 
* Driven Shield support for SAM E5x 
* Driven Shield support for SAM D51 
* Updated the prescaler values in api.h files to include the internal prescaler division factor. 
    * For example, in SAML10, the prescaler values from 1, 2, 4, 8 are updated to 4, 8, 16, 32 
      (to include a fixed internal division factor of 4). Similarly, all prescaler values are 
      updated for all other devices. 

### DEVELOPMENT TOOLS 

* [MPLAB X IDE v5.35](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.40](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.4.2 

### Required MPLAB Harmony v3.x.x Modules 

* csp v3.6.1
* bsp v3.6.1
* dev_packs v3.6.1
* mhc v3.3.5 

### KNOWN ISSUES
* none 


## Touch Library v3.5.0 Release

### NEW DEVICES SUPPORTED

* [SAMDA1](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus)
* [SAMD1x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus)

### NEW FEATURES:
* Driven shield support for SAML10 is addded.

### NEW DEMO PROJECTS:

* ATSAMDA1 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAMDA1 Xplained Pro Self Capacitance Example Project with QT1
* ATSAML10 Xplained Pro Driven Shield Example Project with QT7 (updated with Driven Shield)
* ATSAMD10 Xplained Mini Self Capacitance Example Project with onboard Button
* ATSAMD11 Xplained Pro Self Capacitance Example Project with onboard Button

### Required MPLAB Harmony v3.x.x Modules:

* csp v3.5.0
* bsp v3.5.0
* dev_packs v3.5.0
* mhc v3.3.3

### KNOWN ISSUES:

* SAMD10 (C variant) Project generation fails, error is related to clock support.

### BUG FIXES

### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.25](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.30](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.3.1

## Touch Library v3.4.0 Release

### NEW DEVICES SUPPORTED

* [SAML2x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus)
* [SAML1x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus)

### NEW FEATURES:

### NEW DEMO PROJECTS:

* ATSAML21 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAML21 Xplained Pro Self Capacitance Example Project with onboard Button
* ATSAML22 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAML22 Xplained Pro Self Capacitance Example Project with onboard Button
* ATSAML10 Xplained Pro Self Capacitance Example Project with QT7

### Required MPLAB Harmony v3.x.x Modules:

* csp v3.4.0
* bsp v3.4.0
* dev_packs v3.3.0
* mhc v3.3.0.1

### KNOWN ISSUES:

### BUG FIXES

* Clock configuration set by touch configurator is removed when touch configurator is closed. This bug is fixed.


### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.20](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.20](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.3.1


## Touch Library v3.3.0 Release

### NEW FEATURES

* Touch Surface (One Finger and Two Fingers) and Gesture firmware, GUI along with DataVisualizer and 2D Touch Surface Utility (Kronocomm) support for SAMC2x, SAMD2x, SAMD51, SAME51, SAME53, SAME54 devices.
* Clock selection support for proper operation of Touch, automated through the Touch configurator.

### Required MPLAB Harmony v3.x.x Modules

* csp v3.4.0
* bsp v3.4.0
* dev_packs v3.4.0
* mhc v3.3.1

### KNOWN ISSUES

* Scroller + Surface combination is not supported.

### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.20](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.20](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.3.1

## Touch Library v3.2.0 Release

### NEW DEVICES SUPPORTED

* [SAM D20/D21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus), 
* [SAME5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
* [SAMD5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus)

### NEW FEATURES

* Slider and Wheel Firmware Support along with GUI Support
* Support for Tabbed View of Data-Visualizer Software

### NEW DEMO PROJECTS

* ATSAMD20 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAMD20 Xplained Pro Self Capacitance Example Project with QT1
* ATSAMD21 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAMD21 Xplained Pro Self Capacitance Example Project with QT1
* ATSAME54 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAME54 Xplained Pro Self Capacitance On Board Example Project 
* ATSAMC21 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAMC21 Xplained Pro Self Capacitance Example Project with QT1

### Required MPLAB Harmony v3.x.x Modules

* csp v3.3.0
* bsp v3.3.0
* dev_packs v3.3.0
* mhc v3.3.0.1

### KNOWN ISSUES

* Touch libraries are built with v2.15 compiler version. Touch Applications may not work properly with other compiler versions.

### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.20](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.3.0.1

## Touch Library v3.1.1 Release

### BUG FIX

* Compilation error related to Data Visualizer code when Frequency Hop is NOT enabled.

### Required MPLAB Harmony v3.x.x Modules

* csp v3.2.0
* dev_packs v3.2.0
* mhc v3.2.0

### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.2.0.
  
## Touch Library v3.1.0 Release

### NEW FEATURES

* Button only touch support for SAM C2x device family along with Data Visualizer option
* Touch configurator GUI

### NEW DEMO PROJECTS

* ATSAMC21 Xplained Pro Mutual Capacitance Example Project with QT1
* ATSAMC21 Xplained Pro Self Capacitance Example Project with QT1

### Required MPLAB Harmony v3.x.x Modules

* csp v3.2.0
* dev_packs v3.2.0
* mhc v3.2.0

### KNOWN ISSUES

* None.

### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.2.0.

