#!/usr/bin/python3
'''
a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa:
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    '''Create a SQLAlchemy engine to connect to the MySQL server'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    '''Create all tables defined in the metadata.'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Create the State "California" with the City "San Francisco".'''
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
