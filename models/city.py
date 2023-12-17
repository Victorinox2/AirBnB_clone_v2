#!/usr/bin/python3
""" City Module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKeyConstraint
Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['state_id'], ['state.id']),
    )
