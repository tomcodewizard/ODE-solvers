from ODE_methods import forward_euler, backward_euler, midpoint_method, heuns_method, runge_kutta4, adams_bashforth, adams_moulton
from utility import record_runtime
import matplotlib.pyplot as plt
import numpy as np

def SIR_equations(t, y, beta, gamma):
    """The equations of the SIR system

    Args:
        t (array): array of time values
        y (array): array of y values
        beta (float): transmission rate
        gamma (float): recovery rate

    Returns:
        array: Right hand side of derivative equations
    """

    S, I, R = y
    N = S + I + R

    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I

    return [dSdt, dIdt, dRdt]

@record_runtime
def run_ODE_solver(method, eqns, y0, t0, t_final, h, beta, gamma):
    """Function to run the solver on the SIR system

    Args:
        method (func): function to perform ODE solving
        eqns (func): function to return equation values
        y0 (array): array of initial y-values
        t0 (float): start time of simulation
        t_final (float): end time of simulation
        h (float): step-size
        beta (float): transmission rate
        gamma (float): recovery rate

    Returns:
        array: time values, y-values
    """

    t_values, y_approx = method(SIR_equations, y0, t0, t_final, h, beta, gamma)
    return t_values, y_approx


def plot_SIR(method, t_values, y_approx):
    """Method to plot results of SIR system

    Args:
        method (func): function to perform ODE solving
        t_values (array): time values
        y_approx (array): y-values
    """

    plt.plot(t_values, y_approx[:, 0], label='Susceptible')
    plt.plot(t_values, y_approx[:, 1], label='Infectious')
    plt.plot(t_values, y_approx[:, 2], label='Recovered')
    plt.xlabel('Time (Days)')
    plt.ylabel('Population (# People)')
    plt.title(f'SIR Model with using {method.__name__}')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

    methods = [forward_euler, backward_euler, midpoint_method, heuns_method, runge_kutta4, adams_bashforth, adams_moulton]

    for m in methods:

            # Initial conditions and parameters
        S0 = 990
        I0 = 10
        R0 = 0
        beta = 0.3
        gamma = 0.1
        y0 = [S0, I0, R0]
        t0 = 0
        t_final = 200
        h = 0.1

        print(m.__name__)
        # Solve the SIR modeld
        t_values, y_approx = run_ODE_solver(m, SIR_equations, y0, t0, t_final, h, beta, gamma)

        plot_SIR(m, t_values, y_approx)
