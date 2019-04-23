# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:23:32 2019

@author: KARAN
"""
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(111)

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    figi = plt.figure()
    ax = figi.add_subplot(112)

    ax.scatter(event.x, event.y)
cid = fig.canvas.mpl_connect('button_press_event', onclick)