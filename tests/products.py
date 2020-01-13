import unittest
from app.service import Crud
from app.model import Product, Client
from app.connection import Connection
from app.repository import Repository

class TestsProducts(unittest.TestCase):
    def setUp(self):
        self.connection = Connection(True)
        self.entity = Product()
        self.repository = Repository(self.connection, self.entity.__tablename__)
        
        self.create_product()
        
    def create_product(self):
        _initTest = Crud(self.entity, 'store', self.connection)
        
        data = [
            {
                'client_id': 1,
                'name': 'Product Name',
                'price': 1000
            }
        ]
        
        return _initTest.store(data)
        
    def test_store_products(self):
        _initTest = Crud(self.entity, 'store', self.connection)
        
        data = [
            {
                'client_id': 1,
                'name': 'Product Name',
                'price': 1000
            }
        ]
        
        response = _initTest.store(data)
        self.assertTrue(response != None)
        self.assertEqual(response[1], 1)
        self.assertEqual(response[2], data[0].get('name'))

    def test_show_products(self):
        _initTest = Crud(self.entity, 'show', self.connection)
        
        response = _initTest.show(1)
        self.assertTrue(response != None)
        
    def test_index_products(self):
        _initTest = Crud(self.entity, 'index', self.connection)
        
        response = _initTest.index()
        self.assertTrue(response != None)
        
    def test_update_products(self):
        _initTest = Crud(self.entity, 'update', self.connection)
        
        last = self.repository.last()
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
        
        last = self.repository.last()
        
        response = _initTest.delete(last[0])
        self.assertTrue(response != None)