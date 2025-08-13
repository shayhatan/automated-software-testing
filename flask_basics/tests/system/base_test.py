"""
BaseTest

This class should be the parent class to each system test.
It gives each test a Flask test client that we can use.
"""

from unittest import TestCase
from flask_basics.app import app


class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app = app.test_client