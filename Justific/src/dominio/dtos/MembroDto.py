from pydantic import BaseModel

class MembroDto(BaseModel):
    '''
    DTO com propriedades relacionadas a membro
    '''
    codigo_registro: str
    nome: str
    cnpj_organizacao: str