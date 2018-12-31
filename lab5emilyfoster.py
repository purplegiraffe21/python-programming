from numpy import *
import matplotlib.pyplot as p 

# functions to plot
x = linspace(0.0, (4 * pi), 100)
a = linspace(0.0, 1, 5)
y0 = (e ** (-a[0] * x)) * (cos(x))
y1 = (e ** (-a[1] * x)) * (cos(x))
y2 = (e ** (-a[2] * x)) * (cos(x))
y3 = (e ** (-a[3] * x)) * (cos(x))
y4 = (e ** (-a[4] * x)) * (cos(x))

# plot functions
p.plot (x, y0, 'o')
p.plot (x, y1, 'o')
p.plot (x, y2, 'o')
p.plot (x, y3, 'o')
p.plot (x, y4, 'o')

# label axis
p.xlabel('x - variable')
p.ylabel('y - variable')

# graph title
p.title('function plot')

# set axis range
p.axis ([0.0, 4 * pi, -1.3, 1.3])

# turn grid on
p.grid (True)
p.show()

# integration approximation
def integrate_(x,y):
    N = len(x) # accumaltion stops at final term
    acc = 0 # intialise the accumulation value
    # i - 1 can't be less than 0, no term in array is the '-1' th term
    for i in range(1, N): 
        acc += y[i] * (x[i] - x[i - 1]) 
    return acc


import scipy as s

print(s.integrate.simps(y0, x))
print(s.integrate.simps(y1, x))
print(s.integrate.simps(y2, x))
print(s.integrate.simps(y3, x))
print(s.integrate.simps(y4, x)) 

















