from sympy import Expr, Symbol, expand, symbols, sympify


def lagrange_basis(x_coordinates: list[int], x: Symbol) -> list[Expr]:
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


x_coordinates = [1, 2, 3, 4]
y_coordinates = [2, 3, 4, 5]
x = symbols("x")

bases = lagrange_basis(x_coordinates, x)
polynomial: Expr = sympify(0)

for y, basis in zip(y_coordinates, bases):
    polynomial += sympify(y) * basis

# print(polynomial)
print(expand(polynomial))
