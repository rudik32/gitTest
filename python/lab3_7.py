#!/usr/bin/python
# -*- coding: utf-8 -*-
from sympy import *
#7
x = Symbol('x')
y = Symbol('y')
q1,q2 = symbols('q1 q2')
x01,y01,x02,y02=symbols('x01 y01 x02 y02')
fi = (q1/(2*pi))*log(1/((sqrt((x-x01)**2+(y-y01)**2))*sqrt((x+x01)**2+(y-y01)**2))) + (q2/(2*pi))*log(1/((sqrt((x-x02)**2+(y-y02)**2))*sqrt((x+x02)**2+(y-y02)**2)))
print("Исходная формула")
pprint(fi)

fiy0=fi
fiy0 = fiy0.subs(y,0)
print("При y=0")

pprint(fiy0)
dif1=diff(fi,x)
dif2=dif1.subs(y,0)
print("Частная производная по х при y=0")

pprint(dif2)
dif3=dif1.subs(x,0)
print("Частная производная по х при x=0")
pprint(dif3)


dif3=diff(fi,y)
dif3=dif3.subs(y,0)
print("Частная производная по y при y=0")

pprint(dif3)

#14



