import numpy as np
import matplotlib.pyplot as p
import scipy.integrate as si

# functions to plot
x = np.linspace(0.0, (4 * np.pi), 100)
a = np.linspace(0.0, 1, 5)
y0 = (np.e ** (-a[0] * x)) * (np.cos(x))
y1 = (np.e ** (-a[1] * x)) * (np.cos(x))
y2 = (np.e ** (-a[2] * x)) * (np.cos(x))
y3 = (np.e ** (-a[3] * x)) * (np.cos(x))
y4 = (np.e ** (-a[4] * x)) * (np.cos(x))

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
p.axis ([0.0, 4 * np.pi, -1.3, 1.3])

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

print(si.simps(y0, x))
print(si.simps(y1, x))
print(si.simps(y2, x))
print(si.simps(y3, x))
print(si.simps(y4, x)) 

















