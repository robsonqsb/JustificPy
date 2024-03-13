from abc import ABC, abstractmethod
from typing import Type
from bson import ObjectId
from Justific.src.interfaces.repositorios.IRepositorioBase import IRepositorioBase
from Justific.src.modelos.EntidadeBase import EntidadeBase

class IControllerBase(ABC):
    '''
    Interface de controller base da aplicação
    '''
    def __init__(self, repositorio: Type[IRepositorioBase]):
        self._repositorio = repositorio

    @abstractmethod
    def obter_por_id(self, _id: ObjectId) -> Type[EntidadeBase]:
        '''
        Método para obter a entidade por id
        '''
