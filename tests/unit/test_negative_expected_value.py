import pytest
import random

from src.stats.negative_stock_expected_value import next, deep_next, logistics_index, negative_expected_value


def test_next():
    """ next() """

    test_d = {'A': lambda: (1 if random.random() > 0.5 else 2)}

    z = next(10, 5, test_d)

    assert z == 16 or z == 17


def test_deep_next():
    """ deep_next() """

    test_d = {'A': lambda: (1 if random.random() > 0.5 else 2)}

    zl = [deep_next(10, 5, test_d, 1) for i in range(10)]

    assert all([z in (17, 18, 19) for z in zl])


def test_logistics_index__random(distribution):

    e, p, _ = logistics_index(10, distribution, (0, 100), 1)

    assert e <= 0
    assert p >= 0
    assert p <= 1


def test_negative_expected_value__random(distribution):

    test_d = distribution

    e, p = negative_expected_value(10, 5, (0, 100), test_d, 10)

    assert e >= 0 
    assert p >= 0
    assert p <= 1


def test_negative_expected_value__in_bounds():
    """ negative_expected_value() """

    test_d = {'A': lambda: (1 if random.random() > 0.5 else 2)}

    e, p = negative_expected_value(10, 5, (0, 100), test_d, 10)

    assert e == 0 
    assert p == 1


def test_negative_expected_value__not_in_bounds_negative():
    """ negative_expected_value() """

    test_d = {'A': lambda: (-20 if random.random() > 0.5 else -30)}

    e, p = negative_expected_value(10, 5, (0, 100), test_d, 10)

    assert e > 0 
    assert p == 0


def test_negative_expected_value__not_in_bounds_positive():
    """ negative_expected_value() """

    test_d = {'A': lambda: (200 if random.random() > 0.5 else 300)}

    e, p = negative_expected_value(10, 5, (0, 100), test_d, 10)

    assert e == 0 
    assert p == 0
