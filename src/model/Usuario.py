from flask_restx import fields
from src.service.instance import server
import uuid


usuarioModel = server.api.model('Usuario', {
    'id' : fields.String(default='001a8b41-cb3a-4a7e-b7dd-6bf0fca1f51d'),
    'equipamentoId' : fields.String(default='001a8b41-cb3a-4a7e-b721-6bf0fca1f51d'),
    'nome' : fields.String(default='string'),
    'cpf' : fields.String(default='string'),
    'email' : fields.String(default='string'),
    'nascimento' : fields.String(default='string'),
    'senha' : fields.String(default='string'),
})