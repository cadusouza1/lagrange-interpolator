import sys

from sympy import Expr, expand, symbols, sympify

from lagrange import lagrange_basis
from user_input import get_points_from_cmd


def main() -> None:
    x_coordinates, y_coordinates = get_points_from_cmd()

    if len(x_coordinates) != len(y_coordinates):
        print("x and y coordinates must be pairs")
        sys.exit(1)

    if len(x_coordinates) != len(set(x_coordinates)):
        print("x coordinates must all be different values")
        sys.exit(1)

    x = symbols("x")

    bases = lagrange_basis(x_coordinates, x)
    polynomial: Expr = sympify(0)

    for y, basis in zip(y_coordinates, bases):
        polynomial += sympify(y) * basis

    print(expand(polynomial))


if __name__ == "__main__":
    main()
