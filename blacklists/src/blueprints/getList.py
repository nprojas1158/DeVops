from flask import Blueprint, request, jsonify
from commands.create_blacklist import CreateBlacklist
from commands.authenticate import Authenticate
from errors.errors import MissingToken

getList_blueprint = Blueprint('blacklists', __name__)

@getList_blueprint.route('/blacklists', methods=['GET'])
def create():
    auth = Authenticate(auth_token()).verify()
    client_ip = request.remote_addr
    black = getBlacklist(request.get_json, client_ip).execute()
    return jsonify(black), 201
