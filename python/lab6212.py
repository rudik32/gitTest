#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#создание осей координат со стрелочками
ax = plt.axes()
plt.axis('equal') 
ax.arrow(0,0,8,0,head_width=0.2,head_length=0.2,color='k')
ax.arrow(0,-8,0,16,head_width=0.2,head_length=0.2,color='k')
plt.plot([0,8],[0,0], color='k')
plt.plot([0,0], [-8,8], color='k')
plt.text(8,-0.6,'x',fontsize=14)
plt.text(-0.4,8,'y',fontsize=14)
plt.text(-0.5,-0.3,'0',fontsize=14)
plt.text(7,3.5,'M',fontsize=14)
plt.text(-0.8,1.4,'Lpi',fontsize=12)
x1=[-2.8,-2.1,-1.4,-0.7]
y1= list(range(-8,8,1))
for i in y1:
  for j in x1:
    plt.plot([j,j+0.4],[i,i],'k--')
#1  точка 
#построение пунктиров
plt.plot([3,3,3,3],[0,1,2,3],'k--')
plt.plot([0,1,2,3],[3,3,3,3],'k--')
#построение маркеров
plt.plot([3], [2.7],'k^:')
plt.plot([3], [3.3],'kv:')
plt.plot([2.7], [3],'k>:')
plt.plot([3.3], [3],'k<:')
#окружность
circle1 = plt.Circle((3, 3), 0.7,color='k',fill=False)
ax.add_artist(circle1)
plt.text(4,2,'Lc',fontsize=14)
plt.text(2.9,-0.7,'x01',fontsize=14)
plt.text(-1.3,3,'y01',fontsize=14)
plt.plot(7,3,'k.')

plt.text(2,6.5,'D1',fontsize=14)
ax.arrow(3,3,0.4,0.4,head_width=0.1,head_length=0.1,color='k')
plt.plot([3.4,3.5,3.6,3.7],[3.4,3.5,3.6,3.7],'k')
plt.plot([3.7,3.8,4,4.3],[3.7,3.7,3.7,3.7],'k')
plt.text(3.7,3.8,'Rc',fontsize=14)
#2 точка
#построение пунктиров
plt.plot([5,5,5],[0,-1,-2],'k--')
plt.plot([0,1,2,3,4,5],[-2,-2,-2,-2,-2,-2],'k--')
#построение маркеров
plt.plot([5], [-2.3],'k^:')
plt.plot([5], [-1.7],'kv:')
plt.plot([4.7], [-2],'k>:')
plt.plot([5.3], [-2],'k<:')
#окружность
circle1 = plt.Circle((5, -2), 0.7,color='k',fill=False)
ax.add_artist(circle1)
plt.text(6,-3,'Lc',fontsize=14)
plt.text(4.8,0.3,'x02',fontsize=14)
plt.text(-1.3,-1.8,'y02',fontsize=14)
plt.plot(7,3,'k.')

plt.text(1,-1,'D2',fontsize=14)
ax.arrow(5,-2,0.4,0.4,head_width=0.1,head_length=0.1,color='k')
plt.plot([5.5,5.6,5.7,5.8],[-1.5,-1.4,-1.3,-1.2],'k')
plt.plot([5.8,5.9,6,6.1],[-1.2,-1.2,-1.2,-1.2],'k')
plt.text(5.8,-1,'Rc',fontsize=14)









plt.show()