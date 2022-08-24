#! /usr/bin/env python3
"""The continuous uniform distribution"""
# TODO: std library import
from __future__ import annotations

import math

# TODO: parent class import
from .Generaldistribution import Distribution


# TODO: define a new class for continuous uniform distribution, that is a child
# of distribution
class ContinuousUniform(Distribution):  # noqa: E302

    # TODO: define a constructor
    # NOTE: Continuous uniform distribution has 2 args: a (inclusive start of
    # range) and b (inclusive end of range)
    def __init__(self, left: float, right: float) -> ContinuousUniform:
        """The Continuous Uniform distribution

        Parameters
        ----------
        left: float
            the inclusive start of the range of distribution
        right: float
            the inclusive end of the range of distribution, strictly greater
            than `left`

        Raises
        ------
        ValueError
        """
        super().__init__((left + right) / 2, math.sqrt(((right - left) ** 2) / 12))
        if right >= left:
            raise ValueError(
                "Right end of the distribution must be strictly"
                + " greater than left end"
            )
        self._a = left
        self._b = right

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    # TODO: define methods for calculating mean, std deviation & PDF
    # NOTE: PDF of continuous uniform distribution is 1/b-a for x in [a,b], 0
    # otherwise
    def pdf(self, x: float) -> float:
        """Calculates the PDF for continuous uniform distribution

        Parameters
        ----------
        x: float
            the location to find pdf at

        Returns
        -------
        out: float
            The calculated PDF
        """
        a = self._a
        b = self._b
        if x >= a and x <= b:
            return 1 / (b - a)
        return 0

    # NOTE: mean is (a + b) / 2
    def calculate_mean(self) -> float:
        """Calculates the mean of continuous uniform distribution

        Returns
        -------
        out: float
            the mean of the distribution
        """
        self.mean = (self._a + self._b) / 2
        return self.mean

    # NOTE: variance is ((b - a)^2) / 12
    def calculate_stdev(self) -> float:
        """Calculates the standard deviation of the continuous uniform
        distribution

        Returns
        -------
        out: float
            the standard deviation of the distribution
        """
        self.stdev = math.sqrt(((self._b - self._a) ** 2) / 12)
        return self.stdev
