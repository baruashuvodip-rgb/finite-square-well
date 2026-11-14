def find_sign_change(f, step, a, b):
    x = a
    pairs = []
    while x + step <= b:
        if f(x) * f(x + step) < 0:
            pairs.append((x, x + step))
        x += step
    return pairs



def bisection(f, pairs, tol, max_iter=100):

    zeros = []

    for a, b in pairs:

        iteration = 0

        while abs(b-a) > tol and iteration < max_iter:

            c = (a+b)/2

            if f(a)*f(c) < 0:
                b = c
            else:
                a = c

            iteration += 1

        root = (a+b)/2

        # Check convergence and function value
        if iteration < max_iter and abs(f(root)) < 1e-4:
            zeros.append(root)

    return zeros

