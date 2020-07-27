import mock

import pandas

from src import connections


@mock.patch('psycopg2.connect', mock.MagicMock())
@mock.patch('pandas.read_sql', mock.Mock())
def test_operations(operations_df):
    """ operations() """

    pandas.read_sql.return_value = operations_df

    df = connections.operations(12345678, 10)

    assert df.equals(operations_df)


@mock.patch('psycopg2.connect', mock.MagicMock())
@mock.patch('pandas.read_sql', mock.MagicMock())
def test_operations_weekly(operations_weekly_df):
    """ operations_weekly() """

    pandas.read_sql.return_value = operations_weekly_df

    df = connections.operations_weekly(12345678, 10)

    assert df.equals(operations_weekly_df)


@mock.patch('psycopg2.connect', mock.MagicMock())
@mock.patch('pandas.read_sql', mock.Mock())
def test_price(price_df):
    """ price() """

    pandas.read_sql.return_value = price_df

    df = connections.price(12345678, 10)

    assert df.equals(price_df)
