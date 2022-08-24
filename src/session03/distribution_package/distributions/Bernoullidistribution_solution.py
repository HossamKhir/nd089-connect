#! /usr/bin/env python3
"""The Bernoulli distribution"""
from __future__ import annotations
import math

from .Binomialdistribution import Binomial

# TODO: import the parent distribution for the Bernoulli distribution
from .Generaldistribution import Distribution


# TODO: define a bernoulli class that inherits from a parent distribution
class Bernoulli(Distribution):  # noqa: E302
    """The Bernoulli distribution"""

    # TODO: a good practice is to have a pydoc for the class

    # TODO: type in code for constructor (a magic method)
    # NOTE: Bernoulli uses only 2 arguments p (probability) and q = 1-p, so
    # actually one
    def __init__(self, prob: float = 0.5) -> Bernoulli:
        """Instantiates a distribution of Bernoulli

        Parameters
        ----------
        prob: float
            the probability of success
        """
        super().__init__(prob, (prob * (1 - prob)) ** 0.5)
        # NOTE: A good practice is that a parent's constructor is the first
        # call inside the child constructor
        self.p = prob

    # TODO: implement methods to calculate mean, standard deviation, and PMF
    # NOTE: the mean for the Bernoulli distribution is `p`
    def calculate_mean(self) -> float:
        """calculates the mean for Bernoulli's distribution

        Returns
        -------
        out: float
            the mean for the Bernoulli's distribution
        """
        self.mean = self.p
        return self.mean

    # NOTE: the variance for the Bernoulli distribution is `p*q`
    def calculate_stdev(self) -> float:
        """calculates the standard deviation of Bernoulli's distribution

        Returns
        -------
        out: float
            the standard deviation of the Bernoulli distribution
        """
        self.stdev = math.sqrt(self.p * (1 - self.p))
        return self.stdev

    # NOTE: the PMF for Bernoulli distribution is `(p**k)*(q**(1-k))`
    def pmf(self, k: int = 1) -> float:
        """calculates the PMF for Bernoulli's distribution

        Parameters
        ----------
        k: int
            the expected outcome, 1 for success, 0 for failure

        Returns
        -------
        out: float
            the PMF of Bernoulli's distribution
        """
        p = self.p
        q = 1 - self.p
        return (p ** k) * (q ** (1 - k))


# NOTE: a Bernoulli distribution is a special case of the Binomial distribution
#   where number of trials equals to 1
class Bern(Binomial):
    """An illustration of inheritance using a child class of a parent class as
    a parent to another"""

    def __init__(self, prob: float = 0.5) -> Bern:
        """Instantiates a distribution of Bernoulli

        Parameters
        ----------
        prob: float
            the probability of success
        """
        super().__init__(prob, 1)

    def pdf(self, k: int = 1) -> float:
        """This is an example on why it is not recommended to inherit
        from Binomial despite the Bernoulli being a special case. As Bernoulli
        is discrete, it can't have PDF, only PMF

        Parameters
        ----------
        k: int
            the expected outcome, 1 for success, 0 for failure

        Returns
        -------
        out: float
            the PMF for Bernoulli
        """
        return self.pmf(k)

    def pmf(self, k: int = 1) -> float:
        """calculates the PMF for Bernoulli's distribution

        Parameters
        ----------
        k: int
            the expected outcome, 1 for success, 0 for failure

        Returns
        -------
        out: float
            the PMF of Bernoulli's distribution
        """
        return self.pdf(k)

    def replace_stats_with_data(self):
        """Since Bernoulli discrete and not affected by multiple consecutive
        trials, this method becomes useless to use/implement"""
        pass
