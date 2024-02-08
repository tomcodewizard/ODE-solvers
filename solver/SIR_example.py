from ODE_methods import forward_euler, backward_euler, midpoint_method, heuns_method, \
                        runge_kutta4, adams_bashforth, adams_moulton
from utility import record_runtime
import matplotlib.pyplot as plt


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


def run_solvers(parameters, methods, plot=False):
    """Method to run ODE solvers

    Args:
        parameters (dict): dictionary of parameter values
        methods (array): array of ODE solver methods
        plot (bool): boolean to dictate whether to plot the models
    """

    print(f'Parameters: {parameters}')

    for m in methods:

        S0, I0, R0, beta, gamma, t0, t_final, h = parameters.values()
        y0 = [S0, I0, R0]

        print(m.__name__)

        t_values, y_approx = run_ODE_solver(m, SIR_equations, y0, t0, t_final, h, beta, gamma)

        if plot is True:

            plot_SIR(m, t_values, y_approx)


methods = [forward_euler, backward_euler, midpoint_method, heuns_method, runge_kutta4, adams_bashforth, adams_moulton]

ex1_parameters = {'S0': 990, 'I0': 10, 'R0': 0, 'beta': 0.2, 'gamma': 0.1, 't0': 0, 't_final': 200, 'h': 0.1}
ex2_parameters = {'S0': 990, 'I0': 10, 'R0': 0, 'beta': 0.5, 'gamma': 0.1, 't0': 0, 't_final': 200, 'h': 0.1}
ex3_parameters = {'S0': 990, 'I0': 10, 'R0': 0, 'beta': 0.8, 'gamma': 0.1, 't0': 0, 't_final': 200, 'h': 0.1}

params = [ex1_parameters, ex2_parameters, ex3_parameters]

if __name__ == "__main__":

    for p in params:

        run_solvers(p, methods, plot=False)
