from src.service.instance import server
from src.controller.Evento import *
from src.controller.Acionamento import *
from src.controller.Usuario import *
from src.controller.Auth import *
from src.controller.Mqtt import *
from src.controller.Equipamento import *
from src.controller.Nota import *
from src.controller.Endereco import *
from src.controller.Socket import *

server.api.route()

server.run()