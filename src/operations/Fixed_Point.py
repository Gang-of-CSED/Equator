import sympy as sp 
from .utils import relative_error

def fixed_point(g, x0, rel_err=0.00001, maxiter=10, signif_digits=6):
    flag, steps, roots = True, [], []
    x = sp.symbols('x')
    gx = sp.sympify(g)
    for i in range(maxiter):
        #calculate with signification digits
        x1 = sp.N(gx.subs(x, x0), signif_digits)
        roots.append(x1)
        #explaine the steps
        error = relative_error(x1, x0)
        step = f'Iteration {i+1}:   x{i+1} = {x1}   relative error = {error}\n'
        steps.append(step)
        if error < rel_err:
            return True, steps, roots
        x0 = x1
    return False, steps, roots

if __name__ == "__main__":
    g = 'exp(-x)'
    x0 = 0
    flag, steps, roots = fixed_point(g, x0)
    print(steps)
    print(roots)