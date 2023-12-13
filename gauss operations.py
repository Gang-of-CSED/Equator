import numpy as np
import sympy as sp


def isconsestent(cof_matrix,aug_matrix):
    return np.linalg.matrix_rank(cof_matrix)==np.linalg.matrix_rank(aug_matrix)

def upperAug(cof_matrix, const_matrix):
    steps = []
    n = len(const_matrix)
    aug_matrix = np.hstack((cof_matrix, const_matrix)).astype(np.float64)
    
    for i in range(n):

        # Partial Pivoting with scalling 
        #scalling on the aug matrix just to determine the pivot 
        scaledAug = aug_matrix.copy()
        for x in range(n):
            largestCoeff = max(abs(scaledAug[x, :n]))
            if largestCoeff != 0:
                scaledAug[x, :] /= largestCoeff

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


        for j in range(i + 1, n):
            if aug_matrix[i][i] != 0:
                factor = aug_matrix[j][i] / aug_matrix[i][i]
                aug_matrix[j] = aug_matrix[j] - factor * aug_matrix[i]

                aug_matrix[j][abs(aug_matrix[j]) < np.exp(-10)] = 0.0


            
                step = {"message": f"R{j + 1} <- R{j + 1} - {factor:.6f}*R{i + 1}", "output": aug_matrix.copy()}
                steps.append(step)

    return steps, aug_matrix

def gauss_elimination(cof_matrix, const_matrix):#returns 3 values isSolveAble,answer,steps 
    
    n=len(const_matrix)
    answer=[0]*n
    
    steps,aug_matrix=upperAug(cof_matrix, const_matrix)
    if not isconsestent(cof_matrix,aug_matrix):
           return False,answer,steps
    

    param_counter = 1

    for i in range(n-1,-1,-1):
      isInfiniteSolns=False
      stringAccumelator=""
      accumelator=0
    
      if(aug_matrix[i][i]==0):
          answer[i]='t'+str(param_counter)
          param_counter+=1
          step = {"message": "Back substitutions", "output": f"X{i+1}={answer[i]}"}
          steps.append(step)
          continue
      

      for j in range(i+1,n):
        if isinstance(answer[j], str) or isInfiniteSolns :
            isInfiniteSolns=True
            stringAccumelator+=answer[j]+'*'+str(aug_matrix[i][j])
        else:  
         accumelator+=answer[j]*aug_matrix[i][j]

      if(isInfiniteSolns): 
        answer[i]= str(aug_matrix[i][n])+ '-' +stringAccumelator +'/'+ str(aug_matrix[i][i])
      else: 
       answer[i]= (aug_matrix[i][n] - accumelator) / aug_matrix[i][i]
      step = {"message": "Back substitutions", "output": f"X{i+1}={answer[i]}"}
      steps.append(step)
       

    return True,answer,steps

def gauss_Jordan(cof_matrix, const_matrix):
   
    n=len(const_matrix)
    answer=[0]*n
    steps,aug_matrix=upperAug(cof_matrix, const_matrix)
       
    if not isconsestent(cof_matrix,aug_matrix):
           return False,answer,steps
    
    for i in range(n-1,-1,-1):

        if(aug_matrix[i][i]==0):
                    continue 
        
        aug_matrix[i]/=aug_matrix[i][i]
        step = {"message":f"R{i+1} <- R{i+1} /{aug_matrix[i][i]} ", "output": aug_matrix.copy()}
        steps.append(step)
       
        

        #eleminating elemnts above

        for j in range(i-1,-1,-1):

            if(aug_matrix[i][i]==0):
              continue 

            factor = aug_matrix[j][i] / aug_matrix[i][i]
            aug_matrix[j] = aug_matrix[j] - factor * aug_matrix[i]
            step = {"message":f"R{j+1} <- R{j+1} - {factor}*R{i+1}", "output": aug_matrix.copy()}
            steps.append(step)
       
     

    #get the solutions (handle if their infinite number of solution )
    param_counter = 1
    for i in range(n-1,-1,-1):
      isInfiniteSolns=False
      stringAccumelator=""
      accumelator=0
    
      if(aug_matrix[i][i]==0):
          answer[i]='t'+str(param_counter)
          param_counter+=1
          step = {"message": "Back substitutions", "output": f"X{i+1}={answer[i]}"}
          steps.append(step)
          continue
      

      for j in range(i+1,n):
        if isinstance(answer[j], str) or isInfiniteSolns :
            isInfiniteSolns=True
            stringAccumelator+=answer[j]+'*'+str(aug_matrix[i][j])
        else:  
         accumelator+=answer[j]*aug_matrix[i][j]

      if(isInfiniteSolns): 
        answer[i]= str(aug_matrix[i][n])+ '-' +stringAccumelator +'/'+ str(aug_matrix[i][i])
      else: 
       answer[i]= (aug_matrix[i][n] - accumelator) / aug_matrix[i][i]
      step = {"message": "Back substitutions", "output": f"X{i+1}={answer[i]}"}
      steps.append(step) 
  
    return True,answer,steps   




cof_matrix = np.array(
 [[2, 3, -1], [1, -3, 2], [3, -1, -1]]
 )
const_matrix = np.array(
    [[5], [1], [4]]
    )


issolvabe,answer,steps = gauss_Jordan(cof_matrix, const_matrix)

for step in steps:
    print("\n")
    print(step["message"])
    print(step["output"])


