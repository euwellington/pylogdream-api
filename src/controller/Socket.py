from src.repository.scripts import Evento
from src.service.instance import server
from flask_restx import Resource, Namespace

app, api = server.app, server.api

navigate = Namespace('Socket', ordered=True)
api.add_namespace(navigate)

@navigate.route('/enviar')
class ControllerAll(Resource):
    @api.doc(id='envia somente para um cliente')
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def post(self, ) -> None:
        return 
    
@navigate.route('/broadcast')
class ControllerAll(Resource):

    @api.doc(id='Enviar para todos os clientes')
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def post(self, ) -> None:
        return 
    