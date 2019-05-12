import matplotlib.pyplot as plt
import numpy as np

## parameters
thetamax1 = 0.5
thetamax2 = 0.2
L1 = 1.0
L2 = 2.0
g = 9.81

T1 = 2.0*np.pi*((L1/g)**(0.5))
t = np.linspace(0, 10.0*T1, 100)

theta1 = list()
for ti in t:
    theta1.append(thetamax1*np.sin(((g/L1)**(0.5))*ti))

x1 = L1*np.sin(theta1)
y1 = L1 - L1*np.cos(theta1)

x2 = list()
y2 = list()
for i in range(0, len(x1)):
    theta2 = thetamax2*np.sin(((g/L2)**(0.5))*t[i])
    x2.append(x1[i] + L2*np.sin(theta2))
    y2.append(y1[i] - L2*np.cos(theta2))
    i = i + 1

for j in range(0, len(x1)):
    plt.plot(np.linspace(0, x1[j], 10), np.linspace(L1, y1[j], 10))
    plt.plot(np.linspace(x1[j], x2[j], 10), np.linspace(y1[j], y2[j], 10))

plt.plot(x1, y1, 'r')
plt.plot(x2, y2, 'b')
plt.show()
