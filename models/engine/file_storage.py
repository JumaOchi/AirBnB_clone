#!/usr/bin/python3
''' File storage class module'''
import json


class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects.update({key : obj.to_dict()})


    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json_string = json.dumps(self.__objects)
            f.write(json_string)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_string = f.read()
                if json_string == '':
                    pass
                else:
                    self.__objects = json.loads(json_string)
        except FileNotFoundError:
            pass
