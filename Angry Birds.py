# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from math import sin,cos,radians
import matplotlib.pyplot as plt

# The Pig's location
p = np.random.random(2)
p*= 50
p+= 25

plt.plot(p[0],p[1],'.')
plt.show()

while True:
    Response = input("Play Angry Birds ? (Yes/No):")
    if Response == "No":
        break
    g = 9.8
    z = radians(float(input("Initial Angle:")))
    Vo = float(input("Initial Velocity:"))
    Vx = Vo*cos(z)
    Vy = Vo*sin(z)
    t = 2*Vy/g
    
    mt = np.linspace(0,t,1000)
    mx = mt*Vx
    my = mt*Vy - 0.5*g*(mt**2)
    plt.plot(p[0],p[1],'.')
    plt.plot(mx,my)
    plt.show()
    
    mdis = np.sqrt((mx-p[0])**2+(my-p[1])**2)
    if min(mdis)< 2:
        print("Win")
        break
    else:
        print("Fail")
        print(min(mdis))
    





