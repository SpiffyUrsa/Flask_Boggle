from unittest import TestCase
from flask import session

from app import app, boards
from app import SESS_BOARD_UUID_KEY

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True
# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertIn(SESS_BOARD_UUID_KEY, session)
            self.assertIn("<td>", html)
            self.assertIn("<form action='#' id='submit-word'>", html)


    def test_api_score_word(self):
        """Make sure the word is valid"""

        with app.test_client() as client:
            client.get("/")
            response = client.post('/api/score-word', json={ 'word': 'a' })
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'result': 'ok', 'word': 'A'})

            # make a board to contain certain rows/letters and assertEquals to check for the right answer
            
            