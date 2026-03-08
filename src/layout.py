import dash
from dash import dcc, html

BTN_STYLE = {
    'backgroundColor' : '#2a2a3e',
    'color': 'white', 
    'border': '1px solid #444', 
    'borderRadius' : '6px', 
    'padding': '8px 16px', 
    'fontSize': '16px', 
    'cursor': 'pointer', 
    'width': '44px',
}

TELEMETRY_METRICS = [
    ('Speed (km/h)', 'telemetry-speed', '#00d2ff'),
    ('Throttle (%)', 'telemetry-throttle', '#00ff88'),
    ('Brake', 'telemetry-brake', '#ff4444'),
    ('Gear', 'telemetry-gear', '#ffdd00'), 
    ('RPM', 'telemetry-rpm', "#aeaaa5"), 
    ('DRS', 'telemetry-drs', '#00ff88')
]

def create_layout():
    Telemetry_rows = [
        html.Div(
            style={'display': 'flex', 'flexDirection': 'column', 'gap': '4px'},
            children=[
                html.Span(
                    label,
                    style={
                        'fontSize' : '11px', 
                        'color': '#888',
                        'textTransform': 'uppercase',
                        'letterSpacing': '1px',
                    }
                ),
                html.Span(
                    '--',
                    id=metric_id,
                    style={
                        'fontSize': '28px',
                        'fontWeight': 'bold',
                        'color': color,

                    }
                )
            ]
        )
        for label, metric_id, color in TELEMETRY_METRICS
    ]

    return html.Div(

        style={
            'backgroundColor': '#0f0f1a',
            'height': '100vh',
            'display': 'flex',
            'flexDirection': 'column',
            'fontFamily': 'monospace',
            'color': 'white',
            'overflow': 'hidden',
        },
        children=[
            ##- Header
            html.Div(
                style={
                    'padding': '10px 20px',
                    'borderBottom': '1px solid #333',
                    'flexShrink': '0',  
                },
                children=[
                    html.H2(
                        'F1 Telemetry Dashboard',
                        style={'margin': 0, 'color': '#e10600'},

                    )
                ]
            ), 
            ##- Main area - Circuit map on the left/center and telemetry panel on the right
            html.Div(
                style={
                    'display': 'flex',
                    'flex': '1',
                    'overflow': 'hidden',
                },
                children=[
                    ##Circuit map
                    html.Div(
                        style={
                            'flex': '3',
                            'padding': '10px'
                        },
                        children=[
                            dcc.Graph(
                                id='circuit-map',
                                style={'height': '100%'},
                                config={'displayModeBar': False}
                            )
                        ]
                    ),
                    # Telemetry panel
                    html.Div(
                        style={
                            'flex': '1',
                            'backgroundColor': '#1a1a2e',
                            'borderLeft': '1px solid #333',
                            'padding': '20px', 
                            'display': 'flex',
                            'flexDirection': 'column',
                            'gap': '20px',
                            'overflowY': 'auto',
                            'minWidth': '200px'
                        },
                        children=[
                            html.H3(
                                'Telemetry',
                                style={'color': '#e10600', 'margin': '0 0 10px 0'},
                            ),
                            *Telemetry_rows
                        ]
                    ), 
                ]
            ),
            ##- Bottom Area: Slider + playback controls
            html.Div(
                style={
                    'backgroundColor': '#111122',
                    'borderTop': '1px solid #333',
                    'padding': '12px 20px',
                    'flexShrink': '0'
                },
                children=[
                    dcc.Slider(
                        id='lap-slider',
                        min=0,
                        max=100,
                        step=1,
                        value=0,
                        marks=None,
                        tooltip={'placement': 'top', 'always_visible': True},
                        updatemode='drag'
                    ),
                    html.Div(
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'gap': '10px',
                            'marginTop': '10px'
                        },
                        children=[
                            html.Button('⏮', id='btn-start', title='Go to Start', style=BTN_STYLE),
                            html.Button('⏪', id='btn-rewind', title='Step Back', style=BTN_STYLE),
                            html.Button('▶', id='btn-play-pause', title='Play / Pause', style={**BTN_STYLE, 'backgroundColor': '#e10600', 'width': '52px'}),
                            html.Button('⏩', id='btn-forward', title='Step Forward', style=BTN_STYLE),
                            html.Button('⏭', id='btn-end', title='Go to End', style=BTN_STYLE)
                        ]
                    ),
                    dcc.Interval(
                        id='playback-interval',
                        interval=100,
                        n_intervals=0,
                        disabled=True
                    ), 
                ]
            ),
            dcc.Store(id='telemetry-store'),
            dcc.Store(id='playback-state', data={'playing': False}),
            dcc.Interval(id='init-interval', n_intervals=0, max_intervals=1, interval=500),
        ]
    )

  