import fastf1

fastf1.Cache.enable_cache('data/')


def get_session(year, event, session_type):
    session = fastf1.get_session(year=year, gp=event, identifier=session_type)
    session.load()
    return session


# session = get_session(2024, 'Monza', 'Q')
# print(session)

def get_fast_lap(session, driverNumber):
    laps = session.laps.pick_drivers(driverNumber)
    fastest_lap = laps.pick_fastest()
    return fastest_lap


def get_lap_telemetry(lap):
    telemetry = lap.get_telemetry()
    return telemetry

session = get_session(year=2023, event='Monza', session_type='Q')
fastest_lap = get_fast_lap(session=session, driverNumber='1')
telemetry = get_lap_telemetry(fastest_lap)
print(telemetry.head())
print(telemetry.columns)



