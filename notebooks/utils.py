#! /usr/bin/env python3
"""
"""

import pandas as pd


def get_dataframe() -> pd.DataFrame:
    """ """
    return pd.read_csv("../data/raw/gapminder.tsv", sep="\t")
