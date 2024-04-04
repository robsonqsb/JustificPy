from pydantic import BaseModel

class UsuarioDto(BaseModel):
    '''
    DTO para inclusão de um novo usuário
    '''
    login: str
    senha: str
    