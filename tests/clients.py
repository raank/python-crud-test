import unittest
from app.service import Crud
from app.model import Client
from app.connection import Connection
from app.repository import Repository

class TestsClients(unittest.TestCase):
    def setUp(self):
        self.connection = Connection(True)
        self.entity = Client()
        self.repository = Repository(self.connection, self.entity.__tablename__)
    
    def create_client(self):
        _initTest = Crud(self.entity, 'store', self.connection)
        
        data = [
            {
                'name': 'John Doe',
                'email': 'johon@doe.com'
            }
        ]
        
        return _initTest.store(data)
        
    def test_store_clients(self):
        _initTest = Crud(self.entity, 'store', self.connection)
        
        data = [
            {
                'name': 'John Doe',
                'email': 'johon@doe.com'
            }
        ]
        
        response = _initTest.store(data)
        
        self.assertTrue(response != None)
        self.assertEqual(response[1], data[0].get('name'))
        
    def test_show_clients(self):
        self.create_client()
        _initTest = Crud(self.entity, 'show', self.connection)
        
        response = _initTest.show(1)
        self.assertTrue(response != None)
    
    def test_index_clients(self):
        _initTest = Crud(self.entity, 'index', self.connection)
        
        response = _initTest.index()
        self.assertTrue(response != None)
        
    def test_update_clients(self):
        _initTest = Crud(self.entity, 'update', self.connection)
        
        data = [
            {
                'email': 'johon.doe@gmail.com'
            }
        ]
        
        response = _initTest.update(1, data)
        self.assertTrue(response != None)
        self.assertEqual(response[2], data[0].get('email'))
        
    def test_delete_clients(self):
        _initTest = Crud(self.entity, 'delete', self.connection)
        
        last = _initTest.repository.last()
        
        if last is None:
            last = self.create_client()
        
        response = _initTest.delete(last[0])
        self.assertTrue(response != None)