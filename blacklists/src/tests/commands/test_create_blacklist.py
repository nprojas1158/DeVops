import unittest
from unittest.mock import patch, MagicMock
from src.commands.create_blacklist import CreateBlacklist
from src.model.emailBlacklist import EmailBlacklist
from src.errors.errors import IncompleteParams, ExternalError
from src.session import Session
import datetime

class CreateBlacklistTest(unittest.TestCase):
    def setUp(self):
        self.client_ip = '192.168.1.1'
        self.data_valid = {
            'email': 'prueba@correo.com',
            'app_uuid': '72c0a3c3-0d1b-42d9-ba3c-a42eb0d1c09c',
            'blocked_reason': 'Spam'
        }
        self.data_incomplete = {
            'email': '',
            'app_uuid': '72c0a3c3-0d1b-42d9-ba3c-a42eb0d1c09c'
        }

   # @patch('src.session.Session')
    #@patch('src.model.emailBacklist.EmailBlacklist')
    #def test_execute_success(self, MockEmailBacklist, MockSession, mock_authenticate):
     #   mock_authenticate.return_value.verify.return_value = True
      #  mock_session = MockSession.return_value
       # mock_black_schema = MockEmailBacklist.return_value
        #mock_black_schema.email = self.data_valid['email']
        #mock_black_schema.dateHour = datetime.datetime.now()

        #blacklist_creator = CreateBlacklist(self.data_valid, self. client_ip)
        #result = blacklist_creator.execute()

        #self.assertEqual(result['email'], self.data_valid['email'])
        #self.assertIsInstance(result['dateHour'], datetime.datetime)
        #mock_session.add.assert_called_once()
        #mock_session.close.assert_caled_once()

    def test_execute_incomplete_params(self):
        blacklist_creator = CreateBlacklist(self.data_incomplete, self.client_ip)

        with self.assertRaises(IncompleteParams):
            blacklist_creator.execute()

    #@patch('src.session.Session')
    #def test_execute_external_error(self, MockSession):
     #   mock_session = MockSession.return_value
      #  mock_session.commit.side_effect = TypeError("Test error")

       # blacklist_creator = CreateBlacklist(self.data_incomplete, self.client_ip)

        #with self.assertRaises(ExternalError):
         #   blacklist_creator.execute()
