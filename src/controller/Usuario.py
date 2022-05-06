import hashlib
from src.repository.scripts import Evento
from src.service.instance import server
from flask_restx import Resource, Namespace
from src.service.Usuario import UsuarioService
from src.model.Usuario import usuarioModel
from src.interface.Usuario import UsuarioInterface
from uuid import uuid4

app, api = server.app, server.api

navigate = Namespace('Usuario')
api.add_namespace(navigate)

@navigate.route('')
class ControllerAll(Resource):
    
    def get(self, ) -> None: 
        try:
            return UsuarioService.getAll()
        except Exception as err:
            return err


    @api.expect(usuarioModel, validate=False)
    def post(self, ) -> None:
        try:
            usuario = UsuarioInterface(api.payload)
            usuario.id = str(uuid4())
            usuario.senha = hashlib.sha256(usuario.senha.encode('utf-8')).hexdigest()
            return UsuarioService.create(usuario.object())
        except Exception as err:
            return err



    def put(self, ) -> None:
        return 
    
@navigate.route('/<id>')
class ControllerId(Resource):
    
    def get(self, ) -> None: 
        return 

    def delete(self, ) -> None:
        return 
        
@navigate.route('/equipamento/<id>')
class ControllerEquipamentoId(Resource):
    
    def get(self, ) -> None: 
        return 
        