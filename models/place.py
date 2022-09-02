#!/usr/bin/python3
''' Place class module'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    Places

    Class Attributes:
        (str) city_id - id of City
        (str) user_id - id of User
        (str) name - Name of Place
        (str) description - Description of Place
        (int) number_rooms - Number of rooms at Place
        (int) number_bathrooms - Number of rooms at Place
        (int) max_guest - Maximum allowed guests at place
        (int) price_by_night - Price per night at Place
        (float) latitude - Latitude of Place
        (float) longitude - Longtitude of Place
        (list) amenity_ids - ids of amenities

    Attributes:
        (str) id - unique object id
        (datetime) created_at - Date object was created
        (datetime) updated_at - Date object was last updated

    Methods:
        save
        to_dict

    __str__ returns '[<Class>] (<id>) {__dict__}'
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
