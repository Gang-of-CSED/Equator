import numpy as np
import sympy as sp

def pivoting(matrix, b, i, n, eps=1e-10):
    #Getting Max Pivot
    max_row = i
    max_pivot = sp.Abs(matrix[i, i])
    #Checking if there is a better pivot
    for j in range(i + 1, n):
        if sp.Abs(matrix[j, i]).free_symbols or sp.Abs(matrix[j, i]) >= eps:
            #Checking Max Pivot
            if sp.Abs(matrix[j, i]) > max_pivot:
                max_pivot = sp.Abs(matrix[j, i])
                max_row = j
    #Checking if the pivot has changed
    if max_row != i:
        #Swapping Rows
        matrix[[i, max_row], :] = matrix[[max_row, i], :]
        if b is not None:
            temp = b[i]
            b[i] = b[max_row]
            b[max_row] = temp
        return True, matrix, b, f"Swap rows {i} and {max_row}\n"
    return False, matrix, b, ""

def SolveLU(L, U, b, steps, precision=5):
    eps = 1e-10
    answer = None
    n = L.shape[0]
    for i in range(n):
        b[i] = sp.N(b[i], n=precision)
    y = sp.Matrix(np.zeros((n, 1), dtype=object))
    # starting from letter 's' to avoid conflict with symbols
    free_variable = 's'
    # Foward Substitution Ly = b
    step = "Forward substitution"
    for i in range(n):
        # Checking if the pivot is zero
        if not sp.Abs(L[i, i]).free_symbols and sp.Abs(L[i, i]) < eps:
            # Checking if there is an infinite number of solutions
            if not sp.Abs(b[i] - sum(L[i, 0:i] * y[0:i])).free_symbols and sp.Abs(b[i] - sum(L[i, 0:i] * y[0:i])) < eps:
                step += f"\ny[{i}] = {free_variable} because L[{i},{i}] = 0 (infinite number of solutions)"
                y[i] = free_variable
                free_variable = chr(ord(free_variable) + 1)
            # Checking if there is no solution
            else:
                step += f"\nno solution because L[{i},{i}] = 0 and b[{i}] != {sp.N(sum(L[i, 0:i] * y[0:i]), n=precision)}"
                steps.append(step)
                return steps, answer
        # Calculating y[i]
        else: 
            y[i] = (b[i] - sp.N(sum(L[i, 0:i] * y[0:i]), n=precision)) / L[i, i]
            y[i] = sp.N(y[i], n=precision)
            step += f"\ny[{i}] = ({b[i]} - {sp.N(sum(L[i, 0:i] * y[0:i]), n=precision)}) / {L[i, i]} = {y[i]}"
    # Backward Substitution Ux = y
    step += "\nBackward substitution"
    x = sp.Matrix(np.zeros((n, 1), dtype=object))
    for i in range(n - 1, -1, -1):
        # Checking if the pivot is zero
        if not sp.Abs(U[i, i]).free_symbols and sp.Abs(U[i, i]) < eps:
            # Checking if there is an infinite number of solutions
            if not sp.Abs(y[i] - sum(U[i, i + 1:n] * x[i + 1:n])).free_symbols and sp.Abs(y[i] - sum(U[i, i + 1:n] * x[i + 1:n])) < eps:
                step += f"\nx[{i}] = {free_variable} because U[{i},{i}] = 0 (infinite number of solutions)"
                x[i] = free_variable
                free_variable = chr(ord(free_variable) + 1)
            # Checking if there is no solution
            else:
                step += f"\nno solution because U[{i},{i}] = 0 and y[{i}] != {sp.N(sum(U[i, i + 1:n] * x[i + 1:n]), n=precision)}"
                steps.append(step)
                return steps, answer
        # Calculating x[i]
        else:
            x[i] = (y[i] - sp.N(sum(U[i, i + 1:n] * x[i + 1:n]), n=precision)) / U[i, i]
            x[i] = sp.N(x[i], n=precision)
            step += f"\nx[{i}] = ({y[i]} - {sp.N(sum(U[i, i + 1:n] * x[i + 1:n]), n=precision)}) / {U[i, i]} = {x[i]}"
    steps.append(step)
    x = np.array(x).astype(object)
    y = np.array(y).astype(object)
    answer = {'x': x, 'y': y}
    return steps, answer

def CroutLU(matrix, b=None, precision=5):
    eps = 1e-10
    n = matrix.shape[0]
    m = matrix.shape[1]
    LUs = []
    steps = []
    answer = None
    # Checking if the matrix is square
    if n != m:
        steps.append("matrix is not square")
        return LUs, steps, answer
    # applying precision
    for i in range(n):
        for j in range(n):
            matrix[i, j] = sp.N(matrix[i, j], n=precision)
    print(matrix)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)
    for k in range(n):
        #pivotting
        step = ""
        # Checking if the pivot is zero
        if not sp.Abs(matrix[k, k]).free_symbols and sp.Abs(matrix[k, k]) < eps:
            pivotted, matrix, b, st = pivoting(matrix, b, k, n)
            # Checking if the matrix is singular
            if pivotted:
                step += st
            else:
                steps.append("matrix is singular")
                return LUs, steps, answer
        # Calculating U[k, k]
        U[k, k] = 1
        step += f"U[{k},{k}] = 1"
        # Calculating L[j, k] and U[k, i]
        for j in range(k, n):
            L[j, k] = matrix[j, k] - sum(L[j, 0:k] * U[0:k, k])
            L[j, k] = sp.N(L[j, k], n=precision)
            step += f"\nL[{j},{k}] = {matrix[j, k]} - {sp.N(sum(L[j, 0:k] * U[0:k, k]), n=precision)} = {L[j, k]}"
        for i in range(k + 1, n):
            # Checking division by zero
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
        steps, answer = SolveLU(L, U, b, steps, precision)
        print("########### Crrout LU #############")
        print("L = \n", L)
        print("U = \n", U)
        print("B = \n", b)
        print("Answer = \n", answer)
    return LUs, steps, answer
######################################################################################################################
######################################################################################################################
if __name__ == '__main__':
    a, b, c, d, e = sp.symbols('a b c d e')
    # matrix = sp.Matrix([[1.5055, 2.6678, 3.2587, 6.111], [2.6678, 4.7801, 5.3087, 8.041], [3.2587, 5.3087, 6.5832, 9.010], [6.111, 8.041, 9.010, 13.443]])
    matrix = sp.Matrix([[2*a, 3*b, c], [d, 2*a, 3*b], [3*b, c, 2*a]])
    # matrix = sp.Matrix([[5.55557*a, 2.522*b, 3.2587], [2.6678*d, 5.22248, 6.5832], [3.2587*e, 6.5832, 9.010]])
    # matrix = sp.Matrix([[1.555*a, 5.11*b, 11.258*d], [2.12591*a, 1.0028*b, 7.22*a], [3.211*a, 2.009*b, 0.00003*c]])
    # matrix = sp.Matrix([[1, 2, 0], [3, 4, 0], [1, 2, 0]])
    matrix = sp.Matrix([[0, 2, 5], [2, 1, 1], [3, 1, 0]])
    b = sp.Matrix([1,1,2])
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
    print(len(steps),  len(LUs))
    if answer is not None:
        print('x = \n', answer['x'])
        print('y = \n', answer['y'])
        print('=' * 80)