from pydantic import BaseModel

class FiltroOrganizacaoDto(BaseModel):
    '''
    DTO para filtro da lista de organizações
    '''
    cnpj: str
    nome: str
