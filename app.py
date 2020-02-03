# Import required libraries
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

import json
from textwrap import dedent as d

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Import data
df = pd.read_csv(DATA_PATH.joinpath("data.csv"), low_memory=False)
print(df)
df["Dates"] = pd.to_datetime(df["Dates"])


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("jolyu.svg"),
                            id="jolyu-logo",
                            style={
                                "height": "8em",
                                "width": "auto",
                                "margin-bottom": "4em",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Bird Statictics",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "System overview", style={"margin-top": "0em"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://jolyu.no/",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "1em"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P(
                            "Range filter (or use histogram):",
                            className="control_label",
                        ),
                        dcc.RangeSlider(
                            id="time_slider",
                            min=1960,
                            max=2017,
                            value=[1990, 2010],
                            className="time_control",
                        ),
                        html.P("Filter? Currently min height", className="control_label"),
                    ],
                    className="pretty_container four columns",
                    style={"min-height": "25em"},
                    id="cross-filter-options",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="birds_per_time"), html.P("No. birds per day")],
                                    id="birds",
                                    className="mini_container",
                                    style={"width":"auto"},
                                ),
                                html.Div(
                                    [html.H6(id="most_active_time"), html.P("Most active time of day")],
                                    id="active_time",
                                    className="mini_container",
                                    style={"width":"auto"},
                                ),
                                html.Div(
                                    [html.H6(id="total_birds"), html.P("Total birds spotted")],
                                    id="total",
                                    className="mini_container",
                                    style={"width":"auto"},
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [dcc.Graph(id="count_graph",
                            figure={
                                'data': [dict(
                                    x=df["Dates"],
                                    y=df["Random"],
                                    type="bar",
                                )],                                
                            },
                            config={
                                'showAxisRangeEntryBoxes':True,
                            }
                            )],
                            id="countGraphContainer",
                            className="pretty_container",
                            
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div([
            dcc.Markdown(d("""
                **Zoom and Relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """)),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
    ],)

@app.callback(
    Output('relayout-data', 'children'),
    [Input('count_graph', 'relayoutData')])
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)


# Main
if __name__ == "__main__":
    app.run_server(debug=True)