from src.repository.scripts import Evento
from src.service.instance import server
from flask_restx import Resource, Namespace

app, api = server.app, server.api

navigate = Namespace('Mqtt')
api.add_namespace(navigate)

@navigate.route('/enviar')
class ControllerAll(Resource):

    def post(self, ) -> None:
        return 
    