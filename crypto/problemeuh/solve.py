import sys
from sympy.solvers.diophantine.diophantine import diop_DN
import math
from hashlib import sha256
sys.set_int_max_str_digits(31337)

A = 24 * 487 * 159 * 7 * 23 * 487

t,m = diop_DN(A, 1)[0]

k = 7 * 23 * 487 * m * m
a = 487 * 485 * k
b = 487 * 159 * k
c = 485 * k
x = math.isqrt(a + b)

D = 1 + 24 * b
y = (1 + math.isqrt(D)) // 6
h = sha256(str(a).encode()).hexdigest()

assert a == 487 * c
assert 159 * a == 485 * b
assert x ** 2 == a + b
assert y * (3 * y - 1) == 2 * b

print(f"FCSC{{{h}}}")
