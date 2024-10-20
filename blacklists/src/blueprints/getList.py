from flask import Blueprint, request, jsonify
from commands.getList import getBlacklist
from commands.authenticate import Authenticate
from errors.errors import MissingToken

getList_blueprint = Blueprint('blacklists', __name__)

@getList_blueprint.route('/blacklists/<email>', methods=['GET'])
def ValidarEmail(email):
    auth = Authenticate(auth_token()).verify()
    black = getBlacklist(email).execute()
    return jsonify(black), 201
