#!/usr/bin/python3
''' Base model class module'''
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    '''
    Base model class for all project classes

    Attributes:
        (str) id - unique object id
        (datetime) created_at - Date object was created
        (datetime) updated_at - Date object was last updated

    Methods:
        save
        to_dict

    __str__ returns '[<Class>] (<id>) {__dict__}'

    '''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for (key, value) in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Save object to storage'''
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''Convert dates to isoformat and add class name to dictionary'''
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__' : self.__class__.__name__})
        new_dict.update({'created_at' : self.created_at.isoformat()})
        new_dict.update({'updated_at' : self.updated_at.isoformat()})
        return new_dict
