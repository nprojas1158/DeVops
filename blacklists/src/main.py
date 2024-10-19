from dotenv import load_dotenv, find_dotenv
import os
loaded = load_dotenv(os.path.join(os.path.dirname(__file__), '..','.env.template'))

from .errors.errors import ApiError
from .blueprints.blacklists import blacklists_blueprint
from .model.emailBlacklist import EmailBlacklist
from .session import engine
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(blacklists_blueprint)

EmailBlacklist.metadata.create_all(engine)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code
if __name__ == '__main__':
    app.run(debug=True)