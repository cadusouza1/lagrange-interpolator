import argparse
import sys

from sympy import Expr, Number, expand, symbols, sympify

import plot
from lagrange import lagrange_basis
from user_input import parse_points_from_list


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A program to calculate the lagrange polynomial for a given set of points"
    )

    parser.add_argument(
        "-p",
        "--points",
        nargs="+",
        type=Number,
        required=True,
        help="x y pairs to calculate the lagrange polynomial for",
    )

    parser.add_argument(
        "-j",
        "--num-cores",
        default=1,
        type=int,
        help="Number of cores to use for the polynomial calculations",
    )

    parser.add_argument("--plot", default=False, action="store_true")

    args = parser.parse_args()

    x_coordinates, y_coordinates = parse_points_from_list(args.points)

    if len(x_coordinates) != len(y_coordinates):
        print("x and y coordinates must be pairs")
        sys.exit(1)

    if len(x_coordinates) != len(set(x_coordinates)):
        print("x coordinates must all be different values")
        sys.exit(1)

    x = symbols("x")

    bases = lagrange_basis(x_coordinates, x, args.num_cores)
    polynomial: Expr = sympify(0)

    for y, basis in zip(y_coordinates, bases):
        polynomial += sympify(y) * basis

    print(expand(polynomial))

    if args.plot:
        plot.plot_polynomial(x, polynomial, -10, 10, 1000)


if __name__ == "__main__":
    main()
