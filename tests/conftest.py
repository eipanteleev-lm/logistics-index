import pytest
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
