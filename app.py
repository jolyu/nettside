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
from database import GetDataDF, GetDbRef, GetFirstAndLastDate, GetInitialDates

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

colors = [
    "rgb(123, 199, 255)",
    "rgb(0, 204, 31)",
    "rgb(0, 0, 0)"
]

from webpage import GetMainSite
app.layout = GetMainSite(app, ref, initialDays)

# Create callbacks
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("mainGraph", "figure")],
)

@app.callback(
    [
        Output("dbResponse", "children"),
        Output("dbDates", "data"),
        Output("dbDatePicker", "min_date_allowed"),
        Output("dbDatePicker", "max_date_allowed"),
        Output("checklistShow", "options"),
        Output("checklistShow", "value"),
    ],
    [
        Input("fetchDbButton", "n_clicks"),
    ],
    [
        State("dbDatePicker", "start_date"),
        State("dbDatePicker", "end_date"),
    ]
)
def UpdateDates(nClicks, startDate, endDate):
    dates = GetFirstAndLastDate(ref)

    date = pd.to_datetime([startDate, endDate])

    df = QueryDF(ref, date)
    columns = list(df)

    options = []
    values = []
    for c in columns[1:]:
        options.append(dict(
            label=c.capitalize(),
            value=c,
        ))
        values.append(c)

    response = "Dataset updated with data between " + str(date[0]) + " and " + str(date[1]) + "."
    return [response, date, dates[0], dates[1], options, values]

@app.callback(
    Output("mainGraph", "figure"),
    [
        Input("dbDates", "data"),
    ]
    
)
def CreateMainGraph(dates):
    if dates == None:
        dates = GetInitialDates(ref, initialDays)
    else:
        dates = DaySelectorString(dates)
    #print(dates)
    df = QueryDF(ref, dates)
    #print(df)
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
            marker=dict(color="rgb(123, 199, 255)"),
        ),
    ]

    # More layout settings
    layout_main["title"] = "Total birds per day"
    layout_main["dragmode"] = "select" 
    layout_main["showlegend"] = False
    layout_main["autosize"] = True

    # Create the settings dictionary for the graph
    figure = dict(data=data, layout=layout_main)
    return figure

@app.callback(
    Output("secondGraph", "figure"),
    [
        Input("mainGraph", "selectedData"),
        Input("checklistShow", "value")
    ],
    [
        State("dbDates", "data"),
    ]
)
def CreateSecondGraph(data, checked, dbDates):
    layout_second = copy.deepcopy(layout)
    
    

    if dbDates == None:
        dbDates = GetInitialDates(ref, initialDays)
    else:
        dbDates = pd.to_datetime(dbDates)

    dates = []
    if data == None:
        dates = dbDates
    else:
        dates = DaySelectorString(data["range"]["x"])

    df = QueryDF(ref, dbDates)
    dff = FilterData(df, dates[0], dates[1])

    columns = list(dff)
    
    print(checked)
    if checked == None:
        checked = columns
    else:
        checked.append(columns[0])

    data = []

    def getYaxis(n):
        if n > 0:
            return str(n + 1)
        return ""

    i = 0

    for indx, c in enumerate(columns):
        print(c)
        if c in checked:
            data.append(
                dict(
                    type="spline",
                    x=dff.index,
                    y=dff[c],
                    name=c.capitalize(),
                    marker=dict(color=colors[indx]),
                    
                )
            )

            layout_second.update({"yaxis" + getYaxis(indx): dict(
                title=c.capitalize(),
                color=colors[indx],
                tickfont=colors[indx],
            )})

            if indx > 0:
                data[i].update(yaxis="y" + getYaxis(indx))
                layout_second["yaxis" + getYaxis(indx)].update(
                    overlaying="y",
                    side="right",
                    anchor="free",
                    position= 1 - (indx - 1) * 0.05,
                )
            i += 1
        



    #print(data)
    #print(layout_second)
    # More layout settings
    layout_second["title"] = "Selected data"
    layout_second["dragmode"] = "select" 
    layout_second["showlegend"] = True
    layout_second["autosize"] = True
    layout_second["hovermode"] = "y unified"

    layout_second["xaxis"] = dict(domain=[0,1 - max(0, len(columns) - 2) * 0.05])

    # Create the settings dictionary for the graph
    figure = dict(data=data, layout=layout_second)
    return figure



# Main
if __name__ == "__main__":
    app.run_server(debug=True)