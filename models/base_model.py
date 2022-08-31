#!/usr/bin/python3
''' Base model class module'''
import uuid
from datetime import datetime
from models import storage


class BaseModel():
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

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__' : self.__class__.__name__})
        new_dict.update({'created_at' : self.created_at.isoformat()})
        new_dict.update({'updated_at' : self.updated_at.isoformat()})
        return new_dict
