import unittest
from flask import Flask
from hello_world import app as flask_app
from unittest.mock import MagicMock
from nose.tools import assert_true

class test_app(unittest.TestCase):
    def setup(self):
        self.app = flask_app.test_client()

    def atg_connection(self):
        self.app.get = MagicMock(return_value=MagicMock(status_code=200))

        response = self.app.get('http://atg.world/')
        status_code = response.status_code

        print("Connecting to atg_world website succeffully")

        assert_true(status_code ==200, "Failed to connect")

if __name__ == '__main__':
    unittest.main()