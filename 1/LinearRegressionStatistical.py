import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y = x**2
fig = plt.subplots()
ax = fig.add_subplot(111)
ax.plot(x,y)
x = []
y = []
p = np.linspace(-5.,5.)

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print(ix,iy)
    x.append(ix)
    y.append(iy)
    num=den=0
    if(len(x)>=2):
        for i in range(len(x)):
            num = num+(ix-np.average(x))*iy-np.average(y)*iy-np.average(y)
            den = den+(ix-np.average(x))
            
        m = num/den
        c = np.average(y) - m*np.average(x)
        fig = plt.subplots()
        plt.plot(p,m*p+c)
    plt.scatter(ix, iy, s=10)
    
cid = fig.canvas.mpl_connect('button_release_event', onclick)

"""import matplotlib.pyplot as plt
%matplotlib
import numpy as np

x = np.array([])
y = np.array([])
m=0
c=0
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 20])
ax.set_ylim([0, 20])
plt.show()
def onclick(event):
    
    global x,y,f,m,c
    x = np.append(x,event.xdata)
    y = np.append(y,event.ydata)
    ax.plot(event.xdata, event.ydata, 'ro')
    fig.canvas.draw()
    if(len(x)>=2):
        if(len(x)>2):
            f.remove()
        sumx=np.sum(x)
        sumy=np.sum(y)
        sumx=sumx/len(x)
        sumy=sumy/len(y)
        num=0
        den=0
        for i in range(len(x)):
            num=num+(x[i]-sumx)*(y[i]-sumy)
            den=den+(x[i]-sumx)*(x[i]-sumx)
        m=num/den
        c=sumy-m*sumx
        x_v= np.array(ax.get_xlim())
        y_v= c + m*x_v
        f,=ax.plot( x_v, y_v, linestyle='solid')
        fig.canvas.draw()
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)

def onkey(event):
    global x,y,m,c
    for i in range(len(x)):
        ax.plot([x[i],x[i]],[y[i],m*x[i]+c])
        fig.canvas.draw()
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.set_xlim([0, 20])
    ax1.set_ylim([-15, 20])
    for i in range(len(x)):
        ydiff=y[i]-m*x[i]-c
        ax1.plot( x[i], ydiff, 'ro')

cid1= fig.canvas.mpl_connect('key_press_event',onkey)"""