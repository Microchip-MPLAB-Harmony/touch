![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

#  Microchip MPLAB® Harmony 3 Touch Library Release Notes

## Touch Library v3.14.0 Release
### NEW FEATURES SUPPORTED
* MISRA-C 2012 Mandatory and Required rules Compliance achieved for Harmony generated Touch files.
* Touch Configurator is upgraded to the latest framework.
* Touch Tuning (bidirectional) support is extended for Surface and Gesture features from Touch plugin version 2.2.0.
### BUG FIXES
* SAM D51, E5x acquisition libraries are updated to version 1.5 to fix a bug regarding acquisition module getting struck.
* Fixed the bug to configure more than 3 steps in frequency hop UI.
* Fixed the bug related to SAMD20 Driven Shield Plus.
### DEVELOPMENT TOOLS
* MPLAB® X IDE v6.10
* MPLAB® XC32 C/C++ Compiler v4.30
* MPLAB® XIDE plug-ins:
    * MPLAB® Code Configurator (MCC)
      * MCC Plugin v5.3.7
      * MCC Harmony Core v1.3.2
      * Harmony 3 – Harmony Services – v1.3.1(mandatory)

## Touch Library v3.13.1 Release
### BUG FIXES
* Fixed bug related to SERCOM getting disconnected from Touch Library component when MCC is closed.
* Software based low power code compilation error is fixed.
* Sleep code moved to touch_example template.
* Fixed bug related to PTC mask being disabled for PIC32CMJH device.
* Updated SAML1x and PIC32CM LE00/LS00/LS60 device acquisition libraries for bug fix related to overwriting PORT_MUX registers for pins adjacent to touch pins.
* Touch Configurator summary page update for displaying versions of few acquisition libraries.

## Touch Library v3.13.0 Release
### NEW FEATURES SUPPORTED
Touch Tune tab provides information to user on bidirectional or unidirectional interface.
### BUG FIXES
* Fixed bug related to CSD option shown for devices which doesn't have CSD feature.
* Driven shield on SAMD2x wasn't working correctly. This is fixed.
* Bug related to gesture timing periodicity is fixed.
* Scroller configuration related bug is fixed in GUI.
* Unintended braces in touch timer function is removed.
* SAMD2x Low power related issues are fixed.
### KNOWN ISSUES
* For PIC32CM JH and SAMC2x families, event system based low power has issues when it enters low power mode. Workaround - Use software based low power feature.
* For SAML1x and PIC32CM LE00/LS00/LS60 device families, PORT_MUX registers for pins adjacent to touch pins may be overwritten by touch library.
### DEVELOPMENT TOOLS 
* [MPLAB® X IDE v6.05](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v4.20](https://www.microchip.com/mplab/compilers)
* MPLAB® XIDE plug-ins: 
    * MPLAB® Code Configurator (MCC)
      * MCC Plugin v5.2.2
      * MCC Core v5.4.14

## Touch Library v3.12.1 Release
### BUG FIXES
* Bug related to enabling Drivenshield is resolved
### DEVELOPMENT TOOLS 
* [MPLAB® X IDE v6.00](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB® XC32 C/C++ Compiler v4.10](https://www.microchip.com/mplab/compilers)
* MPLAB® XIDE plug-ins: 
    * MPLAB® Code Configurator (MCC)
      * MCC Plugin v5.1.9
      * MCC Core v5.4.4
  
## Touch Library v3.12.0 Release
### NEW FEATURES SUPPORTED
* PIC32CM JH family device support is done.
* RTC CountSync is disabled by default for all touch projects.
### BUG FIXES
* Goto menu for Touch Configurator is set to proper path.
### KNOWN ISSUES
* Event system based low power has issues when it enters low power mode.
### DEVELOPMENT TOOLS 
* [MPLAB® X IDE v6.00](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB® XC32 C/C++ Compiler v4.10](https://www.microchip.com/mplab/compilers)
* MPLAB® XIDE plug-ins: 
    * MPLAB® Code Configurator (MCC)
      * MCC Plugin v5.1.4
      * MCC Core v5.4.3

## Touch Library v3.11.2 Release
### BUG FIXES
* Bug related to Touch Configurator not opening in MPLAB® Code Configurator (MCC) is resolved. Prerequisite MCC Plugin v5.1.2 and MCC Harmony Core v1.1.0.
* Touch files not properly added to project for Trustzone applications. This is resolved.
* The protocol version used in TouchTune.c file is updated to match with MPLAB® Touch Plugin v2.0.0.
### KNOWN ISSUES
* Touch tune data with MPLAB® Touch Plugin does not work with Boost mode.
### DEVELOPMENT TOOLS 
* [MPLAB® X IDE v6.00](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB® XC32 C/C++ Compiler v4.00](https://www.microchip.com/mplab/compilers)
* MPLAB® XIDE plug-ins: 
    * MPLAB® Harmony Configurator (MHC) v3.8.3
    * MPLAB® Code Configurator (MCC)
      * MCC Plugin v5.1.2
      * MCC Harmony Core v1.1.0

## Touch Library v3.11.1 Release 
### BUG FIXES
* Bug related to SAME5x Prescaler is resolved.
* Bug related to Touch timer periodicity is resolved.
* Data Streamer tune data is sent only once after each touch measurement.
* Compilation error on SAMD10 device is resolved.
* Boost mode libraries and API files are NOT added when Boost mode is enabled. This is resolved.
### KNOWN ISSUES
* Touch tune data with MPLAB Touch Plugin does not work with Boost mode.
### DEVELOPMENT TOOLS 
* [MPLAB X IDE v6.00](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v4.00](https://www.microchip.com/mplab/compilers)
* MPLAB XIDE plug-ins: 
    * MPLAB Harmony Configurator (MHC) v3.8.2
## Touch Library v3.11.0 Release 
### NEW FEATURES SUPPORTED 
* Two-way debug protocol is supported.
  * Now user can select between MPLAB Data Visualizer Touch plugin and old Data Visualizer in the **Parameters->Tune** tab of Touch Configurator.
  * Refer to [Introduction to Touch Plugin](https://microchipdeveloper.com/touch:introduction-to-touch-plugin) for more details on MPLAB Data Visualizer Touch Plugin.

### BUG FIXES 
* Bug related to mutual cap surface sensor node generation is fixed
* Error related to surface two-way debug files are fixed
* Label related issue in Mutual cap table view pin selection is fixed

### DEVELOPMENT TOOLS 
* [MPLAB X IDE v5.50](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.41](https://www.microchip.com/mplab/compilers)
* MPLAB XIDE plug-ins: 
    * MPLAB Harmony Configurator (MHC) v3.8.2

### Required MPLAB Harmony v3.x.x Modules 
* csp v3.10.0
* mhc v3.8.2

### KNOWN ISSUES 
* Touch Configurator does not work properly when configuring Slider/Wheel using MCC Harmony Library. Workaround is to use Harmony Configurator.

## Touch Library v3.10.1 Release
### BUG FIXES
* Low-power related bug fixes for SAMD1x and software low-power
* Touch Library's capability name is reverted back to "TouchData"
* Bug fix related to resistor value not populated on node parameter for Mutual cap sensor

### DEVELOPMENT TOOLS

* [MPLAB X IDE v5.50](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v3.01](https://www.microchip.com/mplab/compilers)
* MPLAB X IDE plug-ins:
  * MPLAB Harmony Configurator (MHC) v3.8.0

## Touch Library v3.10.0 Release 
### NEW FEATURES SUPPORTED 
* Driven shield support extended for - SAM D1x, SAM D20 
* Acquisition engine and library are separate in MHC project graph 
* PIC32MZDA device support 

### BUG FIXES 
* SAMHA1 ondemand Osc8m ondemand not set 
* ATSAMD10D14AS Touch Project Clock Error 
* Enable only non-event system low-power with driven shield 
* Touch GUI dock update issue 
* RTC count sync issue 
* Mutual cap surface XY configuration for XYmuxed devices 
* Lump with boost mode
* Touch_example.c file is generated along with touch.c file
* Sleep instruction is moved from touch_process() to touch_example.c file

### DEVELOPMENT TOOLS 
* [MPLAB X IDE v5.50](https://www.microchip.com/mplabx-ide-windows-installer)
* [MPLAB XC32 C/C++ Compiler v2.50](https://www.microchip.com/mplab/compilers)
* MPLAB XIDE plug-ins: 
    * MPLAB Harmony Configurator (MHC) v3.8.0 
    
### Required MPLAB Harmony v3.x.x Modules 
* csp v3.9.1 
* bsp v3.9.0 
* dev_packs v3.9.0 
* mhc v3.8.0 

### KNOWN ISSUES 
* None. 

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
  * MPLAB Harmony Configurator (MHC) v3.7.0 

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

