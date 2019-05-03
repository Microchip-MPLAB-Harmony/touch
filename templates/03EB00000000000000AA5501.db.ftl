<#assign heading = 'Touch Data Visualizer'>
<#assign debug_data_label = 'Sensor Data' >
<#assign debug_data_key = ['State', 'Delta', 'Threshold']>
<#assign debug_data_node = ['Signal', 'Reference' , 'Delta', 'Compensation'] >
<#assign debug_graph_data = ['Signal', 'Reference' , 'Delta', 'Threshold'] >
<#assign debug_data_node_title = ['Signal', 'Reference' , 'Delta', 'Compensation pF'] >
<#assign label_ele = 10+5+TOUCH_CHAN_ENABLE_CNT*2>
<#assign debug_data_key_label = 'Button Data' >
<#assign debug_data_hop_label = 'Frequency Hop Data' >
<#assign node_cnt = TOUCH_CHAN_ENABLE_CNT>
<#assign key_cnt = TOUCH_KEY_ENABLE_CNT>
<#assign scr_cnt = TOUCH_SCROLLER_ENABLE_CNT>
<#assign debug_data_others_label = 'Debug Data' >
<#assign debug_data_others = ['FrameCounter', 'QTouchLibError'] >
<#assign blank = [" "]>
<#assign scr_info = []>
<#if TUNE_MODE_SELECTED != "CAL_AUTO_TUNE_NONE">
<#assign label_ele = label_ele + 1 >
<#assign debug_data_node_title = ['Signal', 'Reference' , 'Delta', 'Compensation pF', 'CSD'] >
<#assign debug_data_node = ['Signal', 'Reference' , 'Delta', 'Compensation', 'CSD'] >
</#if>

<#assign all_data_tab = '4'>
<#assign sensor_tab = '1'>
<#assign debug_tab = '1'>
<#assign node_tab = '3'>
<#assign freq_hop_tab = '3'>
<#assign graph_tab = '2'>

<#if FREQ_AUTOTUNE==true>
<#--if ENABLE_FREQ_HOP==true-->
<#assign debug_data_hop = ['CurrentFrequency']>
<#list 0..FREQ_HOP_STEPS-1 as i>
<#assign debug_data_hop = debug_data_hop + [('HopFrequency+(i)')]>
</#list>
</#if>

<#if scr_cnt != 0 >
<#assign debug_data_scroller_label = 'Slider & Wheel Data' >
<#assign debug_data_scroller = ['SWState', 'SWDelta', 'SWThreshold', 'SWPosition'] >
<#assign debug_data_scroller_header = ['State', 'SW Delta', 'SW Threshold', 'Position'] >
<#assign debug_graph_data_scr = ['SWDelta', 'SWThreshold'] >
</#if>

<#if scr_cnt != 0 >
<#assign scroller_from_ch = []>
<#assign scroller_num_ch = []>
<#assign scroller_txt = []>
<#assign scr_info = []>
<#list 0..scr_cnt-1 as cnt >
<#assign TOUCH_SCR_START_KEY = "TOUCH_SCR_START_KEY" + cnt>
<#assign DEF_SCR_TYPE = "DEF_SCR_TYPE" + cnt>
<#assign TOUCH_SCR_SIZE = "TOUCH_SCR_SIZE" + cnt>
<#assign scroller_from_ch +=  [.vars[TOUCH_SCR_START_KEY]]>
<#assign scroller_num_ch += [.vars[TOUCH_SCR_SIZE]]>
<#assign temp_info = .vars[DEF_SCR_TYPE]>
<#if temp_info == "SCROLLER_TYPE_SLIDER" >
<#assign temp_info = "Slider" >
<#else>
<#assign temp_info = "Wheel" >
</#if>
<#assign scroller_txt +=  [temp_info] >
</#list>
<#assign scr_info =  scroller_from_ch + scroller_num_ch + scroller_txt>
</#if>

<#-- MACROS for db script -->
<#macro db_buid_graph tab,element,plot_count,x_pos,y_pos>
{
0:0:${tab}, // Dashboard ID
${element}, // Element ID
DB_TYPE_GRAPH, // Element Type
0, // Z-Index (GUI stack order)
${x_pos}, 0, // X-coordinate
${y_pos}, 0, // Y-coordinate
1200, 0, // Width
500, 0, // Height
255, 255, 255, // Title color
0, 0, 0, // Background color
20, 20, 20, // Graph background color
'Q', 'T', 'o', 'u', 'c', 'h', ' ', 'G', 'r', 'a', 'p', 'h','\0', // Title
${plot_count}, // Number of plots
0,0,0,0, // X Minimum
0,0,32,65, // X Maximum
0,0,0,0, // Y Minimum
0,0,32,65, // Y Maximum
5,
1,
};
</#macro>

<#macro db_buid_signal_element tab,element,x_pos,y_pos,width,height>
{
0:0:${tab}, // Dashboard ID
${element}, // Element ID
DB_TYPE_SIGNAL, // Element Type
0, // Z-Index (GUI stack order)
${x_pos}, 0, // X-coordinate
${y_pos}, 0, // Y-coordinate
${width}, 0, // Width
${height}, 0, // Height
128, 0, 255, 0, // Color On
128, 255, 0, 0, // Color Off
};
</#macro>

<#macro db_build_signal_element tab,ele_num,x_pos,y_pos,temp_lable_w, temp_row_h,node_cnt >
<#list 0..(node_cnt-1) as cnt >
<#local temp_y_pos = y_pos + (temp_row_h * cnt)>
<#local temp_ele_num = ele_num + cnt >
<@db_buid_signal_element tab,temp_ele_num, x_pos, temp_y_pos, temp_lable_w, temp_row_h />
</#list>
</#macro>

<#macro db_buid_label tab,height, element,x_pos,y_pos,title,width >
{
0:0:${tab}, // Dashboard ID
${element}, // Element ID
DB_TYPE_LABEL, // Element Type
0, // Z-Index (GUI stack order)
${x_pos}, 0, // X-coordinate
${y_pos}, 0, // Y-coordinate
${width}, 0, // Width
${height}, 0, // Height
14, // Font Size
3,
1, // Horizontal Alignment
1, // Vertical Alignment
77, 77, 77, 77, // Background Color
255, 0, 0, 0, // Foreground Color
<#list 0..(title?length-1) as n >'${title[n]}',</#list>'\0', // Text
};
</#macro>

<#macro db_buid_label_colourless tab,height, element,x_pos,y_pos,title,width >
{
0:0:${tab}, // Dashboard ID
${element}, // Element ID
DB_TYPE_LABEL, // Element Type
0, // Z-Index (GUI stack order)
${x_pos}, 0, // X-coordinate
${y_pos}, 0, // Y-coordinate
${width}, 0, // Width
${height}, 0, // Height
12, // Font Size
3,
0, // Horizontal Alignment
1, // Vertical Alignment
126, 255, 255, 255, // Background Color
255, 0, 0, 0, // Foreground Color
<#list 0..(title?length-1) as n>'${title[n]}',</#list>'\0', // Text
};
</#macro>

<#macro db_buid_label_links tab,height, element,x_pos,y_pos,title,width >
{
0:0:${tab}, // Dashboard ID
${element}, // Element ID
DB_TYPE_LABEL, // Element Type
0, // Z-Index (GUI stack order)
${x_pos}, 0, // X-coordinate
${y_pos}, 0, // Y-coordinate
${width}, 0, // Width
${height}, 0, // Height
14, // Font Size
3,
0, // Horizontal Alignment
1, // Vertical Alignment
126, 255, 255, 255, // Background Color
255, 0, 0, 255, // Foreground Color
<#list 0..(title?length-1) as n>'${title[n]}',</#list>'\0', // Text
};
</#macro>

<#macro db_build_table_element tab,element_num, xpos, ypos, Width, Height, data_width, label_width, row_height, rows, columns >
{
0:0:${tab}, // Dashboard ID
${element_num}, // Element ID
DB_TYPE_TABLE, // Element Type
0, // Z-Index (GUI stack order)
${xpos}, 0, // X-coordinate
${ypos}, 0, // Y-coordinate
${Width}, 0, // Width
${Height}, 0, // Height
12, // Data Font Size
12, // Label Font Size
${data_width},0, // Data Column Width
${label_width},0, // Label Column Width
${row_height},0, // Row Height
${rows}, // Number of Rows
${columns}, // Number of Columns
1, // AutoLabels
'\0', // Label Configuration
0,
0, 255, 255, 255, // Background Color
255, 0, 0, 0, // Foreground Color
0, // Label Horizontal Alignment
1, // Data Horizontal Alignment
};
</#macro>

<#macro db_build_table_element_new_table title, tab,element_num, xpos, ypos, Width, Height, data_width, label_width, row_height, rows, columns >
{
0:0:${tab}, // Dashboard ID
${element_num}, // Element ID
DB_TYPE_TABLE, // Element Type
0, // Z-Index (GUI stack order)
${xpos}, 0, // X-coordinate
${ypos}, 0, // Y-coordinate
${Width}, 0, // Width
${Height}, 0, // Height
12, // Data Font Size
12, // Label Font Size
${data_width},0, // Data Column Width
${label_width},0, // Label Column Width
${row_height},0, // Row Height
${rows}, // Number of Rows
${columns}, // Number of Columns
0, // AutoLabels
<#list 0..(title?size-1) as n ><#list 0..(title[n]?length-1) as n1>'${title[n][n1]}',</#list></#list>'\0', // Text
4,
0, 255, 255, 255, // Background Color
255, 0, 0, 0, // Foreground Color
1, // Label Horizontal Alignment
1, // Data Horizontal Alignment
};
</#macro>

<#macro build_sensor_type_table tab,temp_ele_num, x_pos, y_pos, row_height, temp_lable_w, node_cnt, scr_cnt, scr_info >
<#assign debug_table_title = ['Channel ID', 'Sensor Type'] >
<#assign column_cnt = debug_table_title?size >
<#assign temp_string = [] >
<#assign temp_width1 = (temp_lable_w) * (column_cnt) >
<#assign temp_height1 = (row_height) * node_cnt> 
<#assign element_num = temp_ele_num >
<#assign temp_string = [] >
<#assign sen_type_but_cnt = [] >
<#assign sen_type_scr_cnt = [] >
<#assign sen_type_sli_cnt = [] >
<#assign sen_type_whe_cnt = [] >
<#list 0..(debug_table_title?size-1) as cnt >
<#assign temp_string = temp_string + [((cnt)+":0"+":"+(debug_table_title[cnt])+";")]>
</#list>
<@db_build_table_element_new_table temp_string, tab, element_num,x_pos,y_pos,temp_width1, temp_height1,temp_lable_w, temp_lable_w,row_height,1, column_cnt />
<#local  y_pos = y_pos + row_height >
<#assign temp_string = [] >
<#assign scr_from_ch_info =[] >
<#assign scr_num_ch_info =[]>
<#assign scr_txt =[] >
<#list 0..(node_cnt-1) as cnt >
<#if scr_cnt != 0 >
<#list 0..TOUCH_SCROLLER_ENABLE_CNT-1 as i >
<#assign TOUCH_SCR_START_KEY = "TOUCH_SCR_START_KEY" + i>
<#assign DEF_SCR_TYPE = "DEF_SCR_TYPE" + i>
<#assign TOUCH_SCR_SIZE = "TOUCH_SCR_SIZE" + i>
<#assign scr_from_ch_info += [.vars[TOUCH_SCR_START_KEY]] >
<#assign scr_num_ch_info += [.vars[TOUCH_SCR_SIZE]]>
<#assign scr_txt += [.vars[DEF_SCR_TYPE]] >
</#list>
</#if>
<#assign temp_string = temp_string + [("0:"+(cnt)+":"+(cnt)+";")] >

<#if (sen_type_scr_cnt?size) < scr_cnt >
<#if (scr_cnt > 0) && (cnt == (scr_from_ch_info[sen_type_scr_cnt?size]+scr_num_ch_info[sen_type_scr_cnt?size])) >
<#assign tmp_txt = scr_txt[sen_type_scr_cnt?size] >
<#if tmp_txt == "SCROLLER_TYPE_SLIDER" > <#assign sen_type_sli_cnt=sen_type_sli_cnt + [1] >
<#elseif tmp_txt == "SCROLLER_TYPE_WHEEL" > <#assign sen_type_whe_cnt=sen_type_whe_cnt + [1] >
</#if>
<#assign sen_type_scr_cnt=sen_type_scr_cnt +[1]>
</#if>
</#if>
<#if (sen_type_scr_cnt?size) < scr_cnt >
<#if (scr_cnt > 0) && (cnt >= (scr_from_ch_info[sen_type_scr_cnt?size])) && (cnt <= scr_from_ch_info[sen_type_scr_cnt?size]+scr_num_ch_info[sen_type_scr_cnt?size]) >
<#assign tmp_txt = scr_txt[sen_type_scr_cnt?size] >
<#assign temp_val = cnt - scr_from_ch_info[sen_type_scr_cnt?size] >
<#if tmp_txt == "SCROLLER_TYPE_SLIDER" > <#assign temp_string=temp_string + [("1:"+(cnt)+":"+("Slider")+" "+(sen_type_sli_cnt?size)+"["+(temp_val)+"];")] >
<#elseif tmp_txt == "SCROLLER_TYPE_WHEEL" > <#assign temp_string = temp_string + [("1:"+(cnt)+":"+("Wheel")+" "+(sen_type_whe_cnt?size)+"["+(temp_val)+"];")] >
</#if>
<#else>
<#assign temp_string=temp_string + [("1:"+(cnt)+":"+"Button"+" "+(sen_type_but_cnt?size)+";")] > <#assign sen_type_but_cnt = sen_type_but_cnt +[1]>
</#if>
<#else>
<#assign temp_string=temp_string + [("1:"+(cnt)+":"+"Button"+" "+(sen_type_but_cnt?size)+";")] > <#assign sen_type_but_cnt = sen_type_but_cnt +[1]>
</#if>
</#list>
<@db_build_table_element_new_table temp_string, tab, element_num+1,x_pos,y_pos,temp_width1, temp_height1,temp_lable_w, temp_lable_w,row_height,node_cnt, column_cnt />
</#macro>


<#macro build_sensor_type_table_scr tab, temp_ele_num, x_pos, y_pos, row_height, temp_lable_w, node_cnt, scr_cnt, scr_info >
<#assign column_cnt = scr_cnt >
<#assign temp_string = [] >
<#assign temp_width11 = (temp_lable_w) * (column_cnt) >
<#assign temp_height11 = (row_height) * node_cnt >
<#assign element_num = temp_ele_num >
<#assign scr_from_ch_info =[] >
<#assign scr_num_ch_info =[]>
<#assign scr_txt =[] >
<#if scr_cnt != 0 >
<#list 0..TOUCH_SCROLLER_ENABLE_CNT-1 as i >
<#assign TOUCH_SCR_START_KEY = "TOUCH_SCR_START_KEY" + i>
<#assign DEF_SCR_TYPE = "DEF_SCR_TYPE" + i>
<#assign TOUCH_SCR_SIZE = "TOUCH_SCR_SIZE" + i>
<#assign scr_from_ch_info += [.vars[TOUCH_SCR_START_KEY]] >
<#assign scr_num_ch_info += [.vars[TOUCH_SCR_SIZE]] >
<#assign scr_txt += [.vars[DEF_SCR_TYPE]] >
</#list>
</#if>
<#assign sen_type_scr_cnt = [] >
<#assign sen_type_sli_cnt = [] >
<#assign sen_type_whe_cnt = [] >
<#list 0..(node_cnt-1) as cnt>
<#if (sen_type_scr_cnt?size < scr_cnt) && (cnt == (scr_from_ch_info[sen_type_scr_cnt?size])) >
<#if scr_txt[sen_type_scr_cnt?size] == "SCROLLER_TYPE_SLIDER" > <#assign temp_string = temp_string + [("0:"+(sen_type_scr_cnt?size)+":"+"Slider "+(sen_type_sli_cnt?size)+";")] > <#assign sen_type_sli_cnt = sen_type_sli_cnt + [1] >
<#elseif scr_txt[sen_type_scr_cnt?size] == "SCROLLER_TYPE_WHEEL" > <#assign temp_string = temp_string + [("0:"+(sen_type_scr_cnt?size)+":"+"Wheel "+(sen_type_whe_cnt?size)+";")] > <#assign sen_type_whe_cnt=sen_type_whe_cnt + [1] >
</#if>
<#assign sen_type_scr_cnt = sen_type_scr_cnt +[1] >
</#if>
</#list>
<@db_build_table_element_new_table temp_string, tab, element_num,x_pos,y_pos,temp_width11, temp_height11,temp_lable_w, temp_lable_w,row_height,scr_cnt, 1 />
</#macro>

<#macro build_table_headings tab, title, temp_ele_num, x_pos, y_pos, row_height, temp_lable_w, node_cnt >
<#assign column_cnt = title?size >
<#assign temp_string = [] >
<#assign temp_width2 = (temp_lable_w) * (column_cnt) >
<#assign temp_height2 = (row_height) * node_cnt >
<#assign element_num = temp_ele_num >
<#list 0..(title?size-1) as cnt>
<#assign temp_string =  temp_string + [((cnt)+":0"+":"+(title[cnt])+";")]>
</#list>
<@db_build_table_element_new_table temp_string, tab, element_num,x_pos,y_pos,temp_width2, temp_height2,temp_lable_w, temp_lable_w, row_height,node_cnt, column_cnt />
</#macro>


<#--  ####start of db file scripts#### -->
<#if (TOUCH_CHAN_ENABLE_CNT%2) == 0 >
<#assign dashboard_height = TOUCH_CHAN_ENABLE_CNT/2 >
<#else>
<#assign dashboard_height = (TOUCH_CHAN_ENABLE_CNT+1)/2>
</#if>
<#if dashboard_height  < 2 >
<#assign dashboard_height = 3 >
</#if>
{
0,
<#--'Q', 'T', 'o', 'u', 'c', 'h', ' ', 'D', 'a', 't', 'a', ' ','V', 'i', 's', 'u', 'a', 'l', 'i', 'z', 'e', 'r','\0',-->
<#list 0..(heading?length-1) as n>'${heading[n]}',</#list>'\0', //heading
0, 255, 255, 255,
200, ${dashboard_height+3},
};

{
0, // Dashboard ID
0, // Element ID
DB_TYPE_TAB, // Element Type
1-BasicData,2-Graph,3-AdvanceData,4-AllData,
${(dashboard_height+3) * 300}
};

<#-- Initialize the data visualizer dash board element positions -->
<#assign ele_num = 0 >
<#assign x_pos = 0 >
<#assign y_pos = 0 >
<#assign temp_data_w = 50 >
<#assign temp_lable_w = 125 >
<#assign temp_row_height = 30 >
<#assign y_offset = temp_row_height + 5 >

<#--  -------------------SENSOR SPECIFIC DATA ----------------------- -->

<#if TOUCH_KEY_ENABLE_CNT!= 0 >
<#assign temp_rows = TOUCH_KEY_ENABLE_CNT >
<#assign temp_column = debug_data_key?size >
<#assign temp_width = (temp_lable_w) * temp_column >
<#assign temp_height = (temp_row_height) * temp_rows >

<#-- LINKS  -->
<#assign temp_string = "QTouch Modular Library User Guide: www.microchip.com" >
<@db_buid_label_links all_data_tab, temp_row_height, label_ele,x_pos,y_pos,temp_string,1200/>
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + y_offset >
<#assign temp_string = "Glossary: www.microchip.com" >
<@db_buid_label_links all_data_tab, temp_row_height, label_ele,x_pos,y_pos,temp_string,1200/>
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + y_offset >
<#assign temp_y_pos = 0 >

<#-- Button data label  -->
<@db_buid_label sensor_tab, temp_row_height, label_ele,x_pos,temp_y_pos,debug_data_key_label,(temp_lable_w * (temp_column+2))/>
<#assign label_ele = label_ele + 1 >
<@db_buid_label all_data_tab, temp_row_height, label_ele,x_pos, y_pos,debug_data_key_label,(temp_lable_w * (temp_column+2))/>
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + y_offset >
<#assign temp_y_pos = temp_y_pos + y_offset >

<#-- sensor label -->
<@build_sensor_type_table sensor_tab, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, node_cnt, scr_cnt, scr_info />
<#assign label_ele = label_ele + 2 >
<@build_sensor_type_table all_data_tab, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, node_cnt, scr_cnt, scr_info />
<#assign label_ele = label_ele + 2 >
<#assign x_pos = x_pos + temp_lable_w*2 >
<@build_table_headings sensor_tab, debug_data_key, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, 1 />
<#assign label_ele = label_ele + 1 >
<@build_table_headings all_data_tab, debug_data_key, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, 1 />
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height >
<#assign temp_y_pos = temp_y_pos + temp_row_height >

<#-- Button data table  -->
<@db_build_table_element_new_table  blank,sensor_tab,ele_num,x_pos,temp_y_pos,temp_width, temp_height,temp_lable_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign ele_num = ele_num + 1 >
<@db_build_table_element_new_table blank,all_data_tab,ele_num,x_pos,y_pos,temp_width, temp_height,temp_lable_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign ele_num = ele_num + 1 >
<#assign x_pos = 0 >
<#assign y_pos = y_pos + temp_height >
<#assign temp_y_pos = temp_y_pos + temp_height >

<#-- Signaling ON/OFF -->
<#assign temp_y_pos = temp_y_pos - temp_height>
<#assign y_pos = y_pos - temp_height>
<#assign x_pos = x_pos + 2 * temp_lable_w >
<@db_build_signal_element sensor_tab,ele_num,x_pos,temp_y_pos,temp_lable_w, temp_row_height, node_cnt />
<#assign ele_num = ele_num + node_cnt >
<@db_build_signal_element all_data_tab,ele_num,x_pos,y_pos,temp_lable_w, temp_row_height, node_cnt />
<#assign ele_num = ele_num + node_cnt >
<#assign x_pos = 0 >
<#assign y_pos = y_pos + temp_height >
<#assign temp_y_pos = temp_y_pos + temp_height >
</#if>

<#if (scr_cnt >0)>
<#assign x_pos = (temp_lable_w * (temp_column+3))>
<#assign y_pos = y_pos - temp_height >
<#assign y_pos = y_pos - temp_row_height>
<#assign y_pos = y_pos - y_offset >
<#assign temp_y_pos = temp_y_pos - temp_height >
<#assign temp_y_pos = temp_y_pos - temp_row_height >
<#assign temp_y_pos = temp_y_pos - y_offset >
<#assign temp_rows = scr_cnt >
<#assign temp_column = debug_data_scroller?size >
<#assign temp_width = (temp_data_w+temp_lable_w) * temp_column>
<#assign temp_height = (temp_row_height) * temp_rows >

<#-- Scroller data label -->
<@db_buid_label sensor_tab,temp_row_height, label_ele,x_pos,temp_y_pos,debug_data_scroller_label,(temp_lable_w * (temp_column+1))/>
<#assign label_ele = label_ele + 1 >
<@db_buid_label all_data_tab,temp_row_height, label_ele,x_pos,y_pos,debug_data_scroller_label,(temp_lable_w * (temp_column+1)) />
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + y_offset >
<#assign temp_y_pos = temp_y_pos + y_offset >

<#assign tempdata = ["Sensor"]>
<@build_table_headings sensor_tab, tempdata, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, 1 />
<#assign label_ele = label_ele + 1 >
<@build_table_headings all_data_tab, tempdata, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, 1 />
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height >
<#assign temp_y_pos = temp_y_pos + temp_row_height >

<@build_sensor_type_table_scr sensor_tab, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, node_cnt, scr_cnt, scr_info/>
<#assign label_ele = label_ele + 1 >
<@build_sensor_type_table_scr all_data_tab, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, node_cnt, scr_cnt, scr_info/>
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height >
<#assign temp_y_pos = temp_y_pos + temp_row_height >

<#assign x_pos = x_pos + temp_lable_w >
<#assign y_pos = y_pos - temp_row_height >
<#assign y_pos = y_pos - temp_row_height >
<#assign temp_y_pos = temp_y_pos - temp_row_height >
<#assign temp_y_pos = temp_y_pos - temp_row_height >
<@build_table_headings sensor_tab, debug_data_scroller_header, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, 1 />
<#assign label_ele = label_ele + 1 >
<@build_table_headings all_data_tab, debug_data_scroller_header, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, 1/>
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height >
<#assign temp_y_pos = temp_y_pos + temp_row_height >

<#-- Scroller data table -->
<@db_build_table_element_new_table blank,sensor_tab,ele_num,x_pos,temp_y_pos,temp_width, temp_height,temp_lable_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign ele_num = ele_num + 1 >
<@db_build_table_element_new_table blank,all_data_tab,ele_num,x_pos,y_pos,temp_width, temp_height,temp_lable_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign ele_num = ele_num + 1 >

<#--  Signaling ON/OFF  -->
<@db_build_signal_element sensor_tab, ele_num,x_pos,temp_y_pos,temp_lable_w, temp_row_height, scr_cnt />
<#assign ele_num = ele_num + scr_cnt >
<@db_build_signal_element all_data_tab, ele_num,x_pos,y_pos,temp_lable_w, temp_row_height, scr_cnt />
<#assign ele_num = ele_num + scr_cnt >

<#assign x_pos = 0 >
<#assign y_pos = y_pos + (temp_row_height * key_cnt) >
<#assign temp_y_pos = temp_y_pos + (temp_row_height * key_cnt) >
</#if>
<#--  -------------------GRAPH ELEMENT----------------------- -->
<#assign num_of_plots = node_cnt*(debug_graph_data?size)>
<#if scr_cnt != 0>
<#assign num_of_plots = num_of_plots+(scr_cnt*(debug_graph_data_scr?size)) >
</#if>
<#assign x_pos = 0 >
<#assign y_pos = y_pos + y_offset>
<@db_buid_graph graph_tab,ele_num, num_of_plots,x_pos,0 />
<#assign ele_num = ele_num + 1 >
<@db_buid_graph all_data_tab,ele_num, num_of_plots,x_pos,y_pos />
<#assign ele_num = ele_num + 1 >
<#assign temp_val = 25*((key_cnt/2)?int)>
<#if temp_val < 75>
<#assign temp_val = 75>
</#if>
<#assign y_pos = y_pos + (500) + temp_val>
<#assign temp_y_pos = (500) + temp_val >

<#assign temp_string = "* Vertial Zoom: Ctrl Key + Mouse Scroll (uncheck \"Automatically fit Y\" option).">
<@db_buid_label_colourless graph_tab,temp_row_height, label_ele, x_pos, temp_y_pos, temp_string, 500 />
<#assign label_ele = label_ele + 1>
<@db_buid_label_colourless all_data_tab,temp_row_height, label_ele, x_pos, y_pos, temp_string, 500 />
<#assign label_ele = label_ele + 1 >
<#assign x_pos = x_pos + 500>
<#assign temp_string = "* Horizontal Zoom: Left-Shift Key + Mouse Scroll.">
<@db_buid_label_colourless graph_tab, temp_row_height, label_ele, x_pos, temp_y_pos, temp_string, 300/>
<#assign label_ele = label_ele + 1>
<@db_buid_label_colourless all_data_tab,temp_row_height, label_ele, x_pos, y_pos, temp_string, 300/>
<#assign label_ele = label_ele + 1 >
<#assign x_pos = x_pos + 300>
<#assign temp_string = "* Click on \"Legend\" to enable or disable plot.">
<@db_buid_label_colourless graph_tab, temp_row_height, label_ele, x_pos, temp_y_pos, temp_string, 300/>
<#assign label_ele = label_ele + 1>
<@db_buid_label_colourless all_data_tab,temp_row_height, label_ele, x_pos, y_pos, temp_string, 300/>
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height*2>
<#assign x_pos = 0>

<#--  -------------------NODE SPECIFIC DATA ------------------ -->
<#assign temp_rows = node_cnt>
<#assign temp_column = debug_data_node?size>
<#assign temp_width = (temp_data_w+temp_lable_w) * temp_column>
<#assign temp_height = (temp_row_height) * temp_rows>
<#assign temp_y_pos = 0 >

<#-- Node specific data label -->
<@db_buid_label node_tab,temp_row_height, label_ele,x_pos,temp_y_pos,debug_data_label,(temp_lable_w * (temp_column+2))/>
<#assign label_ele = label_ele + 1 >
<#assign temp_y_pos = temp_y_pos + y_offset >
<@db_buid_label all_data_tab, temp_row_height, label_ele,x_pos,y_pos,debug_data_label,(temp_lable_w * (temp_column+2)) />
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + y_offset >

<#-- print sensor type label for node specific table  -->
<@build_sensor_type_table node_tab, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, node_cnt, scr_cnt, scr_info />
<#assign label_ele = label_ele + 2 >
<@build_sensor_type_table all_data_tab, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, node_cnt, scr_cnt, scr_info />
<#assign label_ele = label_ele + 2>
<#assign x_pos = x_pos + temp_lable_w*2>

<@build_table_headings node_tab, debug_data_node_title, label_ele, x_pos, temp_y_pos, temp_row_height, temp_lable_w, 1/>
<#assign label_ele = label_ele + 1 >
<#assign temp_y_pos = temp_y_pos + temp_row_height >
<@build_table_headings all_data_tab, debug_data_node_title, label_ele, x_pos, y_pos, temp_row_height, temp_lable_w, 1/>
<#assign label_ele = label_ele + 1>
<#assign y_pos = y_pos + temp_row_height>

<#-- Node specific data table  -->
<@db_build_table_element_new_table blank,node_tab,ele_num,x_pos,temp_y_pos,temp_width, temp_height,temp_lable_w, temp_lable_w,temp_row_height,temp_rows, temp_column/>
<#assign temp_y_pos = temp_y_pos + temp_height >
<#assign ele_num = ele_num + 1 >

<@db_build_table_element_new_table blank,all_data_tab,ele_num,x_pos,y_pos,temp_width, temp_height,temp_lable_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign x_pos = 0 >
<#assign y_pos = y_pos + temp_height>
<#assign ele_num = ele_num + 1>

<#assign temp_string = "Compensation: Represents PTC compensation circuit value which is equivalent to sensor capacitance">
<@db_buid_label_colourless node_tab,25, label_ele, x_pos, temp_y_pos, temp_string, 800 />
<#assign label_ele = label_ele + 1 >
<#assign temp_y_pos = temp_y_pos + 25 >
<@db_buid_label_colourless all_data_tab, 25, label_ele, x_pos, y_pos, temp_string, 800 />
<#assign label_ele = label_ele + 1>
<#assign y_pos = y_pos + 25>
<#assign x_pos = 0>
<#assign temp_string = "\"Compensation\" value can be used to check whether sensor is saturated. Refer to User Guide">
<@db_buid_label_colourless node_tab,25, label_ele, x_pos, temp_y_pos, temp_string, 800 />
<#assign label_ele = label_ele + 1 >
<#assign temp_y_pos = temp_y_pos + 25 >
<@db_buid_label_colourless all_data_tab, 25, label_ele, x_pos, y_pos, temp_string, 800 />
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + 25 >
<#assign x_pos = 0>

<#if TUNE_MODE_SELECTED != "CAL_AUTO_TUNE_NONE">
<#if TUNE_MODE_SELECTED=='CAL_AUTO_TUNE_CSD'>
<#assign temp_string = "Charge Share Delay (CSD): displayed values are auto-tuned by QTouch Library">
<#else>
<#assign temp_string = "Prescaler: displayed values are auto-tuned by QTouch Library">
</#if>
<@db_buid_label_colourless node_tab, temp_row_height, label_ele, x_pos, y_pos, temp_string, 800/>
<#assign label_ele = label_ele + 1>
<#assign  temp_y_pos = temp_y_pos + temp_row_height >
<@db_buid_label_colourless all_data_tab,temp_row_height, label_ele, x_pos, y_pos, temp_string, 800/>
<#assign  label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height>
<#assign x_pos = 0>
<#assign y_pos = y_pos + y_offset>
<#else>
<#assign y_pos = y_pos + y_offset>
</#if>

<#if FREQ_AUTOTUNE==true >
<#assign temp_rows = 1 >
<#assign temp_column = debug_data_hop?size >
<#assign temp_width = (temp_data_w+temp_lable_w) * temp_column >
<#assign temp_height = (temp_row_height) * temp_rows >

<#-- Freq Hop data label -->
<@db_buid_label freq_hop_tab,temp_row_height, label_ele,x_pos,temp_y_pos,debug_data_hop_label,temp_width />
<#assign temp_y_pos = temp_y_pos + y_offset >
<#assign label_ele = label_ele + 1 >
<@db_buid_label all_data_tab,temp_row_height, label_ele,x_pos,y_pos,debug_data_hop_label,temp_width />
<#assign y_pos = y_pos + y_offset >
<#assign label_ele = label_ele + 1 >

<#-- Freq Hop data table -->
<@db_build_table_element freq_hop_tab,ele_num,x_pos,temp_y_pos,temp_width, temp_height,temp_data_w, temp_lable_w,temp_row_height,temp_rows, temp_column/>
<#assign temp_y_pos = temp_y_pos + temp_height >
<#assign ele_num = ele_num + 1 >
<@db_build_table_element all_data_tab,ele_num,x_pos,y_pos,temp_width, temp_height,temp_data_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign x_pos = 0 >
<#assign y_pos = y_pos + temp_height >
<#assign ele_num = ele_num + 1 >

<#assign temp_string = "Displayed frequencies are auto-tuned by QTouch Library based on noise levels">
<@db_buid_label_colourless freq_hop_tab,temp_row_height, label_ele, x_pos, temp_y_pos, temp_string, 800 />
<#assign label_ele = label_ele + 1 >
<#assign temp_y_pos = temp_y_pos + temp_row_height >
<@db_buid_label_colourless all_data_tab,temp_row_height, label_ele, x_pos, y_pos, temp_string, 800 />
<#assign label_ele = label_ele + 1 >
<#assign y_pos = y_pos + temp_row_height >
<#assign x_pos = 0 >
<#assign temp_y_pos = temp_y_pos + y_offset >
<#assign y_pos = y_pos + y_offset >

</#if >


<#-- Other Debug Parameters table -->
<#assign temp_rows = debug_data_others?size >
<#assign temp_column = 1 >
<#assign temp_width = (temp_data_w+temp_lable_w) * temp_column >

<#-- Other Debug Parameters data label -->
<@db_buid_label sensor_tab,temp_row_height, label_ele,x_pos,temp_y_pos,debug_data_others_label,temp_width/>
<#assign temp_y_pos = temp_y_pos + y_offset >
<#assign label_ele = label_ele + 1 >
<@db_buid_label all_data_tab, temp_row_height, label_ele,x_pos,y_pos,debug_data_others_label,temp_width />
<#assign y_pos = y_pos + y_offset >
<#assign label_ele = label_ele + 1 >

<@db_build_table_element sensor_tab,ele_num,x_pos,temp_y_pos,temp_width, temp_height,temp_data_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign temp_y_pos = temp_y_pos + temp_height >
<#assign ele_num = ele_num + 1 >
<@db_build_table_element all_data_tab,ele_num,x_pos,y_pos,temp_width, temp_height,temp_data_w, temp_lable_w,temp_row_height,temp_rows, temp_column />
<#assign y_pos = y_pos + temp_height >
<#assign ele_num = ele_num + 1 >

<#assign x_pos = 0 >
<#assign temp_string = "Counter for datastreamer packets.  Missing count indicate packet drop">
<#assign x_pos = (temp_data_w+temp_lable_w) * 1 >
<#assign x_pos = x_pos + 25 >
<#assign y_pos = y_pos - temp_height >
<#assign temp_y_pos = temp_y_pos - temp_height >
<@db_buid_label_colourless sensor_tab, temp_row_height, label_ele, x_pos, temp_y_pos, temp_string, 800 />
<#assign temp_y_pos = temp_y_pos + temp_row_height >
<#assign label_ele = label_ele + 1 >
<@db_buid_label_colourless all_data_tab,temp_row_height, label_ele, x_pos, y_pos, temp_string, 800 />
<#assign y_pos = y_pos + temp_row_height >
<#assign label_ele = label_ele + 1 >
<#assign temp_string = "Indicates library error state. Zero: no error. Refer \"Error Code\" section in User Guide" >
<@db_buid_label_colourless sensor_tab,temp_row_height, label_ele, x_pos, temp_y_pos, temp_string, 800 />
<#assign temp_y_pos = temp_y_pos + temp_row_height >
<#assign label_ele = label_ele + 1 >
<@db_buid_label_colourless all_data_tab, temp_row_height, label_ele, x_pos, y_pos, temp_string, 800 />
<#assign x_pos = 0 >
<#assign y_pos = y_pos + temp_row_height >
<#assign label_ele = label_ele + 1 >
