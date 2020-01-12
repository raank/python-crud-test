import unittest
from app.service import Crud
from app.model import Client
from app.connection import Connection

class TestsClients(unittest.TestCase):
    def setUp(self):
        self.connection = Connection(True)
        self.entity = Client()
        
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
        _initTest = Crud(self.entity, 'show', self.connection)
        
        last = _initTest.repository.last()
        
        response = _initTest.show(last[0])
        self.assertTrue(response != None)
        
    def test_index_clients(self):
        _initTest = Crud(self.entity, 'index', self.connection)
        
        response = _initTest.index()
        self.assertTrue(response != None)
        self.assertTrue(len(list(response)) > 0)
        
    def test_update_clients(self):
        _initTest = Crud(self.entity, 'update', self.connection)
        
        last = _initTest.repository.last()
        data = [
            {
                'email': 'johon.doe@gmail.com'
            }
        ]
        
        response = _initTest.update(last[0], data)
        self.assertTrue(response != None)
        self.assertEqual(response[2], data[0].get('email'))
        
    def test_delete_clients(self):
        _initTest = Crud(self.entity, 'delete', self.connection)
        
        last = _initTest.repository.last()
        
        response = _initTest.show(last[0])
        self.assertTrue(response != None)