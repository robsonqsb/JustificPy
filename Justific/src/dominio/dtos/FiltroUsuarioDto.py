from pydantic import BaseModel

class FiltroUsuarioDto(BaseModel):
    '''
    DTO para filtro dos registros de usuário
    '''
    login: str
    