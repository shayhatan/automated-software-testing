# flask_basics/tests/system/test_home.py
from flask_basics.tests.system.base_test import BaseTest

class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            r = c.get("/")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.get_json(), {"message": "Hello, world!"})
