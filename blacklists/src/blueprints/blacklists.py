from flask import Blueprint, request, jsonify
from ..commands.create_blacklist import CreateBlacklist
from ..commands.authenticate import Authenticate
from ..errors.errors import MissingToken

blacklists_blueprint = Blueprint('blacklists', __name__)

@blacklists_blueprint.route('/blacklists', methods=['POST'])
def create():
    auth = Authenticate(auth_token()).verify()
    
    if auth == True:
        client_ip = request.remote_addr
        black = CreateBlacklist(request.get_json, client_ip).execute()
        return jsonify(black), 201

@blacklists_blueprint.route('/blacklists/ping', methods=['GET'])
def ping():
    auth = Authenticate(auth_token()).verify()
    
    if auth == True:
        return jsonify('pong'), 200
    

def auth_token():
    try:
        if 'Authorization' in request.headers:
            authorization = request.headers['Authorization']
        else:
            raise MissingToken()
        return authorization
    except Exception as e:
        raise MissingToken()
   
