from jinja2 import Undefined
from src.interface.Usuario import UsuarioInterface
from src.repository.Usuario import UsuarioRepository

class UsuarioService:

    def getAll() -> None:
        try:    
            return UsuarioRepository.getAll()
        except Exception as err:
            return err
    
    # def create(u) -> None:
    #     usuario = UsuarioInterface(u)
    #     try:  
    #         response = UsuarioRepository.post(usuario.object())
    #         if response == u:
    #             return True
    #         return response.args
    #     except Exception as err:
    #         return err