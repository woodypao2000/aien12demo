from matplotlib import pyplot as plt
import matplotlib
font={'family':'MicroSoft Yahei',
      'weight':'bold'}
matplotlib.rc('font',**font)
a=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x= range(1,32)
x1=range(51,82)
plt.figure(figsize=(20,8))
plt.scatter(x,a,label="3月氣溫")
plt.scatter(x1,b,label="10月氣溫")
plt.legend()
xticks0=[f'3月{i}日' for i in x]+[f'10月{i}日' for i in x]
plt.xticks((list(x)+list(x1))[::3],xticks0[::3],rotation=45)
plt.xlabel("時間")
plt.ylabel("溫度 單位C",rotation=360,fontsize=18)
plt.title("3月10月每日氣溫",fontsize=18)