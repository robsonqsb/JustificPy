from Justific.src.modelos.EntidadeBase import EntidadeBase

class Usuario(EntidadeBase):
    '''
    Usuário do sistema
    '''

    def __init__(self, login, senha):
        super().__init__()
        self.login = login
        self.senha = senha

    def __str__(self) -> str:
        return 'usuario'
        