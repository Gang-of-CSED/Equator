import numpy as np

from my_functions import is_correct, is_diagonally_dominant, round_to_n_significant

def gauss_seidel_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    # Check if the input matrices are correct
    if not is_diagonally_dominant(coeff_matrix) or not is_correct(coeff_matrix, const_matrix, initial_values):
        return False

    # Initialize the solution vector and the list to store the iteration steps
    ans = np.array(initial_values).astype(float)
    steps_list = []

    # Round the input matrices to a certain number of significant digits
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)

    # Perform the Gauss-Seidel method for a certain number of iterations
    for k in range(num_iterations):
        # Store the previous values of the solution vector
        previous_values = ans.copy()

        # Update the solution vector using the Gauss-Seidel formula
        for i in range(ans.shape[0]):
            ans[i] = const_matrix[i]
            for j in range(coeff_matrix.shape[0]):
                if i != j:
                    ans[i] = round_to_n_significant(ans[i] - ans[j] * coeff_matrix[i][j], n)
            ans[i] = round_to_n_significant(ans[i] / coeff_matrix[i][i], n)

        # Calculate the relative approximation error and store it in the list
        relative_aprox_error = np.round(np.abs((ans - previous_values) / ans * 100), n)
        steps_list.append(np.column_stack((ans, relative_aprox_error)))

        # Check if the relative approximation error is below the specified tolerance
        if relative_aprox_error.max() <= tolarent_error:
            break

    # Return the list of iteration steps
    return np.array(steps_list)


#Examples:
b = np.array([10, 11, 3]) 
i = np.array([0, 0, 0])
a = np.array([[5, -1, 1],
              [2, 8, -1],
              [ -1, 1, 4]])

print("gauss_seidel_method:")
steps2 = gauss_seidel_method(a, b, i, 6, 5, 5)
for i in range(steps2.shape[0]):
    print(f"Iteration {i + 1}:")
    print("Values:")
    for j in range(steps2.shape[1]):
        print(steps2[i][j][0], "  ", end=' ')    
    print("\nRelative:")
    for j in range(steps2.shape[1]):
        print(steps2[i][j][1], "%  ", end=' ')
    print("\n")