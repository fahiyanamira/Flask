from flask import Flask, app
from flask_restful import Api

app = Flask(__name__, template_folder='views')
api = Api(app, prefix='/api')
web = Api(app)

from app import routes