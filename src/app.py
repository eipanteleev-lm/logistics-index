import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
from stats.distributions import make_from_df
from stats.index import logistics_index
from stats.stock_optimum import stock_optimum
from stats.negative_stock_expected_value import find_best_solution

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_pickle("week_dataset.pkl").fillna(0)

app.layout = html.Div(children=[
    html.H1(children="""Logistic index"""),
    
    html.Div(children=[
        html.Div(children=[
            html.Label('Item'),
            dcc.Input(id='item-input', value='18122532', type='text', style={'pading': 2, 'marging': 2}),
            html.Label('Store'),
            dcc.Input(id='store-input', value='2', type='text', style={'pading': 2, 'marging': 2}),
            html.Label('Depth'),
            dcc.Slider(
                id='period-slider',
                min=0,
                max=7,
                value=0,
                marks={str(i): str(i) for i in range(0, 8)},
                step=None
            ),
            html.Button(id='submit-button-state', n_clicks=0, children='Submit', 
                style={'pading': 2, 'marging': 2})
        ], style={'pading': 2, 'marging': 2}),
        html.Div(children=[
            html.H2('Recommended order quantity'),
            dcc.Loading(
                id='order-loader',
                type='default',
                children=[
                    html.Div(id='order-output', style={'pading': 2, 'marging': 2})
                ]
            )
        ], style={'pading': 2, 'marging': 2})
    ], style={'columnCount': 2}),


    html.Hr(),

    dcc.Loading(
        id='logistic-loader',
        type='default',
        children=[
            html.Div(id='logistic-index')
        ]
    )
])

@app.callback(
    [Output('logistic-index', 'children'), Output('order-output', 'children')],
    [Input('submit-button-state', 'n_clicks')], 
    [State('item-input', 'value'), State('store-input', 'value'), State('period-slider', 'value')]
)
def return_index(n_clicks, item, store, depth):
    filtered_df = data[data['loc'] == int(store)]
    distributions = make_from_df(filtered_df[["sale", "defect", "spec_needs", "theft", "unknown"]])
    A = stock_optimum(
        filtered_df[["sale", "defect", "spec_needs", "theft", "unknown"]],
        0.62,
        64)

    z = filtered_df['th_stock'].iloc[-1]

    e, p, _ = logistics_index(z, distributions, (0, A), depth, 10000)

    by, be, bp = find_best_solution(z, distributions, (0, A), depth)

    # return f"""\nResult: Current Stock: {z} -E{{Zt|Zt < 0}} = {e} \n P{{0 < Zt < A}} = {p}"""
    return html.Div(children=[
        html.Div(html.H2('Stock: ' + f'{z}'), 
            style={'backgroundColor': '#E1886B', 'pading': 2, 'marging': 2}
        ),
        html.Div(html.H2('Optimum: ' + f'{A}'), 
            style={'backgroundColor': '#8F4EF2', 'pading': 2, 'marging': 2}
        ),
        html.Div(html.H2('-E{Zt|Zt < 0} = ' + f'{-e}'), 
            style={'backgroundColor': '#FFAB33', 'pading': 2, 'marging': 2}
        ),
        html.Div(html.H2(f'P{{0 < Zt < {A}}} = ' + f'{p}'),
            style={'backgroundColor': '#33FF8B', 'pading': 2, 'marging': 2}
        )
    ]), html.Div(children=[
        html.Div(html.H2('Order: ' + f'{by}'), 
            style={'backgroundColor': '#8F4EF2', 'pading': 2, 'marging': 2}
        ),
        html.Div(html.H2('-E{Zt|Zt < 0} = ' + f'{be}'), 
            style={'backgroundColor': '#FFAB33', 'pading': 2, 'marging': 2}
        ),
        html.Div(html.H2(f'P{{0 < Zt < {A}}} = ' + f'{bp}'),
            style={'backgroundColor': '#33FF8B', 'pading': 2, 'marging': 2}
        )
    ])


if __name__ == '__main__':
    app.run_server(debug=True)