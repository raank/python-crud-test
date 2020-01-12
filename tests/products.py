import unittest
from app.service import Crud
from app.model import Product, Client
from app.connection import Connection

class TestsProducts(unittest.TestCase):
    def setUp(self):
        self.connection = Connection(True)
        self.entity = Product()
        
    def lastClient(self):
        clients = Crud(self.entity, 'show', self.connection)

        return clients.repository.last()
        
    def test_store_products(self):
        _initTest = Crud(self.entity, 'store', self.connection)
        
        client = self.lastClient()
        
        data = [
            {
                'client_id': client[0],
                'name': 'Product Name',
                'price': 1000
            }
        ]
        
        response = _initTest.store(data)
        self.assertTrue(response != None)
        self.assertEqual(response[1], client[0])
        
    def test_show_products(self):
        _initTest = Crud(self.entity, 'show', self.connection)
        
        last = _initTest.repository.last()
        
        response = _initTest.show(last[0])
        self.assertTrue(response != None)
        
    def test_index_products(self):
        _initTest = Crud(self.entity, 'index', self.connection)
        
        response = _initTest.index()
        self.assertTrue(response != None)
        self.assertTrue(len(list(response)) > 0)
        
    def test_update_products(self):
        _initTest = Crud(self.entity, 'update', self.connection)
        
        last = _initTest.repository.last()
        data = [
            {
                'price': 2000
            }
        ]
        
        response = _initTest.update(last[0], data)
        self.assertTrue(response != None)
        self.assertEqual(response[3], data[0].get('price'))
        
    def test_delete_products(self):
        _initTest = Crud(self.entity, 'delete', self.connection)
        
        last = _initTest.repository.last()
        
        response = _initTest.show(last[0])
        self.assertTrue(response != None)