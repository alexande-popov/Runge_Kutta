import matplotlib.pyplot as plt


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