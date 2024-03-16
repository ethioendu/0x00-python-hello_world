#!/usr/bin/python3
'''
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''Access to the database and get a state
    from the database.
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Bind the engine to the Base class.'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Create a new State object.'''
    new_state = State(name="Louisiana")

    '''
    Add the new state to the session and commit the changes to the database
    '''
    session.add(new_state)

    '''Print the new state's ID.'''
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
