import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

data = pd.read_csv("test.csv")
data.sort_values("Year", inplace=True)
years = data.Year.unique()
years = np.sort(years)
data2 = pd.read_csv("test2.csv")
data2.fillna(value="NA", inplace=True)
data2.sort_values(by=['TermYear'],inplace=True)
years1 = data2.TermYear.unique()
years1 = np.sort(years1)
card1_data = data.query('Year==2019')['Jobs'].sum()- data.query('Year==2020')['Jobs'].sum()
df_2019= data.query('Year==2019').reset_index()
df_2020= data.query('Year==2020').reset_index()
df_2019= df_2019.groupby('Industry').sum()
df_2020= df_2020.groupby('Industry').sum()
df_2019['Jobs_Diff']= df_2019['Jobs']-df_2020['Jobs']
df_2019.sort_values('Jobs_Diff', inplace=True)
df_2019= df_2019.reset_index(drop= False)
df_2019=df_2019.head(8)
#external_stylesheets = [
    #{
        #"href": "https://fonts.googleapis.com/css2?"
        #"family=Lato:wght@400;700&display=swap",
        #"rel": "stylesheet",
    #}
#]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = ""

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                    dbc.Col(html.Div(
                    children =[
                            html.Div(
                                children=[
                                    html.P(children="📈",className="header-emoji"),
                                    html.H1(
                                        children="Jobs by Industry", className="header-title"
                                    ),
                                    html.P(
                                        children="Analyze the behavior of Jobs"
                                        " by Region and Industry"
                                        " between 2012 and 2020",
                                        className="header-description",
                                    ),
                                ],
                                className="header",
                            ),
                            html.Div(
                                children=[
                                    html.Div(
                                        children=[
                                            html.Div(children="Region", className="menu-title"),
                                            dcc.Dropdown(
                                                id="region-filter",
                                                options=[
                                                    {"label": Region, "value": Region}
                                                    for Region in np.sort(data.Region.unique())
                                                ],
                                                value="Central New York",
                                                clearable=False,
                                                className="dropdown",
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        children=[
                                            html.Div(children="Industry", className="menu-title"),
                                            dcc.Dropdown(
                                                id="type-filter",
                                                options=[
                                                    {"label": Industry, "value": Industry}
                                                    for Industry in data.Industry.unique()
                                                ],
                                                value="Manufacturing",
                                                clearable=False,
                                                searchable=False,
                                                className="dropdown",
                                            ),
                                        ],
                                        style={"width":"50%"},
                                    ),
                                    html.Div(
                                                [dbc.Label("Years"),
                                                 dcc.RangeSlider(
                                                   id  = "my-range-slider",
                                                   marks={
                                                         2012: '2012',  # key=position, value=what you see
                                                         2013: '2013',
                                                         2014: '2014',
                                                         2015: '2015',
                                                         2016: '2016',
                                                         2017: '2017',
                                                         2018: '2018',
                                                         2019: '2019',
                                                         2020: '2020'
                                                     },
                                                   step=1,
                                                   min = years[0],
                                                   max = years[-1],
                                                   tooltip={"placement": "bottom", "always_visible": True},
                                                   value=[years[0], years[-1]],
                                                 ),
                                            ]
                                    ),
                                ],
                                className="menu",
                            ),
                            html.Div(
                                    html.Div(
                                        children=dcc.Graph(
                                            id="price-chart",
                                            config={"displayModeBar": False},
                                        ),
                                        className="card",
                                    ),
                                className="wrapper",
                            ),
                            html.Div(
                                children=[

                                    html.Div(
                                        children=[
                                            html.Div(children="Institution Name", className="menu-title"),
                                            dcc.Dropdown(
                                                id="name-filter",
                                                options=[
                                                    {"label": name, "value": name}
                                                    for name in data2.Name.unique()
                                                ],
                                                value="Albany",
                                                clearable=False,
                                                searchable=False,
                                                className="dropdown",
                                            ),
                                        ],
                                    ),
                                            html.Div(
                                                [dbc.Label("Years"),
                                                 dcc.RangeSlider(
                                                   id  = "my-range-slider2",
                                                   marks={
                                                         2011: '2011',
                                                         2012: '2012',
                                                         2013: '2013',
                                                         2014: '2014',
                                                         2015: '2015',
                                                         2016: '2016',
                                                         2017: '2017',
                                                         2018: '2018',
                                                         2019: '2019',
                                                         2020: '2020',
                                                         2021: '2021'
                                                     },
                                                   step=1,
                                                   min = years1[0],
                                                   max = years1[-1],
                                                   tooltip={"placement": "bottom", "always_visible": True},
                                                   value=[years1[0], years1[-1]],
                                                 ),
                                            ]
                                    )
                                ],
                                className="menu",
                            ),
                            html.Div(
                                    html.Div(
                                        children=dcc.Graph(
                                            id="price-chart2",
                                            config={"displayModeBar": False},
                                        ),
                                        className="card",
                                    ),
                                className="wrapper",
                            )],
                        ),
                    ),
                    dbc.Col( html.Div(
                    children=[
                           html.Div(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("A Steep Decline", className="card-title"),
                                        html.H6("A decline in Job availabiltiy due to the spread of the COVID-19 Pandemic.", className="card-subtitle"),
                                        html.P(
                                            "A steep decline in jobs amounting to a total difference of "+ str(card1_data)+" jobs alone was seen between 2019 to 2020"
                                            " possibly due to the rising spread of COVID-19 cases.",
                                            className="card-text",
                                        ),
                                    ]
                                )
                           )
                         ),
                        html.Div(
                        dcc.Graph(
                                    figure={
                                            'data': [
                                                {'x': df_2019['Jobs_Diff'], 'y': df_2019['Industry'], 'type': 'bar', 'orientation':'h'},
                                            ],
                                            'layout': {
                                                'title': 'Top 8 Industries with least Job losses in 2020',
                                                "colorway": ["#17B897","#FFB606","3E76A4"],
                                                "horizontal-align": "right"
                                            }
                                    }
                                ), style={"width": "100%", "align": "right"},
                        )]
                     ), width=5
                    ),
            ]
        )
    ]
)

    #html.Div(
    #children=[



    #]
#)


@app.callback(
     [Output("price-chart","figure"),Output("price-chart2", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("my-range-slider", "value"),
        Input("my-range-slider2", "value"),
        Input("name-filter","value")
    ],
)
def update_charts(Region, Industry, years, years1, Name):
    mask = [
            (
                (data.Region == Region)
                    & (data.Industry == Industry)
                    & (data.Year >= years[0]) 
                    & (data.Year <= years[1])
            )
        ]

    mask1 = [
            (
                (data2.Name == Name)
                    & (data2.TermYear >= years1[0])
                    & (data2.TermYear <= years1[1])
            )
        ]

    filtered_data1 = data.loc[mask[0], :]
    filtered_data2 = data2.loc[mask1[0], :]
    
    price_chart_figure1 = {
        "data": [
            {
                "x": filtered_data1["Year"],
                "y": filtered_data1["Jobs"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Jobs By Industry",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "", "fixedrange": True},
            "colorway": ["#17B897"],
            }
        }
    price_chart_figure2 = {
        "data": [
            {
                "x": filtered_data2["TermYear"],
                "y": filtered_data2["Undergraduate Full-Time"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
            {
                "x": filtered_data2["TermYear"],
                "y": filtered_data2["Undergraduate Part-Time"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>"

            },
            {
                "x": filtered_data2["TermYear"],
                "y": filtered_data2["Graduate Full-Time"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>"

            },
            {
                "x": filtered_data2["TermYear"],
                "y": filtered_data2["Graduate Part-Time"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>"

            }
        ],
        "layout": {
            "title": {
                "text": "Enrollments: State University of New York",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "", "fixedrange": True},
            "colorway": ["#E12D39","#17B897","#FFB606","3E76A4"],
        }

    }
    price_chart_figure2['data'][0]['name'] ="Undergraduate Full-Time"
    price_chart_figure2['data'][1]['name'] = "Undergraduate Part-Time"
    price_chart_figure2['data'][2]['name'] = "Graduate Full-Time"
    price_chart_figure2['data'][3]['name'] = "Graduate Part-Time"

    return price_chart_figure1,price_chart_figure2


if __name__ == "__main__":
    app.run_server(debug=True)
