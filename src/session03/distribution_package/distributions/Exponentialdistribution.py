#! /usr/bin/env python3
"""The exponential distribution"""
# TODO: import go here, 1st builtins, then custom/local imports
from __future__ import annotations
import math

from .Generaldistribution import Distribution


# TODO: define an exponential distribution class
class Exponential(Distribution):  # noqa: E302
    """Exponential distribution"""

    # TODO: define constructor
    # NOTE: exponential distribution has a single argument, lambda (the rate
    # parameter)
    def __init__(self, rate: float) -> Exponential:
        """The exponential distribution

        Parameters
        ----------
        rate: float
            the rate of the distribution

        Raises
        ------
        ZeroDivisionError
        """
        super().__init__(1 / rate, math.sqrt(1 / rate ** 2))
        self._lam = rate

    @property
    def lam(self):
        return self._lam

    # TODO: define methods for mean, std deviation, & PDF

    # NOTE: pdf is lambda * exp(-lambda * x)
    def pdf(self, x: float) -> float:
        """calculates the PDF of the exponential distribution

        Parameters
        ----------
        x: float
            the random variable

        Returns
        -------
        out: float
            the PDF for the exponential distribution
        """
        if x < 0:
            return 0
        lam = self._lam
        return lam * math.exp(-lam * x)

    # NOTE: mean is 1 / lambda
    def calculate_mean(self) -> float:
        """Calculates the mean for the exponential distribution

        Returns
        -------
        out: float
            the mean of the distribution
        """
        self.mean = 1 / self._lam
        return self.mean

    # NOTE: variance is 1 / lambda^2
    def calculate_stdev(self) -> float:
        """Calculates the standard deviation for exponential distribution

        Returns
        -------
        out: float
            the standard deviation of the distribution
        """
        self.stdev = math.sqrt(1 / self._lam ** 2)
        return self.stdev
