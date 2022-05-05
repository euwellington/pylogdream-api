from src.repository.scripts import Evento
from src.service.instance import server
from flask_restx import Resource, Namespace
from src.model.Auth import authModel

app, api = server.app, server.api

navigate = Namespace('Auth')
api.add_namespace(navigate)

@navigate.route('')
class ControllerAll(Resource):
    @api.expect(authModel, validate=True)
    def post(self, ) -> None:
        payload = api.payload
        return payload
    