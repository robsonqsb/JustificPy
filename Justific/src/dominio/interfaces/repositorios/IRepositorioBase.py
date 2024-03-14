from abc import ABC, abstractmethod
from typing import Type
from bson import ObjectId
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase

class IRepositorioBase(ABC):
    '''
    Interface de repositório padrão
    '''
    @abstractmethod
    def __init__(self, nome_colecao: str):
        pass

    @abstractmethod
    def obter_por_id(self, _id: ObjectId) -> Type[EntidadeBase]:
        '''
        Método para obter um registro da entidade por id
        '''
