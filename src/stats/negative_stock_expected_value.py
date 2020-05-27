from typing import Dict, Callable, Union, Tuple

def next(y: Union[int, float], z: Union[int, float], d: Dict[Union[int, float], Callable], **kwargs) -> Union[int, float]:
    """
    :param y: Union[int, float], order quantity
    :param z: Union[int, float], current stock level
    :param d: Dict[Union[int, float], Callable], key - column, value - function to generate value 
    :return: Union[int, float], generated new stock level
    """
        
    if not isinstance(d, dict):
        raise TypeError(f'Expected dict type for distributions, got: {type(d)}')
    
    return z + y + sum(d[c]() for c in d if c not in kwargs) + sum(f(d[c]()) for f, c in kwargs.values())

def deep_next(y: Union[int, float], z: Union[int, float], d: Dict[Union[int, float], Callable], depth: int, **kwargs) -> Union[int, float]:
    """
    :param y: Union[int, float], order quantity
    :param z: Union[int, float], current stock level
    :param d: Dict[Union[int, float], Callable], key - column, value - function to generate value 
    :param depth: int, numper of periods to generate
    :return: Union[int, float], generated new stock level after periods from depth
    """
    if depth == 0:
        return next(y, z, d, **kwargs)
    
    return deep_next(y, max(0, next(0, z, d, **kwargs)), d, depth - 1)

def negative_expected_value(y: Union[int, float], z: Union[int, float], z_range: Tuple[Union[int, float]], d:Dict[Union[int, float], Callable], n:int, depth:int=1, **kwargs) -> Tuple[Union[int, float]]:
    """
    :param y: int or float, the order quantity
    :param z: int or float, the current stock level
    :param z_range: tuple, z value boundaries (B, A)
    :param d: list, list of distributions to be realised
    :param n: int, number of realisations to generate
    :param depth: int, number of periods to generate
    :return: tuple, -E{Z|Z < 0}, P{B < Z < A}
    """

    negative_z_count = 0
    negative_z_sum = 0
    unacceptable_z_count = 0

    for i in range(n):
        z_next = deep_next(y, z, d, depth, **kwargs) # {'theft': (lambda x: m.predict(x)[0], 'sale')}
        if z_next < 0:
            negative_z_count += 1
            negative_z_sum += z_next

        if z_next <= z_range[0] or z_next >= z_range[1]:
            unacceptable_z_count += 1

    if negative_z_count == 0:
        return 0, 1 - unacceptable_z_count / n

    return -negative_z_sum / negative_z_count, 1 - unacceptable_z_count / n

def find_best_solution(z: Union[int, float], d: Dict[Union[int, float], Callable], bounds:Tuple[Union[int, float]], n:int, depth:int=0, **kwargs) -> Union[int, float]:
    """
    :param z: int or float, the current stock level
    :param bounds: tuple, z value boundaries (B, A)
    :param d: list, list of distributions to be realised
    :param depth: int, number of periods to generate
    :param n: int, number of realisations to generate
    :return: int or float, the order quantity
    """
    
    be, bp, by = bounds[1], 0, 0
    for y in range(0, int(bounds[1]) + 2, 2):
        e, p = negative_expected_value(y, z, bounds, d, n, depth, **kwargs)
        if bp < 0.9:
            if p > bp:
                be, bp, by = e, p, y
        
        else:
            if p > 0.9 and e <= be:
                be, bp, by = e, p, y
    
    return by, be, bp