

import unittest 
from run import app

class BitcoinTest(unittest.TestCase):

    home = app.test_client()

    def test_1_home(self):

        response = self.home.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_2_read_text(self):

        response = self.home.get('/', content_type='html/text')
        self.assertTrue(b'Choose desired currency' in response.data)

if __name__ == '__main__':
    unittest.main()