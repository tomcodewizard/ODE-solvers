import numpy as np
from scipy.optimize import fsolve


def forward_euler_singular(func, y0, t0, t_final, h):
    """Forward Euler method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """

    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_final:

        y = y + h * func(t, y)
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


def backward_euler_singular(func, y0, t0, t_final, h):
    """Backward Euler method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """

    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0
    y_new = y

    while t < t_final:

        y_new = y + h * func(t + h, y_new)
        t = t + h

        t_values.append(t)
        y_values.append(y_new)

        y = y_new

    return t_values, y_values


def midpoint_method_singular(func, y0, t0, t_final, h):
    """Midpoint method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_final:

        y = y + h * func(t + 0.5 * h, y + 0.5 * h * func(t, y))
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


def heuns_method_singular(func, y0, t0, t_final, h):
    """Heuns method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_final:

        slope_initial = func(t, y)
        y_predictor = y + h * slope_initial

        slope_corrector = func(t + h, y_predictor)
        y = y + (h / 2) * (slope_initial + slope_corrector)

        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


def runge_kutta4_singular(func, y0, t0, t_final, h):
    """Runge-Kutta method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """

    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_final:

        k1 = func(t, y)
        k2 = func(t + 0.5 * h, y + 0.5 * k1)
        k3 = func(t + 0.5 * h, y + 0.5 * k2)
        k4 = func(t + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


def adams_bashforth_singular(func, y0, t0, t_final, h):
    """Adams-Bashforth method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """

    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    # Forward euler for first step
    y = y + h * func(t, y)
    t = t + h

    t_values.append(t)
    y_values.append(y)

    i = 0

    while t < t_final:

        y = y + 0.5 * h * (3 * func(t_values[i + 1], y_values[i + 1]) - func(t_values[i], y_values[i]))
        t = t + h

        t_values.append(t)
        y_values.append(y)

        i += 1

    return t_values, y_values


def adams_moulton_singular(func, y0, t0, t_final, h, *args):
    """Adams-Moulton method for solving a singular ODE

    Args:
        func (func): function equalling dy/dt
        y0 (float): initial value of y
        t0 (float): initial value of t
        t_final (float): final value of t
        h (float): step-size

    Returns:
        list, list: times and y-points
    """

    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    for i in range(1, 3):
        y = y + h * func(t, y, *args)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    while t < t_final:

        corrector = y_values[-1] + (h / 2) * (func(t + h, y_values[-1], *args) + func(t, y, *args))

        # Update values
        t = t + h
        t_values.append(t)
        y_values.append(corrector)

    return t_values, y_values


#############################################

def forward_euler(f, y0, t0, t_final, h, *args):
    """Function to run the Forward Euler method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        y_new = [y[-1][j] + h * f(t[-1], y[-1], *args)[j] for j in range(len(y0))]

        y.append(y_new)
        t.append(t[-1] + h)

    return np.array(t), np.array(y)


def backward_euler(f, y0, t0, t_final, h, *args):
    """Function to run the Backward Euler method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        y_new = fsolve(lambda y_new: y[-1] + h * np.array(f(t[-1] + h, y_new, *args)) - np.array(y_new), y[-1])

        y.append(y_new)
        t.append(t[-1] + h)

    return np.array(t), np.array(y)


def midpoint_method(f, y0, t0, t_final, h, *args):
    """Function to run the Midpoint method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        y_mid = np.array(y[-1]) + 0.5 * h * np.array(f(t[-1], y[-1], *args))
        y_new = np.array(y[-1]) + h * np.array(f(t[-1] + 0.5 * h, y_mid, *args))

        y.append(list(y_new))
        t.append(t[-1] + h)

    return np.array(t), np.array(y)


def heuns_method(f, y0, t0, t_final, h, *args):
    """Function to run the Heuns method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        y_pred = np.array(y[-1]) + h * np.array(f(t[-1], y[-1], *args))
        y_new = np.array(y[-1]) + 0.5 * h * (np.array(f(t[-1], y[-1], *args)) + np.array(f(t[-1] + h, y_pred, *args)))

        y.append(list(y_new))
        t.append(t[-1] + h)

    return np.array(t), np.array(y)


def runge_kutta4(f, y0, t0, t_final, h, *args):
    """Function to run the Runge Kutta RK4 method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        k1 = h * np.array(f(t[-1], y[-1], *args))
        k2 = h * np.array(f(t[-1] + 0.5 * h, np.array(y[-1]) + 0.5 * k1, *args))
        k3 = h * np.array(f(t[-1] + 0.5 * h, np.array(y[-1]) + 0.5 * k2, *args))
        k4 = h * np.array(f(t[-1] + h, np.array(y[-1]) + k3, *args))

        y_new = np.array(y[-1]) + (1 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        y.append(list(y_new))
        t.append(t[-1] + h)

    return np.array(t), np.array(y)


def adams_bashforth(f, y0, t0, t_final, h, *args):
    """Function to run the Adams-Bashforth method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        y_pred = np.array(y[-1]) + 0.5 * h * np.array(f(t[-1], y[-1], *args))
        y_new = np.array(y[-1]) + 0.5 * h * (3 * np.array(f(t[-1] + h, y_pred, *args)) 
                                             - np.array(f(t[-1], y[-1], *args)))

        y.append(list(y_new))
        t.append(t[-1] + h)

    return np.array(t), np.array(y)


def adams_moulton(f, y0, t0, t_final, h, *args):
    """Function to run the Adams-Moulton method

    Args:
        f (func): equations to be solved over
        y0 (float): initial value of y
        t0 (float): starting time value
        t_final (float): ending time value
        h (float): step-size

    Returns:
        np.array: time values, y-values
    """

    y = [y0]
    t = [t0]

    while t[-1] < t_final:

        y_pred = [y[-1][j] + h * f(t[-1], y[-1], *args)[j] for j in range(len(y0))]
        y_new = [y[-1][j] + h * (f(t[-1] + h, y_pred, *args)[j] + f(t[-1], y[-1], *args)[j]) / 2 
                 for j in range(len(y0))]

        y.append(y_new)
        t.append(t[-1] + h)

    return np.array(t), np.array(y)
