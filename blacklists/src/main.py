from dotenv import load_dotenv, find_dotenv
import os
loaded = load_dotenv(os.path.join(os.path.dirname(__file__), '..','.env.template'))

from model.emailBlacklist import EmailBlacklist
from session import engine
from flask import Flask, jsonify

app = Flask(__name__)

EmailBlacklist.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)