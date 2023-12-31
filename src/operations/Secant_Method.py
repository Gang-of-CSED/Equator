import sympy as sp
import relative_error

def secant_method(f, x0, x1, rel_err=0.00001, maxiter=100, signif_digits=5):
    flag, steps, roots = True, [], []
    x = sp.symbols('x')
    fx = sp.sympify(f)
    for i in range(maxiter):
        #calculate with signification digits
        x2 = sp.N(x1 - fx.subs(x, x1)*(x1 - x0)/(fx.subs(x, x1) - fx.subs(x, x0)), signif_digits)
        roots.append(x2)
        error = relative_error(x2, x1)
        #explaine the steps
        step = f'Iteration {i+1}:   x{i+1} = {x2}   relative error = {error}\n'
        steps.append(step)
        if error < rel_err:
            return True, steps, roots
        x0 = x1
        x1 = x2
    return False, steps, roots

if __name__ == "__main__":
    f = 'x**2 - 2'
    x0 = 0.5
    x1 = 1
    flag, steps, roots = secant_method(f, x0, x1)
    print(steps)
    print(roots)