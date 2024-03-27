from Justific.src.controllers.ControllerBase import ControllerBase
from Justific.src.dominio.entidades.Usuario import Usuario
from Justific.src.dominio.interfaces.controllers.IControllerUsuario import IControllerUsuario
from Justific.src.dominio.interfaces.repositorios.IRepositorioUsuario import IRepositorioUsuario

class ControllerUsuario(ControllerBase, IControllerUsuario):
    '''
    Controller para manipulação de usuário
    '''
    def __init__(self, repositorio: IRepositorioUsuario):
        super().__init__(repositorio)
        self._repositorio_usuario = repositorio

    def obter_por_id(self, id: str) -> Usuario:
        return super().obter_por_id(id)

    def confirmar_dados_login(self, login: str, senha: str) -> bool:
        return self._repositorio_usuario.confirmar_dados_autenticacao(login, senha)

    def mapear_entidade(self, registro: dict) -> Usuario:
        id = str(registro['_id']) if '_id' in registro else None
        data_criacao = registro['data_criacao'] if 'data_criacao' in registro else None
        senha = registro['senha'] if 'senha' in registro else None
        usuario = Usuario(id, data_criacao, registro['login'], senha)
        return usuario
    