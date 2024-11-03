import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from unittest.mock import patch
from dotenv import load_dotenv, find_dotenv
import os

# Asumimos que el código de tu blueprint está en un módulo llamado `my_blueprint`
from src.blueprints.blacklists import blacklists_blueprint

app = Flask(__name__)
#app.register_blueprint(blacklists_blueprint)

class BlacklistEmailTestCase(unittest.TestCase):

    def setUp(self):
      self.app: Flask = app.test_client()
      self.app.testing = True
      load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env.test'))

    @patch('blacklists_blueprint.Authenticate')
    @patch('blacklists_blueprint.getBlacklist')
    @patch('src.Session')  # Mock de la sesión de la base de datos
    @patch('model.EmailBlacklist')
    def test_valid_email(self, mock_get_blacklist, mock_authenticate):
        # Simular que la autenticación es exitosa
        mock_authenticate.return_value.verify.return_value = True
        
        # Simular la respuesta de la lista negra

        mock_get_blacklist.return_value.validar_email.return_value = {"status": "valid"}

        response = self.app.get('/blacklists/test@example.com')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "valid"})

    @patch('blacklists.Authenticate')
    def test_authentication_failed(self, mock_authenticate):
        # Simular que la autenticación falla
        mock_authenticate.return_value.verify.return_value = False

        response = self.app.get('/blacklists/test@example.com')

        # Aquí se podría agregar lógica para manejar la respuesta en caso de falla
        self.assertNotEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()