import numpy as np
import matplotlib.pyplot as plt
import sys
sys.stdout=open("karan.txt","w")


#x=[4,4,7,7,8,9]
#y=[2,10,4,22,16,10]

x=[1,2,3,4,5]
y=[1,2,3,4,5]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 50])
ax.set_ylim([0, 50])
plt.show()

#plt.plot(x, y, 'ro') 
#for a,b in zip(x, y):
 #   plt.text(a, b, '({}, {})'.format(a, b))

m=0
b=0
def LinearRegression(x,y):
    global m
    global b
    Xvals = np.linspace(0,50)
    plt.plot(Xvals,m*Xvals+b)
    plt.ylim(0,50)
    
    n=len(x) 
    for i in range(n):
        error = y[i]-(m*x[i]+b)
        m = m + (0.09*error*x[i])
        b = b + 0.09*error
        if 1 :        
            plt.pause(0.4)
            plt.cla()
            plt.plot(Xvals,m*Xvals+b)
            plt.plot(x, y, 'ro') 
            plt.ylim(0,50) 
            plt.xlim(0,50)
            print(m,b) 

def onclick(event):
    global x,y
    x.append(event.xdata)
    y.append(event.ydata)
    ax.plot(event.xdata, event.ydata, 'ro')
    fig.canvas.draw()
    LinearRegression(x,y)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
        
#icnlude
   