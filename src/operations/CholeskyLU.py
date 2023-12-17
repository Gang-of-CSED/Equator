import numpy as np 
import math

def getU(L):
    if L==[]: return[]
    n = matrix.shape[0]
    U = [[0.0] * n for i in range(n)]
    for i in range (n):
        for j in range(n):
            U[i][j] = L[j][i]
    return U

def isPDM(matrix):
    n = matrix.shape[0]
    for i in range(n):
        if(matrix[i][i] <= 0):
            return False
    return True

def isSymmetric(matrix):
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
    return (isSymmetric(matrix) and isPDM(matrix))
    

def Cholesky(matrix):
    steps = []
    NSPDM = "Non Symmetric Positive Definite Matrices"
    if not isSPDM(matrix):
        return [],[NSPDM]
    try:
        n = matrix.shape[0]
        L = [[0.0] * n for i in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                sigma = 0 
                for k in range(j):
                    sigma += L[i][k] * L[j][k]
                
                if i == j:
                    L[i][j] = math.sqrt(matrix[i][j] - sigma)
                    step = f"L[{i+1}][{j+1}] = sqrt(({matrix[i][i]}) - ({sigma})) = {L[i][j]}"
                    steps.append(step)
                else:
                    if(L[j][j] == 0): return [],["ERROR Dividing by ZERO"]
                    L[i][j] = (1.0 / L[j][j]) * (matrix[i][j] - sigma)
                    step = f"L[{i+1}][{j+1}] = ({matrix[i][j]} - {sigma}) / ({L[j][j]}) = {L[i][j]}"
                    steps.append(step)
        return L, steps
    except:
        return [],[NSPDM]


#####################################################################
matrix = np.array([[1, 1, 1],
                   [1, 2, 1],
                   [1, 1, 1]])

L, steps = Cholesky(matrix)
for step in steps:
    print(step)
    print('-' * 50)
    
for row in L:
    print(row)
print('*' * 50)    
for row in getU(L):
    print(row)








