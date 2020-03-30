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

# Helper funtions
from helpers import *
from database import *

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Import data
ref = GetDbRef()
dates = GetFirstAndLastDate(ref)
initialDates = [dates[1] - dt.timedelta(days=180), dates[1]]
global df 
df = GetDataDF(ref, initialDates)

#print(df)

#df = pd.read_csv(DATA_PATH.joinpath("data.csv"), parse_dates=["dates"], low_memory=False, index_col="dates")
#print(df)
#df["dates"] = pd.to_datetime(df["dates"])

# avalible_years = list(set([date.year for date in df.index]))
# avalible_years.sort()
# YEARS = [{'label':str(y), "value":y} for y in avalible_years]
# avalible_months = list(set([date.month for date in df.index]))
# avalible_months.sort()
# avalible_dates = [avalible_years, avalible_months]
#print(avalible_dates)
#print(list(df.columns))
global dff
dff = DataToMonths(df)

#print(dff)

# CACHE_CONFIG = {
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'redis',
#     'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379')
# }
# cache = Cache()
# cache.init_app(app.server, config=CACHE_CONFIG)


layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    barmode="group",
    legend=dict(font=dict(size=10), orientation="h"),
    
)


# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        dcc.Store(id="day_selector"),
        dcc.Store(id="update_graph"),
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
            style={"margin-bottom": "0em"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div([
                            dcc.DatePickerRange(
                                id='db_date_picker',
                                min_date_allowed=dates[0],
                                max_date_allowed=dates[1],
                                start_date=initialDates[0],
                                end_date=initialDates[1]
                            ),
                            html.Div(id='output-container-date-picker-range')
                        ]),
                        html.P(
                            "Range filter (or use histogram):",
                            className="control_label",
                        ),
                        """ dcc.RangeSlider(
                            id="time_slider",
                            min=min(avalible_years),
                            max=max(avalible_years) + 1,
                            value=[min(avalible_years), max(avalible_years)],
                            step=1/12,
                            className="dcc_control",
                        ), 
                        html.P("Filter? Export Currently min height", className="control_label"),
                        dcc.Dropdown(
                            id="year_select",
                            options=YEARS,
                            multi=False,
                            value=max(avalible_years),
                            className="dcc_control",
                        )"""
                    ],
                    className="pretty_container four columns",
                    style={"min-height": "30em"},
                    id="cross-filter-options",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6("0",id="birds_per_time"), html.P("no. birds per day")],
                                    id="birds",
                                    className="mini_container three columns",
                                ),
                                html.Div(
                                    [html.H6("0",id="most_active_time"), html.P("most active time of day")],
                                    id="active_time",
                                    className="mini_container three columns",
                                ),
                                html.Div(
                                    [html.H6("0",id="selected_birds"), html.P("total selected birds")],
                                    id="selected_total",
                                    className="mini_container three columns",
                                ),
                                html.Div(
                                    [html.H6("0",id="total_birds"), html.P("total birds spotted")],
                                    id="total",
                                    className="mini_container four columns",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [dcc.Graph(id="count_graph",)],
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
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="monthAverage")],
                            id="monthAverageContainer",
                            className="pretty_container",
                        )
                    ],
                    id="lower-left-column",
                    className="six columns",
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="dayAverage")],
                            id="dayAverageContainer",
                            className="pretty_container"
                        )
                    ],
                    id="lower-right-column",
                    className="six columns",
                ),
            ],
            className="row flex-display"
        ),
    ],
)


# Create callbacks
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("count_graph", "figure")],
)

# Create Main graph from slider
@app.callback(
    Output("count_graph", "figure"),
    [
        Input("time_slider", "value"),
        Input("update_graph", "data")
    ]
)
def makeCountFigure(timeSlider, data):
    
    ''' Reads the values of the main time slider and updates the main selector graph '''
    # Copy general layout settings
    layout_count = copy.deepcopy(layout)

    # Get times from TimeSlider
    times = TimeSliderToDate(timeSlider)

    # Color the bars according to their selection
    colors = []
    for i in dff.index:
        if i >= times[0] and i < times[1]:
            # If selected, then color blue
            colors.append("rgb(123, 199, 255)")
        else:
            # if not selected, color light blue
            colors.append("rgba(123, 199, 255, 0.2)")
    
    # Insert data from DataFrame dff, which is sorted into months
    data = [
        dict(
            type="scatter",
            mode="markers",
            x=dff.index,
            y=dff["birds"],
            name="All birds",
            opacity=0,
            hoverinfo="skip",
        ),
        dict(
            type="bar",
            x=dff.index,
            y=dff["birds"],
            name="All birds",
            marker=dict(color=colors),
        ),
    ]

    # More layout settings
    layout_count["title"] = "Total birds per month"
    layout_count["dragmode"] = "select" 
    layout_count["showlegend"] = False
    layout_count["autosize"] = True

    # Create the settings dictionary for the graph
    figure = dict(data=data, layout=layout_count)
    return figure

@app.callback(
    Output("update_graph", "data"),
    [
        Input("db_date_picker", "start_date"),
        Input("db_date_picker", "end_date")
    ]
)
def UpdateDB(startDate, endDate):
    global df
    global dff
    #print(startDate, endDate)
    df = GetDataDF(ref, DaySelectorString([startDate, endDate]))
    print(df)
    dff = DataToMonths(df)
    return dt.datetime.now().timestamp()


# Read the main graph and output selection range to slider
# This again runs the update graph, to color the graph correct
@app.callback(
    Output("time_slider", "value"),
    [
        Input("count_graph", "selectedData"),
        Input("year_select", "value"),
    ],
)
def Updateslider(countGraphSelected, year):
    ''' Reads the graph, and the year drop-down, updates the slider'''
    # Check if none items are selected
    if countGraphSelected is None:
        return [year, year + 1]
        
    # Create days from string stored in graph
    nums = DaySelectorString(countGraphSelected["range"]["x"])
    # Returns the year values back to the graph, with step intervals equal to one month
    return [nums[0].year + (nums[0].month - 1) * 1/12 , nums[1].year + nums[1].month * 1/12]

@app.callback(
    Output("aggregate_data", "data"),
    [Input("time_slider", "value")],
)
def UpdateQuickFacts(timeSlider):
    averageBirds = AverageBirdDay(df, timeSlider)
    selTotal = TotalSelBirds(dff, timeSlider)
    total = SumOfBirds(dff, "birds")

    return [averageBirds, selTotal, total]


@app.callback(
    [
        Output("birds_per_time", "children"),
        Output("selected_birds", "children"),
        Output("total_birds", "children"),
    ],
    [Input("aggregate_data", "data")],
)
def UpdateText(data):
    #print(data)
    return [str(i) for i in data]

@app.callback(
    Output("monthAverage", "figure"),
    [Input("time_slider", "value"),
    #Input("monthAverage", "selectedData"),
    Input("day_selector", "data")],
)
def CreateMonthGraph(timeSlider, daySelector):
    layout_count = copy.deepcopy(layout)

    times = TimeSliderToDate(timeSlider)
    dff = FilterData(df, times[0], times[1])
    dfff = DataToDays(dff)
    days = DaySelectorString(daySelector)

    colors = []
    for i in dfff.index:
        if i >= days[0] and i < days[1]:
            colors.append("rgb(123, 199, 255)")
        else:
            colors.append("rgba(123, 199, 255, 0.2)")

    data = [
        dict(
            type="scatter",
            mode="markers",
            x=dfff.index,
            y=dfff["birds"],
            name="All birds",
            opacity=0,
            hoverinfo="skip",
        ),
        dict(
            type="bar",
            x=dfff.index,
            y=dfff["birds"],
            name="All birds",
            marker=dict(color=colors),
        ),
    ]

    layout_count["title"] = "Day to day basis"
    layout_count["dragmode"] = "select"
    layout_count["showlegend"] = False
    layout_count["autosize"] = True

    figure = dict(data=data, layout=layout_count)
    return figure

@app.callback(
    Output("day_selector", "data"),
    [Input("monthAverage", "selectedData"),
    Input("time_slider", "value")],
)
def UpdateDaySel(daySelector, timeSlider):
    days = []
    if daySelector is None:
        days = TimeSliderToDate(timeSlider)
    else:
        days = daySelector["range"]["x"]
    #print(days)
    return days

@app.callback(
    Output("dayAverage", "figure"),
    [Input("day_selector", "data")]
)
def CreateDayGraph(dates):
    layout_count = copy.deepcopy(layout)

    dates = DaySelectorString(dates)
    dff = FilterData(df, dates[0], dates[1])

    dfff = HourAverage(dff)
    #print(dfff)
    data = [
        dict(
            type="scatter",
            mode="markers",
            x=dfff.index,
            y=dfff["birds"],
            name="All birds",
            opacity=0,
            hoverinfo="skip",
        ),
        dict(
            type="spline",
            line=dict(shape="spline"),
            x=dfff.index,
            y=dfff["birds"],
            name="All birds",
            marker=dict(color="rgb(123, 199, 255)"),
        ),
    ]

    layout_count["title"] = "Hourly"
    layout_count["dragmode"] = "select"
    layout_count["showlegend"] = False
    layout_count["autosize"] = True

    figure = dict(data=data, layout=layout_count)
    return figure





# Main
if __name__ == "__main__":
    app.run_server(debug=True)