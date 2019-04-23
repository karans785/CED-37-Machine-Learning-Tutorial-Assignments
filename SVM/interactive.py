import matplotlib.pyplot as plt
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

def calculate(x1,y1,x2,y2):
    return math.sqrt((y2-y1) * (y2-y1)+(x2-x1) * (x2-x1))

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
        plt.plot(x1[i], y1[i], ',', marker = 'x', markersize=10, color='green')
    if len(x2)>0:
        for i in range(0,len(x1)):
            plt.plot(x1[i], y1[i], ',', marker = 'x', markersize=10, color='green')
        for i in range(0,len(x2)):
            plt.plot(x2[i], y2[i], ',', marker = 'x', markersize=10, color='yellow')
    if len(x2) >= point :
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
        
        print("Support Vectors are:")
        for i in range(2):
            print(svx[i],svy[i])
        plt.plot(svx,svy,marker = 'o', markersize=10, color='blue',label= 'Support vectors')
            
        y = (svy[1]+svy[0])/2
        x = (svx[1]+svx[0])/2
        print("the mid point is",x,y)
        
        slope = -1*(1/slope)
        constant = y-slope*x
        point_x = np.linspace(0,10)
        point_y = slope*point_x + constant
        plt.plot(point_x,point_y,'r',label = 'Classifying line')
        print(x1,y1,x2,y2)

        plt.axis([0,10,0,10])
        plt.legend(loc= 'upper left')
#        for i in range(0,len(Xdata)):
#           plt.plot([Xdata[i],Xdata[i]],[Ydata[i],m*(Xdata[i])+c],color='blue', linestyle='dashed')
    fig.canvas.draw()
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.axis([0,10,0,10])
plt.show()

