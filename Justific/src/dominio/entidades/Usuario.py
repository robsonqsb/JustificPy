import datetime
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase

class Usuario(EntidadeBase):
    '''
    Entidade que representa um usuário do sistema
    '''
    def __init__(self, _id: str = None, data_criacao: datetime = None, login: str = None, senha: str = None):
        super().__init__(_id, data_criacao)
        self.login = login
        if senha is not None:
            self.senha = senha
