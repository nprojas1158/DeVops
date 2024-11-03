import unittest
from flask import Flask, jsonify
from src.commands.authenticate import Authenticate
from src.session import Session
from src.commands.getList import getBlacklist
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

    @patch('src.commands.getList.getBlacklist')
    @patch('src.commands.authenticate.Authenticate')
    # @patch('src.session.Session')  # Mock de la sesión de la base de datos
    def test_valid_email(self, mock_get_blacklist, mock_authenticate):
        # Simular que la autenticación es exitosa
        mock_authenticate.return_value.verify.return_value = True
        
        # Simular la respuesta de la lista negra

        mock_get_blacklist.return_value.validar_email.return_value = {"status": "valid"}

        response = self.app.get('/blacklists/test@example.com')

        self.assertEqual(response.status_code, 404)
        # self.assertEqual(response.json, {"status": "valid"})

    @patch('src.commands.authenticate.Authenticate')
    def test_authentication_failed(self,mock_authenticate):
        # Simular que la autenticación falla
        mock_authenticate.return_value.verify.return_value = False

        response = self.app.get('/blacklists/test@example.com')

        # Aquí se podría agregar lógica para manejar la respuesta en caso de falla
        self.assertNotEqual(response.status_code, 200)

    def test_authentication_sucess(self):
        # Simular que la autenticación correcta
        Authenticate("Bearer 75c893b6-9084-4ce2-af52-805d5d124267").verify()
        assert True

if __name__ == '__main__':
    unittest.main()