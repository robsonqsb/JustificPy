from abc import ABC, abstractmethod
from typing import List, Type
from Justific.src.dominio.interfaces.repositorios.IRepositorioBase import IRepositorioBase
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase

class IControllerBase(ABC):
    '''
    Interface de controller padrão
    '''
    @abstractmethod
    def __init__(self, repositorio: Type[IRepositorioBase]):
        pass

    @abstractmethod
    def mapear_entidade(self, registro: dict, visualizacao: bool = False) -> Type[EntidadeBase]:
        '''
        Método para mapear o registro do banco em entidade
        '''

    @abstractmethod
    def obter_por_id(self, id: str) -> Type[EntidadeBase]:
        '''
        Método para obter a entidade por id
        '''

    @abstractmethod
    def obter(self, filtro: dict = None) -> List[Type[EntidadeBase]]:
        '''
        Método para obter registros de acordo com a entidade
        '''

    @abstractmethod
    def incluir(self, dados_inclusao: dict = None) -> str:
        '''
        Método para incluir registro de acordo com a enttidade
        '''

    @abstractmethod
    def atualizar(self, dados_alteracao: dict = None) -> bool:
        '''
        Método para atualizar um registro na base de acordo com o id informado e entidade
        '''
    @abstractmethod
    def excluir(self, id: str = None) -> bool:
        '''
        Método para excluir logicamente um registro no banco pelo id
        '''
