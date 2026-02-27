import fastf1

import plotly.graph_objects as go
import pandas as pd

from data_loader import get_session, get_fast_lap, get_lap_telemetry


def create_circuit_map(telemetry_data, color_by='Speed'):

    color_values = pd.to_numeric(telemetry_data[color_by], errors='coerce').values

    fig = go.Figure() ##Empty plotly figure object

    fig.add_trace(go.Scatter(
        x = telemetry_data['X'], ##Pulling all of the X coordinates from the Dataframe
        y = telemetry_data['Y'], ##Pulling all of the Y coordinates from the Dataframe
        mode = 'markers+lines', ##Draw lines connecting the points
        marker=dict(
            color=color_values, ##Passing in an array of values from the dataframe from the Speed column
            colorscale = 'jet',
            size = 8, ##The width of the line connecting the pixels is going to be 8 pixels
            colorbar = dict(title=color_by), ##colorbar is used to show what the different colors mean
            showscale=True
        ),
        line=dict(
            color='lightgray',
            width = 2
        ),
        name='Track'
    ))

    fig.update_layout(
        title='Circuit Map',
        xaxis = dict(visible=False), ##Hide the x axis
        yaxis = dict(visible=False, scaleanchor='x', scaleratio=1), ##Ensure the x and y axis use the same scale scale so that the track is not stretched or squished
        showlegend = False, 
        plot_bgcolor = 'black',
        height = 600
    )

    return fig

