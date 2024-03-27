from abc import ABC, abstractmethod
from typing import List, Type

from Justific.src.dominio.entidades import EntidadeBase

class IRepositorioBase(ABC):
    '''
    Interface de repositório padrão
    '''
    @abstractmethod
    def __init__(self, nome_colecao: str):
        pass

    @abstractmethod
    def obter_por_id(self, _id: str) -> dict:
        '''
        Método para obter um registro da entidade por id
        '''

    @abstractmethod
    def obter(self, filtro: dict = None) -> List:
        '''
        Método para obter registros da coleção por
        '''

    @abstractmethod
    def incluir(self, entidade: Type[EntidadeBase]) -> str:
        '''
        Método para inclusão de um registro na base
        '''

    @abstractmethod
    def atualizar(self, entidade: Type[EntidadeBase]) -> bool:
        '''
        Método para atualizar um registro de acordo com os dados da entidade
        '''
        