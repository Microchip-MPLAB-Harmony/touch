<#assign pic_devices = ["PIC32MZW","PIC32MZDA"]>

<#if (TOUCH_CHAN_ENABLE_CNT > 0) >
<#assign total_channels = TOUCH_CHAN_ENABLE_CNT-1>


<#if ENABLE_SCROLLER ==true>
<#assign scr_cnt = TOUCH_SCROLLER_ENABLE_CNT>
<#else>
<#assign scr_cnt = 0>
</#if>

<#assign offset = 0>
<#list 0..total_channels as i>
State${i}, ${offset} (Column:0;Row:${i})
Delta${i}, ${offset} (Column:1;Row:${i})
Threshold${i}, ${offset} (Column:2;Row:${i})
</#list>
<#assign offset = offset +1>
<#list 0..total_channels as i>
State${i}, ${offset} (Column:0;Row:${i})
Delta${i}, ${offset} (Column:1;Row:${i})
Threshold${i}, ${offset} (Column:2;Row:${i})
</#list>

<#assign offset = offset +1>
<#list 0..total_channels as i>
State${i}, ${i+offset}
</#list>
<#assign offset = offset +1>
<#list 0..total_channels as i>
State${i}, ${total_channels+i+offset}
</#list>

<#assign offset = total_channels+offset +1>
<#if (scr_cnt > 0)> 
<#list 0..scr_cnt-1 as y>
SWState${y}, ${total_channels+offset} (Column:0;Row:${y})
SWDelta${y}, ${total_channels+offset}(Column:1;Row:${y})
SWThreshold${y}, ${total_channels+offset} (Column:2;Row:${y})
SWPosition${y}, ${total_channels+offset} (Column:3;Row:${y})
</#list>
<#assign offset = offset +1>
<#list 0..scr_cnt-1 as y>
SWState${y}, ${total_channels+offset} (Column:0;Row:${y})
SWDelta${y}, ${total_channels+offset}(Column:1;Row:${y})
SWThreshold${y}, ${total_channels+offset} (Column:2;Row:${y})
SWPosition${y}, ${total_channels+offset} (Column:3;Row:${y})
</#list>

<#assign offset = offset +1>
<#list 0..scr_cnt-1 as y>
SWState${y}, ${total_channels+offset+y}
</#list>
<#assign offset = offset +scr_cnt>
<#list 0..scr_cnt-1 as y>
SWState${y}, ${total_channels+offset+y}
</#list>
<#assign offset = offset +scr_cnt>
</#if>

<#if ENABLE_SURFACE == true>
<#if ENABLE_SURFACE1T != true>
<#assign position = 1>
<#else>
<#assign position = 0>
</#if>
<#list 0..position as i>
SurStatus${i}, ${total_channels+offset} (Column:0;Row:${i})
hposition${i}, ${total_channels+offset}(Column:1;Row:${i})
vposition${i}, ${total_channels+offset} (Column:2;Row:${i})
conctsize${i}, ${total_channels+offset} (Column:3;Row:${i})
</#list>
<#assign offset = offset +1>
<#list 0..position as i>
SurStatus${i}, ${total_channels+offset} (Column:0;Row:${i})
hposition${i}, ${total_channels+offset}(Column:1;Row:${i})
vposition${i}, ${total_channels+offset} (Column:2;Row:${i})
conctsize${i}, ${total_channels+offset} (Column:3;Row:${i})
</#list>

<#assign offset = offset +1>
<#if ENABLE_SURFACE1T != true>
Sur2TStatus0, ${total_channels+offset} (Column:0;Row:0)
<#assign offset = offset +1>
Sur2TStatus0, ${total_channels+offset} (Column:0;Row:0)
<#assign offset = offset +1>
</#if>
</#if>

<#list 0..total_channels as i>
Signal${i},${total_channels+offset}(visible:0)
</#list>
<#list 0..total_channels as i>
Reference${i},${total_channels+offset}(visible:0)
</#list>
<#list 0..total_channels as i>
Delta${i},${total_channels+offset}(visible:1)
</#list>
<#list 0..total_channels as i>
Threshold${i},${total_channels+offset}(visible:1)
</#list>

<#if (scr_cnt > 0)> 
<#list 0..scr_cnt-1 as y>
SWDelta${y},${total_channels+offset}(visible:1)
</#list>
<#list 0..scr_cnt-1 as y>
SWThreshold${y},${total_channels+offset}(visible:1)
</#list>
</#if>

<#assign offset = offset +1>
<#list 0..total_channels as i>
Signal${i},${total_channels+offset}(visible:0)
</#list>
<#list 0..total_channels as i>
Reference${i},${total_channels+offset}(visible:0)
</#list>
<#list 0..total_channels as i>
Delta${i},${total_channels+offset}(visible:1)
</#list>
<#list 0..total_channels as i>
Threshold${i},${total_channels+offset}(visible:1)
</#list>

<#if (scr_cnt > 0)> 
<#list 0..scr_cnt-1 as y>
SWDelta${y},${total_channels+offset}(visible:1)
</#list>
<#list 0..scr_cnt-1 as y>
SWThreshold${y},${total_channels+offset}(visible:1)
</#list>
</#if>

<#assign offset = offset +1>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Signal${i},${total_channels+offset} (Column:0;Row:${i})
Reference${i},${total_channels+offset} (Column:1;Row:${i})
Delta${i},${total_channels+offset} (Column:2;Row:${i})
Compensation${i},${total_channels+offset} (Column:3;Row:${i})
<#if TUNE_MODE_SELECTED != "CAL_AUTO_TUNE_NONE">
CSD${i},${total_channels+offset} (Column:4;Row:${i})
State${i},${total_channels+offset} (Column:5;Row:${i})
Threshold${i},${total_channels+offset} (Column:6;Row:${i})
<#else>
State${i},${total_channels+offset} (Column:4;Row:${i})
Threshold${i},${total_channels+offset} (Column:5;Row:${i})
</#if>
</#list>
<#assign offset = offset +1>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Signal${i},${total_channels+offset} (Column:0;Row:${i})
Reference${i},${total_channels+offset} (Column:1;Row:${i})
Delta${i},${total_channels+offset} (Column:2;Row:${i})
Compensation${i},${total_channels+offset} (Column:3;Row:${i})
<#if TUNE_MODE_SELECTED != "CAL_AUTO_TUNE_NONE">
CSD${i},${total_channels+offset} (Column:4;Row:${i})
State${i},${total_channels+offset} (Column:5;Row:${i})
Threshold${i},${total_channels+offset} (Column:6;Row:${i})
<#else>
State${i},${total_channels+offset} (Column:4;Row:${i})
Threshold${i},${total_channels+offset} (Column:5;Row:${i})
</#if>
</#list>

<#if ENABLE_FREQ_HOP==true>
<#if FREQ_AUTOTUNE>
<#assign offset = offset +1>
CurrentFrequency, ${total_channels+offset} (Column:0;Row:0)
<#list 0..FREQ_HOP_STEPS-1 as i>
HopFrequency${i},${total_channels+offset} (Column:${i+1};Row:0)
</#list>
<#assign offset = offset +1>
CurrentFrequency, ${total_channels+offset} (Column:0;Row:0)
<#list 0..FREQ_HOP_STEPS-1 as i>
HopFrequency${i},${total_channels+offset} (Column:${i+1};Row:0)
</#list>
</#if>
</#if>

<#assign offset = offset +1>
FrameCounter, ${total_channels+offset} (Column:0;Row:0)
QTouchLibError, ${total_channels+offset} (Column:0;Row:1)
<#assign offset = offset +1>
FrameCounter, ${total_channels+offset} (Column:0;Row:0)
QTouchLibError, ${total_channels+offset} (Column:0;Row:1)

</#if>