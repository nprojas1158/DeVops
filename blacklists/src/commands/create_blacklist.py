from ..errors.errors import IncompleteParams, ExternalError
from ..model.emailBlacklist import EmailBlacklist,CreatedEmailBlacklistSchema
from ..session import Session
import datetime
import json

class CreateBlacklist():
    def __init__(self, data, client_ip):
        self.data = data
        self.ip = client_ip
    
    def execute(self):
        # try:
        required_fields = ['email', 'app_uuid']
        if not all(field in self.data for field in required_fields):
            raise IncompleteParams()

        black_schema = EmailBlacklist(
        email = self.data['email'],
        appId = self.data['app_uuid'],
        reason = self.data['blocked_reason'],
        dirIp = self.ip,
        dateHour = datetime.datetime.now()
        )
        
        session = Session()
        session.add(black_schema)
        session.commit()

        new_black = {}
        new_black['email'] = black_schema.email
        new_black['dateHour'] = black_schema.dateHour

        session.close()
        return new_black
        
        # except (TypeError):
        #     raise ExternalError




            

            