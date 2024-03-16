#!/usr/bin/python3
"""
a python file that contains the class definition of a
State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): represents a column of an auto-generated
        name (str): represents a column of a string with maximum 128 characters

    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
