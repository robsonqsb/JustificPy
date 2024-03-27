from abc import ABC, abstractmethod
from Justific.src.dominio.interfaces.repositorios.IRepositorioBase import IRepositorioBase

class IRepositorioUsuario(IRepositorioBase, ABC):
    '''
    Repositório de operação dos dados de usuário
    '''
    @abstractmethod
    def confirmar_dados_autenticacao(self, login: str, senha: str):
        '''
        Localiza o usuário pelo login e confirma se a senha está correta para autenticação
        '''
