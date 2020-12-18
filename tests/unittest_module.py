import unittest
from importlib import util

class TestStringMethods(unittest.TestCase):

    def test_module_http(self):
        http_spec = util.find_spec("http")
        self.assertTrue(http_spec is not None)
        
    def test_module_socketserver(self):
        sser = util.find_spec("socketserver")
        self.assertTrue(sser is not None)
    
if __name__ == '__main__':
    unittest.main()

