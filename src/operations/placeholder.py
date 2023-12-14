import numpy as np
import sympy as sp

def getSymbols(matrix):
    symbols = set()

    for row in matrix:
        for element in row:
            if isinstance(element, sp.Symbol):
                symbols.add(element)
            elif isinstance(element, sp.Expr):
                symbols.update(element.free_symbols)
    print(symbols)
    return list(symbols)


def CroutLU(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    steps = []
    steps2 = []
    if n != m:
        steps2.append("matrix is not square")
        return steps, steps2
    symbols = getSymbols(matrix)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)
    for k in range(n):
        U[k, k] = 1
        for j in range(k, n):
            L[j, k] = matrix[j, k] - sum(L[j, 0:k] * U[0:k, k])
            steps2.append(f"L[{j},{k}] = {matrix[j, k]} - {sum(L[j, 0:k] * U[0:k, k])} = {L[j, k]}")
        for i in range(k + 1, n):
            if not sp.Abs(L[k, k]).free_symbols:
                if sp.Abs(L[k, k]) < 1e-10:
                    step = {'L': np.copy(L), 'U': np.copy(U)}
                    steps.append(step)
                    steps2.append(f"L[{k},{k}] = 0 (matrix is singular)")
                    return steps, steps2
            U[k, i] = (matrix[k, i] - sum(L[k, 0:k] * U[0:k, i])) / L[k, k]
            steps2.append(f"U[{k},{i}] = ({matrix[k, i]} - {sum(L[k, 0:k] * U[0:k, i])}) / {L[k, k]} = {U[k, i]}")
        step = {'L': np.copy(L), 'U': np.copy(U)}
        steps.append(step)
    return steps, steps2
######################################################################################################################
######################################################################################################################
a, b, c, d = sp.symbols('a b c d')
# matrix = sp.Matrix([[1, 2, 3, 6], [4, 5, 6, 9], [7, 8, 9, 12], [10, 11, 12, 15]])
matrix = sp.Matrix([[2*a, 3*b, c], [d, 2*a, 3*b], [3*b, c, 2*a]])
matrixx = np.array(matrix).astype(object)

steps, steps2 = CroutLU(matrixx)

print('matrix = \n', matrix)
print('=' * 80)
for step in steps2:
    print(step)
    print('=' * 80)
for step in steps:
    print('L = \n', step['L'])
    print('U = \n', step['U'])
    print('=' * 80)