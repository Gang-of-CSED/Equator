import sympy as sp

def ModificationTwo(str_equation, x0, precision=5, eps=1e-5, max_iterations=50):
    x = sp.symbols('x')
    equation = sp.N(sp.sympify(str_equation), precision)
    steps = []
    roots = []
    error = None
    
    diff = sp.diff(equation, x)
    if diff == 0:
        error = "linear equation, has no roots"
        steps.append(error)
        return error, roots, steps
    
    diff2 = sp.diff(diff, x)
    
    for i in range(max_iterations):
        root = 0
        f = equation.evalf(subs={x: x0}, n=precision)
        # f = equation.subs(x, x0)
        f1 = diff.evalf(subs={x: x0}, n=precision)
        # f1 = diff.subs(x, x0)
        if f1 == 0:
            error = "First derivative of equation becomes zero at " + (f"it: {i+1}")
            steps.append(error)
            return error, roots, steps
        
        f2 = diff2.evalf(subs={x: x0}, n=precision)
        # f2 = diff2.subs(x, x0)
        root = x0 - (f * f1) / (f1 ** 2 - f * f2)
        roots.append(root)
        steps.append(f"Iteration {i+1}:  X = {x0} - {f} * {f1} /  [{f1}]^2 - {f} * {f2}")
        if abs(root - x0) < eps:
            break
        if roots.count(root) > 1:
            error = "Method diverges at " + (f"it: {i}")
            steps.append(error)
            return error, roots, steps
            
        x0 = root

    return error, roots, steps

#modificationone functiom
def ModificationOne(str_equation, x0, m=1, precision=5, eps=1e-5, max_iterations=50):
    x = sp.symbols('x')
    equation = sp.N(sp.sympify(str_equation), precision)
    steps = []
    roots = []
    error = None

    diff = sp.diff(equation, x)
    if diff == 0:
        error = "linear equation, has no roots"
        steps.append(error)
        return error, roots, steps
    
    for i in range(max_iterations):
        root = 0
        f = equation.evalf(subs={x: x0}, n=precision)
        f1 = diff.evalf(subs={x: x0}, n=precision)
        if f1 == 0:
            error = "First derivative of equation becomes zero at " + (f"it: {i+1}")
            steps.append(error)
            return error, roots, steps
        root = x0 - m * (f / f1)
        roots.append(root)
        steps.append(f"Iteration {i+1}:  X = {x0} - {m} * {f} / {f1}")
        if abs(root - x0) < eps:
            break
        if roots.count(root) > 1:
            error = "Method diverges at " + (f"it: {i}")
            steps.append(error)
            return error, roots, steps
        
        x0 = root

    return error, roots, steps

## main function
if __name__ == '__main__':
    
    # test_cases = [
    #     ("x**3 - 2*x**2 - 5", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
    #     ("x**3 - x**2 + 2", -20, 1, 5, 1e-6, 200),  # root multiplicity: 1
    #     ("x**4 - 3*x**3 + 2", 1, 1, 6, 1e-6, 200),  # root multiplicity: 1
    #     ("x**5 - 11*x**4 + 46*x**3 - 90*x**2 + 81*x - 27", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
    #     ("x**2 - 4", 5, 2, 5, 1e-6, 200),  # root multiplicity: 2
    #     ("x**3 - 2*x - 5", 5, 1, 6, 1e-6, 200),  # root multiplicity: 1
    #     ("x**3 - 3*x**2 + 2*x - 1", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
    #     ("x**4 - 4*x**3 + 6*x**2 - 4*x + 1", 5, 1, 5, 1e-6, 200),  # root multiplicity: 1
    #     ("x**5 - 5*x**4 + 10*x**3 - 10*x**2 + 5*x - 1", 5, 1, 6, 1e-6, 200),  # root multiplicity: 1
    #     ("x**6 - 6*x**5 + 15*x**4 - 20*x**3 + 15*x**2 - 6*x + 1", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
    #     ("x + 2", 5, 1, 4, 1e-6, 200),  # root multiplicity: 1
    #     ("10", 5, 0, 4, 1e-6, 200),  # root multiplicity: 0 (constant function)
    # ]
    
    test_cases = [
        ("sin(x)", 3.15, 1, 10, 1e-6, 50)
        #("e**x-5+x", 5, 1, 4, 1e-6, 3)
    ]

    for i, (str_equation, x0, m, precision, eps, max_iterations) in enumerate(test_cases, 1):
        print(f"Test case {i}: {str_equation}")
        x = sp.symbols('x')
        equation = sp.N(sp.sympify(str_equation), precision)
        rootss = sp.solve(equation, x)
        roots = [root.evalf(precision) for root in rootss]
        print(f"\nThe true roots of the equation is {roots}\n")
        
        error1, roots1, steps1 = ModificationOne(str_equation, x0, m, precision, eps, max_iterations)
        print("modification one", error1 ,"\n", roots1 ,"\n" , steps1 ,"\n")

        error2, roots2, steps2 = ModificationTwo(str_equation, x0, precision, eps, max_iterations)
        print("modification two", error2 ,"\n", roots2 ,"\n" , steps2 ,"\n\n\n")
       
