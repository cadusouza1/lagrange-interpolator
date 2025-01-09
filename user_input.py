import sys

from sympy import Number, sympify


def get_points_from_cmd() -> tuple[list[Number], list[Number]]:
    # tuple of x and y coordinates lists
    coordinates: tuple[list[Number], list[Number]] = ([], [])

    # Skipping the program's name in sys.argv
    for i, arg in enumerate(sys.argv[1:]):
        coordinates[i % 2].append(sympify(arg))

    return coordinates
