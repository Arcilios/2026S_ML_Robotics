import numpy as np
import matplotlib.pyplot as plt

#7
#(a)
y = np.array([1, 0, 0, 0, 1, 0, 1, 1, 0, 1])
X = y.mean()

plt.hist(y,bins=4, range = (-0.5,1.5),edgecolor='black')
plt.xlabel('y')
plt.ylabel('Count')
plt.title('Histogram of y')
plt.show()

ynew = np.array([0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0,
0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0,
0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,
0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1,
0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,
1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1,
1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1,
1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1])

ynew = np.concatenate((y, ynew))
Xnew = ynew.mean()
plt.hist(ynew,bins=4, range = (-0.5,1.5),edgecolor='black')
plt.xlabel('ynew')
plt.ylabel('Count')
plt.title('Histogram of ynew')
plt.show()