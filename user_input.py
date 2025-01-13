from sympy import Number, sympify


def parse_points_from_list(lst: list[int]) -> tuple[list[Number], list[Number]]:
    """
    Parses a list of x and y coordinates and returns them as two separate lists where:
    - The even-indexed arguments (0, 2, 4, ...) are treated as x-coordinates.
    - The odd-indexed arguments (1, 3, 5, ...) are treated as y-coordinates.

    Returns:
        tuple[list[Number], list[Number]]: A tuple containing two lists:
            - The first list contains the x-coordinates.
            - The second list contains the y-coordinates.

    Example:
        If the list contains [1, 2, 3, 4], the function will return:
        ([1, 3], [2, 4])
    """

    coordinates: tuple[list[Number], list[Number]] = ([], [])

    for i, arg in enumerate(lst):
        coordinates[i % 2].append(sympify(arg))

    return coordinates
