#!/usr/bin/env python3
##################################################################################################################
##################################################################################################################
#####                                                                                                        #####
#####  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xddddddddddddddddddddddddddddddxKWMMMMMMM  #####
#####  MMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMNl                                lWMMMMMMM  #####
#####  MMMMMM0c,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cKMMMMMMMMMMMMMWx,''''''''''''''''''''''''''.    lWMMMMMMM  #####
#####  MMMMMMk.                                  .OMMMMMMMMMMMMMMWNNNNNNNNNNNNNNNNNNNNNNNNNNNO'   lWMMMMMMM  #####
#####  MMMMMMXxoooooooooooooo,    ;ooooooooooooooxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0'   lWMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMWd   .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWO'   lWMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMNc    cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:,,,,,,,,,,,,,,,,,,,,,,,,,,'    lWMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMk.    .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo                                oWMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMM0,      ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMWo   .lxxxxxxxxxxxxxxxxxxxxxxxxxxkKWMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMWO'   ;;   ,OWMMMMMMMMMMMMMMMMMMMMMMMMMWo   'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMXo.   cXXc   .oXMMMMMMMMMMMMMMMMMMMMMMMMWd   'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMXd'   .oNMMNo.   'dXWMMMMMMMMMMMMMMMMMMMMMWd   .d000000000000000000000000000KXMMMMMMM  #####
#####  MMMMMMMMMMMMW0o'    ;OWMMMMWO;    .lONMMMMMMMMMMMMMMMMMMMWo     ............................oWMMMMMM  #####
#####  MMMMMMMMWXOo,.    ,xNMMMMMMMMNk;.    'lkKNMMMMMMMMMMMMMMMWd.                               .oWMMMMMM  #####
#####  MMMMMKdl;.     .:kNMMMMMMMMMMMMNOc.     .,:o0WMMMMMMMMMMMMN000000000000000000000000000000000XMMMMMMM  #####
#####  MMMMMO'     .:dKWMMMMMNK00KNMMMMMWXkc'.    'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMWk,,:oOXWMMMMMMMMO'..'kMMMMMMMMMN0xl::kWMMMMMMMMWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMM  #####
#####  MMMMMMWNNMMMMMMMMMMMMMk.  .kMMMMMMMMMMMMMMWMMMMMMMMMNo,'''''''''''''''''''''''''''''''''''''''',oNMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMk.  .kMMMMMMMMMMMMMMMMMMMMMMMMX:                                          :XMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMk.  .kMMMMMMMMMMMMMMMMMMMMMMMMWOdddddddddo,   .cddddddddddc.   ,odddddddddOWMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMk.  .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMk.  .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMMWNNNNNNNNNNNNNNNNNNd.  .dNNNNNNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMNo...................    ...................oNMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMX:                                          :XMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMWOddddddddddddddddddddddddddddddddddddddddddOWMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkdxXMMMMMMMMMMMMMWo   '0MMMMMMMMMM0'   oWMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMWOl:l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMNc  .kMMMMMMMMMMMMMWd.  ,0MMMMMMMMMM0,  .dWMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMK,   :XMMMMMMMMMMMMMMMMMMMMMMMMMMMNc  .kMMMMMMMMMMMMMMXOkk0NMMMMMMMMMMN0kkOXMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMNk:;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMNc  .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc  .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMKxdxKMMMMMMMMWXOdlcccldOXWMMMMMMMNc  .kMMMMNOddkNMMMMMMMMW0xdxKMMNOddONMMMMMMMW0ddkNMMMMM  #####
#####  MMMMMMMMMMWo  .dMMMMMMWOc.   ..    .l0WMMMMMNc  .kMMMMXc  .dWMMMMMMMK;  .OMMK,  ,KMMMMMMMX:  'OMMMMM  #####
#####  MMMMMMMMMMWo  .dMMMMMXl.  'lk000kc.  .dNMMMMNc  .kMMMMMO.  ,0MMMMMMWx.  lNMMK,  ,KMMMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMMNl   cXMMMMMMW0;  .dWMMMNc  .kMMMMMNo   lNMMMMMK;  '0MMMK,  ,KMMMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMMk.  ,KMMMMMMMMMO.  '0MMMNc  .kMMMMMMX;  .xWMMMWd.  oWMMMK,  ,KMMMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMWd.  cNMMMMMMMMMX;  .kMMMNc  .kMMMMMMMO'  ,0MMMK,  ;KMMMMK,  ,KMMMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMWd.  cNMMMMMMMMMK;  .kMMMNc  .kMMMMMMMWx.  :XMNo  .kWMMMMK,  '0MMMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMMO'  '0MMMMMMMMWk.  ;KMMMNc  .kMMMMMMMMWd.  oNO.  lNMMMMMX;  .kMMMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dMMMMWd.  ,OWMMMMMNx'  .kWMMMNc  .xWWMMMMMMMNo. .c,  ;KMMMMMMWd.  ;0WMMMMMX;  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMMMNx'  .;ldxdl,.  ,OWMMMMWx.  .:cxXMMMMMMNl     'OMMMMMMMMXl.  .:odddoc.  .OMMMMM  #####
#####  MMMMMMMMMMWo  .dWMMMMMWXd;.       .:xXMMMMMMMNx,.   '0MMMMMMMNl   .xWMMMMMMMMMNk:..        ..cKMMMMM  #####
#####  MMMMMMMMMMNc  .xMMMMMMMMMWX0kxdxk0XWMMMMMMMMMMMNKOkk0WMMMMMMMWx. .dWMMMMMMMMMMMMWX0kxxxxkk0KXNMMMMMM  #####
#####  MMMMMMWWNXd.  ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWWWN0l. .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMM0:,'.   ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;,;;'.  ;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMM0c,',;lkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:,'',:oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  #####
#####                                                                                                        #####
##################################################################################################################
##################################################################################################################



##################################################################################
##### Created by Øyvind Skaaden for jolyu. ELSYS project at NTNU spring 2020 #####
##################################################################################



#######################################################################################
#######################################################################################
#####                                                                             #####
#####  db    db  .d8b.  d8888b. d888888b  .d8b.  d8888b. db      d88888b .d8888.  #####
#####  88    88 d8' `8b 88  `8D   `88'   d8' `8b 88  `8D 88      88'     88'  YP  #####
#####  Y8    8P 88ooo88 88oobY'    88    88ooo88 88oooY' 88      88ooooo `8bo.    #####
#####  `8b  d8' 88~~~88 88`8b      88    88~~~88 88~~~b. 88      88~~~~~   `Y8b.  #####
#####   `8bd8'  88   88 88 `88.   .88.   88   88 88   8D 88booo. 88.     db   8D  #####
#####     YP    YP   YP 88   YD Y888888P YP   YP Y8888P' Y88888P Y88888P `8888Y'  #####
#####                                                                             #####
#######################################################################################
#######################################################################################

# How many days in the past should be shown when launching the app
initialDays = 7

# Colors for different lines
colors = [
    "rgb(166,206,227)",
    "rgb(31,120,180)",
    "rgb(178,223,138)",
    "rgb(51,160,44)",
    "rgb(251,154,153)",
    "rgb(227,26,28)",
    "rgb(253,191,111)",
    "rgb(255,127,0)",
    "rgb(202,178,214)",
    "rgb(106,61,154)",
    "rgb(255,255,153)",
    "rgb(177,89,40)"
]




###########################################################################
###########################################################################
#####                                                                 #####
#####  d888888b .88b  d88. d8888b.  .d88b.  d8888b. d888888b .d8888.  ##### 
#####    `88'   88'YbdP`88 88  `8D .8P  Y8. 88  `8D `~~88~~' 88'  YP  ##### 
#####     88    88  88  88 88oodD' 88    88 88oobY'    88    `8bo.    ##### 
#####     88    88  88  88 88~~~   88    88 88`8b      88      `Y8b.  ##### 
#####    .88.   88  88  88 88      `8b  d8' 88 `88.    88    db   8D  ##### 
#####  Y888888P YP  YP  YP 88       `Y88P'  88   YD    YP    `8888Y'  ##### 
#####                                                                 #####
###########################################################################
###########################################################################

# Import dash
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import flask
import os


# Flask Cache
from flask_caching import Cache

# Import copy and pathlibs
import copy

# Import supportlibs
import math
import datetime as dt
import pandas as pd
import urllib.parse as urlParse

# Selfmade helpers
from app.helpers import DataToTimescale, FilterData
from app.database import GetDataDF, GetDbRef, GetFirstAndLastDate, GetInitialDates



################################################################
################################################################
#####                                                      #####
#####   .o88b.  .d88b.  d8b   db d88888b d888888b  d888b   ##### 
#####  d8P  Y8 .8P  Y8. 888o  88 88'       `88'   88' Y8b  ##### 
#####  8P      88    88 88V8o 88 88ooo      88    88       ##### 
#####  8b      88    88 88 V8o88 88~~~      88    88  ooo  ##### 
#####  Y8b  d8 `8b  d8' 88  V888 88        .88.   88. ~8~  ##### 
#####   `Y88P'  `Y88P'  VP   V8P YP      Y888888P  Y888P   #####
#####                                                      #####
################################################################
################################################################

# Set up flask and dash server
app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

app.title = "jolyu | Dashboard"

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

# Basic and general layout for the graphs
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

###########################################################################
###########################################################################
#####                                                                 #####
#####  db   d8b   db d88888b d8888b. d8888b.  .d8b.   d888b  d88888b  #####
#####  88   I8I   88 88'     88  `8D 88  `8D d8' `8b 88' Y8b 88'      #####
#####  88   I8I   88 88ooooo 88oooY' 88oodD' 88ooo88 88      88ooooo  #####
#####  Y8   I8I   88 88~~~~~ 88~~~b. 88~~~   88~~~88 88  ooo 88~~~~~  #####
#####  `8b d8'8b d8' 88.     88   8D 88      88   88 88. ~8~ 88.      #####
#####   `8b8' `8d8'  Y88888P Y8888P' 88      YP   YP  Y888P  Y88888P  #####
#####                                                                 #####
###########################################################################
###########################################################################

# Gets the websites layout from function in webpage.py
from app.webpage import GetMainSite
app.layout = GetMainSite(app, ref, initialDays)



#####################################################################################
#####################################################################################
#####                                                                           #####
#####   .o88b.  .d8b.  db      db      d8888b.  .d8b.   .o88b. db   dD .d8888.  #####
#####  d8P  Y8 d8' `8b 88      88      88  `8D d8' `8b d8P  Y8 88 ,8P' 88'  YP  #####
#####  8P      88ooo88 88      88      88oooY' 88ooo88 8P      88,8P   `8bo.    #####
#####  8b      88~~~88 88      88      88~~~b. 88~~~88 8b      88`8b     `Y8b.  #####
#####  Y8b  d8 88   88 88booo. 88booo. 88   8D 88   88 Y8b  d8 88 `88. db   8D  #####
#####   `Y88P' YP   YP Y88888P Y88888P Y8888P' YP   YP  `Y88P' YP   YD `8888Y'  #####
#####                                                                           #####
#####################################################################################
#####################################################################################

# Resize the graphs and resizescripts
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("mainGraph", "figure")],
)



####################
####################
##### Query DB #####
####################
####################

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
    """ Query and cache the dataset, also sets the different settings across webpage. """
    # Get dates for use as endstops for rangeselector
    dates = GetFirstAndLastDate(ref)

    # Translates string to datetime objecs
    date = pd.to_datetime([startDate, endDate])

    # Cache and query the database and update checkboxes below the second graph
    df = QueryDF(ref, date)
    columns = list(df)
    columns.remove("birds")

    # Update the options and values in second graph
    options = []
    values = []
    for c in columns:
        options.append(dict(
            label=c.capitalize(),
            value=c,
        ))
        values.append(c)

    # Database response string, tells the range for the dataset
    response = "Dataset updated with data between " + str(date[0]) + " UTC and " + str(date[1]) + " UTC."
    return [response, date, dates[0], dates[1], options, values]



######################
######################
##### MAIN GRAPH #####
######################
######################

@app.callback(
    Output("mainGraph", "figure"),
    [
        Input("dbDates", "data"),
    ]
)
def CreateMainGraph(dates):
    """ Creates the main graph based on the selected dates """
    # Check if dates contains something, else just use the initial dates
    if dates == None:
        dates = GetInitialDates(ref, initialDays)
    else:
        dates = pd.to_datetime(dates)
    
    # Get the dataset
    df = QueryDF(ref, dates)

    # Filter the dataframe to scale according to time and get what scale is being used
    dff, scale = DataToTimescale(df)
    
    # Get a deepcopy of the base layout
    layout_main = copy.deepcopy(layout)

    # Insert the data into the figure
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
            marker=dict(color=colors[0]),
        ),
    ]

    # More layout settings
    layout_main["title"] = "Total birds per " + scale
    layout_main["dragmode"] = "select" 
    layout_main["showlegend"] = False
    layout_main["autosize"] = True

    # Create the settings dictionary for the graph
    figure = dict(data=data, layout=layout_main)
    return figure



########################
########################
##### SECOND GRAPH #####
########################
########################

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
    """ Creates the second graph based on the selected data in the main graph """
    layout_second = copy.deepcopy(layout)

    # General check to see if dbDates is not empty
    if dbDates == None:
        dbDates = GetInitialDates(ref, initialDays)
    else:
        dbDates = pd.to_datetime(dbDates)

    # If there are none selected data, use the database dates
    dates = []
    if data == None:
        dates = dbDates
    else:
        dates = pd.to_datetime(data["range"]["x"])
        # Check if the selected dates is outside the allowed dates, given by the dataset
        if dbDates[0] > dates[0] or dbDates[1] < dates[1]:
            dates = dbDates

    # Query the the loaded dataset
    df = QueryDF(ref, dbDates)
    # Sort data into months, weeks, days or hours depending on the timespan of the dataset
    dff = FilterData(df, dates[0], dates[1])

    # Get the clumns for use with drawing the lines that are not birds
    columns = list(dff)
    
    #print(checked)
    if checked == None:
        checked = columns
    else:
        # nearly always add the birds section because the checkBoxlist does not contain birds
        checked.insert(0, "birds")
    #print(checked)
    # the list used to hold the data that goes into the graph
    data = []

    # Local function to give number + 1 if n is greater than 0
    def getYaxis(n):
        if n > 0:
            return str(n + 1)
        return ""

    # index for use with naming of axis
    i = 0
    # Generate the data and layout based on what graphs is shown
    for indx, c in enumerate(columns):
        if c in checked:
            data.append(
                dict(
                    type="scatter",
                    line=dict(shape="spline"),
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
                    position= 1 - (i - 1) * 0.05,
                )
            i += 1
    

    # More layout settings
    layout_second["title"] = "Selected data"
    layout_second["dragmode"] = "select" 
    layout_second["showlegend"] = True
    layout_second["autosize"] = True
    layout_second["hovermode"] = "y unified"

    layout_second["xaxis"] = dict(domain=[0,1 - (max(0, len(checked) - 2) * 0.05)])

    # Create the settings dictionary for the graph
    figure = dict(data=data, layout=layout_second)
    return figure



####################
####################
##### DOWNLOAD #####
####################
####################

@app.callback(
    Output("downloadBut", "href"),
    [
        Input("dbDates", "data"),
    ]
)
def UpdateDownloadButton(dates):
    """ Updates the download button with the data from the current dataset """
    # Check if the dates variable is not empty
    if dates == None:
        dates = GetInitialDates(ref, initialDays)
    else:
        dates = pd.to_datetime(dates)
    
    # Query the dataset
    df = QueryDF(ref, dates)

    # Convert dataframe to csv and convert into a "file" that is parsed into a string with no invalid characters
    csvString = df.to_csv(encoding="utf-8")
    csvString = "data:text/csv;charset=utf-8," + urlParse.quote(csvString)
    return csvString



###################
###################
##### FAVICON #####
###################
###################

@server.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(app.get_asset_url("favicon.ico"), "favicon")


##################################################
##################################################
#####                                        #####
#####  .88b  d88.  .d8b.  d888888b d8b   db  #####
#####  88'YbdP`88 d8' `8b   `88'   888o  88  #####
#####  88  88  88 88ooo88    88    88V8o 88  #####
#####  88  88  88 88~~~88    88    88 V8o88  #####
#####  88  88  88 88   88   .88.   88  V888  #####
#####  YP  YP  YP YP   YP Y888888P VP   V8P  #####
#####                                        #####
##################################################
##################################################

if __name__ == "__main__":
    app.run_server(debug=True)