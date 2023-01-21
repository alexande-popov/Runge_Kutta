import matplotlib.pyplot as plt
import sqlite3


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


def save_to_db(x, y, ye, e, table_name='runge_kutta'):
    """Save x, y_numeric, y_exact, errors to DB"""

    rows_list = [(x[i], y[i][0], ye[i], e[i]) for i in range(0,x.size)]

    with sqlite3.connect("out/RK4.db") as con:
        cur = con.cursor()

        # delete every time for rewriting to conveniently run script
        cur.execute(f"DROP TABLE IF EXISTS {table_name}")

        cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
            x REAL NOT NULL,
            y_numeric REAL  NOT NULL,
            y_exact REAL NOT NULL,
            error REAL NOT NULL
        )""")

        cur.executemany(f"INSERT INTO {table_name} (x, y_numeric, y_exact, error) VALUES (?, ?, ?, ?)", rows_list)
        con.commit()