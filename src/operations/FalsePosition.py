import sympy as sp
# from src.operations.Bisection import relative_error
from .Bisection import relative_error, infinite_check
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
        # func = sp.lambdify(x, equation, 'numpy')
        a = sp.N(a, precision)
        b = sp.N(b, precision)
        if infinite_check(equation.subs (x, a)):
            return f"function is undefined at {a}, Cannot proceed", [], []
        if infinite_check(equation.subs (x, b)):
            return f"function is undefined at {b}, Cannot proceed", [], []
        # step = f"a = {a}, b = {b}, f(a) = {sp.N(equation.subs (x, a), precision)}, f(b) = {sp.N(equation.subs (x, b), precision)}"
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
            steps.append(f"Root of f(x) = {equation} using False Position method on [{start}, {end}]: {root} with 0 iterations")
            return error, steps, roots
        # step+=f"\nf(a) and f(b) have opposite signs, so we can proceed"
        # steps.append(step)
        it = 1
        mid = None
        test = True
        old_mid = None
        while test:
            old_mid = mid
            mid = sp.N((a * equation.subs (x, b) - b * equation.subs (x, a)) / (equation.subs (x, b) - equation.subs (x, a)), precision)
            if infinite_check(equation.subs (x, mid)):
                return f"Root does not exist", [], []
            step = f"iteration {it}:\na = {a}, f(a) = {sp.N(equation.subs (x, a), precision)}\nb = {b}, f(b) = {sp.N(equation.subs (x, b), precision)}\nmid = (a * f(b) - b * f(a)) / (f(b) - f(a)) = {mid}, f(mid) = {sp.N(equation.subs (x, mid), precision)}"
            relativeError = sp.N(relative_error(old_mid, mid), precision)
            if old_mid != None:
                step+=f"\nrelative error = {relativeError}"
            if equation.subs (x, a) * equation.subs (x, mid) == 0:
                step+=f"\nf(a) * f(mid) = 0, so we stop"
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
    except Exception as e:
        return "Cannot Solve", [], []

if __name__ == "__main__":
    # equation = "3*x**4 + 6.1*x**3 - 2*x**2 + 3*x + 2"
    # equation = "-12 - 21*x + 18*x**2 - 2.75*x**3"
    # equation = "5*x-sin(x)"
    # error, steps, roots = FalsePosition(equation, -1, 1,precision=5, eps=1e-2, max_iterations=50)
    equation = "x**4 + 3*x - 4"
    error, steps, roots = FalsePosition(equation, 0, 3, precision=5, eps=1e-5, max_iterations=100)
    if error != None:
        print(error)
    else:
        for i in range(len(steps)):
            print(steps[i])
            print(f"Root: {roots[i]}")
            print('----------------------')