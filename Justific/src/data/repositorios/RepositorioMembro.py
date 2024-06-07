from Justific.src.data.repositorios.RepositorioBase import RepositorioBase
from Justific.src.dominio.interfaces.repositorios.IRepositorioMembro import IRepositorioMembro

class RepositorioMembro(RepositorioBase, IRepositorioMembro):
    '''
    Repositório para operações de dados para membros
    '''
    def __init__(self):
        super().__init__('membro')
