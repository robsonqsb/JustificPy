from Justific.src.controllers.ControllerBase import ControllerBase
from Justific.src.dominio.entidades.Organizacao import Organizacao
from Justific.src.dominio.interfaces.controllers.IControllerOrganizacao import IControllerOrganizacao
from Justific.src.dominio.interfaces.repositorios.IRepositorioOrganizacao import IRepositorioOrganizacao

class ControllerOrganizacao(ControllerBase, IControllerOrganizacao):
    '''
    Controller e manipulação da organização
    '''
    def __init__(self, repositorio: IRepositorioOrganizacao):
        super().__init__(repositorio)

    def obter_por_id(self, id: str) -> Organizacao:
        return super().obter_por_id(id)

    def mapear_entidade(self, registro: dict, visualizacao: bool = False) -> Organizacao:
        id = str(registro['_id']) if '_id' in registro else None
        data_criacao = registro['data_criacao'] if 'data_criacao' in registro and visualizacao else None
        organizacao = Organizacao(id, data_criacao, registro['nome'], registro['cnpj'])
        return organizacao
