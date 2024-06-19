'''
Module:json_handler
This module contains a JsonHandler class for handling read, write, update operations
for JSON files.
'''
import json
class JsonHandler:
    '''A class to handle JSON read, write, update operations.'''
    def read_json(self, file_path):
        '''Read JSON data from a file.'''
        with open(file_path, 'r',encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_json(self, data, file_path):
        '''Write JSON data from a file.'''
        with open(file_path, 'w',encoding='utf-8') as f:
            json.dump(data, f)

    def check_key(self, data, key):
        '''Check if a key exists in a dictionary.'''
        return key in data

    def update_json(self, key, value, file_path):
        '''Update a JSON file with a new key-value pair or modify an existing one.'''
        with open(file_path, 'r+',encoding='utf-8') as f:
            data = json.load(f)
            data[key] = value
            f.seek(0)
            json.dump(data, f)
            f.truncate()
