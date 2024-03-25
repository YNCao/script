import matplotlib.pyplot as plt
import numpy as np

def cycle(x, T):
    if 0<=x%T<=T/2:
        return 0.001
    elif T/2<x%T<3*T/4:
        return x
    else:
        return 0.3
    
plt.style.use('seaborn-v0_8')
# 定义 x 轴和 y 轴数据
T=10
rate=4
x = np.linspace(0,3*T,3*T*rate)
y = np.ones(3*T*rate)
# y = y%T
y[x%T<=T/2]=0.001
y[3*T/4<=x%T]=0.3
y[(x%T>T/2)*(x%T<3*T/4)]=np.tile(np.linspace(0.001,0.3,int(rate*T/4)),3)
# 创建一个 Figure 对象
plt.figure(figsize=(6,4))

# 绘制折线图
plt.plot(x, y, 'k')

# 设置标题
plt.title("Cyclic annealing schedule",fontsize=14)
plt.xticks(range(0,31,5),['0', 'T/2', 'T', '3T/2', '2T', '5T/2', '3T'])

# 设置 x 轴和 y 轴标签
plt.xlabel("Iteration", fontsize=14)
plt.ylabel(r"$\beta$", fontsize=14)
plt.tight_layout()
plt.savefig('./cyclic_annealing.png')
# 显示图形
plt.show()