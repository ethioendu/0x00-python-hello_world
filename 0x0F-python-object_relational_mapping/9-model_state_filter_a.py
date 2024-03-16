#!/usr/bin/python3
'''
a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    '''
    access to the database and get a state
    from the database.
    '''

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Bind the engine to the Base class.'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Display the results.'''
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
