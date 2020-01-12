import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

from alembic import op
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date
from app.repository import Repository
from app.connection import Connection

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    ## Columns of model Client
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    
    fields_store = {
        'name': 'Nome do Cliente: ',
        'email': 'Email do Cliente: '
    }
    
    fields_update = {
        'name': 'Novo nome do Cliente: ',
        'email': 'Novo e-mail do Cliente: '
    }
    
class Product(Base):
    __tablename__ = 'products'

    ## Columns of model Product
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    name = Column(String(50))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    
    fields_store = {
        'client_id': 'Id do cliente: ',
        'name': 'Nome do Produto: ',
        'price': 'Valor do produto: '
    }
    
    fields_update = {
        'name': 'Novo nome do Produto: ',
        'price': 'Novo valor do produto: '
    }
    
    def validators(self, data):
        tableClient = Client.__tablename__
        entityClient = Entity(tableClient)
        repository = entityClient.repository()
        
        errors = []
        
        for row in data:
            clientId = row.get('client_id')
            find = repository.find(clientId, tableClient)
            
            if find is None:
                errors.append('Client notfound')
                
        errors = list(errors)
        
        if len(errors) > 0:
            return errors
        
        return False
    
class Entity(object):
    def __init__(self, table, connection):
        self.table = table
        self.connection = connection
    
    def repository(self):
        rep = Repository(self.connection, self.table);
        
        return rep
    
    def setDate(self, data, type):
        items = []
        date = datetime.datetime.now()
        for row in data:
            item = row
            item.update({
                '%s' % type: date.strftime("%Y-%m-%d %H:%M:%S")
            })
            items.append(item)
        
        return items
    
    def index(self):
        return self.repository().findAll()
    
    def store(self, data):
        items = self.setDate(data, 'created_at')
        rep = self.repository().insert(items)
        
        return rep.last()
    
    def show(self, id):
        return self.repository().find(id)
    
    def update(self, id, data):
        items = self.setDate(data, 'updated_at')
        rep = self.repository().update(id, items)
            
        return rep.find(id)
    
    def delete(self, id):
        try:
            self.repository().delete(id)
            return True
        except Exception as err:
            print('Could not remove item. %s' % err)
            return False