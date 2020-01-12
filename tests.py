import unittest
from tests.clients import TestsClients
from tests.products import TestsProducts

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._clients = TestsClients
        cls._products = TestProducts
    
if __name__ == '__main__':
    unittest.main()