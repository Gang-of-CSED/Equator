import numpy as np

def relative_error(x, x0):
    """
    :return: relative error
    """
    if x == None:
        return 1e10
    if x == x0:
        return 0
    if x == 0:
        return 1e10
    return abs(x - x0) / abs(x)


# Function to round all the elements of an array to a given number of significant digits
def round_to_n_significant(x, n):
    # Define a function to round each element of the array
    def round_element(val):
        # Check if the value is close to zero
        if np.isclose(val, 0):
            # Return zero if it is close to zero
            return 0
        # Use round function to round the value to the given number of significant digits
        return round(val, -int(np.floor(np.log10(np.abs(val)))) + (n - 1))
    # Use vectorize function to apply the round_element function to all the elements of the array
    return np.vectorize(round_element)(x)


# Function to check if the given coefficient and constant matrices and initial values are correct
def is_correct(coeff_matrix, const_matrix, initial_values):
    # Check if the shapes of the coefficient and constant matrices are correct
    if (coeff_matrix.shape[0] == coeff_matrix.shape[1] == initial_values.shape[0] == const_matrix.shape[0]):
        # Check if the diagonal elements of the coefficient matrix are all not zero
        if np.all(np.diag(coeff_matrix) != 0):
            # Return true if the shapes are correct and all the diagonal elements are not zero
            return True
    # Return false if the shapes are not correct or all the diagonal elements are zero
    return False


# # Function to check if the given coefficient matrix is diagonally dominant
# def is_diagonally_dominant(coeff_matrix):
#     # Calculate the comparison result by subtracting the product of the diagonal elements and 2 from the sum of the elements along the diagonal
#     comparison_result = np.subtract(np.multiply(np.diag(coeff_matrix), 2), np.sum(coeff_matrix, axis=1))
#     # Check if all the elements in the comparison result are greater than or equal to zero
#     if (np.all(comparison_result >= 0) and np.any(comparison_result > 0)):
#         # Return true if there are elements greater than zero
#         return True
#     # Return false if there are no elements greater than zero
#     return False