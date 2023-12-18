import numpy as np 
import sympy as sp 
import math
from src.operations.CroutLU import SolveLU

def getU(L):
    """
    Transpose a lower triangular matrix to obtain the upper triangular matrix.

    Parameters:
        L (numpy.ndarray): Lower triangular matrix.

    Returns:
        numpy.ndarray: Upper triangular matrix.

    """
    if len(L)==0: return L
    n = L.shape[0]
    U = np.zeros((n, n), dtype=object)
    for i in range (n):
        for j in range(n):
            U[i][j] = L[j][i]
    return U

def isPDM(matrix):
    """
    Check if a matrix is positive definite.

    Parameters:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        bool: True if the matrix is positive definite, False otherwise.

    """
    n = matrix.shape[0]
    for i in range(n):
        if(matrix[i][i] <= 0):
            return False
    return True

def isSymmetric(matrix):
    """
    Check if a matrix is symmetric.

    Parameters:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        bool: True if the matrix is symmetric, False otherwise.

    """
    n = matrix.shape[0]
    m = matrix.shape[1]
    if n != m:
        return False
    for i in range (n):
        for j in range(m):
            if(matrix[i][j] != matrix[j][i]):
                return False
    return True

def isSPDM(matrix):
    """
    Check if a matrix is symmetric positive definite.

    Parameters:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        bool: True if the matrix is symmetric positive definite, False otherwise.

    """
    return (isSymmetric(matrix) and isPDM(matrix))
    

def Cholesky(matrix, b=None, precision=5):
    """
    Perform Cholesky decomposition on a symmetric positive definite matrix.

    Parameters:
        matrix (numpy.ndarray): Symmetric positive definite matrix.
        b (numpy.ndarray): Right-hand side vector for solving the system (optional).
        precision (int): Number of decimal places for numerical precision.

    Returns:
        tuple: List of intermediate steps, list of LU decompositions, and the solution (if provided).

    """
    steps = []
    LUs = []
    answer = None
    NSPDM = "Non Symmetric Positive Definite Matrices"
    if not isSPDM(matrix):
        return [],[NSPDM],answer
    try:
        n = matrix.shape[0]
        L = np.zeros((n, n), dtype=object)

        for i in range(n):
            for j in range(i+1):
                sp.N(matrix[i][j] , n=precision)
                sigma = 0 
                for k in range(j):
                    L[i][k] = sp.N(L[i][k], n=precision)
                    L[j][k] = sp.N(L[j][k], n=precision)
                    sigma += L[i][k] * L[j][k]
                    sigma = sp.N(sigma, n=precision)

                if i == j:
                    L[i][j] = math.sqrt(matrix[i][j] - sigma)
                    L[i][j] = sp.N(L[i][j], n=precision)
                    step = f"L[{i+1}][{j+1}] = sqrt(({matrix[i][i]}) - ({sigma})) = {L[i][j]}"
                    steps.append(step)
                else:
                    if(L[j][j] == 0): return [],["!!unavailable decomposition!!"],answer
                    L[i][j] = (1.0 / L[j][j]) * (matrix[i][j] - sigma)
                    L[i][j] = sp.N(L[i][j], n=precision)
                    step = f"L[{i+1}][{j+1}] = ({matrix[i][j]} - {sigma}) / ({L[j][j]}) = {L[i][j]}"
                    steps.append(step)
                LU = {'L': np.copy(L), 'U': np.copy(getU(L))}
                LUs.append(LU)
    
        U = getU(L)
        LU = {'L': np.copy(L), 'U': np.copy(U)}
        # LUs.append(LU)
        if b is not None:
            steps, answer = SolveLU(L, U, b, steps, precision)
        print("########### Cholesky LU #############")
        print("L = \n", L)
        print("U = \n", U)
        print("B = \n", b)
        print("Answer = \n", answer)

        return LUs, steps, answer
    except Exception as e:
        print(e)
        return [],[NSPDM],answer


#####################################################################
matrix = np.array([[6, 15, 55],
                   [15, 55, 225],
                   [55, 225, 979]])
b = np.array([0, 0, 0])
LUs, steps, answer = Cholesky(matrix, b)
print('matrix = \n', matrix)
print('\nb = \n', b[:, np.newaxis])
print('=' * 80)
for i in range(len(LUs)):
        print(steps[i])
        print('=' * 80)
        print('L = \n', LUs[i]['L'])
        print('U = \n', LUs[i]['U'])
        print('=' * 80)
for i in range(len(LUs), len(steps)):
    print(i)
    print(steps[i])
    print('=' * 80)
if answer is not None:
    print('x = \n', answer['x'])
    print('y = \n', answer['y'])
    print('=' * 80)
