import numpy as np

from .utils import is_correct, round_to_n_significant

def gacobi_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    steps_list, comments, flag = [], [], True
    # Check if the given input is correct
    if not is_correct(coeff_matrix, const_matrix, initial_values):
        flag = False
        return flag, steps_list, comments
    # Round the coefficient and constant matrices to the given number of significant digits
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)
    # Calculate the inverse of the diagonal matrix of the coefficient matrix
    D_inv = round_to_n_significant(np.linalg.inv(np.diag(np.diag(coeff_matrix))), n)
    # Initialize the solution vector with the given initial values
    ans = np.array(initial_values).astype(float)
    # Fill the diagonal elements of the coefficient matrix with zeros
    np.fill_diagonal(coeff_matrix, 0)
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
        if (relative_aprox_error.max() < tolarent_error):
            comments.append(f"(max relative approximate error) {relative_aprox_error.max()} % < {tolarent_error} % (tolarent error)\n No need to more iterations")
            break
        comments.append(f"(max relative approximate error) {relative_aprox_error.max()} % > {tolarent_error} % (tolarent error)")
    # Return the list of iteration steps
    return flag, steps_list, comments



#Examples:
if __name__ == "__main__":
    b = np.array([10, 11, 3]) 
    i = np.array([0, 0, 0])
    a = np.array([[5, -1, 1],
                [2, 8, -1],
                [ -1, 1, 4]])

    print("gacobi_method:")
    flag, steps, comments = gacobi_method(a, b, i, 6, 5, 5)
    for i, iteration in enumerate(steps):
        print(f"Iteration {i + 1}:")
        print("Values:")
        for value in iteration[0]:
            print(value, end='   ')    
        print("\nRelative errors:")
        for error in iteration[1]:
            print(error, end='   ')
        print("\n", comments[i], "\n")