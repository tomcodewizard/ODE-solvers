from ODE_methods import forward_euler
import matplotlib.pyplot as plt
import math, time

def f(t, y):

    return math.sin(t)


# Initial conditions
y0 = 1.0
t0 = 0.0
tn = 2.0
h = 0.1

t_values, y_values = forward_euler(f, y0, t0, tn, h)

plt.plot(t_values, y_values)
plt.show()