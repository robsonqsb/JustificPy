from pydantic import BaseModel

class OrganizacaoDto(BaseModel):
    '''
    DTO com propriedades relacionadas a organização
    '''
    cnpj: str
    nome: str
    