#!/usr/bin/python3
''' State class module'''
from models.base_model import BaseModel


class State(BaseModel):
    name = ''

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
