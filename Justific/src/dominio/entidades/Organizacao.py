from datetime import datetime
from Justific.src.dominio.entidades import EntidadeBase

class Organizacao(EntidadeBase):
    '''
    Classe que representa uma organização
    '''
    def __init__(self, _id: str = None, data_criacao: datetime = None, nome: str = None, cnpj: str = None):
        super().__init__(_id, data_criacao)
        self.nome = nome
        self.cnpj = cnpj
