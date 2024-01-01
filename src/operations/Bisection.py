import sympy as sp

def relative_error(x, x0):
    """
    :return: relative error
    """
    if x == None:
        return 1e10
    if x == x0:
        return 0
    if x0 == 0:
        return 1e10
    return abs(x - x0) / abs(x0)

def infinite_check(x):
    """
    :return: True if x is infinite, False otherwise
    """
    return  x == sp.zoo or not x.is_real or not x.is_finite

def bisection(str_equation, a, b, precision=5, eps=1e-5, max_iterations=50):
    """
    Bisection method for finding a root of a function
    :param equation: string of the function
    :param a: left boundary
    :param b: right boundary
    :param precision: precision
    :param eps: tolerance
    :param max_iterations: maximum number of iterations
    :return: root
    """
    try:
        start = a
        end = b
        error = None
        root = None
        roots = []
        steps = []
        x = sp.symbols('x')
        # equation = sp.lambdify(x, sp.N(sp.sympify(str_equation), precision))
        equation = sp.N(sp.sympify(str_equation), precision)
        # lambdify FAILED
        # func = sp.lambdify(x, equation, 'numpy')
        a = sp.N(a, precision)
        b = sp.N(b, precision)
        # step = f"a = {a}, b = {b}, f(a) = {sp.N(equation.subs (x, a), precision)}, f(b) = {sp.N(equation.subs (x, b), precision)}"
        if infinite_check(equation.subs (x, a)):
            return f"function is undefined at {a}, Cannot proceed", [], []
        if infinite_check(equation.subs (x, b)):
            return f"function is undefined at {b}, Cannot proceed", [], []
        if equation.subs (x, a) * equation.subs (x, b) > 0:
            # step+="\nf(a) and f(b) must have opposite signs, so we cannot proceed"
            # steps.append(step)
            error = f"f({a}) and f({b}) must have opposite signs, so we cannot proceed"
            return error, steps, root
        if equation.subs (x, a) * equation.subs (x, b) == 0:
            if equation.subs (x, a) == 0:
                root = a
            else:
                root = b
            roots.append(root)
            steps.append(f"Root of f(x) = {equation} using bisection method on [{start}, {end}]: {root} with 0 iterations")
            return error, steps, roots
        # step+=f"\nf(a) and f(b) have opposite signs, so we can proceed"
        # steps.append(step)
        it = 1
        mid = None
        test = True
        old_mid = None
        while test:
            old_mid = mid
            mid = sp.N((a + b) / 2, precision)
            if infinite_check(equation.subs (x, mid)):
                return f"Root does not exist", [], []
            step = f"iteration {it}:\na = {a}, f(a) = {sp.N(equation.subs (x, a), precision)}\nb = {b}, f(b) = {sp.N(equation.subs (x, b), precision)}\nmid = (a + b) / 2 = {mid}, f(mid) = {sp.N(equation.subs (x, mid), precision)}"
            relativeError = sp.N(relative_error(old_mid, mid), precision)
            if old_mid != None:
                step+=f"\nrelative error = {relativeError}"
            if equation.subs (x, a) * equation.subs (x, mid) == 0:
                step += f"\nf(a) * f(mid) = 0, so we stop"
                roots.append(mid)
                steps.append(step)
                break
            if equation.subs (x, a) * equation.subs (x, mid) < 0:
                b = mid
                step+=f"\nf(a) and f(mid) have opposite signs, so we set b = mid = {mid}"
            else:
                a = mid
                step+=f"\nf(a) and f(mid) have same signs, so we set a = mid = {mid}"
            # steps.append(step)
            it+=1
            test = relativeError > eps and it <= max_iterations
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
        steps.append(f"Root of f(x) = {equation} using bisection method on [{start}, {end}]: {root} with {it-1} iterations")
        return error, steps, roots
    except Exception as e:
        return "Cannot Solve", [], []

if __name__ == "__main__":
    # equation = "x**4 - 2*x**3 - 4*x**2 + 4*x + 4"
    # root, steps, iterations = bisection(equation, -2, -1, precision=5, eps=1e-3)
    # equation = "1.5*x - 6 - 1/2 * sin(2*x)"
    # error, steps, roots = bisection(equation, 4, 5, precision=5, eps=1e-5)
    # equation = "x**3 - 0.165*x**2 + 3.993*10**-4"
    # error, steps, roots = bisection(equation, 0, 0.11, precision=4, eps=2e-3)
    # equation = "x**4 + 3*x - 4"
    # error, steps, roots = bisection(equation, 0, 3, precision=5, eps=1e-5, max_iterations=100)
    equation = "x-4"
    error, steps, roots = bisection(equation, -15, 5,precision=5, eps=1e-2, max_iterations=50)
    if error:
        print(error)
    else:
        for i in range(len(steps)):
            print(steps[i])
            print(f"Root: {roots[i]}")
            print('----------------------')