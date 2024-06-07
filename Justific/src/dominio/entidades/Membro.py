from datetime import datetime
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase

class Membro(EntidadeBase):
    '''
    Classe que representa o membro de uma organização
    '''
    def __init__(self, _id: str = None, data_criacao: datetime = None, codigo_registro: str = None, nome: str = None, organizacao_id: str = None):
        super().__init__(_id, data_criacao)
        self.codigo_registro = codigo_registro
        self.nome = nome
        self.organizacao_id = organizacao_id
