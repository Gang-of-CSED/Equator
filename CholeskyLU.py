import numpy as np 
import math

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
    
    if not isSPDM(matrix):
        steps.append("Non Symmetric Positive Definite Matrices")
        return [],steps
    
    n = matrix.shape[0]
    L = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(i+1):
            sigma = 0 
            for k in range(j):
                sigma += L[i][k] * L[j][k]
                #sum_step = f"{L[i][k]}+{L[j][k]} "
                #steps.append(sum_step)
            
            if i == j:
                print(i,j,matrix[i][i],sigma,matrix[i][i] - sigma)
                L[i][j] = math.sqrt(matrix[i][j] - sigma)
                step = f"L[{i+1}][{j+1}] = sqrt(({matrix[i][i]}) - ({sigma})) = {L[i][j]}"
                steps.append(step)
            else:
                L[i][j] = (matrix[i][j] - sigma) / (L[j][j])
                step = f"L[{i+1}][{j+1}] = ({matrix[i][j]} - {sigma}) / ({L[j][j]}) = {L[i][j]}"
                steps.append(step)
    return L, steps

#####################################################################
matrix = np.array([[6,15, 55],
                   [15, 55, 225],
                   [55, 225, 979]])

L, steps = Cholesky(matrix)
for step in steps:
    print(step)
    print('-' * 50)
    
for row in L:
    print(row)







