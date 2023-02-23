import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.sqrt(5), np.sqrt(5), 10000)
y = np.sqrt(5-x**2)
x2 = np.linspace(-np.sqrt(5), np.sqrt(5), 10000)
y2 = -np.sqrt(5-x**2)
t=np.linspace(-np.sqrt(5), np.sqrt(5), 10000)
l=np.sqrt(2)-np.sqrt(1.5)*(t-np.sqrt(3))
plt.plot(x, y, label='f(x)',color='blue')
plt.plot(x2, y2,color='blue')
plt.plot(t, l, label='f(x)')

plt.legend()
plt.show()
