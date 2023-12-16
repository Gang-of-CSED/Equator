import numpy as np

from my_functions import is_correct, is_diagonally_dominant, round_to_n_significant

def gacobi_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    # Check if the given input is correct
    if (not is_correct(coeff_matrix, const_matrix, initial_values)):
        # Return false if the input is not correct
        return False
    # Round the coefficient and constant matrices to the given number of significant digits
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)
    # Check if the coefficient matrix is diagonally dominant
    if (not is_diagonally_dominant(coeff_matrix)):
        # Return false if the coefficient matrix is not diagonally dominant
        return False
    # Calculate the inverse of the diagonal matrix of the coefficient matrix
    D_inv = round_to_n_significant(np.linalg.inv(np.diag(np.diag(coeff_matrix))), n)
    # Initialize the solution vector with the given initial values
    ans = np.array(initial_values).astype(float)
    # Fill the diagonal elements of the coefficient matrix with zeros
    np.fill_diagonal(coeff_matrix, 0)
    # Initialize a list to store the solution steps
    steps_list = []
    # Loop through all the iterations
    for i in range(num_iterations):
        # Store the previous values of the solution vector
        previous_values = ans.copy()
        # Calculate the new values of the solution vector using the Gauß-Seidel formula
        ans = round_to_n_significant(np.matmul(D_inv, round_to_n_significant(const_matrix - (round_to_n_significant(np.matmul(coeff_matrix, ans), n)), n)), n)
        # Calculate the relative approximation error
        relative_aprox_error = np.round(np.abs((((ans - previous_values)/ans)*100)), n)
        # Add the current values of the solution vector and the relative approximation error to the list
        steps_list.append(np.column_stack((ans, relative_aprox_error)))
        # Check if the maximum relative approximation error is less than or equal to the given tolerance
        if (relative_aprox_error.max() <= tolarent_error):
            # Return the list of solution steps if the maximum relative approximation error is less than or equal to the given tolerance
            return np.array(steps_list)
        
#Examples:
b = np.array([10, 11, 3]) 
i = np.array([0, 0, 0])
a = np.array([[5, -1, 1],
              [2, 8, -1],
              [ -1, 1, 4]])

print("gacobi_method:")
steps = gacobi_method(a, b, i, 6, 5, 5)
for i in range(steps.shape[0]):
    print(f"Iteration {i + 1}:")
    print("Values:")
    for j in range(steps.shape[1]):
        print(steps[i][j][0], "  ", end=' ')    
    print("\nRelative:")
    for j in range(steps.shape[1]):
        print(steps[i][j][1], "%  ", end=' ')
    print("\n")