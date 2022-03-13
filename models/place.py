#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False, default=0)
        longitude = Column(Float, nullable=False, default=0)
        reviews = relationship('Place', cascade='all, delete, delete-orphan',
                               backref='place')
        #amenity_ids = []
    else:
        city_id = ""    # City.id
        user_id = ""    # User.id
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []    # list of Amenity.ids

        @property
        def reviews(self):
            """returns a list of Review instances with place_id equals to
            the current Place.id"""

            from models import storage

            place_reviews = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews
