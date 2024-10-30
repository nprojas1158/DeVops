from ..errors.errors import MissingToken, Unauthorized, ExternalError


class Authenticate():
    def __init__(self, token):
        self.token = token

    def verify(self):
        val_token = "Bearer 75c893b6-9084-4ce2-af52-805d5d124267"
        
        if self.token is None:
            raise MissingToken()
        
        if val_token == self.token:
            return True
        else:
            raise Unauthorized()