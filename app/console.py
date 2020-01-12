import os
import click
import datetime
import sys

from app.service import Crud
from app.model import Client, Product
from app.connection import Connection

import config

class Console(object):
    actions = ('index', 'store', 'show', 'update', 'delete', 'export')
    idRequired = ('show', 'update', 'delete')
    
    def __init__(self, model, action, id, export=False):
        if model is None:
            model = config.get('entity_default')
        
        if action is None and id:
            action = 'show'
        elif action is None and id is None:
            action = config.get('action_default')
            
        if action not in self.actions:
            print('Action is not enabled')
            os.abort()
        
        if action in self.idRequired:
            if id is None or len(id.split('=')[1]) == 0:
                print('Identifier is required')
                os.abort()
            else:
                id = id.split('=')[1]

        if model == 'products':
            entity = Product()
        else:
            entity = Client()
        
        connection = Connection()
        service = Crud(entity, action, connection)
        crudObj = getattr(service, action)
        
        if action == 'store':
            data = self.asking(entity.fields_store)
            runner = crudObj(data)
        elif action == 'update':
            data = self.asking(entity.fields_update)
            runner = crudObj(id, data)
        elif id is not None:
            runner = crudObj(id)
        else:
            runner = crudObj()
        
        print(runner)
            
    def asking(self, fields):
        inputs = {}
        keys = list(fields.keys())
        values = list(fields.values())
        
        for key in keys:
            inputs.update({key: input(fields.get(key))})
            
        return list([inputs])