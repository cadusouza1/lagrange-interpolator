import sys

from sympy import Number, sympify


def get_points_from_cmd() -> tuple[list[Number], list[Number]]:
    """
    Reads x and y coordinates from command-line arguments and returns them as two separate lists.

    The function expects an even number of command-line arguments, where:
    - The odd-indexed arguments (1st, 3rd, 5th, ...) are treated as x-coordinates.
    - The even-indexed arguments (2nd, 4th, 6th, ...) are treated as y-coordinates.

    Returns:
        tuple[list[Number], list[Number]]: A tuple containing two lists:
            - The first list contains the x-coordinates.
            - The second list contains the y-coordinates.

    Example:
        If the command-line arguments are `1 2 3 4`, the function will return:
        ([1, 3], [2, 4])
    """

    coordinates: tuple[list[Number], list[Number]] = ([], [])

    # Skipping the program's name in sys.argv
    for i, arg in enumerate(sys.argv[1:]):
        coordinates[i % 2].append(sympify(arg))

    return coordinates
