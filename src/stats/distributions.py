from random import random
from typing import Dict, Callable, Any, Union
from pandas import DataFrame


def fit(h: Dict[Any, Union[int, float]]) -> Callable:
    """
    :param h: Dict[Any, Union[int, float]], dict with values and their
        frequencies
    :return: Callable, fuction, generates random values with
    """

    assert h
    vs = sum(h.values())
    vl = sorted(h.items(), key=lambda x: x[0], reverse=True)

    def distribution():
        s = 0
        r = vs*random()
        for k, v in vl:
            s += v
            if s >= r:
                return k

        return vl[-1][0]

    return distribution


def make_from_df(df: DataFrame) -> Dict[Any, Union[int, float]]:
    """
    :param df: pandas.DataFrame, DataFrame for which the distributions needed
        to build
    :return: Dict[Any, Union[int, float]], dict with keys as columns of the x
        DataFrame and values as discrete distributions of values in these
    columns
    """

    return dict((c, fit(df[c].value_counts().to_dict())) for c in df.columns)
