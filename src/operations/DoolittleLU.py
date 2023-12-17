import numpy as np
import sympy as sp
from src.operations.CroutLU import SolveLU
def DoolittleLU(matrix, b=None, precision=5):
    eps = 1e-10
    n = matrix.shape[0]
    m = matrix.shape[1]
    LUs = []
    steps = []
    answer = None
    if n != m:
        steps.append("matrix is not square")
        return LUs, steps, answer
    # symbols = getSymbols(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i, j] = sp.N(matrix[i, j], n=precision)
    print(matrix)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)
    for i in range(n):
        L[i, i] = 1
        step = f"L[{i},{i}] = 1"
        for j in range(i, n):
            U[i, j] = matrix[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
            U[i, j] = sp.N(U[i, j], n=precision)
            step += f"\nU[{i},{j}] = {matrix[i, j]} - {sp.N(sum(L[i, k] * U[k, j] for k in range(i)), n=precision)} = {U[i, j]}"
        for j in range(i + 1, n):
            if not sp.Abs(U[i, i]).free_symbols and sp.Abs(U[i, i]) < eps:
                LU = {'L': np.copy(L), 'U': np.copy(U)}
                LUs.append(LU)
                step += f"\nU[{i},{i}] = 0 (matrix is singular)"
                steps.append(step)
                return LUs, steps, answer
            L[j, i] = (matrix[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
            L[j, i] = sp.N(L[j, i], n=precision)
            step += f"\nL[{j},{i}] = ({matrix[j, i]} - {sp.N(sum(L[j, k] * U[k, i] for k in range(i)), n=precision)}) / {U[i, i]} = {L[j, i]}"
        LU = {'L': np.copy(L), 'U': np.copy(U)}
        LUs.append(LU)
        steps.append(step)
    if b is not None:
        steps, answer = SolveLU(L, U, b, steps, precision)
    return LUs, steps, answer

######################################################################################################################
######################################################################################################################
if __name__ == '__main__':
    a, b, c, d, e = sp.symbols('a b c d e')
    # matrix = sp.Matrix([[1.5055, 2.6678, 3.2587, 6.111], [2.6678, 4.7801, 5.3087, 8.041], [3.2587, 5.3087, 6.5832, 9.010], [6.111, 8.041, 9.010, 13.443]])
    matrix = sp.Matrix([[2*a, 3*b, c], [d, 2*a, 3*b], [3*b, c, 2*a]])
    # matrix = sp.Matrix([[5.55557*a, 2.522*b, 3.2587], [2.6678*d, 5.22248, 6.5832], [3.2587*e, 6.5832, 9.010]])
    # matrix = sp.Matrix([[1.555*a, 5.11*b, 11.258*d], [2.12591*a, 1.0028*b, 7.22*a], [3.211*a, 2.009*b, 0.00003*c]])
    matrix = sp.Matrix([[1, 2, 0], [3, 4, 0], [1, 2, 0]])
    # matrix = sp.Matrix([[2, 5, 3], [3, 1, 1], [4, 5, 6]])
    b = sp.Matrix([16, 11, 28])
    matrixx = np.array(matrix).astype(object)
    LUs, steps, answer = DoolittleLU(matrixx, b, 3)

    print('matrix = \n', matrixx)
    print('=' * 80)
    for i in range(len(LUs)):
        print('L = \n', LUs[i]['L'])
        print('U = \n', LUs[i]['U'])
        print('=' * 80)
        print(steps[i])
        print('=' * 80)
    for i in range(len(LUs), len(steps)):
        print(i)
        print(steps[i])
        print('=' * 80)
    if answer is not None:
        print('x = \n', answer['x'])
        print('y = \n', answer['y'])
        print('=' * 80)