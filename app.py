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
def queryDF(dbRef, dates):
    return GetDataDF(dbRef, dates)

# Cache the first and last date for one hour, then the db does not update every 5 minutes
@cache.memoize(timeout=TIMEOUT)
def getFiaLaDates(dbRef):
    return GetFirstAndLastDate(dbRef)

from webpage import GetMainSite
app.layout = GetMainSite(app)


# Main
if __name__ == "__main__":
    app.run_server(debug=True)