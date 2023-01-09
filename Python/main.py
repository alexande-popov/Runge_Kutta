import matplotlib.pyplot as plt

from models import *

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
    ax = fig.subplots()
    plt.title(f'Solution RC4, h = {h}')
    ax.plot(X, Y[:,0], 'ro', label='Numeric')
    ax.plot(X, Ye, label='Exact', color='black')
    ax.grid()
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    plt.savefig('pics/solution_RC4.png')
    # Errors
    fig = plt.figure(1)
    ax = fig.subplots()
    plt.title(f'Errors RC4, h = {h}')
    ax.plot(X, E, 'ro', label='Numeric')
    ax.grid()
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('Difference between exact and RK4 solutions')
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
    ax = fig.subplots()
    plt.title(f'Solution RC4 with variable step, accuracy = {tol}')
    ax.plot(X, Y[:,0], 'ro', label='Numeric')
    ax.plot(X, Ye, label='Exact', color='black')
    ax.grid()
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    plt.savefig('pics/solution_RC4_tolerance.png')
    # Errors
    fig = plt.figure(3)
    ax = fig.subplots()
    plt.title(f'Errors RC4 with variable step, accuracy = {tol}')
    ax.plot(X, E, 'ro', label='Numeric')
    ax.grid()
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('Difference between exact and RK4 solutions')
    plt.savefig('pics/errors_RC4_tolerance.png')

    plt.show()