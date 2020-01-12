import os
import csv
import datetime
from app.model import Entity
from pathlib import Path
import env_file

class Crud(object):
    def __init__(self, entity, action):
        self.table = entity.__tablename__
        self.entity = Entity(self.table)
        self.action = action
        self.model = entity
        self.repository = self.entity.repository()
        
    def asking(self, fields):
        inputs = {}
        keys = list(fields.keys())
        values = list(fields.values())
        
        for key in keys:
            inputs.update({key: input(fields.get(key))})
            
        return list([inputs])
    
    def index(self):
        return self.entity.index()
    
    def store(self):
        data = self.asking(self.model.fields_store)
        
        getValidators = getattr(self.model, 'validators')
        
        validation = getValidators(data)
        
        if validation:
            return validation
        
        return self.entity.store(data)
        
    def show(self, id):
        item = self.repository.find(id)
        
        if item is not None:
            return self.entity.show(id)
        else:
            return 'Item notfound'
    
    def update(self, id):
        item = self.repository.find(id)
        
        if item is not None:
            data = self.asking(self.model.fields_update)
            return self.entity.update(id, data)
        else:
            return 'Item notfound'
    
    def delete(self, id):
        item = self.repository.find(id)
        
        if item is not None:
            if (self.entity.delete(id)):
                return 'Item removed'
            else:
                return 'Could not remove item.'
        else:
            return 'Item notfound'
        
    def export(self):
        date = datetime.datetime.now()
        envs = env_file.get('.env')
        file = '%s/%s-%s.csv' % (envs.get('EXPORT_PATH'), self.table, date.strftime("%Y-%m-%d-%H%M%S"))
        Path(file).touch()
        
        with open(file, 'wb') as csv_file:
            data = self.entity.index()
            
            for row in data:
                item = []
                for column in row:
                    item.append(str(column))
                    
                writeRow = "%s\n" % " ".join(item)
                csv_file.write(writeRow.encode())
                
        return file