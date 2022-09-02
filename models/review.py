#!/usr/bin/python3
''' Review class module'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review

    Class Attributes:
        (str) place_id - id of Place
        (str) user_id - id of User
        (str) text - Review text

    Attributes:
        (str) id - unique object id
        (datetime) created_at - Date object was created
        (datetime) updated_at - Date object was last updated

    Methods:
        save
        to_dict

    __str__ returns '[<Class>] (<id>) {__dict__}'
    '''

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
