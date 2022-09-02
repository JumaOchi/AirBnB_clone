#!/usr/bin/python3
''' File storage class module'''
import json


class FileStorage():
    '''
    File storage manager object

    Class Attributes:
        (str) __file_path = file location
        (dict) __objects = dictionary of saved objects

    Methods:
        all
        new
        save
        reload
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns all stored objects'''
        return self.__objects

    def new(self, obj):
        '''Adds/Updates an object to/in the Object dictionary'''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects.update({key : obj.to_dict()})


    def save(self):
        '''Saves the Object Dictionary to a file'''
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json_string = json.dumps(self.__objects)
            f.write(json_string)

    def reload(self):
        '''Loads Objects from the file into the Object Dictionary'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_string = f.read()
                if json_string == '':
                    pass
                else:
                    self.__objects = json.loads(json_string)
        except FileNotFoundError:
            pass
