import numpy as np

def round_to_n_significant(x, n):
    def round_element(val):
        if np.isclose(val, 0):
            return 0
        return round(val, -int(np.floor(np.log10(np.abs(val)))) + (n - 1))
    return np.vectorize(round_element)(x)


def is_correct(coeff_matrix, const_matrix, initial_values):
    return (coeff_matrix.shape[0] == coeff_matrix.shape[1] == initial_values.shape[0] == const_matrix.shape[0] and np.all(np.diag(coeff_matrix) != 0))

def is_diagonally_dominant(coeff_matrix):
    comparison_result = np.subtract(np.multiply(np.diag(coeff_matrix), 2), np.sum(coeff_matrix, axis=1))
    return (np.all(comparison_result >= 0) and np.any(comparison_result > 0))

def gacobi_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    if(not is_correct(coeff_matrix, const_matrix, initial_values)):
        return False
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)
    D_inv = round_to_n_significant(np.linalg.inv(np.diag(np.diag(coeff_matrix))), n)
    ans = np.array(initial_values).astype(float)    
    np.fill_diagonal(coeff_matrix, 0)
    steps_list = []
    for i in range(num_iterations):
        previous_values = ans.copy()
        ans = round_to_n_significant(np.matmul(D_inv, round_to_n_significant(const_matrix - (round_to_n_significant(np.matmul(coeff_matrix, ans), n)), n)), n)
        relative_aprox_error = np.round(np.abs((((ans - previous_values)/ans)*100)), n)
        steps_list.append(np.column_stack((ans, relative_aprox_error)))
        if(relative_aprox_error.max() <= tolarent_error): break
    return np.array(steps_list)


def gauss_seidel_method(coeff_matrix, const_matrix, initial_values, num_iterations, tolarent_error, n):
    if(not is_diagonally_dominant(coeff_matrix) or not is_correct(coeff_matrix, const_matrix, initial_values)):
        return False
    steps_list = []
    ans = np.array(initial_values).astype(float)
    coeff_matrix = round_to_n_significant(coeff_matrix, n)
    const_matrix = round_to_n_significant(const_matrix, n)
    for k in range(num_iterations):
        previous_values = ans.copy()
        for i in range(ans.shape[0]):
            ans[i] = const_matrix[i]
            for j in range(coeff_matrix.shape[0]):
                if(i != j): ans[i] = round_to_n_significant((ans[i] - (round_to_n_significant(ans[j]*coeff_matrix[i][j], n))), n)
            ans[i] = round_to_n_significant((ans[i]/coeff_matrix[i][i]), n)
        relative_aprox_error = np.round(np.abs((((ans - previous_values)/ans)*100)), n)
        steps_list.append(np.column_stack((ans, relative_aprox_error)))
        if(relative_aprox_error.max() <= tolarent_error): break
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