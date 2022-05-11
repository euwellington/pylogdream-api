import hashlib
import jwt
from src.interface.Auth import AuthInterface
from src.service.instance import server
from src.interface.Usuario import UsuarioInterface
from src.service.Usuario import UsuarioService

api = server.api

class AuthService:
    def getUser(u):
        payload = AuthInterface(u)
        try:
            usuarios = UsuarioService.getAll()
            for u in usuarios:
                usuario = UsuarioInterface(u)
                if(usuario.email == payload.email and usuario.senha == hashlib.sha256(payload.senha.encode('utf-8')).hexdigest()):
                    generateToken = jwt.encode(
                        payload=usuario.object(),
                        key='MY_SECRET'
                    )
                    return generateToken
        except Exception as err:
            return err