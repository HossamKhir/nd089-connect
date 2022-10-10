---
marp: true
theme: gaia
class: gaia
color: black
math: katex
---

<!--
_class:
  - gaia
  - lead
-->

# AI Programming with Python

![bg right](https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/2dmDLmWvCncVHcQ6lz9u5v/9ebc8c914fcf0e8b546bce78133b2a4a/OpenGraph_Udacity_Logo_Update__1_.png)

## Session 10

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

<!-- # TODO insert quote -->
![bg right:33%](https://upload.wikimedia.org/wikipedia/commons/f/f4/Raymond_Kurzweil_Fantastic_Voyage.jpg)

> Artificial Intelligence will reach human levels by around 2029.
> Follow that out further to, say, 2045,
> we will have multiplied the intelligence,
> the human biological machine intelligence of our civilization a billion-fold.

# [Ray Kurzweil](https://www.kurzweilai.net/), 2017

---

# Last session

- Linear Algebra
  - Linear combination & spans.
  - Linear transformation & matrices.

---

# Agenda

- Q&A
- Linear Algebra labs.
- Q&A _(encore)_

---

# Material

```sh
git fetch
git checkout template/session10
```

---

# `numpy.linalg`

A submodule of [NumPy](https://numpy.org), that focuses on linear algebra.

- `numpy.dot`
- `numpy.matmul`
- `numpy.linalg.norm`
- `numpy.linalg.solve`
- `numpy.linalg.eig`

---

# `numpy.dot`

The dot product of two arrays (including matrices).

> more on dot product [here](https://www.youtube.com/watch?v=LyGKycYT2v0).

```py
# M is a matrix, a is a vector, assume proper dimensions
a_new = np.dot(M, a)
# alternatively
a_new = M @ a # less recommended
```

---

# `numpy.matmul`

Matrix product of two arrays (specifically matrices, yet works with 1D vectors too).

```py
# A (mA, nA) & B (mB, nB) are matrices, nA == mB
res = np.matmul(A, B)
# alternatively 
res = A @ B
# dimension mismatch exception
_ = np.matmul(B, A)
```

---

# `numpy.linalg.solve`

Finds the solution to a linear (full rank) matrix equation, or a system of linear scalars.

```py
# uv is a matrix of 2 columns, each represents a unit basis vector
# a is a vector in a similar space to uv (R2 for instance)
combination = np.linalg.solve(uv, a)
# if `a` is indeed in the span of uv, the returned vector
#   is the scalar components that lead to `a`
#   i.e a = combination * uv
#   otherwise (`a` is not in the span) an exception is raised
```

---

# extra: `numpy.linalg.eig`

Calculates the eigenvalues & eigenvectors of a square array.

```py
vals, vecs = np.linalg.eig(array)
```

---

<!--
_class:
  - gaia
  - lead
-->

# Q&A _(encore)_ <!-- fit -->

---

<!--
_class:
  - gaia
  - lead
 -->

# Thank You

## Good Luck

## Have Fun
