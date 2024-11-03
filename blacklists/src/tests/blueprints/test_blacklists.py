import unittest
from flask import Flask, jsonify
from unittest.mock import patch, MagicMock
from src.blueprints.blacklists import blacklists_blueprint
from src.errors.errors import MissingToken
from src.commands.create_blacklist import CreateBlacklist
from src.commands.authenticate import Authenticate
from src.session import Session
from src.commands.getList import getBlacklist
from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)

class TestBlacklists(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(blacklists_blueprint)
        self.client = self.app.test_client()

    @patch('src.commands.create_blacklist.CreateBlacklist')
    @patch('src.commands.authenticate.Authenticate')
    def test_create_blacklist_success(self, MockCreateBlacklist, MockAuthenticate):
        MockAuthenticate.return_value.verify.return_value = True

        mock_blacklist_response = {'email': 'test@correo.com', 'dateHour': '2024-10-28T12:00:00'}
        MockCreateBlacklist.return_value.execute.return_value = mock_blacklist_response

        response = self.client.post('/blacklists', json={
            'email': 'test@correo.com',
            'app_uuid': '1234-5678',
            'blocked_reason': 'Spam'
        
        }, headers={'Authorization': 'Bearer 75c893b6-9084-4ce2-af52-805d5d124267'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, mock_blacklist_response)

    @patch('src.commands.authenticate.Authenticate') 
    def test_create_blacklist_missing_token(self, MockAuthenticate):
        MockAuthenticate.return_value.verify.side_effect = MissingToken()

        response = self.client.post('/blacklists', json={
            'email': 'test@example.com',
            'app_uuid': '1234-5678',
            'blocked_reason': 'Spam'
        }, headers={'Authorization': 'Bearer 75c893b6-9084-4ce2-af52-805d5d124267'})

        self.assertEqual(response.status_code, 403)  

    @patch('src.commands.getList.getBlacklist')  
    @patch('src.commands.authenticate.Authenticate')  
    def test_validar_email_success(self, MockGetBlacklist, MockAuthenticate):
        MockAuthenticate.return_value.verify.return_value = True

        mock_email_response = {'email': 'test@example.com', 'status': 'blacklisted'}
        MockGetBlacklist.return_value.validar_email.return_value = mock_email_response
        
        response = self.client.get('/blacklists/test@example.com', 
                                   headers={'Authorization': 'Bearer 75c893b6-9084-4ce2-af52-805d5d124267'})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_email_response)

    @patch('src.commands.authenticate.Authenticate')
    def test_validar_email_missing_token(self, MockAuthenticate):
        MockAuthenticate.return_value.verify.side_effect = MissingToken()

        response = self.client.get('/blacklists/test@example.com')

        self.assertEqual(response.status_code, 403)  

    def test_ping(self):
        response = self.client.get('http://127.0.0.1:3000/blacklists/ping')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, 'pong')