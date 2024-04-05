from Justific.src.data.repositorios.RepositorioBase import RepositorioBase
from Justific.src.dominio.interfaces.repositorios.IRepositorioOrganizacao import IRepositorioOrganizacao

class RepositorioOrganizacao(RepositorioBase, IRepositorioOrganizacao):
    '''
    Classe de repositório para manipulação dos dados de organização
    '''
    