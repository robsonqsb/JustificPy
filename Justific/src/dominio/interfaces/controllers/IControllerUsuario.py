from abc import abstractmethod
from Justific.src.dominio.interfaces.controllers.IControllerBase import IControllerBase

class IControllerUsuario(IControllerBase):
    '''
    Controller para manipulação do usuário
    '''

    @abstractmethod
    def confirmar_dados_login(self, login: str, senha: str) -> bool:
        '''
        Método para confirmação do dados de login
        '''
