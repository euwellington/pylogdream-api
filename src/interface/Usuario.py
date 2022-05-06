from typing import Any


class UsuarioInterface:
    def __init__(self, usuario) -> None:
        self.id: str = usuario['id']
        self.equipamentoId: str = usuario['equipamentoId']
        self.nome: str = usuario['nome']
        self.cpf: str = usuario['cpf']
        self.email: str = usuario['email']
        self.nascimento: str = usuario['nascimento']
        self.senha: str = usuario['senha']
        # self.dataCadastro: str = usuario['dataCadastro'] 

    def object(self):
        object = {
            'id': self.id,
            'equipamentoId': self.equipamentoId,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'nascimento': self.nascimento,
            'senha': self.senha,
            # 'dataCadastro': self.dataCadastro
        }
        return object