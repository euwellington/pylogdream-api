from flask_restx import fields
from src.service.instance import server


authModel = server.api.model('Auth', {
    'email' : fields.String(Description='Email do usuário', required=True),
    'senha' : fields.String(Description='Senha do usuário', required=True)
})