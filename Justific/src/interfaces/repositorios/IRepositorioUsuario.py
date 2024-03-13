from abc import abstractmethod
from Justific.src.interfaces.repositorios.IRepositorioBase import IRepositorioBase

class IRepositorioUsuario(IRepositorioBase):
    '''
    Repositório para obter informações de usuário a base
    '''
    @abstractmethod
    def confirmar_login(self, login, senha) -> bool:
        '''
        Verifica se o login e senha estão corretos
        '''
