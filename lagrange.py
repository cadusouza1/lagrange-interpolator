from sympy import Expr, Number, Symbol, sympify


def lagrange_basis(x_coordinates: list[Number], x: Symbol) -> list[Expr]:
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

    bases: list[Expr] = []

    for i in range(0, len(x_coordinates)):
        basis: Expr = sympify(1)

        for j in range(0, len(x_coordinates)):
            if i != j:
                numerator = x - sympify(x_coordinates[j])
                denominator = x_coordinates[i] - x_coordinates[j]
                basis *= numerator / denominator

        bases.append(basis)

    return bases
