from src.interface.Usuario import UsuarioInterface
from datetime import datetime

class Script():

    def getAll():
        query = 'SELECT * FROM usuarios'
        return query

    def create(u):
        usuario = UsuarioInterface(u)
        query = "INSERT INTO usuarios (id, equipamentoId, nome, cpf, email, nascimento, senha, dataCadastro) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(usuario.id, usuario.equipamentoId, usuario.nome, usuario.cpf, usuario.email, usuario.nascimento, usuario.senha, datetime.now()) 
        return query