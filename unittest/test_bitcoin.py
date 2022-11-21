
from run import app 
import unittest 

class BitcoinTest(unittest.TestCase):

    def setUp(self):
        self.home = app.test_client(self)

    def test_home_load(self):

        result = self.home.get('/', content_type='html/text')
        self.assertEqual(result.status_code, 200)

    def test_home_page_text(self):

        result = self.home.get('/', content_type = 'html/text')
        self.assertTrue(b'Choose desired currency' in result.data)

if __name__ == '__main__':
    unittest.main()
