# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:42:27 2020

@author: hzsdl
"""
# In[]
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]="SimHei"
plt.rcParams["axes.unicode_minus"]=False

# In[]
huabu=plt.figure(figsize=(8,6))
ax1=huabu.add_subplot(1,1,1)
x=np.arange(3)
y=[1000,5000,3000]
ax1.set_xticks(np.arange(3))

display_xticks=0
if display_xticks:
    ax1.set_xticklabels(labels=["第一季度","第二季度","第三季度"])
else:
    ax1.tick_params(bottom=False)#图表下轴（x)轴刻度线不显示
    ax1.set_xticklabels(labels=["","",""])
ax1.set_yticks(np.arange(0,10000,1000))


ax1.plot(x,y,label="折线图")
yangshi={"color":"#FFE1FF",
         "edgecolor":"#FFD39B",
         "linewidth":3
         }
ax1.bar(x,y,width=0.5,label="柱形图",**yangshi)

#数据标签
zt_yangshi={"fontsize":"large",
            "color":"red"}
for x_tmp,y_tmp in zip(x,y):
    plt.text(x_tmp,y_tmp+100,y_tmp,ha="center",va="bottom",**zt_yangshi)
    
#图表标签
offset=0.3
plt.annotate("最大成交量",(1,5000),xytext=(1+offset,5000),
             arrowprops=dict(facecolor="red",arrowstyle="<-",linewidth=3))

#数据表
plt.table(cellText=[y],rowLabels=["销量"],colLabels=["第一季度","第二季度","第三季度"])
plt.legend()
huabu
