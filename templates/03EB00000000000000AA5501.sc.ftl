<#assign total_channels = TOUCH_CHAN_ENABLE_CNT-1>

<#assign offset = 0>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
State${i}, ${offset} (Column:0;Row:${i})
Delta${i}, ${offset} (Column:1;Row:${i})
Threshold${i}, ${offset} (Column:2;Row:${i})
</#list>

<#assign offset = offset +1>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
State${i}, ${i+offset}
</#list>

<#assign offset = offset +1>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Signal${i},${total_channels+offset}(visible:0)
</#list>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Reference${i},${total_channels+offset}(visible:0)
</#list>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Delta${i},${total_channels+offset}(visible:1)
</#list>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Threshold${i},${total_channels+offset}(visible:1)
</#list>

<#assign offset = offset +1>
<#list 0..TOUCH_CHAN_ENABLE_CNT-1 as i>
Signal${i},${total_channels+offset} (Column:0;Row:${i})
Reference${i},${total_channels+offset} (Column:1;Row:${i})
Delta${i},${total_channels+offset} (Column:2;Row:${i})
Compensation${i},${total_channels+offset} (Column:3;Row:${i})
<#if TUNE_MODE>
CSD${i},${total_channels+offset} (Column:4;Row:${i})
State${i},${total_channels+offset} (Column:5;Row:${i})
Threshold${i},${total_channels+offset} (Column:6;Row:${i})
<#else>
State${i},${total_channels+offset} (Column:4;Row:${i})
Threshold${i},${total_channels+offset} (Column:5;Row:${i})
</#if>
</#list>

<#if FREQ_AUTOTUNE>
<#assign offset = offset +1>
CurrentFrequency, ${total_channels+offset} (Column:0;Row:0)
<#list 0..FREQ_HOP_STEPS-1 as i>
HopFrequency${i},${total_channels+offset} (Column:${i+1};Row:0)
</#list>
</#if>

<#assign offset = offset +1>
FrameCounter, ${total_channels+offset} (Column:0;Row:0)
QTouchLibError, ${total_channels+offset} (Column:0;Row:1)

