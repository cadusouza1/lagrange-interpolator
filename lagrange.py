import multiprocessing

from sympy import Expr, Number, Symbol, sympify


def lagrange_basis(
    x_coordinates: list[Number], x: Symbol, j: int
) -> list[Expr]:
    """
    Computes the Lagrange basis polynomials for a given set of x-coordinates.

    Args:
        x_coordinates (list[Number]): A list of x-coordinates for which the basis polynomials
                                      are computed.
        x (Symbol): The symbolic variable used in the basis polynomials.

    Returns:
        list[Expr]: A list of symbolic expressions representing the Lagrange basis polynomials.
                   Each polynomial corresponds to one of the x-coordinates.
    """

    with multiprocessing.Pool(processes=j) as pool:
        bases = pool.starmap(
            lagrange_base_li,
            [(x_coordinates, x, i) for i in range(0, len(x_coordinates))],
        )

    return bases


def lagrange_base_li(
    x_coordinates: list[Number], x: Symbol, index: int
) -> Expr:
    """
    Computes the Lagrange base polynomial L_i for a given set of x-coordinates.

    Args:
        x_coordinates (list[Number]): A list of x-coordinates for which the base polynomial is computed.
        x (Symbol): The symbolic variable used in the basis polynomials.

    Returns:
        Expr: A symbolic expressions representing the Lagrange base polynomial L_i.
    """

    base: Expr = sympify(1)

    for j in range(0, len(x_coordinates)):
        if index != j:
            numerator = x - sympify(x_coordinates[j])
            denominator = x_coordinates[index] - x_coordinates[j]
            base *= numerator / denominator

    return base
