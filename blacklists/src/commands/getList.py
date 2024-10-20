from flask import jsonify
from errors.errors import IncompleteParams, ExternalError
from model.emailBlacklist import EmailBlacklist
from session import Session


class getBlacklist():
    def __init__(self,  email):
    
        self.email = email
    
    def validar_email(self):
        email_entry = EmailBlacklist.query.filter_by(email=self.email).first()
    
        if email_entry:
            return jsonify({'mensaje': 'El email existe en la base de datos.', 'email': self.email}), 200
        else:
            return jsonify({'mensaje': 'El email no existe en la base de datos.', 'email': self.email}), 404

        
      