from src.interface.Usuario import UsuarioInterface
from datetime import datetime

class Script():

    def getAll():
        query = 'SELECT * FROM usuarios'
        return query

    def create(u):
        usuario = UsuarioInterface(u)
        query = 'SELECT * FROM eventos{0}'.format(usuario.nome)
        
        return query