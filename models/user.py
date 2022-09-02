#!/usr/bin/python3
''' User class module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    User

    Class Attributes:
        (str) email - User's email
        (str) password - User's password
        (str) first_name - User's first name
        (str) last_name - User's last name

    Attributes:
        (str) id - unique object id
        (datetime) created_at - Date object was created
        (datetime) updated_at - Date object was last updated

    Methods:
        save
        to_dict

    __str__ returns '[<Class>] (<id>) {__dict__}'
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
