from abc import abstractmethod
from typing import Type
from Justific.src.interfaces.controllers.IControllerBase import IControllerBase
from Justific.src.interfaces.repositorios.IRepositorioUsuario import IRepositorioUsuario

class IControllerUsuario(IControllerBase):
    '''
    Controller para operações relacionadas a usuário
    '''
    def __init__(self, repositorio: Type[IRepositorioUsuario]):
        super().__init__(repositorio)

    @abstractmethod
    def confirmar_autenticacao(self, login: str, senha: str) -> bool:
        '''
        Verificar se os de login e senha estão corretos para autenticação
        '''
