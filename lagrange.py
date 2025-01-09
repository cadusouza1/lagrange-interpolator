from sympy import Expr, Number, Symbol, sympify


def lagrange_basis(x_coordinates: list[Number], x: Symbol) -> list[Expr]:
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
