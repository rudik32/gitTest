#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import scipy.special

x,y,m,x0,y0 = symbols('x y m x0 y0')

phi=0.5/pi*cosh(m*y0)/cosh(m*y) *( besselk(0,m*sqrt((x-x0)**2+(y-y0)**2)) - besselk(0,m*sqrt((x+x0)**2+(y-y0)**2)) )

vx = diff(phi,x)
vy = diff(phi,y)
x01=0.5
y01=0.5
x1=np.linspace(0,2,25)
y1=np.linspace(0,2,25)
m1=0.5
pprint(phi)


X,Y=np.meshgrid(x1,y1)

mydic = {"besselk": scipy.special.kn}

Vx=lambdify((x,y,m,x0,y0),vx,(mydic, "numpy"))(X,Y,m1,x01,y01)

Vy=lambdify((x,y,m,x0,y0),vy,(mydic, "numpy"))(X,Y,m1,x01,y01)
#print(Vy)
plt.quiver(X,Y,Vx,Vy)
plt.show()



