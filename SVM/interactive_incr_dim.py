import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
x1= []
y1  = []
x2=[]
y2=[]
points= int(input(print("Enter the number of points for each class : ")))
point=points

def calculate(x1,y1,z1,x2,y2,z2):
    return math.sqrt((y2-y1) * (y2-y1)+(x2-x1) * (x2-x1)+ (z2-z1)*(z2-z1))

def onclick(event):
    global points
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    plt.cla()    
    if points>0 :  
        x1.append(event.xdata)
        y1.append(event.ydata)
        points = points-1
    else:
        x2.append(event.xdata)
        y2.append(event.ydata)
    print(event.xdata,event.ydata)
    plt.axis([0,10,0,10])
    for i in range(0,len(x1)):
        plt.plot(x1[i], y1[i],',', marker = 'x', markersize=10, color='green')
    if len(x2)>0:
        for i in range(0,len(x1)):
            plt.plot(x1[i], y1[i], ',', marker = 'x',markersize=10, color='green')
        for i in range(0,len(x2)):
            plt.plot(x2[i], y2[i], ',', marker = 'x',markersize=10, color='yellow')
    if len(x2) == point :
        z1=[]
        z2=[]
        for i in range(len(x1)):
            z1.append(x1[i]*x1[i] + y1[i]*y1[i])
        for i in range(len(x2)):
            z2.append(x2[i]*x2[i] + y2[i]*y2[i])
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x1, y1, z1, zdir='z')
        ax.scatter(x2,y2,z2,zdir='z')
        min_dist = 10000
        svx = []
        svy = []
        svz = []
        for i in range(len(x1)):
            for j in range(len(x2)):
                dist = calculate(x1[i],y1[i],z1[i],x2[j],y2[j],z2[j])
                if dist<min_dist:
                    min_dist = dist
                    min_i = i
                    min_j = j
        i = min_i
        j = min_j
        svx.append(x1[i])
        svx.append(x2[j])
        
        svy.append(y1[i])
        svy.append(y2[j])
        
        svz.append(z1[i])
        svz.append(z2[j])
        
        ax.plot(svx,svy,svz,'blue')
        slope = (svx[0]-svx[1])/(svy[0]-svy[1])
        xmid,ymid,zmid = svx[0]+svx[1]/2,svy[0]+svy[1]/2,svz[0]+svz[1]/2
        #ax.plot_surface()
        fig.canvas.mpl_disconnect(cid)
    fig.canvas.draw()
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.axis([0,10,0,10])
plt.show()

