function HTML_ID_Mapping(id: Integer): Integer;
begin
  case id of
    IDH_DRV_Touch_Library                                 : result := IDH_HTML_DRV_Touch_Library;
    IDH_DRV_Touch_Introduction                            : result := IDH_HTML_DRV_Touch_Introduction;
    IDH_DRV_Touch_Applications_Help                       : result := IDH_HTML_DRV_Touch_Applications_Help;
    IDH_DRV_Touch_qt1_selfcap                             : result := IDH_HTML_DRV_Touch_qt1_selfcap;
    IDH_DRV_Touch_qt1_setlfcap_Building_The_Application   : result := IDH_HTML_DRV_Touch_qt1_setlfcap_Building_The_Application;
    IDH_DRV_Touch_qt1_selfcap_MPLAB_Harmony_Configurations: result := IDH_HTML_DRV_Touch_qt1_selfcap_MPLAB_Harmony_Configurations;
    IDH_DRV_Touch_qt1_selfcap_Hardware_Setup              : result := IDH_HTML_DRV_Touch_qt1_selfcap_Hardware_Setup;
    IDH_DRV_Touch_qt1_selfcap_Running_The_Application     : result := IDH_HTML_DRV_Touch_qt1_selfcap_Running_The_Application;
    IDH_DRV_Touch_qt1_mutualcap                           : result := IDH_HTML_DRV_Touch_qt1_mutualcap;
    IDH_DRV_Touch_qt1_mutualcap_Building_The_Application  : result := IDH_HTML_DRV_Touch_qt1_mutualcap_Building_The_Application;
    IDH_DRV_Touch_qt1_mutualcap_MPLAB_Harmony_Configurations: result := IDH_HTML_DRV_Touch_qt1_mutualcap_MPLAB_Harmony_Configurations;
    IDH_DRV_Touch_qt1_mutualcap_Hardware_Setup            : result := IDH_HTML_DRV_Touch_qt1_mutualcap_Hardware_Setup;
    IDH_DRV_Touch_qt1_mutualcap_Running_The_Application   : result := IDH_HTML_DRV_Touch_qt1_mutualcap_Running_The_Application;
    IDH_DRV_Touch_on_board_sensor                         : result := IDH_HTML_DRV_Touch_on_board_sensor;
    IDH_DRV_Touch_on_board_sensor_Building_The_Application: result := IDH_HTML_DRV_Touch_on_board_sensor_Building_The_Application;
    IDH_DRV_Touch_on_board_sensor_MPLAB_Harmony_Configurations: result := IDH_HTML_DRV_Touch_on_board_sensor_MPLAB_Harmony_Configurations;
    IDH_DRV_Touch_on_board_sensor_Hardware_Setup          : result := IDH_HTML_DRV_Touch_on_board_sensor_Hardware_Setup;
    IDH_DRV_Touch_on_board_sensor_Running_The_Application : result := IDH_HTML_DRV_Touch_on_board_sensor_Running_The_Application;
    IDH_app_qt7_self_cap                                  : result := IDH_HTML_app_qt7_self_cap;
    IDH_qt7_self_cap_Building_the_Applications            : result := IDH_HTML_qt7_self_cap_Building_the_Applications;
    IDH_qt7_self_cap_MPLAB_Harmony_Configurations         : result := IDH_HTML_qt7_self_cap_MPLAB_Harmony_Configurations;
    IDH_qt7_self_cap_Hardware_Setup                       : result := IDH_HTML_qt7_self_cap_Hardware_Setup;
    IDH_qt7_self_cap_Running_The_Application              : result := IDH_HTML_qt7_self_cap_Running_The_Application;
    else result := -1;
  end;
end;
