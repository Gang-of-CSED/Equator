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

def Round(number, precision=5, symbols=None):
    if isinstance(number, sp.Expr):
        if not number.free_symbols:
            return round(number, precision)
    else:
        return round(number, precision)
    return number

def CroutLU(matrix, precision=5):
    n = matrix.shape[0]
    m = matrix.shape[1]
    LUs = []
    steps = []
    if n != m:
        steps.append("matrix is not square")
        return LUs, steps
    symbols = getSymbols(matrix)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)
    for k in range(n):
        U[k, k] = 1
        step = f"U[{k},{k}] = 1"
        for j in range(k, n):
            L[j, k] = matrix[j, k] - sum(L[j, 0:k] * U[0:k, k])
            L[j, k] = Round(L[j, k], precision, symbols)
            step += f"\nL[{j},{k}] = {Round(matrix[j, k], precision, symbols)} - {Round(sum(L[j, 0:k] * U[0:k, k]), precision, symbols)} = {L[j, k]}"
        for i in range(k + 1, n):
            if not sp.Abs(L[k, k]).free_symbols:
                if sp.Abs(L[k, k]) < 1e-10:
                    LU = {'L': np.copy(L), 'U': np.copy(U)}
                    LUs.append(LU)
                    step += f"\nL[{k},{k}] = 0 (matrix is singular)"
                    steps.append(step)
                    return LUs, steps
            U[k, i] = (matrix[k, i] - sum(L[k, 0:k] * U[0:k, i])) / L[k, k]
            U[k, i] = Round(U[k, i], precision, symbols)
            step += f"\nU[{k},{i}] = ({Round(matrix[k, i], precision, symbols)} - {Round(sum(L[k, 0:k] * U[0:k, i]), precision, symbols)}) / {L[k, k]} = {U[k, i]}"
        LU = {'L': np.copy(L), 'U': np.copy(U)}
        LUs.append(LU)
        steps.append(step)
    return LUs, steps
######################################################################################################################
######################################################################################################################
a, b, c, d, e = sp.symbols('a b c d e')
matrix = sp.Matrix([[1.5055, 2.6678, 3.2587, 6.111], [2.6678, 4.7801, 5.3087, 8.041], [3.2587, 5.3087, 6.5832, 9.010], [6.111, 8.041, 9.010, 13.443]])
# matrix = sp.Matrix([[2*a, 3*b, c], [d, 2*a, 3*b], [3*b, c, 2*a]])
matrix = sp.Matrix([[5.57, 2.522, 3.2587], [2.6678*d, 5.22248, 6.5832], [3.2587*e, 6.5832, 9.010]])
matrixx = np.array(matrix).astype(object)

LUs, steps = CroutLU(matrixx, 2)

print('matrix = \n', matrix)
print('=' * 80)
for i in range(len(LUs)):
    print('L = \n', LUs[i]['L'])
    print('U = \n', LUs[i]['U'])
    print('=' * 80)
    print(steps[i])
    print('=' * 80)