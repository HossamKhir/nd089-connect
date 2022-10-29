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

## Session 13

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

<!-- https://analyticsindiamag.com/ten-famous-quotes-about-artificial-intelligence/ -->

![bg right:33%](https://imageio.forbes.com/specials-images/imageserve/62d700cd6094d2c180f269b9/0x0.jpg)

> AI doesn’t have to be evil to destroy humanity&#8230;
> if AI has a goal and humanity just happens to come in the way,
> it will destroy humanity as a matter of course without even thinking about it,
> no hard feelings.

# [Elon Musk](https://www.forbes.com/profile/elon-musk/)

---

# Last session

- Calculus
  - Univariate calculus & chain rule.
  - Multi-variate calculus & partial derivative.

---

# Agenda

- Q&A
- Calculus in Neural Networks
- Q&A _(encore)_

---

# Recall

- A neural network is a **universal approximation _function_**.
- Functions could be linear, & could be made linear (substitution).
- Linear functions could be represented using linear algebra (mainly matrix-vector product, & vector addition).
- Chain rule helps simplify the calculation of otherwise complex operations.
- Multi-variate calculus relies on the simple idea of treating non-relevant _variables_ as _constants_.
- The partial derivatives of a multi-variate function is the **gradient**.

---

# The gradient

We have seen that the derivative of a function at a given point is the tangent to the curve of the function at that point.

But for multi-variate functions, that goes into higher dimensions, and gets complex, and thus the **gradient** was defined. The gradient is somewhat a tangent **vector**, so it has a _magnitude_ and a _direction_.

The most notable piece of information here, is that the gradient, by default, points in the direction of the steepest (largest) ascent, i.e. the direction that would maximise the value at the given point.

---

# Neuron

- A neuron is a function that takes in inputs, and gives out an output.
- A neuron does a summation of inputs, alongside an optional bias, and then performs an activation (a non-linear transformation).
- Most commonly used activations:
  - Sigmoid `logistic function` (for multi-class classification)
  - ReLU (`Re`ctified `L`inear `U`nit)
  - $\tanh$ `hyperbolic tangent`
- A neural network is the full connection between _layers_ of neurons.

---

# MNIST handwritten digits

The handwritten digits classification could be seen as:

$$
\bar{d}=f(p_0,p_1,\dots,p_{783})
$$

where $\bar{d}$ is the predicted digit, and $p_i$ is a pixel in the flattened vector of the image.

In the video, Grant defined a $2$ hidden layers network, but he also mentioned it was arbitrary, and whatever your choice is, the same function above is still valid; the difference is the number of parameters (Grant had $13,002$).

---

# Feed forward

As Grant eventually explained, each layer in the neural network captures some specific _feature_.

Since the domain is quite difficult for us humans to imagine ($\mathbb{R}^{784}$), the result of each neuron as depicted in the video was almost meaningless to us, yet meaningful for the network.

---

The general formula (popular in the domain of NN):

$$
a^{(L)}_j=\Phi(z^{(L)});z^{(L)}=w^{(L)}_{jk}a^{(L-1)}_k+b^{(L)}_j
$$

Where:

- $a^{(L)}_j$: output of neuron $j$ in current layer $L$
- $a^{(L-1)}_k$: output of neuron $k$ in previous layer $L-1$
- $\Phi$ is the activation function
- $w^{(L)}_{jk}$ weights from previous layer to current
- $b^{(L)}_j$ bias for the neuron $j$ in the current layer $L$.

---

# Feed backward `Back Propagation`

<!-- video 4 -->

$$
\nabla{C}=\begin{bmatrix}
\frac{\partial{C}}{\partial{w^{(0)}_{00}}} & \dots & \frac{\partial{C}}{\partial{w^{(0)}_{0k}}} \\
\vdots & \ddots \\
\frac{\partial{C}}{\partial{w^{(L)}_{j0}}} & \dots &\frac{\partial{C}}{\partial{w^{(L)}_{jk}}}
\end{bmatrix}
$$

$$
\frac{\partial{C}}{\partial{w^{(l)}_{jk}}}=\frac{\partial{z^{(L)}_j}}{\partial{w^{(l)}_{jk}}}\frac{\partial{a^{(L)}_j}}{\partial{z^{(L)}_j}}\frac{\partial{C}}{\partial{a^{(L)}_j}}
$$

---

$$
z^{(L)}_j=\dots+w^{(L)}_{jk}a^{(L-1)}_k+\dots
$$

$$
a^{(L)}_j=\Phi(z^{(L)}_j)
$$

$$
C=\sum^{n_L-1}_{j=0}(a^{(L)}_j-y_j)^2
$$

[Neural Network Playground](https://playground.tensorflow.org/)

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
