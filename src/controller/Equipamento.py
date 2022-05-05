from src.repository.scripts import Evento
from src.service.instance import server
from flask_restx import Resource, Namespace

app, api = server.app, server.api

navigate = Namespace('Equipamento')
api.add_namespace(navigate)

@navigate.route('')
class ControllerAll(Resource):
    
    def get(self, ) -> None: 
        return 

    def post(self, ) -> None:
        return 

    def put(self, ) -> None:
        return 
    
@navigate.route('/<id>')
class ControllerId(Resource):
    
    def get(self, ) -> None: 
        return 

    def delete(self, ) -> None:
        return 

        