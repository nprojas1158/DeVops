from ..errors.errors import MissingToken, Unauthorized
import jwt

SECRET_KEY = 'temporal'

class Authenticate():
    def __init__(self, token):
        self.token = token

    def verify(self):
        if not self.token:
            raise MissingToken
        
        # decoded = jwt.decode(self.token, SECRET_KEY, algorithms=["HS256"])
        # print(decoded)
        return self.token

        #except jwt.InvalidTokenError:
         #   raise Unauthorized