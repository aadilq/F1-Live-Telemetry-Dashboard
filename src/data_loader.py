import fastf1

fastf1.Cache.enable_cache('data/')


def get_session(year, event, session_type):
    session = fastf1.get_session(year=year, gp=event, identifier=session_type)
    session.load()
    return session


# session = get_session(2024, 'Monza', 'Q')
# print(session)

def get_fast_lap(session, driverNumber):
    laps = session.laps.pick_driver(driverNumber)
    fastest_lap = laps.pick_fastest()
    return fastest_lap
fastest_lap = get_fast_lap(session=session, driverNumber='1')
print(fastest_lap)



