#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', passive_deletes=True, backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """ cities getter
            """
            objects = models.storage.all(City)
            city_list = []
            for val in objects.values():
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
