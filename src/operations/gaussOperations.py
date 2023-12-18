import numpy as np
import sympy as sp

def round_to_n_significant(x, n=5):
    def round_element(val):
        if np.isclose(val, 0):
            return 0
        return round(val, -int(np.floor(np.log10(np.abs(val)))) + (n - 1))
    return np.vectorize(round_element)(x)

def isconsistent(cof_matrix,aug_matrix):
    return np.linalg.matrix_rank(cof_matrix)==np.linalg.matrix_rank(aug_matrix)

def upperAug(cof_matrix, const_matrix,significantD=5):
    steps = []
    n = len(const_matrix)
    # aug_matrix = np.hstack((cof_matrix, const_matrix))
    aug_matrix = np.hstack((cof_matrix, const_matrix)).astype(np.float64)
    aug_matrix=round_to_n_significant(aug_matrix,significantD).astype(np.float64)
    for i in range(n):

        # Partial Pivoting with scalling 
        scaledAug = aug_matrix.copy()
        #scalling on the aug matrix just to determine the pivot 
        for x in range(n):
            largestCoeff = max(abs(scaledAug[x, :n]))
            if largestCoeff != 0:
                
                
                scaledAug[x, :] /= largestCoeff
                for z in range (n+1):
                
                 scaledAug[x][z]=round_to_n_significant(scaledAug[x][z],significantD)
                 

        step = {"message": f"Matrix after scaling (just to choose the pivot)" , "output": scaledAug.copy()}
        steps.append(step)
        # Now find the pivot using the scaled matrix
        max_row = i
        for j in range(i + 1, n):
            if abs(scaledAug[j][i]) > abs(scaledAug[max_row][i]):
                max_row = j

        if i != max_row:
            aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]]
            step = {"message": f"Swapping R{i + 1} with R{max_row + 1}" , "output": aug_matrix.copy()}

            steps.append(step)
        else :
            step = {"message": "we already have  the correct pivot " , "output": aug_matrix.copy()}
            steps.append(step)

        for j in range(i + 1, n):

            if aug_matrix[i][i] != 0 and aug_matrix[j][i] != 0 :

                factor = round_to_n_significant(aug_matrix[j][i] / aug_matrix[i][i],significantD)
                for x in range (n+1):
                            
                    aug_matrix[j][x] -=round_to_n_significant(factor * aug_matrix[i][x],significantD)   
                    aug_matrix[j][x]=  round_to_n_significant(aug_matrix[j][x],significantD)          

                step = {"message": f"R{j + 1} <- R{j + 1} - {factor}*R{i + 1}", "output": aug_matrix.copy()}
                steps.append(step)
            elif steps:#delete the last 2 steps if the element is zero already 
             steps.pop()    
             steps.pop()    
    return steps, aug_matrix

import sympy as sp

def backSubstitutions(aug_matrix, significantD=5):
    aug_matrix = round_to_n_significant(aug_matrix, significantD)

    n = len(aug_matrix)
    answer = ['None']*n  # Initialize with SymPy zeros
    steps = []

    param_counter = 1
    for i in range(n-1, -1, -1):
        accumelator = sp.S.Zero

        # if the coefficient is 0, it indicates infinite solutions
        if aug_matrix[i][i] == 0:
            param_name = 't{}'.format(param_counter)
            answer[i] = sp.symbols(param_name)
            param_counter += 1
            step = {"message": "Back substitutions (infinite solutions)", "output": answer.copy()}
            steps.append(step)
            continue

        for j in range(i + 1, n):
            if aug_matrix[i][j] != 0:
                accumelator += sp.N(answer[j] * aug_matrix[i][j],n=significantD)
                accumelator=sp.N(accumelator,n=significantD)
        # Simplify the expression
        accumelator = sp.simplify(accumelator)

        if aug_matrix[i][i] != 0:
            answer[i] = sp.N((aug_matrix[i][n] - accumelator),significantD) / aug_matrix[i][i]
            answer[i]=sp.N(answer[i],significantD)
            answer[i] = sp.simplify(answer[i])

        step = {"message": "Back substitutions", "output": answer.copy()}
        steps.append(step)

    return steps, answer
     
def gauss_elimination(cof_matrix, const_matrix,significantD=5):#returns 3 values isSolveAble,answer,steps 
    
    #get the upper triabgle matrix 
    steps,aug_matrix=upperAug(cof_matrix, const_matrix,significantD)
   
    if not isconsistent(cof_matrix,aug_matrix):
           return False,[],steps
    
    steps2,answer=backSubstitutions(aug_matrix,significantD)

    for step in steps2:
     steps.append(step)

    return True,answer,steps
      
def gauss_Jordan(cof_matrix, const_matrix,significantD=5):
   
    n=len(const_matrix)
    steps,aug_matrix=upperAug(cof_matrix, const_matrix,significantD)
       
    if not isconsistent(cof_matrix,aug_matrix):
           return False,[],steps

    for i in range(n-1,-1,-1):
        
        #avoid division by 0
        if(aug_matrix[i][i]==0 or aug_matrix[i][i]==1):
            continue

        #making the pivot =1
        temp=aug_matrix[i][i] 
        aug_matrix[i]/=aug_matrix[i][i]
        aug_matrix = round_to_n_significant(aug_matrix,significantD)

        step = {"message":f"R{i+1} <- R{i+1} /{temp} ", "output": aug_matrix.copy()}
        steps.append(step)
       
        # aug_matrix = round_to_n_significant(aug_matrix,significantD)
        #eleminating elemnts above
        for j in range(i-1,-1,-1):

            if(aug_matrix[i][i]==0):
              continue 

            factor = (round_to_n_significant(aug_matrix[j][i] / aug_matrix[i][i],significantD))
            # print(aug_matrix)
            for x in range (n+1):
             aug_matrix[j][x] -=round_to_n_significant(factor * aug_matrix[i][x],significantD)
             aug_matrix[j][x]=round_to_n_significant(aug_matrix[j][x],significantD)

            step = {"message":f"R{j+1} <- R{j+1} - {factor}*R{i+1}", "output": aug_matrix.copy()}
            steps.append(step)
       
    steps2,answer=backSubstitutions(aug_matrix,significantD)

    for step in steps2:
      steps.append(step)
  
    return True,answer,steps   

if __name__ == '__main__':
    cof_matrix = np.array(
   [[0,2,3],[4,5,6],[7,8,9]]
    )
    const_matrix = np.array(
        [[6],
         [19],
         [31]]
        )
  
    issolvabe,answer,steps = gauss_elimination(cof_matrix, const_matrix,6)

    for step in steps:
        print("\n")
        print(step["message"])
        print(step["output"])


