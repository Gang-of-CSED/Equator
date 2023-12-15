# Import the necessary libraries
import numpy as np

# Define the round_to_n_significant function
def round_to_n_significant(x, n):
    """
    This function rounds each element of a numpy array to n significant figures.
    """
    # Define the round_element function
    def round_element(val):
        if np.isclose(val, 0):
            return 0
        return round(val, -int(np.floor(np.log10(np.abs(val)))) + (n - 1))

    # Apply the vectorized function to the array
    return np.vectorize(round_element)(x)


# Define the is_correct function
def is_correct(coeff_matrix, const_matrix, initial_values):
    """
    This function checks if the input matrices have the correct dimensions and if the diagonal elements of the coefficient matrix are not all zero.
    """
    # Check if the input matrices have the correct dimensions
    if (coeff_matrix.shape[0] == coeff_matrix.shape[1] == initial_values.shape[0] == const_matrix.shape[0] and np.all(np.diag(coeff_matrix) != 0)):
        # Return True if the input matrices are correct
        return True
    # Return False if the input matrices are incorrect
    return False


# Define the is_diagonally_dominant function
def is_diagonally_dominant(coeff_matrix):
    """
    This function checks if the diagonal elements of the input matrix are greater than or equal to the sum of the off-diagonal elements.
    """
    # Calculate the comparison result
    comparison_result = np.subtract(np.multiply(np.diag(coeff_matrix), 2), np.sum(coeff_matrix, axis=1))

    # Check if all elements in the comparison result are greater than or equal to zero
    if (np.all(comparison_result >= 0)):
        # Check if there are any positive elements in the comparison result
        if (np.any(comparison_result > 0)):
            # Return True if the matrix is diagonally dominant
            return True
    # Return False if the matrix is not diagonally dominant
    return False


# Define the gauß-seidel_method function
def gauß_seidel_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    """
    This function implements the Gauss-Seidel method for solving a system of linear equations.
    """
    # Check if the input matrices are correct
    if (not is_correct(coeff_matrix, const_matrix, initial_values)):
        # Return False if the input matrices are incorrect
        return False

    # Round the input matrices to n significant figures
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)

    # Calculate the inverse of the diagonal matrix
    D_inv = round_to_n_significant(np.linalg.inv(np.diag(np.diag(coeff_matrix))), n)

    # Initialize the solution vector with the initial values
    ans = np.array(initial_values).astype(float)

    # Create a list to store the solution steps
    steps_list = []

    # Iterate through the specified number of iterations
    for i in range(num_iterations):
        # Store the previous values
        previous_values = ans.copy()

        # Calculate the next solution vector
        ans = round_to_n_significant(np.matmul(D_inv, round_to_n_significant(const_matrix - (round_to_n_significant(np.matmul(coeff_matrix, ans), n)), n)), n)

        # Calculate the relative approximation error
        relative_aprox_error = np.round(np.abs((((ans - previous_values)/ans)*100)), n)

        # Store the solution step in the list
        steps_list.append(np.column_stack((ans, relative_aprox_error)))

        # Check if the maximum relative approximation error is less than the specified tolerance
        if (relative_aprox_error.max() <= tolarent_error):
            # Return the solution steps list if the maximum relative approximation error is less than the specified tolerance
            return np.array(steps_list)


# Define the gauss_seidel_method function
def gauss_seidel_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    """
    This function implements the Gauss-Seidel method for solving a system of linear equations.
    """
    # Check if the matrix is diagonally dominant and if the input matrices are correct
    if (not is_diagonally_dominant(coeff_matrix) or not is_correct(coeff_matrix, const_matrix, initial_values)):
        # Return False if the matrix is not diagonally dominant or the input matrices are incorrect
        return False

    # Create a list to store the solution steps
    steps_list = []

    # Initialize the solution vector with the initial values
    ans = np.array(initial_values).astype(float)

    # Round the input matrices to n significant figures
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)

    # Iterate through the specified number of iterations
    for k in range(num_iterations):
        # Store the previous values
        previous_values = ans.copy()

        # Iterate through each element in the solution vector
        for i in range(ans.shape[0]):
            # Calculate the next element of the solution vector
            ans[i] = const_matrix[i]
            for j in range(coeff_matrix.shape[0]):
                # Update the ith element of the solution vector based on the jth element of the coefficient matrix
                if (i != j): ans[i] = round_to_n_significant((ans[i] - (round_to_n_significant(ans[j]*coeff_matrix[i][j], n))), n)
            # Update the ith element of the solution vector based on the ith element of the diagonal matrix
            ans[i] = round_to_n_significant((ans[i]/coeff_matrix[i][i]), n)

        # Calculate the relative approximation error
        relative_aprox_error = np.round(np.abs((((ans - previous_values)/ans)*100)), n)

        # Store the solution step in the list
        steps_list.append(np.column_stack((ans, relative_aprox_error)))

        # Check if the maximum relative approximation error is less than the specified tolerance
        if (relative_aprox_error.max() <= tolarent_error):
            # Return the solution steps list if the maximum relative approximation error is less than the specified tolerance
            return np.array(steps_list)


# Examples:
# Create some example matrices and vectors
b = np.array([10, 11, 3])  # Right-hand side vector
i = np.array([0, 0, 0])    # Initial guess vector
a = np.array([[5, -1, 1],
                [2, 8, -1],
                [ -1, 1, 4]])  # Coefficient matrix

# Solve the system of linear equations using the Gauss-Seidel method with 6 iterations and a tolerance of 5%
print("gauss_seidel_method:")
steps2 = gauss_seidel_method(a, b, i, 6, 5, 5)

# Print the solution steps
for i in range(steps2.shape[0]):
    print(f"Iteration {i + 1}:")
    print("Values:")
    for j in range(steps2.shape[1]):
        print(steps2[i][j][0], "  ", end=' ')     # Print the values
    print("\nRelative:")
    for j in range(steps2.shape[1]):
        print(steps2[i][j][1], "%  ", end=' ')  # Print the relative approximation errors
    print("\n")