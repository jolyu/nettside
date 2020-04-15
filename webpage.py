#Import dash compontents
import dash_core_components as dcc
import dash_html_components as html

import pathlib

def GetMainSite(dashApp):
    PATH = pathlib.Path(__file__).parent
    ASSET_PATH = PATH.joinpath("assets").resolve()
    print(ASSET_PATH)
    mainSite = html.Div(
        [
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
        ]
    )
    return mainSite