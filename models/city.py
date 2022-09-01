#!/usr/bin/python3
''' City class module'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Cities

    Class Attributes:
        (str) name - name of amenity
        (str) state_id - id of state

    Attributes:
        (str) id - unique object id
        (datetime) created_at - Date object was created
        (datetime) updated_at - Date object was last updated

    Methods:
        save
        to_dict

    __str__ returns '[<Class>] (<id>) {__dict__}'
    '''
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
