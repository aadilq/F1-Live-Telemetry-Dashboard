from data_loader import get_session, get_fast_lap, get_lap_telemetry
from visualization import create_circuit_map

session = get_session(2024, 'Hungaroring', 'Q')
fastest_lap = get_fast_lap(session, '1')
telemetry = get_lap_telemetry(fastest_lap)

print(telemetry[['X', 'Y', 'Speed']].head())  # Check if data looks good
print(telemetry['Speed'].min(), telemetry['Speed'].max())  # Check speed range

fig = create_circuit_map(telemetry_data=telemetry, color_by='Speed')
fig.show()