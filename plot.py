import matplotlib.pyplot as plt
import numpy as np
from sympy import Expr, Symbol, lambdify


def plot_polynomial(
    x_symbol: Symbol, func: Expr, x_min: int, x_max: int, num: int
) -> None:
    """
    Plots the given polynomial function.

    Args:
        x_symbol (Symbol): The symbolic variable used in the polynomial.
        func (Expr): The polynomial function to be plotted.
        x_min (int): The minimum x value for the plot.
        x_max (int): The maximum x value for the plot.
        num (int): The number of points to use for the plot.

    Returns:
        None: This function does not return any values. It simply displays a plot.

    Example:
        To plot a polynomial function, call this function with the symbolic variable,
        the polynomial expression, and the desired x-values as arguments.
        For example:
            x = symbols("x")
            f = x**2 + 3*x - 4
            plot_polynomial(x, f, -10, 10, 100)
    """

    f = lambdify(x_symbol, func, "numpy")
    x = np.linspace(x_min, x_max, num)
    y = f(x)

    _, ax = plt.subplots()
    ax.plot(x, y)

    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_xlabel(r"$x$", loc="right")
    ax.set_ylabel(r"$y$", loc="top")

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    plt.show()
