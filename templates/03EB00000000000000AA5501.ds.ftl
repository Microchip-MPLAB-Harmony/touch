B,1,1,FrameCounter
<#if (TOUCH_CHAN_ENABLE_CNT > 0)>
<#assign x= TOUCH_CHAN_ENABLE_CNT-1>
</#if>

<#list 0..x as i>
D,${2},${i+1},Signal${i}
D,${3},${i+1},Reference${i}
-D,${4},${i+1},Delta${i}
D,${5},${i+1},Compensation${i},F,(variable & 0x0F)*0.00675+((variable >> 4) & 0x0F)*0.0675+((variable >> 8) & 0x0F)*0.675+((variable >> 12) & 0x3) * 6.75
<#if TUNE_MODE_SELECTED != "CAL_AUTO_TUNE_NONE">
B,${6},${i+1},CSD${i}
</#if>
B,${7},${i+1},State${i}
B,${8},${i+1},Threshold${i}

</#list>

<#if FREQ_AUTOTUNE>
B,${9},${1},CurrentFrequency
<#list 0..FREQ_HOP_STEPS-1 as j>
B,${10+j},${1},HopFrequency${j}
</#list>
</#if>

B,1,3,QTouchLibError

B,1,2,FRAME_END
