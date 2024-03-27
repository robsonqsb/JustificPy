from Justific.src.data.repositorios.RepositorioBase import RepositorioBase
from Justific.src.dominio.interfaces.repositorios.IRepositorioUsuario import IRepositorioUsuario

class RepositorioUsuario(RepositorioBase, IRepositorioUsuario):
    '''
    Repositório de manipulação dos dados de usuário
    '''
    def __init__(self):
        super().__init__('usuario')

    def confirmar_dados_autenticacao(self, login: str, senha: str) -> bool:
        '''
        Confirma os dados de autenticação estão corretos com o registro na base
        '''
        registro_usuario = self._colecao.find_one({ "login": login })
        return  registro_usuario is not None and registro_usuario['senha'] == senha
    