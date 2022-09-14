#! /usr/bin/env python3
"""
"""

import pandas as pd


def get_dataframe() -> pd.DataFrame:
    """ """
    return pd.read_csv(
        "https://github.com/jennybc/gapminder/raw/main/data-raw/04_gap-merged.tsv",
        sep="\t",
    )
