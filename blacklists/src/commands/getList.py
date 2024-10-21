from flask import jsonify
from ..errors.errors import NoContent
from ..model.emailBlacklist import EmailBlacklist
from ..session import Session


class getBlacklist():
    def __init__(self,  email):
    
        self.email = email
    
    def validar_email(self):
        session = Session()
        email_entry = session.query(EmailBlacklist).filter_by(email=self.email).first()

        response = {}
        response['exists'] = False
        if email_entry:
            response['exists'] = True
            response['blocked_reason'] = email_entry.blocked_reason
        else:
            response['blocked_reason'] = None
        
        return response