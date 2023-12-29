import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def is_valid_function(function_str):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(function_str)
        # we may need to comment this next line if lambdify is not working
        func = sp.lambdify(x, expr, 'numpy')
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def plot_function(function_str, num_points=100000, x_range=(-10, 10)):

    if is_valid_function(function_str) is False:
        print(f"Error: {function_str} is not a valid function")
        return "Invalid function"
    try:
        x = sp.symbols('x')
        expr = sp.sympify(function_str)

        # Lambdify the expression for numerical evaluation (under testing)
        # if it is not working use the commented line below
        # y_vals = expr.subs(x, x_val)

        func = sp.lambdify(x, expr, 'numpy')
        # Generate x values
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        # Evaluate the function
        y_vals = func(x_vals)
        # Find points where y = 0
        zero_points = x_vals[np.where(np.diff(np.sign(y_vals)))[0]]
        # Plot the function
        plt.plot(x_vals, y_vals, label='f(x)')
        # Mark points where y = 0
        plt.scatter(zero_points, np.zeros_like(zero_points), color='red', label='y=0 points')
        # Display x-coordinates on the right outside the graph
        zero_points_str = '\n'.join([f'x{i} = {x:.2f}' for i, x in enumerate(zero_points, start=1)])
        plt.legend([f'f(x)', f'y=0 points:\n{zero_points_str}'], loc='upper left', bbox_to_anchor=(1, 1))
        plt.title(f'Plot of {function_str}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        # Add x-axis line
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)  
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return "Invalid function"
    return None

# Example usage
function_string = "x**4 - 3*x**2 + sin(2*x)+exp(-x**2) + 1"
error = plot_function(function_string, num_points=100000, x_range=(-2, 2))
print(error)
