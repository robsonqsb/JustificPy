from pydantic import BaseModel

class FiltroMembroDto(BaseModel):
    '''
    DTO para filtro de membros
    '''
    codigo_registro: str
    nome: str
    cnpj_organizacao: str
