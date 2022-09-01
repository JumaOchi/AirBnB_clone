#!/usr/bin/python3
''' State class module'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    State

    Class Attributes:
        (str) name - Name of State

    Attributes:
        (str) id - unique object id
        (datetime) created_at - Date object was created
        (datetime) updated_at - Date object was last updated

    Methods:
        save
        to_dict

    __str__ returns '[<Class>] (<id>) {__dict__}'
    '''

    name = ''

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
