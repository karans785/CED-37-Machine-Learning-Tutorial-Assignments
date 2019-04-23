import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
x1 =[]
y1 =[]
x2 =[]
y2 =[]
points= int(input(print("Enter the number of points for each class : ")))

def calculate(x1,y1,x2,y2):
    return math.sqrt((y2-y1) * (y2-y1)+(x2-x1) * (x2-x1))
ax.plot([1,2,3],[1,2,3])
def SVM(x1,y1,x2,y2):
    global ax
    min_dist = 10000
    svx = []
    svy = []
    for i in range(len(x1)):
        for j in range(len(x2)):
            dist = calculate(x1[i],y1[i],x2[j],y2[j])
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
    slope = (svy[1]-svy[0]/svx[1]-svx[0])
    constant = svy[0]-slope*svx[0]
    point_x = np.linspace(svx[0],svx[1])
    point_y = slope*point_x + constant
    ax.plot(point_x,point_y,'g')

    print("Critical points are:")
    for i in range(2):
        print(svx[i],svy[i])
    
    y = (svy[1]+svy[0])/2
    x = (svx[1]+svx[0])/2
    print("the mid point is",x,y)
    
    slope = -1*(1/slope)
    constant = y-slope*x
    point_x = np.linspace(0,10)
    point_y = slope*point_x + constant
    ax.plot(point_x,point_y,'r')
    print(x1,y1,x2,y2)
    ax.scatter(x1,y1)
    ax.scatter(x2,y2)
    return

def onclick(event):
    global x1,y1,x2,y2,points
    if points>0 :  
        x1.append(event.xdata)
        y1.append(event.ydata)
        points = points-1
    else:
        x2.append(event.xdata)
        y2.append(event.ydata)
    print(event.xdata,event.ydata)
    ax.scatter(event.xdata,event.ydata)
def on_key(event):
    global x1,y1,x2,y2,ax
    ax.scatter(x1,y1)
    ax.scatter(x2,y2)
    SVM(x1,y1,x2,y2)
    fig.canvas.mpl_disconnect(cid1)
    fig.canvas.mpl_disconnect(cid2)

    

cid1 = fig.canvas.mpl_connect('button_press_event', onclick)
cid2 = fig.canvas.mpl_connect('key_press_event', on_key)