# FCSC : Problemeuh (Crypto)

Difficulty : medium

## Context


This is a math challenge, we need provide an array of input that solve a system of equations,

Challenge code :
```py
import sys
from hashlib import sha256
sys.set_int_max_str_digits(31337)
try:
    a, b, c, x, y = [ int(input(f"{x} = ")) for x in "abcxy" ]
    assert a > 0
    assert a == 487 * c
    assert 159 * a == 485 * b
    assert x ** 2 == a + b
    assert y * (3 * y - 1) == 2 * b
    h = sha256(str(a).encode()).hexdigest()
    print(f"FCSC{{{h}}}")
except:
    print("Nope!")
```

## Solution

We need to find  $a,b,c,x,y  \in \Z$ such that ,
$$
\begin{align}
a &> 0 \\
a &= 487c \\
159a &= 485b \\
x ^ 2 &= a + b \\
2b &= y(3y - 1)
\end{align}
$$

Since we know $(1)$ and $(2)$, in order for $a \in \Z$ to hold true we need,

$$
a \equiv 0 [485] \text{ and } a \equiv 0[487]
$$

Which means that, $a \equiv 0 [487 \cdot 485]$ or written more coveniently
$$
a = 487 \cdot 485\cdot k
$$

This allows us to thus express $b$ and $c$ with k,
$$
\begin{align*}
b &= 487 \cdot 159 k \\
c &= 485k
\end{align*}
$$

Which in turn gives us,
$$

\begin{align*}
(4) &\iff x^2 = 487 \cdot 485k + 487 \cdot 159k \\
    &\iff x^2 = 487 \cdot 644k \\
\end{align*}
$$

We can deduce from $(1)$ and $(3)$ that $b > 0$ and thus that $a + b > 0$. So,
$$
x = \sqrt{487.644k}
$$

Here, in order for $x \in \Z$, we need $487 \cdot 644k$ to be a perfect square. The prime decomposition gives us :

$$
x = \sqrt{2^2 \cdot 7 \cdot 23 \cdot 487 k}
$$

In order, for that square root to be an integer, we need all the factors to be square which adds a constraint to k such that,

$$
k = 7 \cdot 23 \cdot 487 \cdot k'^2
$$

We move onto (5),

$$
\begin{align*}
(5) \iff 3y^2 - y - 2b = 0  
\end{align*}
$$

Let's find the solution of that equation :

$$
\Delta = 1 + 24b
$$

And since, $\Delta > 0$ and because we can't yeet out the negative solution because $2b > 0$.

$$
y = {1 + \sqrt{\Delta} \over 6}
$$

Another square-root, which means we need to ensure again that $\Delta$ is a perfect square. Let $\delta \in \N$

$$
\begin{align*}
\delta^2 &= 1 + 24b \\
\delta^2 &= 1 + 24 \cdot 487^2 \cdot 159 \cdot 7 \cdot 23 \cdot 487 k'^2 \\
1 &= \delta^2 - A k'^2
\end{align*}
$$

This is a Pell-Fermat equation and I have no clue how to solve that so we'll probably ask <3 sympy <3 to solve it for us, which gives us the script :

```py
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

```

Youpi ! We have the flag after a bit of time :

```txt
$ py solve.py
FCSC{b313c611e23a09e5479b10793705fb40a7a32dbcbd8c4bc2b1a33e42c4579cae}
```