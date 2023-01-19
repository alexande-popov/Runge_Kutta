import matplotlib.pyplot as plt

from models import *


def beauty(axes, xlabel=r'$x$', ylabel=r'$y(x)$' ):
    """Set x & y labels, draw legend, draw grid"""
    axes.grid()
    axes.legend()
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)


def draw_solution(x, y, ye, figure, title):
    """x, y, ye - arrays of x, numeric solutions, exact solution"""
    ax = figure.subplots()
    plt.title(title)
    ax.plot(x, y[:,0], 'ro', label='Numeric')
    ax.plot(x, ye, label='Exact', color='black')
    beauty(ax)


def draw_errors(x, e, figure, title):
    """x, e - arrays of x, error e"""
    ax = figure.subplots()
    plt.title(title)
    ax.plot(x, e, 'ro', label='Numeric')
    beauty(ax, ylabel='Difference between exact and RK4 solutions')


if __name__ == '__main__':

    # conditions of the problem
    x0 = 0
    xN = 5
    y0 = np.array([0, 3, -9, -8, 0])

    # solver parameters
    h = 0.01   # for RK4 with fixed step
    tol = 0.5  # for RK4 with defined tolerance

    # graph titles
    titles = {'solution': [f'Solution RC4, fixed step $h = {h}$',
                            f'Solution RC4 with variable step, accuracy = {tol}'],
               'errors': [f'Errors RC4, fixed step $h = {h}$',
                          f'Errors RC4 with variable step, accuracy = {tol}']}

    # saving names of graphs files
    save_to = {'solution': ['pics/solution_RC4.png',
                             'pics/solution_RC4_tolerance.png'],
                'errors': ['pics/errors_RC4.png',
                           'pics/errors_RC4_tolerance.png']}

    # both methods
    for ind, method in enumerate(
            [runge_kutta(x0, y0, xN, h),
             runge_kutta_tolerance(x0, y0, xN, h=0.1, t=tol)]):

        # grid of solutions
        X, Y = method

        # Exact solution
        Ye = -np.exp(-3 * X) * X * (129 * X ** 3 + 16 * X ** 2 - 54 * X - 36) / 12

        # Errors - difference of RC4_tol and exact solution
        E = (Ye - Y[:, 0])

        # === Draw ===

        # Solution
        fig = plt.figure(ind * 2)
        draw_solution(x=X, y=Y, ye=Ye, figure=fig, title=titles['solution'][ind])
        plt.savefig(save_to['solution'][ind])

        # Errors
        fig = plt.figure(ind * 2 + 1)
        draw_errors(x=X, e=E, figure=fig, title=titles['errors'][ind])
        plt.savefig(save_to['errors'][ind])

    #plt.show()