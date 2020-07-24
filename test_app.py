from unittest import TestCase
from flask import session

from app import app, boards
from app import SESS_BOARD_UUID_KEY


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            self.assertIn(SESS_BOARD_UUID_KEY, session)

            self.assertFalse("Write expectations here!")
