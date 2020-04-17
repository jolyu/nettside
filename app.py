# Import dash
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


# Flask Cache
from flask_caching import Cache

# Import copy and pathlibs
import copy
import pathlib

# Import supportlibs
import math
import datetime as dt
import pandas as pd

# Selfmade helpers
from helpers import *
from database import GetDataDF, GetDbRef, GetFirstAndLastDate

initialDays = 7

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
ASSET_PATH = PATH.joinpath("assets").resolve()

# Set up flask and dash server
app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
# Cache timeout is one hour
TIMEOUT = 3600

# Create DB ref
ref = GetDbRef()

# Cache functions to remember the database for up to one hour to reduce stress on the db and enable a multi user setup
@cache.memoize(timeout=TIMEOUT)
def QueryDF(dbRef, dates):
    return GetDataDF(dbRef, dates)

# Cache the first and last date for one hour, then the db does not update every 5 minutes
@cache.memoize(timeout=TIMEOUT)
def getFiaLaDates(dbRef):
    return GetFirstAndLastDate(dbRef)


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

from webpage import GetMainSite
app.layout = GetMainSite(app, ref, initialDays)


@app.callback(
    [
        Output("dbResponse", "children"),
        Output("dbDates", "data"),
        Output("dbDatePicker", "min_date_allowed"),
        Output("dbDatePicker", "max_date_allowed"),
    ],
    [
        Input("fetchDbButton", "n_clicks"),
        Input("dbDatePicker", "start_date"),
        Input("dbDatePicker", "end_date"),
    ]
)
def UpdateDates(nClicks, startDate, endDate):
    dates = GetFirstAndLastDate(ref)
    initialDates = [GetFirstAndLastDate(ref)[1] - dt.timedelta(days=7), GetFirstAndLastDate(ref)[1]]
    changedId = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "fetchDbButton" in changedId:
        date = pd.to_datetime([startDate, endDate])

        QueryDF(ref, date)

        return ["Dataset updated!", date, dates[0], dates[1]]
    return ["", initialDates, dates[0], dates[1]]

@app.callback(
    Output("mainGraph", "figure"),
    [
        Input("dbDates", "data"),
    ]
    
)
def CreateMainGraph(dates):
    if dates == None:
        dates = [GetFirstAndLastDate(ref)[1] - dt.timedelta(days=7),GetFirstAndLastDate(ref)[1]]
    else:
        dates = DaySelectorString(dates)
    print(dates)
    df = QueryDF(ref, dates)
    print(df)
    dff = DataToDays(df)
    layout_main = copy.deepcopy(layout)

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
        ),
    ]

    # More layout settings
    layout_main["title"] = "Total birds per month"
    layout_main["dragmode"] = "select" 
    layout_main["showlegend"] = False
    layout_main["autosize"] = True

    # Create the settings dictionary for the graph
    figure = dict(data=data, layout=layout_main)
    return figure


# Main
if __name__ == "__main__":
    app.run_server(debug=True)