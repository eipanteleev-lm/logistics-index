import pytest

from src.stats.stock_optimum import stock_optimum


params = [(i, 10 - i) for i in range(11)]
ids = ['k1={0}, k2={1}'.format(*p) for p in params]


@pytest.mark.parametrize('k1, k2', params, ids=ids)
def test_stock_optimum__random(k1, k2, df_sample):

    s = stock_optimum(df_sample, k1, k2)

    assert s >= 0
    assert s <= 3


def test_stock_optimum__max(df_sample):

    s = stock_optimum(df_sample, 0, 10)

    assert s == 3


def test_stock_optimum__min(df_sample):

    s = stock_optimum(df_sample, 10, 0)

    assert s == 0
