import matplotlib
from pylab import *

def show_plot():
    x = arange(50)*2*pi/50
    y = sin(x)
    #plot(y)
    #http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
    plot(x,sin(y),'y-^')
    xlabel('x-axis label')
    ylabel('some value')
    show()

def show_scatter():
    x = rand(200)
    y = rand(200)
    size = rand(200)*50
    color = rand(200)
    scatter(x,y, size, color)
    ## mandates x & y to be same size
    colorbar()
    show()

def bar_plot():
    x = arange(50)*2*pi/50
    bar(x,sin(x),width=x[1]-x[0])
    show()


def hist_plot():
    hist(randn(2000))
    show()

def multi_plot():
    t1=arange(0.0,5.0,0.1)
    t2=arange(0.0,5.0,0.02)
    t3 = arange(0.0,2.0,0.01)

    subplot(211)
    I = plot(t1,f(t1),'rs',t2,f(t2),'k--')
    setp(I,'markerfacecolor','r')
    grid(True)
    title('Sample of two subplots')
    ylabel('y')

    subplot(212)
    plot(t3,cos(2*pi*t3),'g.')
    grid(True)
    xlabel('x')
    ylabel('y')
    show()

def f(t):
    s1=cos(2*pi*t)
    e1=exp(-t)
    return multiply(s1,e1)


show_plot()
#show_scatter()
#bar_plot()
#hist_plot()
# multi_plot()


