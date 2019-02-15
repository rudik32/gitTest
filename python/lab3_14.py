#!/usr/bin/python
# -*- coding: utf-8 -*-
from sympy import *
q,k1,k2,x,y,x0,y0= symbols('q k1 k2 x y x0 y0')

l=(k1-k2)/(k1+k2)

fi1 = (q/(2*pi*k1))*(log((1)/(sqrt((x-x0)**2+(y-y0)**2)))+l*log(1/(sqrt((x-x0)**2+(y+y0)**2))))
pprint(fi1)
print("***************************************************")
fi2=(1-l)*(q/(2*pi*k2))*log(1/(sqrt((x-x0)**2+(y-y0)**2)))
pprint(fi2)

fi1_M=fi1.subs(y,0)
fi2_M=fi2.subs(y,0)
print("amfklsdhghdjkgh")
pprint(fi1_M)
pprint(fi2_M)
print("производные")
dif1=k1*diff(fi1,y)
dif1=dif1.subs(y,0)
dif2=k2*diff(fi2,y)
dif2=dif2.subs(y,0)

pprint(dif1)
pprint(dif2)
