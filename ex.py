import numpy as np
from matplotlib import pyplot as plt 
n=np.arange(1,500)
F=250;
FS=10000;
s=0.5*np.cos(2*np.pi*F/FS*n+np.pi/2);
plt.plot(n,s);
plt.show()


