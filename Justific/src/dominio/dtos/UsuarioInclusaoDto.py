from pydantic import BaseModel

class UsuarioInclusaoDto(BaseModel):
    '''
    DTO para inclusão de um novo usuário
    '''
    login: str
    senha: str
    