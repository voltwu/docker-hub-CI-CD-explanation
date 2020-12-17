import unittest
import urllib.request

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        req = urllib.request.Request(url = 'http://0.0.0.0:8000/cgi-bin/hello.py?first_name=test&last_name=test',method = 'GET')
        f = urllib.request.urlopen(req)
        self.assertEqual(f.code,200)

if __name__ == '__main__':
    unittest.main()
