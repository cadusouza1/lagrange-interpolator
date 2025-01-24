import matplotlib.pyplot as plt
import numpy as np
from sympy import Expr, Symbol, lambdify


def plot_polynomial(
    x_symbol: Symbol, func: Expr, x_min: int, x_max: int, num: int
):
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

    # plt.plot(x, y)
    # plt.ylabel("Nums")
    # plt.show()
