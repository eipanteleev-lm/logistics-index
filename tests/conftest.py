import sys

import pytest
import mock

import pandas as pd


@pytest.fixture()
def df_sample():
    return pd.DataFrame([
        {'A': -2, 'B': -1},
        {'A': -3, 'B': 1},
        {'A': -2, 'B': 0},
        {'A': -1, 'B': 0},
        {'A': -1, 'B': 3}
    ])


distributions = [
    {'A': lambda: -1000},
    {'A': lambda: -100},
    {'A': lambda: -10},
    {'A': lambda: -1},
    {'A': lambda: 0},
    {'A': lambda: 1},
    {'A': lambda: 10},
    {'A': lambda: 100},
    {'A': lambda: 1000}
]

distributions_ids = ['const: {}'.format(d['A']()) for d in distributions]


@pytest.fixture(params=distributions, ids=distributions_ids)
def distribution(request):
    return request.param


sys.modules['config'] = mock.MagicMock()


@pytest.fixture()
def operations_df():
    return pd.DataFrame(
        [
            (
                10, 12345678, -51, 'Продажа', None, 1849,
                pd.Timestamp('2020-01-01 00:00:00')),
            (
                10, 12345678, -52, 'Продажа', None, 1797,
                pd.Timestamp('2020-01-01 12:09:36')),
            (
                10, 12345678, -80, 'Продажа', None, 1870,
                pd.Timestamp('2020-01-03 00:38:24'))
        ],
        columns=[
            "store_id",
            "product_code",
            "quantity",
            "reason",
            "no",
            "stock",
            "created"
        ]
    )


@pytest.fixture()
def operations_weekly_df():
    return pd.DataFrame(
        [
            (
                pd.Timestamp("2020-01-04 00:00:00"), 10, 12345678, -199, 322,
                0, -11, 0, 0, 1900),
            (
                pd.Timestamp("2020-01-11 00:00:00"), 10, 12345678, -268, 728,
                0, -50, -45, 75, 2012),
            (
                pd.Timestamp("2020-01-18 00:00:00"), 10, 12345678, -286, 520,
                -93, -207, 0, 117, 2452)
        ],
        columns=[
            "created",
            "store_id",
            "product_code",
            "sale",
            "shipment",
            "defect",
            "theft",
            "unknown",
            "spec_needs",
            "stock"
        ]
    )


@pytest.fixture()
def price_df():
    return pd.DataFrame(
        [
            (10, 12345678, 64, 0.62, None)
        ],
        columns=[
            "store_id",
            "product_code",
            "selling_price",
            "storage_cost",
            "purchase_price"
        ]
    )
