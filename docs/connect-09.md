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

## Session 9

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

<!-- # TODO insert quote -->

---

# Last session

- Linear Algebra
  - Vectors

---

# Agenda

- Q&A
- Linear combination & spans.
- Linear transformation & matrices.
- Q&A _(encore)_

---

# Linear Combination 1

> N.B: it is preferred to practice using pencil & paper over programming (e.g. MATLAB, python, etc&#8230;)

- for the given vectors, rewrite them in form of scalar multiplication & vector addition using cartesian basis vectors (i & j):
  1. $\begin{bmatrix}1 & -2\end{bmatrix}^T$
  1. $\begin{bmatrix}2 & 1\end{bmatrix}^T$
  1. $\begin{bmatrix}4 & -2\end{bmatrix}^T$

---

# Linear Combination 1, solution

given $\hat{i}=\begin{bmatrix}1 \\ 0\end{bmatrix}$ & $\hat{j}=\begin{bmatrix}0 \\ 1\end{bmatrix}$

- $\begin{bmatrix}1 \\ -2\end{bmatrix}=1.\hat{i}+(-2).\hat{j}$
- $\begin{bmatrix}2 \\ 1\end{bmatrix}=2.\hat{i}+1.\hat{j}$
- $\begin{bmatrix}4 \\ -2\end{bmatrix}=4.\hat{i}+(-2).\hat{j}$

---

# Linear Combination 2

- if $\vec{u}=\begin{bmatrix}3 \\ 2\end{bmatrix}$ & $\vec{v}=\begin{bmatrix}-1 \\ 4\end{bmatrix}$, can those be basis vectors?
- given $\vec{a}=\begin{bmatrix}1 \\ 2 \\ 3\end{bmatrix}$, $\vec{b}=\begin{bmatrix}2 \\ 2 \\ 2\end{bmatrix}$, $\vec{c}=\begin{bmatrix}8 \\ 8 \\ 8\end{bmatrix}$, what is the span of these vectors?

---

# Linear Combination 2, solution

- for all values of $\vec{u}$ & $\vec{v}$, it is possible to be basis vectors!
- the span for $\vec{a}$, $\vec{b}$, & $\vec{c}$ is a plane, as $\vec{b}$ & $\vec{c}$ are linearly dependant.

---

# Linear transformation

`Optional`: use $\vec{u}$ & $\vec{v}$ from Q2 to build a transformation matrix, then use the new transformation matrix to transform the vectors from Q1.

- given $M=\begin{bmatrix}-3 & 2 & -5 \\ 2 & -3 & 4 \\ 1 & 1 &1 \end{bmatrix}$, find the transformed vectors of:
  1. $\vec{a}=\begin{bmatrix}2 & 3 & -1\end{bmatrix}^T$
  1. $\vec{b}=\begin{bmatrix}1 & -2 & 0\end{bmatrix}^T$
  1. $\vec{c}=\begin{bmatrix}3 & 1 & 1\end{bmatrix}^T$
  <!-- 1. $a=\begin{bmatrix}2 & 3 & -1\end{bmatrix}^T$
  1. $a=\begin{bmatrix}2 & 3 & -1\end{bmatrix}^T$ -->

---

$$
M.a = \begin{bmatrix}
  \begin{bmatrix}
    -3 \\ 2 \\ 1
  \end{bmatrix}
  \begin{bmatrix}
    2 \\ -3 \\ 1
  \end{bmatrix}
  \begin{bmatrix}
    -5 \\ 4 \\ 1
  \end{bmatrix}
\end{bmatrix} * \begin{bmatrix}2 \\ 3 \\ -1\end{bmatrix}
$$
$$
= 2 * \begin{bmatrix}-3 \\ 2 \\ 1\end{bmatrix}
+ 3 * \begin{bmatrix}2 \\ -3 \\ 1\end{bmatrix}
+ (-1) * \begin{bmatrix}-5 \\ 4 \\ 1\end{bmatrix}
$$

$$
= \begin{bmatrix}-6 \\ 4 \\ 2\end{bmatrix}
+ \begin{bmatrix}6 \\ -9 \\ 3\end{bmatrix}
+ \begin{bmatrix}5 \\ -4 \\ -1\end{bmatrix}

= \begin{bmatrix}-6+6+5 \\ 4-9-4 \\ 2+3-1\end{bmatrix}

= \begin{bmatrix}5 \\ -9 \\ 4\end{bmatrix}
$$

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
