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

## Session 16

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

<!-- https://analyticsindiamag.com/ten-famous-quotes-about-artificial-intelligence/ -->

![bg right:33%](https://imageio.forbes.com/specials-images/imageserve/62d700cd6094d2c180f269b9/0x0.jpg)

> I'm increasingly inclined to think that there should be some regulatory oversight, maybe at the national and international level, just to make sure that we don't do something very foolish.
> I mean with artificial intelligence we're summoning the demon.

# [Elon Musk](https://www.forbes.com/profile/elon-musk/), 2014 at MIT

---

# Last session

- Implementing Gradient Descent

---

# Agenda

- Q&A
- Training Neural Networks
- Project 2 Walkthrough
- Q&A _(encore)_

---

# Train, validate & test

In most AI/ML solutions, it is best to split the data into $3$ main sets:

- The training set, which is the largest, and used to train the model,
- The validation set, which is a small set that the model uses for testing during training,
- The testing set, which is another small set that the model only sees at the end of training, no more training afterwards.

---

Some quick sub-setting follows this general rule, but not obligatory:

||Train|Validate|Test|
|:-:|:-:|:-:|:-:|
|classic ML|$60$~$80$%|$10$~$20$%|$10$~$20$%|
|Neural Networks|$90$~$98$%|$1$~$8$%|$1$~$2$%|

## Underfit & Overfit

The most common issues relating to models training, is either you end up with a severely simple model (not much better than random $50$%), or a very bad model that performs great on the training set. Those are underfitting & overfitting respectively.

---

# Model complexity

That might be changes to any hyperparameter: number of epochs, number of layers, the number of neurons per layer, activation functions, etc&#8230;

<!-- https://playground.tensorflow.org/ -->

![cmplx h:350px w:1000px](./../data/img/model-complexity.png)

---

# Regularisation

Simply put, the prediction loss is no longer solely focused on minimising the error, but takes into consideration the weights that build the model. Models with large coefficients are too confident, which later leads to overfitting (error due to variance).

The most common modes for regularisation are:

- Lasso `L1` regularisation,
- Ridge `L2` regularisation,
- ElasticNet regularisation $L1+L2$.

---

# Dropout

As the problem of weights is the main cause of overfitting, there is another attempt, by trying to intentionally (and randomly) _drop_ weights during training. That way, other weights have a chance to contribute to the output, and potentially minimising overfitting.

---

# Local Minima

Almost all datasets are not simple & straightforward, that is reflected on the loss function, which might be something familiar (like MSE), or something special per the case.

The most important part is, it is likely that we might have multiple minima, where it is possible that only one is the global minimum (sometimes more). But plain old Gradient Descent might not arrive at that, depending on where it started.

---

One of several methods to overcome that, is the random restart, where you randomly initialise the weights, and train multiple times, and hopefully one of these times would lead to the global minimum.

Other solutions include:

- Momentum-based GD (more about that ahead),
- Adaptive Gradient, and
- A mixture of both.

> N.B: the same methods mentioned can also be solutions to vanishing & exploding gradients.

---

# Vanishing Gradient

This is a problem that arises mainly from multiplying multiple small numbers, most likely obtained from derivatives of activation functions.

One solution is using different activation functions, amongst are:

<!-- - Sigmoid, this is least recommended as it leads to vanishing gradient -->
- Hyperbolic tangent $tanh$, which gives output in the range $[-1,1]$, much better than sigmoid
- Rectified Linear Unit `relu`, it is advised to avoid this mostly because it has no derivative at $0$, but it mitigates the vanishing gradient issue.

---

# Variants of the Gradient Descent

|Vanilla|Mini-batch|Stochastic|
|:-:|:-:|:-:|
|loss on the entire dataset at once|loss on small equal-sized batches of the dataset|loss of single entry|

- Updates with vanilla GD happen after each epoch, considering all the entries of the dataset.
- Updates with mini-batch & stochastic GD happen after each iteration and considers only the batch/entry in question.

> Vanilla GD is Mini-batch GD with batch size of the entire dataset, Stochastic GD is also mini-batch GD with batch size of one!

---

# Learning rate

Remember how the gradient descent used a portion of the gradient to update the weights? and that portion is determined by a _learning rate_? A question that comes to everybody's mind is, "which value is the best for learning rate?"

Sadly, there is no clear definitive formula for that, mostly just practices, but you can always tune that hyperparameter in order to find the one which fits your dataset the best.

---

# Momentum

Remember how we mentioned few slides ago that local minima issue can be solved by momentum-based GD.

The momentum here is the same concept, as you move down you gain energy, and you lose energy if you go up.

The formula is a tad different though:

$$
\nabla{W_t}^{\prime} = \nabla{W_t}
+ \beta\nabla{W_{t-1}}
+ \beta^2\nabla{W_{t-2}}
+ \dots
+ \beta^{n}\nabla{W_{t-n}}
\\
\nabla{W_0} = 0; \beta \in [0, 1]
$$

---

<!--
_class:
  - lead
  - gaia
-->

# Project 2 Walkthrough <!-- fit -->

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
