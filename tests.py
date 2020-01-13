import unittest
from tests.clients import TestsClients
from tests.products import TestsProducts
from app.connection import Connection

class Test(unittest.TestCase):
    def __init__(self):
        self.connection = Connection(True)
        
    @classmethod
    def setUpClass(cls):
        cls._clients = TestsClients(self.connection)
        cls._products = TestProducts(self.connection)
    
if __name__ == '__main__':
    unittest.main()