# -*- coding: utf-8 -*-

# Run this app with `python chum.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


valuation_card = dbc.Card(   
    [
        dbc.CardHeader("Total Valuation"),
        dbc.CardBody(
            [
                html.H3(id='valuation-output-container',className="card-title text-center"),
            ]
        )
    ],
    style={"width": "15rem"},
)

investment_card = dbc.Card(
    [
        dbc.CardHeader("Investment Amount"),
        dbc.CardBody(
            [
                html.H3(id='investment-output-container',className="card-title text-center"),
            ]
        )
    ],
    style={"width": "15rem"},
)

equity_card = dbc.Card(
    [
        dbc.CardHeader("Equity Percentage"),
        dbc.CardBody(
            [
                html.H3(id='equity-output-container',className="card-title text-center"),
            ]
        )
    ],
    style={"width": "15rem"}
)


app.layout = dbc.Container(
    [
        html.Div(children=[
            html.Br(),

            html.H1(children='CHUM', className="text-center"),
            html.H4(children='The Shark Tank TV show companion app!', className="text-center"),

            html.Br(),

            dbc.Row(
                [
                    dbc.Col(valuation_card, width="auto"),
                    dbc.Col(investment_card, width="auto"),
                    dbc.Col(equity_card, width="auto")
                ],
                justify = "center"
            ),

            html.Br(),

            html.H4(children='''
                Investment amount
            '''),

            html.Br(),

            html.Div(children=[
                dcc.Slider(
                    id = 'investment-slider',
                    min = 100000,
                    max = 500000,
                    step = 10000,
                    marks = {
                        100000: '$100K',
                        150000: '$150K',
                        200000: '$200K',
                        250000: '$250K',
                        300000: '$300K',
                        350000: '$350K',
                        400000: '$400K',
                        450000: '$450K',
                        500000: '$500K'
                    },
                    value = 150000,
                    tooltip = {"always_visible" : False, "placement" : "top"}
                )
            ]),

            html.Br(),

            html.H4(children='''
                Equity percentage
            '''),

            html.Br(),

            html.Div(children=[
                dcc.Slider(
                    id = 'equity-slider',
                    min = 5,
                    max = 35,
                    step = 0.5,
                    marks = {
                        5: '5%',
                        10: '10%',
                        15: '15%',
                        20: '20%',
                        25: '25%',
                        30: '30%',
                        35: '35%'
                    },
                    value = 15,
                    tooltip = {"always_visible" : False, "placement" : "top"}
                )
            ]),
        ])
    ]
)


@app.callback(
    [
        dash.dependencies.Output('equity-output-container', 'children'),
        dash.dependencies.Output('valuation-output-container', 'children'),
        dash.dependencies.Output('investment-output-container', 'children')
    ],
    [
        dash.dependencies.Input('investment-slider', 'value'),
        dash.dependencies.Input('equity-slider', 'value')
    ]
)
def update_output(investment_value, equity_value):
    equity_percent = f"{equity_value:.1f}%"
    investment_amt = f"${investment_value:,}"

    percentage = equity_value / 100
    valuation = f"${investment_value / percentage:,.2f}"

    return equity_percent, valuation, investment_amt


if __name__ == '__main__':
    app.run_server(debug=True)
    