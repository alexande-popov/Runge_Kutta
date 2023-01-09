import numpy as np


def rhs(x, y):
    """Right hand side function"""
    f = np.array([y[1], y[2], y[3], y[4],
                  (-1)*(15*y[4] + 90*y[3] + 270*y[2] + 405*y[1] + 243*y[0])
                  ])
    return f


def runge_kutta(x0, y0, xN, h):
    """ X, Y = runge_kutta(x0, y0, xN, h).
    4th - order Runge - Kutta for equation y' = f(x, y)
    INPUT:
    x0, y0 = initial conditions
    xN = final point of x.
    h = step in x used in integration.
    y = {y[0], y[1], ...y[n - 1]}
    rhs = right hand side, user - supplied function that returns the array f(x, y) = {y’[0], y’[1], ..., y’[n - 1]}.
    OUTPUT:
    X, Y grid of points of solution
    """
    X = []
    Y = []
    X.append(x0)
    Y.append(y0)

    xi, yi = x0, y0
    # fill the grid by integration
    while xi < xN:

        h = min(h, xN-xi)

        k1 = h * rhs(xi, yi)
        k2 = h * rhs(xi + h/2, yi + k1/2)
        k3 = h * rhs(xi + h/2, yi + k2/2)
        k4 = h * rhs(xi + h, yi + k3)

        yi = yi + (k1  + 2*k2 + 2*k3 + k4) / 6
        xi = xi + h

        X.append(xi)
        Y.append(yi)

    return np.array(X), np.array(Y)


def runge_kutta_tolerance(x0, y0, xN, h=0.1, t=0.1):
    """ X, Y = runge_kutta(x0, y0, xN, h).
    4th - order Runge - Kutta for equation y' = f(x, y)
    INPUT:
    x0, y0 = initial conditions
    xN = final point of x.
    h = step in x used in integration.
    t = tolerance
    y = {y[0], y[1], ...y[n - 1]}
    rhs = right hand side, user - supplied function that returns the array f(x, y) = {y’[0], y’[1], ..., y’[n - 1]}.
    OUTPUT:
    X, Y grid of points of solution
    """
    X = []
    Y = []
    E = []
    X.append(x0)
    Y.append(y0)
    E.append(np.array([0, 0, 0, 0, 0]))

    xi, yi = x0, y0
    # fill the grid by integration
    while xi < xN:

        h = min(h, xN-xi)

        def increment(x, y, h, what='both'):
            """If "increment" returns increment of Runge-Kutta-4
            If "error" returns difference between Runge-Kutta-4 and Euler
            Else returns both increment and error"""

            k1 = h*rhs(x, y)
            k2 = h*rhs(x + h/2, y + k1/2)
            k3 = h*rhs(x + h/2, y + k2/2)
            k4 = h*rhs(x + h, y + k3)

            incr = (k1 + 2*k2 + 2*k3 + k4) / 6
            error = abs((-5*k1 + 2*k2 + 2*k3 + k4) / 6)

            if what == 'increment':
                return incr
            elif what == 'error':
                return error
            else:
                return incr, error

        ei = increment(xi, yi, h, 'error')
        while ei.max() > t:
            ei = increment(xi, yi, h, 'error')
            h = h / 2

        yi = yi + increment(xi, yi, h, 'increment')
        xi = xi + h

        if ei.max() < t/16:
            h = 2 * h

        X.append(xi)
        Y.append(yi)
        E.append(ei)

    return np.array(X), np.array(Y)