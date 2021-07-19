from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from sub_programs import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_blue(self):
    # We will mock a response of 1 and test that we get football returned.
        with patch('requests.get') as g:
            g.return_value.text = "Blue"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)