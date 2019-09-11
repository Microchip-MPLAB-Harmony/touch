#include "help_harmony_touch_map.h"
#include "help_harmony_touch_html_map.h"

int HTML_ID_Mapping(int id)
{
  switch(id)
  {
    case IDH_DRV_Touch_Library                                 : return IDH_HTML_DRV_Touch_Library;
    case IDH_DRV_Touch_Introduction                            : return IDH_HTML_DRV_Touch_Introduction;
    case IDH_DRV_Touch_Applications_Help                       : return IDH_HTML_DRV_Touch_Applications_Help;
    case IDH_DRV_Touch_qt1_selfcap                             : return IDH_HTML_DRV_Touch_qt1_selfcap;
    case IDH_DRV_Touch_qt1_setlfcap_Building_The_Application   : return IDH_HTML_DRV_Touch_qt1_setlfcap_Building_The_Application;
    case IDH_DRV_Touch_qt1_selfcap_MPLAB_Harmony_Configurations: return IDH_HTML_DRV_Touch_qt1_selfcap_MPLAB_Harmony_Configurations;
    case IDH_DRV_Touch_qt1_selfcap_Hardware_Setup              : return IDH_HTML_DRV_Touch_qt1_selfcap_Hardware_Setup;
    case IDH_DRV_Touch_qt1_selfcap_Running_The_Application     : return IDH_HTML_DRV_Touch_qt1_selfcap_Running_The_Application;
    case IDH_DRV_Touch_qt1_mutualcap                           : return IDH_HTML_DRV_Touch_qt1_mutualcap;
    case IDH_DRV_Touch_qt1_mutualcap_Building_The_Application  : return IDH_HTML_DRV_Touch_qt1_mutualcap_Building_The_Application;
    case IDH_DRV_Touch_qt1_mutualcap_MPLAB_Harmony_Configurations: return IDH_HTML_DRV_Touch_qt1_mutualcap_MPLAB_Harmony_Configurations;
    case IDH_DRV_Touch_qt1_mutualcap_Hardware_Setup            : return IDH_HTML_DRV_Touch_qt1_mutualcap_Hardware_Setup;
    case IDH_DRV_Touch_qt1_mutualcap_Running_The_Application   : return IDH_HTML_DRV_Touch_qt1_mutualcap_Running_The_Application;
    case IDH_DRV_Touch_on_board_sensor                         : return IDH_HTML_DRV_Touch_on_board_sensor;
    case IDH_DRV_Touch_on_board_sensor_Building_The_Application: return IDH_HTML_DRV_Touch_on_board_sensor_Building_The_Application;
    case IDH_DRV_Touch_on_board_sensor_MPLAB_Harmony_Configurations: return IDH_HTML_DRV_Touch_on_board_sensor_MPLAB_Harmony_Configurations;
    case IDH_DRV_Touch_on_board_sensor_Hardware_Setup          : return IDH_HTML_DRV_Touch_on_board_sensor_Hardware_Setup;
    case IDH_DRV_Touch_on_board_sensor_Running_The_Application : return IDH_HTML_DRV_Touch_on_board_sensor_Running_The_Application;
    case IDH_app_qt7_self_cap                                  : return IDH_HTML_app_qt7_self_cap;
    case IDH_qt7_self_cap_Building_the_Applications            : return IDH_HTML_qt7_self_cap_Building_the_Applications;
    case IDH_qt7_self_cap_MPLAB_Harmony_Configurations         : return IDH_HTML_qt7_self_cap_MPLAB_Harmony_Configurations;
    case IDH_qt7_self_cap_Hardware_Setup                       : return IDH_HTML_qt7_self_cap_Hardware_Setup;
    case IDH_qt7_self_cap_Running_The_Application              : return IDH_HTML_qt7_self_cap_Running_The_Application;
    default: return -1;
  }
}
