#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x,y,x0,y0,lyamb = symbols('x y x0 y0 lyamb')

phi = (1/(2*pi))*(log(((x-x0)**2+(y+y0)**2)**0.5/((x-x0)**2+(y-y0)**2)**0.5)+lyamb*log(((x+x0)**2+(y+y0)**2)**0.5/((x+x0)**2+(y-y0)**2)**0.5))

vx = diff(phi,x)
vy = diff(phi,y)
x01=1
y01=1
x1=np.linspace(0,2,25)
y1=np.linspace(0,2,25)
lyamb1=-1
pprint(phi)
X,Y=np.meshgrid(x1,y1)
Vx=lambdify((x,y,lyamb,x0,y0),vx,modules='numpy')(X,Y,lyamb1,x01,y01)
Vy=lambdify((x,y,lyamb,x0,y0),vy,modules='numpy')(X,Y,lyamb1,x01,y01)
plt.quiver(X,Y,Vx,Vy)
plt.show()



