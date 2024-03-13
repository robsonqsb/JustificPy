from Justific.src.data.repositorios.RepositorioBase import RepositorioBase
from Justific.src.interfaces.repositorios.IRepositorioUsuario import IRepositorioUsuario

class RepositorioUsuario(RepositorioBase, IRepositorioUsuario):
    '''
    Repositório para operações com usuário
    '''
    def confirmar_login(self, login: str, senha: str) -> bool:
        return self.collection.find_one({ "login": login })['senha'] == senha
    