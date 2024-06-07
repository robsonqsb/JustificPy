from typing import Type
from Justific.src.controllers.ControllerBase import ControllerBase
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase
from Justific.src.dominio.entidades.Membro import Membro
from Justific.src.dominio.interfaces.controllers.IControllerMembro import IControllerMembro
from Justific.src.dominio.interfaces.repositorios.IRepositorioMembro import IRepositorioMembro

class ControllerMembro(ControllerBase, IControllerMembro):
    '''
    Classe de controller para operações de membro
    '''
    def __init__(self, repositorio: IRepositorioMembro):
        super().__init__(repositorio)

    def obter_por_id(self, id: str) -> Membro:
        return super().obter_por_id(id)
    
    def mapear_entidade(self, registro: dict, visualizacao: bool = False) -> Membro:
        id = str(registro['_id']) if '_id' in registro else None
        data_criacao = registro['data_criacao'] if 'data_criacao' in registro and visualizacao else None
        organizacao = Membro(id, data_criacao, registro['codigo_registro'], registro['nome'], registro['organizacao_id'])
        return organizacao
