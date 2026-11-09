import numpy as np

def find_sign_change(f, step, a, b):
    x = a
    pairs = []
    while x < b:
        if f(x) * f(x + step) < 0:
            pairs.append((x, x + step))
        x += step
    return pairs

def bisection(f, pairs, tol):
    zeros = []
    for a, b in pairs:
        if f(a) * f(b) >= 0:
            raise ValueError("f(a) and f(b) must have opposite signs")
        c = (a + b) / 2
        while abs(f(c)) > tol:
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            c = (a + b) / 2
        zeros.append(c)
        
    return zeros

pairs = find_sign_change(f, 0.1, 0, 10)
print("Sign change pairs:", pairs)

zeros = bisection(f, pairs, 1e-10)
print("Zeros:", zeros)