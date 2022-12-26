import matplotlib.pyplot as plt #匯入Pyplot 套件並命名為plt
import numpy as np #as fun name 
#from sklearn.metrics import r2_score
 

num=[]
n=[]
x=[]
y=[]
n1=[]
n2=[]
path = 'oddExperiment.txt'
f = open(path, 'r')
d=f.read().splitlines()#no read \n
for i in range(len(d)):
	if i!=0:#no xy
		num.append(d[i])
for i in range(len(num)):#no blank
	s=num[i].split()
	for j in range(2):
		n.append(s[j])

for i in range(0,len(n),2):
	y.append(float(n[i]))
for i in range(1,len(n),2):
	x.append(int(n[i]))
f.close()

fig = plt.figure()

plt.scatter(x, y,label='data') # 繪製散點圖
p1o=np.polyfit(x,y,1)
p2o=np.polyfit(x,y,2)
p1=np.poly1d(p1o)
p2=np.poly1d(p2o)
s2=np.subtract(y,p1(x))

MSE = str(round(np.square(s2).mean(),5))
s3=np.subtract(y,p2(x))
MSE2 = str(round(np.square(s3).mean(),5))
av=sum(y)/len(y)
k=[]
k2=[]
k3=[]
for i in range(len(y)):
	k.append((p1(x)[i]-y[i])**2)
	k2.append((av-y[i])**2)
for i in range(len(y)):
	k3.append((p2(x)[i]-y[i])**2)
r2_1=str(round(1-(sum(k)/sum(k2)),5))
r2_2=str(round(1-(sum(k3)/sum(k2)),5))

plt.plot(x,p1(x),color='#ffff00',label='degree 1 LSE fit='+MSE)
plt.plot(x,p2(x),color='g',label='degree 2 LSE fit='+MSE2)
plt.plot(x,p1(x),color='r',label='degree r1 fit='+r2_1)
plt.plot(x,p2(x),color='#800080',label='degree r2 fit='+r2_2)
plt.title('oddExperimentData')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
fig.set_size_inches(6, 6)
fig.savefig('lab13_plus.png')
plt.show()


