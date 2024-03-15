
#!/usr/bin/python3

"""This module prints all City objects from
the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id)

    for state, city in states:
        print(f"{state.name}: ({city.id}) {city.name}")
