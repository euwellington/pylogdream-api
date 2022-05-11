import json
from os import stat
from src.repository.scripts import Evento
from src.service.instance import server
from flask_restx import Resource, Namespace
from src.model.Auth import authModel
from src.service.Auth import AuthService
from flask import Response

app, api = server.app, server.api

navigate = Namespace('Auth')
api.add_namespace(navigate)

@navigate.route('')
class ControllerAll(Resource):
    @api.expect(authModel, validate=True)
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def post(self, ) -> None:
        status = Response()
        response = AuthService.getUser(api.payload)
        if response:
            return response
        else:
            status.response = 'Usuário o senha incorreto'
            status.status_code = 400
            return status
