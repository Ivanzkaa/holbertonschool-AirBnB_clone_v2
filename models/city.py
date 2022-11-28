#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models import storage_type
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """

    if storage_type == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='city', cascade="all")
    else:
        state_id = ""
        name = ""
