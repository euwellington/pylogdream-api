
class AuthInterface:
    def __init__(self, usuario) -> None:
        self.email: str = usuario['email']
        self.senha: str = usuario['senha']
        # self.dataCadastro: str = usuario['dataCadastro'] 

    def object(self):
        object = {
            'email': self.email,
            'senha': self.senha,
            # 'dataCadastro': self.dataCadastro
        }
        return object