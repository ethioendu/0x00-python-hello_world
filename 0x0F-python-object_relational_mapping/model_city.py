#!/usr/bin/python3
'''
reperesents a python City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated,
class attribute name that represents a column of a string
class attribute state_id that represents a column of an integer,
'''

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''
    Class that defines each city.
    attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): represents a column of an integer
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
