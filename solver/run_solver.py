from ODE_methods import forward_euler, backward_euler, rk4, adams_bashforth
from utility import record_run_time
import matplotlib.pyplot as plt
import math


def f(t, y):

    return math.cos(t)



@record_run_time
def main():

    # Initial conditions
    y0 = 0.0
    t0 = 0.0
    t_final = 20
    h = 0.1

    t_values, y_values = adams_bashforth(f, y0, t0, t_final, h)

    plt.plot(t_values, y_values)
    plt.show()


if "__name__" == "__main__":

    main()
