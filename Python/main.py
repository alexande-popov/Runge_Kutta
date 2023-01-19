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
    x0 = 0
    xN = 5
    y0 = np.array([0, 3, -9, -8, 0])
    h = 0.01

    # grid of solutions with RK4
    X, Y = runge_kutta(x0, y0, xN, h)

    # exact solution
    Ye = -np.exp(-3 * X) * X * (129 * X ** 3 + 16 * X ** 2 - 54 * X - 36) / 12

    # Errors - difference of RC4 and exaxt solution
    E = (Ye - Y[:, 0])

    # Draw
    # Solution
    fig = plt.figure(0)
    draw_solution(x=X, y=Y, ye=Ye, figure=fig, title=f'Solution RC4, h = {h}')
    plt.savefig('pics/solution_RC4.png')
    # Errors
    fig = plt.figure(1)
    draw_errors(x=X, e=E, figure=fig, title=f'Errors RC4, h = {h}')
    plt.savefig('pics/errors_RC4.png')


    # RK4 with defined tolerance
    tol = 0.5
    X, Y = runge_kutta_tolerance(x0, y0, xN, h=0.1, t=tol)
    # Exact solution
    Ye = -np.exp(-3 * X) * X * (129 * X ** 3 + 16 * X ** 2 - 54 * X - 36) / 12
    # Errors - difference of RC4_tol and exact solution
    E = (Ye - Y[:, 0])

    # Draw
    # Solution
    fig = plt.figure(2)
    draw_solution(x=X, y=Y, ye=Ye, figure=fig, title=f'Solution RC4 with variable step, accuracy = {tol}')
    plt.savefig('pics/solution_RC4_tolerance.png')
    # Errors
    fig = plt.figure(3)
    draw_errors(x=X, e=E, figure=fig, title=f'Errors RC4 with variable step, accuracy = {tol}')
    plt.savefig('pics/errors_RC4_tolerance.png')

    #plt.show()