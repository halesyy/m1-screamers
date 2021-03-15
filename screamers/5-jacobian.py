
from timeit import default_timer as timer
import numpy as np

"""
Sourced from: https://math.stackexchange.com/questions/2869047/python-compute-jacobian-numerically
A helpful diagnostic for cryptographic wallet generation (as far as I'm aware).
"""


start = timer()

def f(t, x, **params):

    a = params['a']
    c = params['c']

    f1 = a * (x[0] - x[0] * x[1])
    f2 = -c * (x[1] - x[0] * x[1])

    return np.array([f1, f2], dtype = float)

def df(t, x, **params):

    eps = 1e-10
    J = np.zeros([len(x), len(x)], dtype = float)

    for i in range(len(x)):
        x1 = x.copy()
        x2 = x.copy()

        x1[i] += eps
        x2[i] -= eps

        f1 = f(t, x1, **params)
        f2 = f(t, x2, **params)

        J[ : , i] = (f1 - f2) / (2 * eps)

    return J

for t in range(1000):
    for a in range(1000):
        x = np.array([1, 2], dtype=float)
        df(t, x, a=a, c=a)

end = timer()

time_taken = (end - start)

print("took", time_taken, "seconds")
