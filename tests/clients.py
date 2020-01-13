import unittest
from app.service import Crud
from app.model import Client
from app.connection import Connection
from app.repository import Repository

class TestsClients(unittest.TestCase):
    def setUp(self):
        self.entity = Client()
        self.connection = Connection(True)
        
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
        
        last = _initTest.last()
        
        if last is None:
            id = 1
        else:
            id = last[0]
        
        response = _initTest.show(id)
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
        
        last = _initTest.last()
        response = _initTest.update(last[0], data)
        
        self.assertTrue(response != None)
        self.assertEqual(response[2], data[0].get('email'))