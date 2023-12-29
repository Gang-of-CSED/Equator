import sympy as sp
# from src.operations.Bisection import relative_error
from Bisection import relative_error
def FalsePosition(str_equation, a, b, precision=5, eps=1e-5, max_iterations=50):
    """
    False Position method for finding a root of a function
    :param equation: string of the function
    :param a: left boundary
    :param b: right boundary
    :param precision: precision
    :param eps: tolerance
    :param max_iterations: maximum number of iterations
    :return: root
    """
    start = a
    end = b
    error = None
    root = None
    roots = []
    steps = []
    x = sp.symbols('x')
    # equation = sp.lambdify(x, sp.N(sp.sympify(str_equation), precision))
    equation = sp.N(sp.sympify(str_equation), precision)
    func = sp.lambdify(x, equation, 'numpy')
    a = sp.N(a, precision)
    b = sp.N(b, precision)
    # step = f"a = {a}, b = {b}, f(a) = {sp.N(func(a), precision)}, f(b) = {sp.N(func(b), precision)}"
    if func(a) * func(b) > 0:
        # step+="\nf(a) and f(b) must have opposite signs, so we cannot proceed"
        # steps.append(step)
        error = f"f({a}) and f({b}) must have opposite signs, so we cannot proceed"
        return error, steps, root
    # step+=f"\nf(a) and f(b) have opposite signs, so we can proceed"
    # steps.append(step)
    it = 1
    mid = None
    test = True
    old_mid = None
    while test:
        old_mid = mid
        mid = sp.N((a * func(b) - b * func(a)) / (func(b) - func(a)), precision)
        step = f"iteration {it}:\na = {a}, f(a) = {sp.N(func(a), precision)}\nb = {b}, f(b) = {sp.N(func(b), precision)}\nmid = (a * f(b) - b * f(a)) / (f(b) - f(a)) = {mid}, f(mid) = {sp.N(func(mid), precision)}"
        relativeError = sp.N(relative_error(old_mid, mid), precision)
        if old_mid != None:
            step+=f"\nrelative error = {relativeError}"
        if func(a) * func(mid) < 0:
            b = mid
            step+=f"\nf(a) and f(mid) have opposite signs, so we set b = mid = {mid}"
        else:
            a = mid
            step+=f"\nf(a) and f(mid) have same signs, so we set a = mid = {mid}"
        # steps.append(step)
        it+=1
        test = relativeError > eps and it < max_iterations
        if old_mid != None:
            if relativeError <= eps:
                step += f"\n{relativeError} <= {eps}, so we stop"
            else:
                step += f"\n{relativeError} > {eps}, so we continue"
        if it > max_iterations:
            step += f"\nmax iterations reached ({max_iterations}) so we stop"
        roots.append(mid)
        steps.append(step)

    root = mid
    roots.append(root)
    steps.append(f"Root of f(x) = {equation} using False Position method on [{start}, {end}]: {root} with {it-1} iterations")
    return error, steps, roots

if __name__ == "__main__":
    # equation = "3*x**4 + 6.1*x**3 - 2*x**2 + 3*x + 2"
    equation = "-12 - 21*x + 18*x**2 - 2.75*x**3"
    error, steps, roots = FalsePosition(equation, -1, 0,precision=5, eps=1e-2, max_iterations=50)
    if error != None:
        print(error)
    else:
        for i in range(len(steps)):
            print(steps[i])
            print(f"Root: {roots[i]}")
            print('----------------------')