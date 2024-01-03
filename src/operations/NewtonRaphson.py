import sympy as sp
from .Bisection import relative_error

def ModificationTwo(str_equation, x0, precision=5, eps=1e-5, max_iterations=50):
    x0 = sp.N(x0, precision)
    x = sp.symbols('x')
    equation = sp.N(sp.sympify(str_equation), precision)
    steps = []
    roots = []
    error = None
    errors = []
    
    if equation.subs(x, x0).evalf(n=precision) == 0:
        root = x0
        roots.append(root)
        step = (f"X0 = {x0}, X = {root} , f = 0, Relative Error = 0\nBEST CASE!!!!")
        steps.append(step)
        return error, roots, steps
    
    diff = sp.N(sp.diff(equation, x), precision)
    
    if diff == 0:
        error = "linear equation, has no roots"
        return error, roots, steps
    
    diff2 = sp.N(sp.diff(diff, x), precision)
    
    for i in range(max_iterations):

        f = sp.N(equation.subs(x, x0).evalf(), precision)
        f1 = sp.N(diff.subs(x, x0).evalf(), precision)
        
        if f1 == 0:
            error = "First derivative of equation becomes zero at " + (f"it: {i+1}")
            steps.append(error)
            break
        
        f2 = sp.N(diff2.subs(x, x0).evalf(), precision)
        
        root = sp.N((x0 - (f * f1) / (f1 ** 2 - f * f2)), precision)
        aRE = sp.N(relative_error(root, x0), precision)
        roots.append(root)
        step = (f"Iteration {i+1}:\nX0 = {x0}, X = {root} , f = {f}, f' = {f1}, f'' = {f2},\nX = {x0} - {f} * {f1} /  [{f1}]^2 - {f} * {f2}\nRelative Error = {aRE}")
        errors.append(aRE)
        
        if equation.subs(x, root).evalf(n=precision) == 0:
            step = step + (f"\nf({root}) = 0\n")
            steps.append(step)
            break
        if aRE < eps:
            step = step + (f"\nRelative Error {aRE} < {eps} so we stop")
            steps.append(step)
            break
        if roots.count(root) > 1:
            step = step + "\nMethod Starts Occilating at " + (f"it: {i}")
            steps.append(step)
            break
        if i == max_iterations - 1:
            step = step + (f"\nMaximum number of iterations reached {max_iterations}")
            
        steps.append(step)
        x0 = root

    if errors[-1] > errors[0]:
        steps[-1] = steps[-1] + ("\nMethod diverges")
    else:
        steps[-1] = steps[-1] + ("\nMethod converges")
    
    return error, roots, steps


def ModificationOne(str_equation, x0, m=1, precision=5, eps=1e-5, max_iterations=50):
    x0 = sp.N(x0, precision)
    x = sp.symbols('x')
    equation = sp.N(sp.sympify(str_equation), precision)
    steps = []
    roots = []
    error = None
    errors = []
    
    if equation.subs(x, x0).evalf(n=precision) == 0:
        root = x0
        roots.append(root)
        step = (f"X0 = {x0}, X = {root} , f = 0, Relative Error = 0\nBEST CASE!!!!")
        steps.append(step)
        return error, roots, steps

    diff = sp.N(sp.diff(equation, x), precision)
    
    if diff == 0:
        error = "linear equation, has no roots"
        return error, roots, steps
    
    for i in range(max_iterations):

        f = sp.N(equation.subs(x, x0).evalf(), precision)
        f1 = sp.N(diff.subs(x, x0).evalf(n=precision), precision)
        
        if f1 == 0:
            error = "First derivative of equation becomes zero at " + (f"it: {i+1}")
            steps.append(error)
            break
        
        root = sp.N((x0 - m * (f / f1)), precision)
        roots.append(root)
        aRE = sp.N(relative_error(root, x0), precision)
        step = (f"Iteration {i+1}:\nX0 = {x0}, X = {root} , f = {f}, f' = {f1},\nX = {x0} - {m} * {f} / {f1}\nRelative Error = {aRE}")
        errors.append(aRE)

        if equation.subs(x, root).evalf(n=precision) == 0:
            step = step + (f"\nf({root}) = 0\n")
            steps.append(step)
            break
        if aRE < eps:
            step = step + (f"\nRelative Error {aRE} < {eps} so we stop")
            steps.append(step)
            break
        if roots.count(root) > 1:
            step = step + "\nMethod Starts Occilating at " + (f"it: {i}")
            steps.append(step)
            break
        
        steps.append(step)
        x0 = root

    if errors[-1] > errors[0]:
        steps[-1] = steps[-1] + ("\nMethod diverges")
    else:
        steps[-1] = steps[-1] + ("\nMethod converges")
    
    return error, roots, steps

## main function
if __name__ == '__main__':
    
    test_cases = [
        ("-0.9*x**2 + 1.7*x + 2.5", 5, 1, 7, 0.0001, 50),  # root multiplicity: 1
        ("x**3-5*x**2+7*x-3", 0, 2, 7, 0.0001, 50),  # root multiplicity: 1
        # ("x**3 - x**2 + 2", -20, 1, 5, 1e-6, 200),  # root multiplicity: 1
        # ("x**4 - 3*x**3 + 2", 1, 1, 6, 1e-6, 200),  # root multiplicity: 1
        # ("x**5 - 11*x**4 + 46*x**3 - 90*x**2 + 81*x - 27", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
        # ("x**2 - 4", 5, 2, 5, 1e-6, 200),  # root multiplicity: 2
        # ("x**3 - 2*x - 5", 5, 1, 6, 1e-6, 200),  # root multiplicity: 1
        # ("x**3 - 3*x**2 + 2*x - 1", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
        # ("x**4 - 4*x**3 + 6*x**2 - 4*x + 1", 5, 1, 5, 1e-6, 200),  # root multiplicity: 1
        # ("x**5 - 5*x**4 + 10*x**3 - 10*x**2 + 5*x - 1", 5, 1, 6, 1e-6, 200),  # root multiplicity: 1
        # ("x**6 - 6*x**5 + 15*x**4 - 20*x**3 + 15*x**2 - 6*x + 1", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
        # ("x + 2", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
        # ("10", 5, 0, 4, 1e-6, 200),  # root multiplicity: 0 (constant function)
        # ("sin(x) + x", 1, 1, 5, 1e-5, 50),
        # ("(exp(x) * exp(x)) - 1", 1, 1, 5, 1e-5, 50)
    ]

    for i, (str_equation, x0, m, precision, eps, max_iterations) in enumerate(test_cases, 1):
        print(f"Test case {i}: {str_equation}")
        # x = sp.symbols('x')
        # equation = sp.N(sp.sympify(str_equation), precision)
        # rootss = sp.solve(equation, x)
        # roots = [root.evalf(precision) for root in rootss]
        # print(f"\nThe true roots of the equation is {roots}\n")
        
        error1, roots1, steps1 = ModificationOne(str_equation, x0, m, precision, eps, max_iterations)
        print("modification one", error1 ,"\n", roots1 ,"\n" , steps1 ,"\n")

        error2, roots2, steps2 = ModificationTwo(str_equation, x0, precision, eps, max_iterations)
        print("modification two", error2 ,"\n", roots2 ,"\n" , steps2 ,"\n\n\n")
       
