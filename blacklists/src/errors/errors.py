class ApiError(Exception):
    code = 422
    description = "Default message"

class Unauthorized(ApiError):
    code = 401
    description = "Unauthorized"

class NoContent(ApiError):
    code = 204
    description = "NoContent"

class IncompleteParams(ApiError):
    code = 400
    description = "Bad request"

class MissingToken(ApiError):
    code = 403
    description = "Missing token"

class ExternalError(ApiError):
    code = 422  # Default
    description = "External error"

    def __init__(self, code):
        self.code = code