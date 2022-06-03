import unittest
from main import result_api

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'https://api.kauri.finance/api/v1/currency'

    def test_result(self):
        data = 'success'
        self.assertEqual(data, result_api(self.url)['status'])
    
    def test_fake(self):
        fake_url = 'https://api.kauri.finance/api/v1/user/create'
        data = 'error'
        self.assertEqual(data, result_api(fake_url)['status'])

    def test_dict(self):
        self.assertEqual('dict', type(result_api(self.url)).__name__)

if __name__ == '__main__':
    unittest.main()