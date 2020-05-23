from functools import reduce
from typing import Union, Dict, Callable, Tuple
from stats.negative_stock_expected_value import deep_next

def logistics_index(z: Union[int, float], d: Dict[Union[int, float], Callable], bounds: Tuple[Union[int, float]], depth: int, n: int=100, **kwargs) -> Tuple[Union[int, float]]:
    """
    :param z: Union[int, float], current stock level
    :param d: Dict[Union[int, float], Callable], key - column, value - function to generate value
    :param bounds: Tuple[Union[int, float]], z value boundaries (B, A)
    :param depth: int, number of period to generate
    :param n: int, number of times to generate
    """

    zl = [deep_next(0, z, d, depth, **kwargs) for i in range(n)]
    nz = list(filter(lambda x: x < 0, zl))
    bl = reduce(lambda s, e: s + 1, filter(lambda x: x >= bounds[0] and x <= bounds[1], zl))

    if not nz:
        return 0, bl/n, sum(zl)/n

    return sum(nz)/len(nz), bl/n, sum(zl)/n


