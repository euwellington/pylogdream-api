from jinja2 import Undefined
from src.interface.Usuario import UsuarioInterface
from src.repository.Usuario import UsuarioRepository

class UsuarioService:

    def getAll() -> None:
        try:    
            return UsuarioRepository.getAll()
        except Exception as err:
            return err
    
    def create(u) -> None:
        usuario = UsuarioInterface(u)
        try:    
            # return usuario.object()
            if(UsuarioRepository.post(usuario.object())):
                return usuario
            return 'Erro ao cadastrar usuário'
        except Exception as err:
            return err