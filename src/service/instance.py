import email
import os
from flask import Flask
from flask_restx import Api
from flask_cors import CORS

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

port = int(os.environ.get("PORT", 5000))

class Server():
    def __init__(self, ) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app,
            title='LOGDREAM-API',
            description='API DO LOGDREAM - CRIADO: 05/05/2022',
            version='1.0',
            security='Bearer Auth',
            authorizations=authorizations,
            email='wellingtoncontato02@gmail.com'
            # doc='/api'
        )

    def run(self):
        self.app.run(
            debug=True,
            host='0.0.0.0',
            port=port
        )

server = Server()