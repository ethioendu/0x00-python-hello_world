#!/usr/bin/python3
'''
a python script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa.
'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    '''
    Create a SQLAlchemy engine to connect to the MySQL server
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Create all tables defined in the metadata.'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Display the states and cities.'''
    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
