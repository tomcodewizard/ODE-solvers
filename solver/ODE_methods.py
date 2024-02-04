
def forward_euler(func, y0, t0, t_final, h):
    """Forward Euler method for solving ODEs

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


def backward_euler(func, y0, t0, t_final, h):
    """Backward Euler method for solving ODEs

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


def rk4(func, y0, t0, t_final, h):
    """Runge-Kutta method for solving ODEs

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


def adams_bashforth(func, y0, t0, t_final, h):
    """Adams-Bashforth method for solving ODEs

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
