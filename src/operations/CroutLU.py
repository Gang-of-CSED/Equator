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
    return list(symbols)

def CroutLU(matrix, b=None, precision=5):
    eps = 1e-10
    n = matrix.shape[0]
    m = matrix.shape[1]
    LUs = []
    steps = []
    answer = None
    if n != m:
        steps.append("matrix is not square")
        return LUs, steps, answer
    symbols = getSymbols(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i, j] = sp.N(matrix[i, j], n=precision)
    print(matrix)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)
    for k in range(n):
        U[k, k] = 1
        step = f"U[{k},{k}] = 1"
        for j in range(k, n):
            L[j, k] = matrix[j, k] - sum(L[j, 0:k] * U[0:k, k])
            L[j, k] = sp.N(L[j, k], n=precision)
            step += f"\nL[{j},{k}] = {matrix[j, k]} - {sp.N(sum(L[j, 0:k] * U[0:k, k]), n=precision)} = {L[j, k]}"
        for i in range(k + 1, n):
            if not sp.Abs(L[k, k]).free_symbols and sp.Abs(L[k, k]) < eps:
                LU = {'L': np.copy(L), 'U': np.copy(U)}
                LUs.append(LU)
                step += f"\nL[{k},{k}] = 0 (matrix is singular)"
                steps.append(step)
                return LUs, steps, answer
            U[k, i] = (matrix[k, i] - sum(L[k, 0:k] * U[0:k, i])) / L[k, k]
            U[k, i] = sp.N(U[k, i], n=precision)
            step += f"\nU[{k},{i}] = ({matrix[k, i]} - {sp.N(sum(L[k, 0:k] * U[0:k, i]), n=precision)}) / {L[k, k]} = {U[k, i]}"
        LU = {'L': np.copy(L), 'U': np.copy(U)}
        LUs.append(LU)
        steps.append(step)
        # LUx = b
        # Ux = y   
        # Ly = b
    if b is not None:
        for i in range(n):
            b[i] = sp.N(b[i], n=precision)
        y = sp.Matrix(np.zeros((n, 1), dtype=object))
        # starting from letter 's' to avoid conflict with symbols
        free_variable = 's'
        step = "Forward substitution"
        for i in range(n):
            if not sp.Abs(L[i, i]).free_symbols and sp.Abs(L[i, i]) < eps:
                if not sp.Abs(b[i] - sum(L[i, 0:i] * y[0:i])).free_symbols and sp.Abs(b[i] - sum(L[i, 0:i] * y[0:i])) < eps:
                    step += f"\ny[{i}] = {free_variable} because L[{i},{i}] = 0 (infinite number of solutions)"
                    symbols.append(free_variable)
                    y[i] = free_variable
                    free_variable = chr(ord(free_variable) + 1)
                else:
                    step += f"\nno solution because L[{i},{i}] = 0 and b[{i}] != {sp.N(sum(L[i, 0:i] * y[0:i]), n=precision)}"
                    steps.append(step)
                    return LUs, steps, answer
            else: 
                y[i] = (b[i] - sum(L[i, 0:i] * y[0:i])) / L[i, i]
                y[i] = sp.N(y[i], n=precision)
                step += f"\ny[{i}] = ({b[i]} - {sp.N(sum(L[i, 0:i] * y[0:i]), n=precision)}) / {L[i, i]} = {y[i]}"
        steps.append(step)
        step = "Backward substitution"
        x = sp.Matrix(np.zeros((n, 1), dtype=object))
        for i in range(n - 1, -1, -1):
            if not sp.Abs(U[i, i]).free_symbols and sp.Abs(U[i, i]) < eps:
                if not sp.Abs(y[i] - sum(U[i, i + 1:n] * x[i + 1:n])).free_symbols and sp.Abs(y[i] - sum(U[i, i + 1:n] * x[i + 1:n])) < eps:
                    step += f"\nx[{i}] = {free_variable} because U[{i},{i}] = 0 (infinite number of solutions)"
                    symbols.append(free_variable)
                    x[i] = free_variable
                    free_variable = chr(ord(free_variable) + 1)
                else:
                    step += f"\nno solution because U[{i},{i}] = 0 and y[{i}] != {sp.N(sum(U[i, i + 1:n] * x[i + 1:n]), n=precision)}"
                    steps.append(step)
                    return LUs, steps, answer
            else:
                x[i] = (y[i] - sum(U[i, i + 1:n] * x[i + 1:n])) / U[i, i]
                x[i] = sp.N(x[i], n=precision)
            step += f"\nx[{i}] = ({y[i]} - {sp.N(sum(U[i, i + 1:n] * x[i + 1:n]), n=precision)}) / {U[i, i]} = {x[i]}"
        steps.append(step)
        x = np.array(x).astype(object)
        y = np.array(y).astype(object)
        answer = {'x': x, 'y': y}
    return LUs, steps, answer
######################################################################################################################
######################################################################################################################
if __name__ == '__main__':
    a, b, c, d, e = sp.symbols('a b c d e')
    # matrix = sp.Matrix([[1.5055, 2.6678, 3.2587, 6.111], [2.6678, 4.7801, 5.3087, 8.041], [3.2587, 5.3087, 6.5832, 9.010], [6.111, 8.041, 9.010, 13.443]])
    # matrix = sp.Matrix([[2*a, 3*b, c], [d, 2*a, 3*b], [3*b, c, 2*a]])
    # matrix = sp.Matrix([[5.55557*a, 2.522*b, 3.2587], [2.6678*d, 5.22248, 6.5832], [3.2587*e, 6.5832, 9.010]])
    # matrix = sp.Matrix([[1.555*a, 5.11*b, 11.258*d], [2.12591*a, 1.0028*b, 7.22*a], [3.211*a, 2.009*b, 0.00003*c]])
    matrix = sp.Matrix([[1, 2, 0], [3, 4, 0], [1, 2, 0]])
    b = sp.Matrix([3, 7, 3])
    matrixx = np.array(matrix).astype(object)
    LUs, steps, answer = CroutLU(matrixx, b, 3)

    print('matrix = \n', matrixx)
    print('=' * 80)
    for i in range(len(LUs)):
        print('L = \n', LUs[i]['L'])
        print('U = \n', LUs[i]['U'])
        print('=' * 80)
        print(steps[i])
        print('=' * 80)
    for i in range(len(LUs), len(steps)):
        print(steps[i])
        print('=' * 80)
    if answer is not None:
        print('x = \n', answer['x'])
        print('y = \n', answer['y'])
        print('=' * 80)