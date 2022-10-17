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

## Session 11

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

<!-- https://analyticsindiamag.com/ten-famous-quotes-about-artificial-intelligence/ -->

> The development of full artificial intelligence could spell the end of the human race&#8230;
> It would take off on its own, and re-design itself at an ever-increasing rate.
> Humans, who are limited by slow biological evolution, couldn’t compete, and would be superseded.

# [Stephen Hawking](https://en.wikipedia.org/wiki/Stephen_Hawking)

---

# Last session

- Linear Algebra labs.

---

# Agenda

- Q&A
- Linear Algebra in Neural Networks.
  - System of linear equations.
  - Perceptron.
- Q&A _(encore)_

---

# Gentle reminder: system of linear equations

The straight line equation: $y=m.x+c$, where $m$ is the slope, $c$ is the $y$-axis intercept.

For a line that's $45\degree$ from $x$-axis, the equation is $y=x$ (i.e. $m=1,c=0$).

<!-- Let's for a moment write the equation like: $b.y=a.x+c;m=b/a$ -->

---

$2y=x$ and $y=2x$ are two straight lines, both having $c=0$, but the first has $m=\frac{1}{2}$, and the second has $m=2$.

Those two lines we mentioned meet at a single point, let's find it, first on the [graph](https://geogebra.org/graphing)!

Do you remember how to find it algebraically?

first, we rewrite the equations in the form of $b.y+a.x=c$.

$$
y-2x=0 \to (1)\\
2y-x=0 \to (2)
$$

---

then multiply $(1)$ by $2$, then subtract $(2)$ from $2*(1)$

$$
2(y-2x=0) \to 2y-4x=0 \\
-(2y-x=0) \to -2y+x=0 \\
0y-3x=0
$$

Then $x=0$, substituting that in any of $(1)$ or $(2)$ gives us $y=0$, so the point becomes $(0, 0)$.

That was called **solving** the system of the _linear_ equations.

---

Let's rewrite the equations again, but this time in matrix format.

$$
\begin{bmatrix}
y-2x \\
2y-x
\end{bmatrix} =
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

seems familiar? sure it does, the left matrix is a product of matrix-vector multiplication.

$$
\begin{bmatrix}
1 & -2 \\
2 & -1
\end{bmatrix}
\begin{bmatrix}
y \\
x
\end{bmatrix} =
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

This now could leverage linear algebra for finding the solution, namely here the **inverse** of the matrix.

---

The last matrix equations could be viewed as $W\vec{X}=\vec{c}$, where $W$ is called a weight matrix.

The solution is $\vec{X}=W^{-1}\vec{c}$, in our given case it is the trivial solution, as $\vec{c}$ is a zero vector.

The original equations (before rearranging) could still be written in matrix form.

$$
\begin{bmatrix}
1 \\
2
\end{bmatrix}.y =
\begin{bmatrix}
2 \\
1
\end{bmatrix}.x +
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

---

of course if we made the originals in the form of $y=mx+c$, then we have $y=\frac{1}{2}x+0$ & $y=2x+0$, then:

$$
y =
\begin{bmatrix}
2 \\
\frac{1}{2}
\end{bmatrix}.x +
\begin{bmatrix}
0 \\
0
\end{bmatrix} \\
y = \vec{m}.x + \vec{c}
$$

Since now we're in the realm of linear algebra, the same goes for higher dimensions:

$$
z=\vec{m}_{x}x+\vec{m}_{y}y+\vec{c} \\
z = M.\begin{bmatrix}
  x \\
  y
\end{bmatrix} + \vec{c}
$$

---

So, in general, assuming _output_ axes ($y_m$), all the other axes are _numbered features_ ($x_n$):

$$
\begin{bmatrix}
  y_1 \\
  y_2 \\
  \vdots \\
  y_m
\end{bmatrix} = \begin{bmatrix}
  w_{11} & w_{12} & \dots & w_{1n} \\
  w_{21} & w_{22} & \dots & w_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  w_{m1} & w_{m2} & \dots & w_{mn} \\
\end{bmatrix}\begin{bmatrix}
  x_1 \\
  x_2 \\
  \vdots \\
  x_n
\end{bmatrix}+\begin{bmatrix}
  c_1 \\
  c_2 \\
  \vdots \\
  c_m
\end{bmatrix} \\
$$

$$
y=W.X+c
$$

which is the general formula for a system of linear equations.

---

# Intro to perceptron

Let's assume we have an equation to a set of _points_ in $\mathbb{R}^3$ space, we can leverage the linear algebra to describe it as:
$y=m_1x_1+m_2x_2+c$, equivalently: $y=MX+c$
and we can graph it on the axis to visualise it, but let's try to visualise the **equation**!

---

![bg contain](../data/img/single-perceptron.svg)

---

now let's leverage the general equation, say we have,
$y_1=m_{11}x_1+m_{12}x_2+c_1$ **&** $y_2=m_{21}x_1+m_{22}x_2+c_2$
those become: $y=MX+c$ once again, so let's visualise those.

---

![bg contain](../data/img/perceptron-2.svg)

---

What we've seen so far is something called `perceptron`, and there is an algorithm called the `perceptron algorithm`, that is the foundation for the artificial neural networks.

> The only difference between a perceptron and a neuron is the _activation function_!

Knowing that, a perceptron could be a neuron with a _linear_ activation function.

Hopefully, now you can see how linear algebra fits into neural networks!

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
