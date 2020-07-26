import pytest
import pandas as pd

from src.stats.distributions import fit, make_from_df


def test_fit__simple():
    """
    fit () should return callable, which returns one of the passed dictionary's keys
    """

    test_data = {
        1: 0.5, 
        2: 0.5
    }

    d = fit(test_data)
    
    assert callable(d)
    assert all([d() in (1, 2) for i in range(10)])


def test_fit__empty():
    """
    fit() should raise an exception if empty dict passed
    """

    test_data = dict()

    with pytest.raises(AssertionError):
        _ = fit(test_data)


def test_make_from_df__simple():
    """
    make_from_df should return dict of callable objects
    """

    data = pd.DataFrame([
        {"A": 1, "B": 2},
        {"A": 2, "B": 3},
        {"A": 1, "B": 3}
    ])

    d = make_from_df(data)

    assert isinstance(d, dict)
    assert all([callable(e) for e in d.values()])
    assert set(data.columns) == set(d.keys())
    assert all([d['A']() in (1, 2) for i in range(10)])
    assert all([d['B']() in (2, 3) for i in range(10)])


def test_make_from_df_empty():
    """
    make_from_df should raise an exception if empty DataFrame passed
    """

    data = pd.DataFrame(columns=['A', 'B'])

    with pytest.raises(AssertionError):
        _ = make_from_df(data)
