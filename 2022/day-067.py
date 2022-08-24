import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
fig = plt.figure(figsize=(8, 8))
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")
x=np.linspace(-10,10,100)
y=x**2+3
plt.xlim(-12,12)
plt.ylim(-10, 100)
plt.plot(x,y)
plt.show()


#引入axisartist工具
import mpl_toolkits.axisartist as axisartist
#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建绘图区对象ax
ax=axisartist.Subplot(fig,111)  
#把绘图区对象添加至画布
fig.add_axes(ax)
#使用set_visible方法隐藏绘图区原有所有坐标轴
ax.axis[:].set_visible(False)
#使用ax.new_floating_axis添加新坐标轴
ax.axis["x"] = ax.new_floating_axis(0,0)
#给x轴添加箭头
ax.axis["x"].set_axisline_style("->", size = 1.0)
#给y轴添加箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#设置刻度显示方向，x轴为下方显示，y轴为右侧显示
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")
#x轴范围为-10～10，且分割为100份
x=np.linspace(-10,10,100)
#生成一元函数y值
y=x**2+3
#设置x、y轴范围
plt.xlim(-12,12)
plt.ylim(-10, 100)
#绘制显示图形
plt.plot(x,y)
plt.show()



