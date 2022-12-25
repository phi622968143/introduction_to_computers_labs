import matplotlib.pyplot as plt #匯入Pyplot 套件並命名為plt
import numpy as np #as fun name 

weather=[[17.5, 20.4, 22.5, 23.9, 27.3, 29.5, 29.4, 28.9, 28.6, 25.7, 22.8, 18.0],
 [17.6, 18.4, 21.3, 25.0, 27.2, 29.0, 30.4, 29.0, 29.5, 26.4, 23.9, 17.9],
 [17.8, 18.9, 21.8, 24.9, 27.7, 30.4, 29.1, 28.4, 28.4, 26.8, 25.1, 20.5],
 [17.3, 17.4, 19.7, 26.3, 28.4, 29.4, 29.9, 29.3, 28.0, 27.8, 24.3, 20.9],
 [19.4, 18.6, 21.5, 24.6, 27.7, 29.3, 29.6, 29.9, 30.0, 27.1, 23.8, 19.1],
 [18.1, 17.5, 22.3, 25.6, 28.9, 29.0, 29.2, 27.8, 28.9, 25.8, 24.2, 21.6],
 [19.7, 22.0, 22.5, 26.0, 26.9, 29.3, 29.2, 28.7, 28.4, 27.1, 23.5, 19.8],
 [19.0, 20.0, 23.3, 23.4, 28.1, 30.1, 30.2, 28.8, 29.3, 26.8, 24.2, 20.1],
 [16.5, 19.7, 22.4, 24.6, 29.0, 28.3, 29.1, 28.4, 29.5, 27.3, 23.2, 19.3]]
years = np.array(range(2013,2022))
years = np.arange(2013,2022)
years=list(map(str,years))
month=[1,2,3,4,5,6,7,8,9,10,11,12]
s=[]
av=[]

#first pb
fig = plt.figure()
for i in range(9):
	plt.plot(month,weather[i], label=years[i])
plt.title('tainan monthly aver T')
plt.xlabel('month')
plt.ylabel('T in °C')
plt.xticks(range(1,13,1))
plt.legend()
fig.set_size_inches(4.5, 4.5)
#plt.show()
fig.savefig('lab13_01.png')

#sec pb
fig = plt.figure()
for i in range(12):
	av.append((weather[0][i]+weather[1][i]+weather[2][i]+weather[3][i]+weather[4][i]+weather[5][i]+weather[6][i]+weather[7][i]+weather[8][i])/9)
a=list(map(str,[("%.2f" % i) for i in av])) 
plt.plot(month,av,'-o',markerfacecolor='r')
plt.title('Tainan average monthly T 2013~21')
plt.xlabel('month')
plt.ylabel('T in °C')
plt.xticks(range(1,13,1))
plt.yticks(range(16,34,2))
plt.axhline(y=sum(av)/12, xmin=0, xmax=13,linestyle='--', color='r',label='average of all')
plt.text(x=2,y=sum(av)/12,s=str(round(sum(av)/12,2)),horizontalalignment='right' ,fontsize=10)
for i in range(12):#asssign the position and content of each txt 
    plt.text(x = month[i], y =av[i], s=a[i], fontsize=10)
plt.legend()
plt.tight_layout() #讓子圖之間適當排列不重疊
#plt.show()
fig.set_size_inches(5, 5)
fig.savefig('lab13_02.png')

#pb3
fig = plt.figure(figsize=(15,6))
fig.add_subplot(1, 2, 1)

plt.subplot(1,2,1)
for i in range(9):
	plt.plot(month,weather[i], label=years[i])
plt.title('tainan monthly aver T')
plt.xlabel('month')
plt.ylabel('T in °C')
plt.xticks(range(1,13,1))
plt.legend()

plt.subplot(1,2,2)
plt.plot(month,av,'-o',markerfacecolor='r')
plt.title('Tainan average monthly T 2013~21')
plt.xlabel('month')
plt.ylabel('T in °C')
plt.xticks(range(1,13,1))
plt.yticks(range(16,34,2))
plt.axhline(y=sum(av)/12, xmin=0, xmax=13,linestyle='--', color='r',label='average of all')
plt.text(x=2,y=sum(av)/12,s=str(round(sum(av)/12,2)),horizontalalignment='right' ,fontsize=10)
for i in range(12):#asssign the position and content of each txt 
    plt.text(x = month[i], y =av[i], s=a[i], fontsize=10)
plt.legend()

plt.tight_layout() #讓子圖之間適當排列不重疊
plt.show()

fig.savefig('lab13_03.png')

