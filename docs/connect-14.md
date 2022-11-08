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

## Session 14

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

<!-- https://analyticsindiamag.com/ten-famous-quotes-about-artificial-intelligence/ -->

# TODO insert quote here

---

# Last session

- Calculus in Neural Network

---

# Agenda

- Q&A
- Introduction to Neural Networks
  - classification
  - perceptron
- Q&A _(encore)_

---

# Recall

- The relation between a system of linear equations and linear algebra.
  - $\begin{bmatrix}y_1 \\ \vdots \\ y_n\end{bmatrix}=\begin{bmatrix}w_{11} & \dots & w_{1m} \\ \vdots & \ddots & \vdots \\ w_{n1} & \dots & w_{nm}\end{bmatrix}\begin{bmatrix}x_1 \\ \vdots \\ x_m\end{bmatrix}+\begin{bmatrix}b_1 \\ \vdots \\ b_n\end{bmatrix}$
  - $y=Wx+b$
- Matrix-vector multiplication could be visualised by the aid of a **perceptron**

---

## Gradient descent

The gradient is the vector of partial derivative of some multi-variate function, and that it always points to the direction of the steepest ascend.

The gradient descent algorithm leverages the gradient in order to take steps in the opposing direction of the gradient, thus allowing the function to reach a local minima. Of course the function here is the cost function, the lower it is, the better the predictions.

_Taking steps_ is plain English for saying updating the weights to better predict the results.

---

example:

$$
C=\frac{1}{2m}\sum_{i=0}^m(y_i-\hat{y}_i)^2 \\
C=\frac{1}{2m}\sum_{i=0}^m(y_i-\Phi(z_i^{(L)}))^2; z_i^{(L)}=W^{(L)}a^{(L-1)}+b^{(L)} \\
\nabla{C}=\frac{1}{m}\sum_{i=0}^{m}(y_i-\hat{y})\begin{bmatrix}\frac{\partial{\hat{y}}}{\partial{W}} & \frac{\partial{\hat{y}}}{\partial{b}}\end{bmatrix} \\
w_i^\prime \gets w_i - \alpha\frac{\partial{C}}{\partial{w_i}} \\
b^\prime \gets b - \alpha\frac{\partial{C}}{\partial{b}}
$$

---

# Chain rule

The chain rule states that a complex operation could be broken down to a product of a series of simpler operations, and we leverage that for partial derivatives.

$$
\frac{\partial{C}}{\partial{w^{(1)}}}=
\frac{\partial{C}}{\partial{\Phi}}
\frac{\partial{\Phi}}{\partial{z^{(L)}}}
\frac{\partial(z^{(L)})}{\partial{w^{(L)}}}
\frac{\partial{w^{(L)}}}{\partial{w^{(1)}}}
$$

---

# Neural Networks

- The basic building block of deep learning is the neural network.
- Most common usages of neural networks are classification, and regression.

---

# Classification

- Binary: exactly two outcomes ($p,1-p$)
  - Yes/No
  - Cat/Dog
  - Cat/Not cat
- Multi-class: 3 or more outcomes
  - Dog breeds
  - Plant family

---

# Multilayer Perceptron `MLP`

When the decision boundary is quite simple, a perceptron, or a single layer of perceptrons can be sufficient, but in most complex cases (which is basically everything in life), one perceptron or a layer is not enough, that's why we had MLP.

At each layer, it could be interpreted as if the current layer is working on an input, even if that input is output of a former layer. In such case, that output could be called transformed feature.

---

# Neuron

In the classroom, Luis introduced the preceptron with the step function as activation.
A neuron is simply that, a summation followed by a function of non-linearity, the most notable are:

<!-- - The step function, -->
- the sigmoid (logistic function) $\sigma{(z)}=\frac{1}{1+e^{-z}}$,
- the hyperbolic tangent $tanh$,
- the rectified linear unit (ReLU), and its modification, leaky ReLU, and
- The softmax function (for multi-class classification)

---

# Neural Network

Neural network `NN` used to be called `MLP` in some older references. The subtle difference is the building unit. If it is a neuron, then it is a `NN`, if it is a perceptron, then it is a `MLP`.

In short `MLP` is a _VERY_ special case of `NN`.

---

# Training `NN`s

_Training_ and _Learning_ are fancy names to some algorithmic/mathematical operations, one of which is Gradient Descent.

First, we need a way to tell how good/accurate our network works, that's why we have **Error** and **Cost** functions, both work on the same concept of how far my prediction is from the ground truth, but some slight difference.
An **Error** (loss) function is for a single example, whereas a **Cost** function is for the entire dataset (i.e. the cost function is the average loss over the (training) dataset).

---

Error functions should be:

- continuos,
- differentiable.

Some of the most well known cost functions:

- Mean absolute errors `MAE`,
- Mean squared errors `MSE` & root MSE `RMSE`
- $R^2$ score, and adjusted $R^2$,
- Cross-Entropy,
- Log likelihood & negative log likelihood `NLL`.

---

# Multi-class classification

The output layer of a multi-class neural network is better as probabilities rather than scores, and if you recall, probabilities of a set should sum up to one. That's best achieved by the **softmax** activation.

$$
P(Z=z_m)=\frac{e^{z_m}}{\sum_{i=0}^Ne^{z_i}}
$$

---

# Data preprocessing

Rarely in life that data is in clean, clear numeric format. The first step, and arguably the most important one, is data preprocessing, that includes feature engineering, data cleaning, and many other techniques that each serves a different purpose.

Some of those techniques is the one-hot encoding.

---

## One-hot encoding

Categorical data are usually textual, to be able to plug such data into models, it needs to be converted to numbers. Number-coding could work for humans and machine alike, but in models, that might incorrectly entail a ranking that is not there (e.g. $1$ is greater than $0$)

For one-hot encoding, each category in the feature is added as its own feature. e.g.: a feature called `temperature` might hold `hot`, `cold`, & `moderate`. One-hot encoding those will lead to three different features, with the same names of the category's entries.

As you can tell, one-hot encoding increases number of features.

---

# Cross-Entropy

Statistics is widely used with machine/deep learning, one of the important topics is the maximum likelihood.

<!-- > There is a statistical technique for finding the best weights called Maximum Likelihood Estimation `MLE`. -->

**Cross-Entropy** is the negative of log of product of probabilities output by the model. That is derived from a simple assumption (for simplicity) that the events are independent.

$$
-\sum_{i=0}^N\sum_{j=0}^M y_{ij}ln(p_{ij}); y_{ij}\in (0,1)
$$

> Remember, Maximum likelihood $\Leftrightarrow$ Minimum cross entropy

---

## Perceptron algorithm vs Gradient Descent

Both of these approaches seem almost identical, but the subtle difference is that the perceptron algorithm updates only on misclassification, while GD updates on all points.

### Logistic regression

Unlike how the name might convey, this algorithm is used for classification. The network outputs probabilities (regression), and we apply the exponent function on them (logistic) to eventually select the highest probability as the predicted class (classification).

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
