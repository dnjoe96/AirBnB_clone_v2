#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascase="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """a getter attribute that returns a list of city instances
            with state_id equal to the current State.id"""

            from models import storage
            state_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
