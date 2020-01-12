import os
import csv
import datetime
from app.model import Entity
from pathlib import Path
import config

class Crud(object):
    def __init__(self, entity, action, connection):
        self.table = entity.__tablename__
        self.entity = Entity(self.table, connection)
        self.action = action
        self.model = entity
        self.repository = self.entity.repository()
    
    def index(self):
        return self.entity.index()
    
    def store(self, data):
        try:
            getValidators = getattr(self.model, 'validators')
            validation = getValidators(data)
            
            if validation:
                return validation
            else:
                return self.entity.store(data)
        finally:
            return self.entity.store(data)
        
    def show(self, id):
        item = self.repository.find(id)
        
        if item is not None:
            return self.entity.show(id)
        else:
            return 'Item notfound'
    
    def update(self, id, data):
        item = self.repository.find(id)
        
        if item is not None:
            return self.entity.update(id, data)
        else:
            return 'Item notfound'
    
    def delete(self, id):
        item = self.repository.find(id)
        
        if item is not None:
            if (self.entity.delete(id)):
                return 'Item Removed'
            else:
                return 'Could not remove item.'
        else:
            return 'Item notfound'
        
    def export(self):
        date = datetime.datetime.now()
        file = '%s/%s-%s.csv' % (config.get('export_path'), self.table, date.strftime("%Y-%m-%d-%H%M%S"))
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