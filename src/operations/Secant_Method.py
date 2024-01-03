import sympy as sp
from .utils import relative_error

def secant_method(f, x0, x1, rel_err=0.00001, maxiter=100, signif_digits=5):
    try:
        flag, converge, steps, roots = True, '', [], []
        errors = []
        x = sp.symbols('x')
        fx = sp.sympify(f)
        for i in range(maxiter):
            #calculate with signification digits
            x2 = sp.N(x1 - fx.subs(x, x1)*(x1 - x0)/(fx.subs(x, x1) - fx.subs(x, x0)), signif_digits)
            roots.append(x2)
            error = sp.N(relative_error(x2, x1), signif_digits)
            errors.append(error)
            #explaine the steps
            step = f'Iteration {i+1}:   x{i+1} = {x2}   relative error = {error}'
            steps.append(step)
            if error < rel_err:
                return True, 'Solution found and method has converged', steps, roots
            x0 = x1
            x1 = x2
            # check whether the method converged or not
            if i>1 and error > errors[i-2]:
                return True, 'Method diverges', steps, roots
        return True, 'Method converges', steps, roots
        
    except Exception as e:
        raise e

if __name__ == "__main__":
    f = 'x**2 - 2'
    x0 = 0.5
    x1 = 1
    flag, converge, steps, roots = secant_method(f, x0, x1)
    print(message)
    print(steps)
    print(roots)