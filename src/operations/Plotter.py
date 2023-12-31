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

def click_points(plt, function_str, num_clicked_points=2):
    points = []
    old_title = plt.gca().get_title()
    plt.title(f"Click {num_clicked_points} points on the function line")
    plt.show(block=False)

    x = sp.symbols('x')
    expr = sp.sympify(function_str)
    func = sp.lambdify(x, expr, 'numpy')

    def on_click(event):
        nonlocal points

        if event.xdata is not None:
            x_clicked = event.xdata

            # Find the y-value on the function line for the clicked x-coordinate
            y_clicked = func(x_clicked)

            points.append((x_clicked, y_clicked))
            print(f"Clicked at (x, y) = ({x_clicked:.2f}, {y_clicked:.2f}) on the function line")

            # Annotate the clicked points on the graph with their x-values
            plt.annotate(f'x={x_clicked:.4f}', (x_clicked, y_clicked), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')
            plt.scatter(x_clicked, y_clicked, color='black', marker='x')
            if len(points) == num_clicked_points:
                plt.gcf().canvas.mpl_disconnect(cid)
                print(f"{num_clicked_points} points clicked. Returning array:", points)

    if num_clicked_points > 0:
        cid = plt.gcf().canvas.mpl_connect('button_press_event', on_click)

    while len(points) < num_clicked_points:
        plt.pause(0.1)
    plt.title(old_title)
    plt.pause(0.5)
    return points

def plot_function(function_str, num_points=100000, x_range=(-10, 10)):

    if is_valid_function(function_str) is False:
        print(f"Error: {function_str} is not a valid function")
        return "Invalid function", None, None
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
        # Create a figure
        fig, ax = plt.subplots()
        # Plot the function
        ax.plot(x_vals, y_vals, label='f(x)')
        # Mark points where y = 0
        ax.scatter(zero_points, np.zeros_like(zero_points), color='red', label='y=0 points')
        # Display x-coordinates on the right outside the graph
        zero_points_str = '\n'.join([f'x{i} = {x:.2f}' for i, x in enumerate(zero_points, start=1)])
        ax.legend([f'f(x)', f'y=0 points:\n{zero_points_str}'], loc='upper left', bbox_to_anchor=(1, 1))
        ax.set_title(f'Plot of {function_str}')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        # Add x-axis line
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)  
        ax.grid(True)
        fig.tight_layout()
    except Exception as e:
        print(f"Error: {e}")
        return "Invalid function", None, None
    return None, fig,ax

if __name__ == "__main__":
    function_string = "x**4 - 3*x**2 + sin(2*x)+exp(-x**2) + 1"
    error, fig = plot_function(function_string, num_points=100000, x_range=(-2, 2))
    if error is None:
        points = click_points(plt, function_string, num_clicked_points=2)
        print(points)
    else:
        print(error)
    plt.show()
