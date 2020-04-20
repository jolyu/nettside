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

#Import dash compontents
import dash_core_components as dcc
import dash_html_components as html

import datetime as dt

from app.database import GetInitialDates



#####################
#####################
##### MAIN SITE #####
#####################
#####################

def GetMainSite(dashApp, dbRef, days):
    """ Returns the layout for the website. Documentation on dash.plotly.com """
    dates = GetInitialDates(dbRef, days)
    mainSite = html.Div(
        [
            # empty Div to trigger javascript file for graph resizing
            html.Div(id="output-clientside"),
            dcc.Store(id="dbDates"),
            # Header Div
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src=dashApp.get_asset_url("jolyu.svg"),
                                style={
                                    "height": "8em",
                                    "width": "auto",
                                },
                            )
                        ],
                        id="jolyu-logo",
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
                                href="https://jolyu.glados.no/",
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
            # Div for main site
            html.Div(
                [
                    html.Div(
                        [
                            dcc.DatePickerRange(
                                id="dbDatePicker",
                                display_format="YYYY-MM-DD",
                                start_date_placeholder_text='YYYY-MM-DD',
                                end_date_placeholder_text='YYYY-MM-DD',
                                start_date=dates[0],
                                end_date=dates[1],
                                first_day_of_week=1,
                            ),
                            html.Button("Fetch DB",
                                id="fetchDbButton"
                            ),
                            html.A(
                                html.Button("Download Dataset",
                                    id="downloadDbButton"
                                ),
                                id="downloadBut",
                                download="rawdata.csv",
                                href="",
                                target="_blank"
                            ),
                            
                        ],
                        className="pretty_container six columns",
                    ),
                    html.Div(
                        [
                            html.P(id="dbResponse"),
                        ],
                        className="pretty_container six columns",
                    ),
                ],
                id="quick-facts",
                className="row flex-display"
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(id="mainGraph"),
                                ],
                                id="mainGraphContainer",
                                className="pretty_container",
                            ) 
                        ],
                        className="twelve columns",
                    )
                ],
                id="mainGraphDiv",
                className="row flex-display",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    
                                    dcc.Graph(id="secondGraph"),
                                    html.H5("Show:"),
                                    dcc.Checklist(
                                        
                                        labelStyle={'display': 'inline-block'},
                                        id="checklistShow",
                                    )
                                ],
                                id="secondaryGraphContainer",
                                className="pretty_container",
                            ) 
                        ],
                        className="twelve columns",
                    )
                ],
                id="second_graph_div",
                className="row flex-display",
            )
        ]
    )
    return mainSite