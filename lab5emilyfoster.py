

from numpy import *
import matplotlib.pyplot as p
import scipy.integrate as si

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
p.xlabel('x')
p.ylabel('y(x)')

# graph title
p.title('a = 0.0 (black), 0.25 (red), 0.50 (blue), 0.75 (green), 1.0 (cyan)')

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

def analytic(xmin, xmax, a):
    result = ((e ** -(a * xmax)) / (1 + (a ** 2))) * (sin(xmax) - (a * cos(xmax))) - ((e ** -(a * xmin)) / (1 + (a ** 2))) * (sin(xmin) - (a * cos(xmin)))
    return result

print("a - value: 0.0")
print("My integral: ", integrate_(x, y0))
print("SciPy's: ", si.simps(y0, x))
print("Analytic: ", analytic(0, 4 * pi, 0.0), "\n")

print("a - value: 0.25")
print("My integral: ", integrate_(x, y1))
print("SciPy's: ", si.simps(y1, x))
print("Analytic: ", analytic(0, 4 * pi, 0.25, "\n"))

print("a - value: 0.5")
print("My integral: ", integrate_(x, y2))
print("SciPy's: ", si.simps(y2, x))
print("Analytic: ", analytic(0, 4 * pi, 0.5), "\n")

print("a - value: 0.75")
print("My integral: ", integrate_(x, y3))
print("SciPy's: ", si.simps(y3, x))
print("Analytic: ", analytic(0, 4 * pi, 0.75), "\n")

print("a - value: 1.0")
print("My integral: ", integrate_(x, y4))
print("SciPy's: ", si.simps(y4, x))
print("Analytic: ", analytic(0, 4 * pi, 1.0), "\n")











