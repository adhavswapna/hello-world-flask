import unittest
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/atg')
def atg_world():
    response = request.get('http//atg.world')

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_connect_to_atg_website(self):
        response = self.app.get('/atg')
        self.assertEqual(response.status_code, 200, f"Failed to connect. Status code: {response.status_code}")
        print("Successfully connected to /atg.")

    def test_hello_world_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, f"Failed to access the home route. Status code: {response.status_code}")
        self.assertIn('Hello, World!', response.data.decode())
        print("Successfully accessed the home route.")

if __name__ == '__main__':
    unittest.main()
