#!/usr/bin/python3
'''
a script that changes the name of a State
object from the database hbtn_0e_6_usa.
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

    '''Bind the engine to the Base class.'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Retrieve the State object with id = 2.'''
    new_instance = session.query(State).filter_by(id=2).first()

    '''Change the name of the state.'''
    new_instance.name = 'New Mexico'
    session.commit()
