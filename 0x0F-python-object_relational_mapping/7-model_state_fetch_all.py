#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    """
    Check if the script is run directly
    and gather the command-line arguments
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    """Create a session to interact with the database."""
    Session = sessionmaker(bind=engine)
    session = Session

    """Display the results."""
    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
