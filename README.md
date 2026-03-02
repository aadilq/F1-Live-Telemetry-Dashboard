# F1-Live-Telemetry-Dashboard

## Source Files Overview

### `src/data_loader.py`

Handles all data fetching from the FastF1 API. Enables a local cache in `data/` to avoid re-downloading session data.

**Functions:**
- `get_session(year, event, session_type)` — Loads a race weekend session (e.g. Qualifying, Race) for a given year and Grand Prix.
- `get_fast_lap(session, driverNumber)` — Returns the fastest lap for a given driver in a session.
- `get_lap_telemetry(lap)` — Returns the full telemetry DataFrame for a given lap (speed, position, throttle, brake, etc.).

---

### `src/visualization.py`

Builds Plotly figures for visualizing telemetry data on a circuit map.

**Functions:**
- `create_circuit_map(telemetry_data, color_by)` — Plots the circuit track using X/Y coordinates from telemetry, with markers colored by a chosen telemetry channel (default: `Speed`). Uses a jet colorscale on a black background.
- `add_driver_position(telemetry_data, current_position, color_by)` — Calls `create_circuit_map` and overlays a white circle marker at a specific point along the track to represent the driver's current position.

---

### `src/layout.py`

Defines the Dash UI layout. Currently contains a stub `create_layout()` function that returns an empty `html.Div`. This is where dashboard components (dropdowns, graphs, sliders) will be added.

---

### `src/callbacks.py`

Empty file reserved for Dash callback definitions. Callbacks will wire up user interactions (e.g. selecting a driver or lap) to update the visualizations.

---

### `src/test_visualization.py`

Manual test/demo script. Loads the 2024 Hungarian GP Qualifying session, fetches Verstappen's (driver `1`) fastest lap, and renders the circuit map at two different driver positions (`0` and `100`) using `add_driver_position`. Run directly to visually verify the map and marker work correctly.

---

### `src/tempCodeRunnerFile.py`

Auto-generated scratch file created by the VS Code Code Runner extension. Contains a leftover string (`"Hungaroring"`) and can be ignored or deleted.
