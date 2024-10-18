from errors.errors import IncompleteParams, ExternalError
from model.emailBlacklist import EmailBlacklist
from session import Session
import datetime

class CreateBlacklist():
    def __init__(self, data, client_ip):
        self.data = data
        self.ip = client_ip
    
    def execute(self):
        try:
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
            session.close()
            return black_schema
        
        except (TypeError):
            raise ExternalError




            

            