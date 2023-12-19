import unittest
from flask import Flask
from flask.testing import FlaskClient
import requests

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def atg_website(self):
        url = 'http://atg.world'
        response = requests.get(url)

        self.assertEqual(response.status_code, 200, f"Failed to connect to {url}. Status code: {response.status_code}")
        print(f"Successfully connected to {url}")

    def hello_world_route(self):
        client = self.app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
