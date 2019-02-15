#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time

x0=0
y0=1
x=np.linspace(-2,2,4000)
y=np.linspace(0,4,4000)
X_,Y_=np.meshgrid(x,y)

phi=0.5*np.log((X_-x0)**2+(Y_-y0)**2)+0.5*np.log((X_-x0)**2+(Y_+y0)**2)
time_start=time.clock()
#phi=np.log(((x-x0)**2+(y-y0)**2)**0.5)
C1=0.5*np.log((1.3-x0)**2+(2.3-y0)**2)+0.5*np.log((1.3-x0)**2+(2.3+y0)**2)
C2=0.5*np.log((1.4-x0)**2+(2.4-y0)**2)+0.5*np.log((1.4-x0)**2+(2.4+y0)**2)
C3=0.5*np.log((1.5-x0)**2+(2.5-y0)**2)+0.5*np.log((1.5-x0)**2+(2.5+y0)**2)
C4=0.5*np.log((1.6-x0)**2+(2.6-y0)**2)+0.5*np.log((1.6-x0)**2+(2.6+y0)**2)
print time.clock()-time_start
for i in [C1,C2,C3,C4]:
    q=np.abs(phi-i)<0.003
    X1=X_[q]
    Y1=Y_[q]
    plt.plot(X1,Y1,',')
#print time.clock()-time_start
plt.show()

