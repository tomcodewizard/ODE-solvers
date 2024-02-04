
class ODE_methods:


    def __init__():

        ...

    def forward_euler(func, y0, t0, tn, h):
        """Forward Euler method for solving ODEs

        Args:
            func (func): function equalling dy/dt 
            y0 (float): initial value of y
            t0 (float): initial value of t
            tn (float): current value of t at iteration n
            h (float): step-size

        Returns:
            list, list: times and y-points
        """

        t_values = [t0]
        y_values = [y0]

        t = t0
        y = y0

        while t < tn:

            y = y + h * func(t, y)
            t = t + h

            t_values.append(t)
            y_values.append(y)

        return t_values, y_values
    
    def backward_euler(func, y0, t0, tn, h):
        """Backward Euler method for solving ODEs

        Args:
            func (func): function equalling dy/dt 
            y0 (float): initial value of y
            t0 (float): initial value of t
            tn (float): current value of t at iteration n
            h (float): step-size

        Returns:
            list, list: times and y-points
        """

        t_values = [t0]
        y_values = [y0]

        t = t0
        y = y0

        while t < tn:
            
            y_new = y + h * func(t + h, y_new)
            t = t + h

            t_values.append(t)
            y_values.append(y_new)
            y = y_new

        return t_values, y_values
