#!/usr/bin/python3
'''
represent a relationship with the class City.
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    ''' class that defines each city.'''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
