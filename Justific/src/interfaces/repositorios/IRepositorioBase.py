from abc import ABC, abstractmethod
from typing import Type

from bson import ObjectId
from Justific.src.modelos.EntidadeBase import EntidadeBase

class IRepositorioBase(ABC):
    '''
    Repositório padrão
    '''
    @abstractmethod
    def obter_por_id(self, _id: ObjectId) -> Type[EntidadeBase]:
        '''
        Obter o registro por id 
        '''
