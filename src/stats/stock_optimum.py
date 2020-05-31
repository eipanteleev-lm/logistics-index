from typing import Union
from pandas import DataFrame

def stock_optimum(df: DataFrame, k1: Union[int, float], k2: Union[int, float]) -> Union[int, float]:
    """
    :param df: DataFrame, stock moving data
    :param k1: int or float, in case of perishable product - storage cost + purchase price 
                             else - only storage cost
    :param k2: int or float, selling price
    :return: int or float, optimal value for stock level
    """

    l = sorted(df.sum(axis=1).values, reverse=True)
    if l:
        return -l[-1] if k2/(k1+k2) == 1 else -l[int(len(l)*k2/(k1+k2))]
        
    return 0

def order_optimum(df: DataFrame, k1: Union[int, float], k2: Union[int, float], z: Union[int, float], depth: int):
    """
    :param df: DataFrame, stock moving data
    :param k1: int or float, in case of perishable product - storage cost + purchase price 
                             else - only storage cost
    :param k2: int or float, selling price
    :return: int or float, optimal order quantity
    """
    if depth == 1:
        return stock_optimum(df, k1, k2) - z

    return stock_optimum(df, k1, k2) - z + depth * df.sum(axis=1).mean()
