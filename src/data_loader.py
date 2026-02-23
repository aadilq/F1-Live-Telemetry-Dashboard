import fastf1

fastf1.Cache.enable_cache('data/')


def get_session(year, event, session_type):
    session = fastf1.get_session(year=year, gp=event, identifier=session_type)
    session.load()


# session = get_session(2024, 'Monza', 'Q')
# print(session)

