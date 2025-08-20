# flask_basics/tests/system/base_test.py
from unittest import TestCase
from flask_basics.app import app

class BaseTest(TestCase):
    def setUp(self):
        super().setUp()
        app.config.update(TESTING=True)

        self.app = app.test_client
