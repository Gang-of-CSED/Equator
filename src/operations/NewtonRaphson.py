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
        return error, roots, steps
    
    diff2 = sp.diff(diff, x)
    
    for i in range(max_iterations):
        root = 0
        f = equation.subs(x, x0)
        f1 = diff.subs(x, x0)
        if f1 == 0:
            error = "First diff of equation is zero, cannot proceed"
            return error, [], []
        f2 = diff2.subs(x, x0)
        root = x0 - (f * f1) / (f1 ** 2 - f * f2)
        roots.append(root)
        if abs(root - x0) < eps:
            break
        else:
            steps.append(f"Iteration {i+1}:  X = {x0} - {f} * {f1} /  [{f1}]^2 - {f} * {f2}")
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
        return error, roots, steps
    
    for i in range(max_iterations):
        root = 0
        f = equation.subs(x, x0)
        f1 = diff.subs(x, x0)
        if f1 == 0:
            error = "First diff of equation is zero, cannot proceed"
            return error, [], []
        root = x0 - m * (f / f1)
        roots.append(root)
        if abs(root - x0) < eps:
            break
        else:
            steps.append(f"Iteration {i+1}:  X = {x0} - {m} * {f} / {f1}")
        x0 = root

    return error, roots, steps

## main function
if __name__ == '__main__':
    
    str_equation = "x**5 - 11*x**4 + 46*x**3 - 90*x**2 + 81*x - 27"
    x0 = 5
    m = 3
    precision = 2
    eps = 1e-6
    max_iterations = 200
    
    print(str_equation)
    
    #print true root of the function
    x = sp.symbols('x')
    equation = sp.N(sp.sympify(str_equation), precision)
    root = sp.solve(equation, x)
    print(f"\nThe true roots of the equation is {root}\n\n")
   
    print("Modification One\n")
    error1 ,roots1, steps1 = ModificationOne(str_equation, x0, m, precision, eps, max_iterations)
    print(f"The root of the equation is approximately {roots1[-1]}\n")
    print(error1, roots1, steps1)
    
    print("Modification Two\n")
    error2, roots2, steps2 = ModificationTwo(str_equation, x0, precision, eps, max_iterations)
    print(f"The root of the equation is approximately {roots2[-1]}\n")
    print(error2, roots2, steps2)