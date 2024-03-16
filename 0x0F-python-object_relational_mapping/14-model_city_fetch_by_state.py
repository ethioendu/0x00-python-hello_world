#!/usr/bin/python3
'''
prints the State object with the name passed as argument from the database
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    '''
    Create a SQLAlchemy engine to connect to the MySQL server.
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Bind the engine to the Base class.'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Retrieve all City objects from the database.'''
    cities = session.query(City).order_by(City.id).all()

    '''Close the session.'''
    session.close()

    '''Display the cities by state.'''
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
