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
        # else:
        #     rounded_expr = number.copy()
        #     for symbol in symbols:
        #         if symbol in number.free_symbols:
        #             coefficient = number.coeff(symbol)
        #             rounded_coefficient = round(float(coefficient), precision)
        #             rounded_expr = rounded_expr.subs(coefficient, rounded_coefficient * symbol)
        #     return rounded_expr
    else:
        return round(number, precision)
    return number

def CroutLU(matrix, b=None, precision=5):
    n = matrix.shape[0]
    m = matrix.shape[1]
    LUs = []
    steps = []
    answer = None
    if n != m:
        steps.append("matrix is not square")
        return LUs, steps, answer
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
                    return LUs, steps, answer
            U[k, i] = (matrix[k, i] - sum(L[k, 0:k] * U[0:k, i])) / L[k, k]
            U[k, i] = Round(U[k, i], precision, symbols)
            step += f"\nU[{k},{i}] = ({Round(matrix[k, i], precision, symbols)} - {Round(sum(L[k, 0:k] * U[0:k, i]), precision, symbols)}) / {L[k, k]} = {U[k, i]}"
        LU = {'L': np.copy(L), 'U': np.copy(U)}
        LUs.append(LU)
        steps.append(step)
        # LUx = b
        # Ux = y   
        # Ly = b
    if b is not None:
        y = sp.Matrix(np.zeros((n, 1), dtype=object))
        # starting from letter 's' to avoid conflict with symbols
        free_variable = 's'
        step = "Forward substitution"
        for i in range(n):
            if not sp.Abs(L[i, i]).free_symbols and sp.Abs(L[i, i]) < 1e-10:
                step += f"\ny[{i}] = {free_variable} because L[{i},{i}] = 0 (infinite number of solutions)"
                symbols.append(free_variable)
                y[i] = free_variable
                free_variable = chr(ord(free_variable) + 1)
            else: 
                y[i] = (b[i] - sum(L[i, 0:i] * y[0:i])) / L[i, i]
                y[i] = Round(y[i], precision, symbols)
                step += f"\ny[{i}] = ({Round(b[i], precision, symbols)} - {Round(sum(L[i, 0:i] * y[0:i]), precision, symbols)}) / {L[i, i]} = {y[i]}"
        steps.append(step)
        step = "Backward substitution"
        x = sp.Matrix(np.zeros((n, 1), dtype=object))
        for i in range(n - 1, -1, -1):
            if not sp.Abs(U[i, i]).free_symbols and sp.Abs(U[i, i]) < 1e-10:
                step += f"\nx[{i}] = {free_variable} because U[{i},{i}] = 0 (infinite number of solutions)"
                symbols.append(free_variable)
                x[i] = free_variable
                free_variable = chr(ord(free_variable) + 1)
            else:
                x[i] = (y[i] - sum(U[i, i + 1:n] * x[i + 1:n])) / U[i, i]
                x[i] = Round(x[i], precision, symbols)
            step += f"\nx[{i}] = ({Round(y[i], precision, symbols)} - {Round(sum(U[i, i + 1:n] * x[i + 1:n]), precision, symbols)}) / {U[i, i]} = {x[i]}"
        steps.append(step)
        answer = {'x': x, 'y': y}
    return LUs, steps, answer
######################################################################################################################
######################################################################################################################
if __name__ == '__main__':
    a, b, c, d, e = sp.symbols('a b c d e')
    # matrix = sp.Matrix([[1.5055, 2.6678, 3.2587, 6.111], [2.6678, 4.7801, 5.3087, 8.041], [3.2587, 5.3087, 6.5832, 9.010], [6.111, 8.041, 9.010, 13.443]])
    matrix = sp.Matrix([[2*a, 3*b, c], [d, 2*a, 3*b], [3*b, c, 2*a]])
    # matrix = sp.Matrix([[5.55557*a, 2.522*b, 3.2587], [2.6678*d, 5.22248, 6.5832], [3.2587*e, 6.5832, 9.010]])
    b = sp.Matrix([1, 2, 3])
    matrixx = np.array(matrix).astype(object)
    LUs, steps, answer = CroutLU(matrixx, b, 2)

    print('matrix = \n', matrix)
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