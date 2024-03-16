#!/usr/bin/python3
'''
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''
    Create a SQLAlchemy engine to connect to the MySQL server.
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    ''' Bind the engine to the Base class.'''
    Base.metadata.bind = engine

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Retrieve all State objects with names containing the letter "a".'''
    states = session.query(State).filter(State.name.like('%a%')).all()

    '''Delete the retrieved states.'''
    for state in states:
        session.delete(state)
    session.commit()

    '''Close the session.'''
    session.close()
