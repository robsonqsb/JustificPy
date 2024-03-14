from EntidadeBase import EntidadeBase

class Usuario(EntidadeBase):
    '''
    Entidade que representa um usuário do sistema
    '''
    def __init__(self, login: str, senha: str):
        super().__init__()
        self.login = login
        self.senha = senha
