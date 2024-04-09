import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
import flaskr.db

class GetDBTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config = {"DATABASE": "test_db", "SERVER_NAME": "localhost.localdomain", "APPLICATION_ROOT": "/", "PREFERRED_URL_SCHEME": "http"}

    @patch('flaskr.db.get_db')
    def test_get_db_new_connection(self, mock_get_db):
        with self.app.app_context():
            mock_get_db.return_value = MagicMock()
            flaskr.db.get_db()
            mock_get_db.assert_called_once()

if __name__ == "__main__":
    unittest.main()
