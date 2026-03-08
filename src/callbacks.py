import pandas as pd
from dash import Input, Output, State, ctx
from dash.exceptions import PreventUpdate

from data_loader import get_session, get_fast_lap, get_lap_telemetry
from visualization import add_driver_position

## Load telemetry once when the server starts
_session = get_session(2024, 'Hungaroring', 'Q')
_lap = get_fast_lap(_session, '1')
_telemetry = (
    get_lap_telemetry(_lap)[['X', 'Y', 'Speed', 'Throttle', 'Brake', 'nGear', 'RPM', 'DRS']]
    .reset_index(drop=True)
)

TELEMETRY_JSON = _telemetry.to_json()
MAX_POS = len(_telemetry) - 1


def register_callbacks(app):

    ## ── 1. Populate the store and set slider max on page load ────────────────
    @app.callback(
        Output('telemetry-store', 'data'),
        Output('lap-slider', 'max'),
        Input('init-interval', 'n_intervals'),
    )
    def init_store(_):
        return TELEMETRY_JSON, MAX_POS


    ## ── 2. Update circuit map + telemetry panel when slider moves ────────────
    @app.callback(
        Output('circuit-map', 'figure'),
        Output('telemetry-speed', 'children'),
        Output('telemetry-throttle', 'children'),
        Output('telemetry-brake', 'children'),
        Output('telemetry-gear', 'children'),
        Output('telemetry-rpm', 'children'),
        Output('telemetry-drs', 'children'),
        Input('lap-slider', 'value'),
        State('telemetry-store', 'data'),
    )
    def update_dashboard(position, telemetry_json):
        if telemetry_json is None:
            raise PreventUpdate

        df = pd.read_json(telemetry_json)
        position = min(position, len(df) - 1)
        row = df.iloc[position]

        fig = add_driver_position(df, position)

        return (
            fig,
            f"{row['Speed']:.0f}",
            f"{row['Throttle']:.0f}",
            'ON' if row['Brake'] else 'OFF',
            str(int(row['nGear'])),
            f"{row['RPM']:.0f}",
            'ON' if row['DRS'] >= 10 else 'OFF',
        )


    ## ── 3. Playback controls ─────────────────────────────────────────────────
    @app.callback(
        Output('lap-slider', 'value'),
        Output('playback-interval', 'disabled'),
        Output('btn-play-pause', 'children'),
        Input('btn-play-pause', 'n_clicks'),
        Input('btn-start', 'n_clicks'),
        Input('btn-end', 'n_clicks'),
        Input('btn-rewind', 'n_clicks'),
        Input('btn-forward', 'n_clicks'),
        Input('playback-interval', 'n_intervals'),
        State('lap-slider', 'value'),
        State('lap-slider', 'max'),
        State('playback-interval', 'disabled'),
        prevent_initial_call=True,
    )
    def handle_playback(play_clicks, start_clicks, end_clicks, rewind_clicks,
                        forward_clicks, n_intervals, position, max_pos, interval_disabled):

        triggered = ctx.triggered_id

        if triggered == 'btn-play-pause':
            ## interval_disabled=True means currently paused, so we're about to play
            playing = interval_disabled
            return position, not playing, '⏸' if playing else '▶'

        if triggered == 'btn-start':
            return 0, True, '▶'

        if triggered == 'btn-end':
            return max_pos, True, '▶'

        if triggered == 'btn-rewind':
            icon = '⏸' if not interval_disabled else '▶'
            return max(0, position - 1), interval_disabled, icon

        if triggered == 'btn-forward':
            icon = '⏸' if not interval_disabled else '▶'
            return min(max_pos, position + 1), interval_disabled, icon

        if triggered == 'playback-interval':
            next_pos = position + 1
            if next_pos >= max_pos:
                return max_pos, True, '▶'  ## stop at end of lap
            return next_pos, False, '⏸'

        raise PreventUpdate
