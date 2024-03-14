from bson import ObjectId
from Justific.src.dominio.entidades.Usuario import Usuario
from Justific.src.data.repositorios.RepositorioBase import RepositorioBase

class RepositorioUsuario(RepositorioBase):
    '''
    Repositório de manipulação dos dados de usuário
    '''
    def __init__(self):
        super().__init__('usuario')

    def obter_por_id(self, _id: ObjectId) -> type[Usuario]:
        return super().obter_por_id(_id)

    def confirmar_autenticacao(self, login: str, senha: str) -> bool:
        '''
        Confirma os dados de autenticação estão corretos com o registro na base
        '''
        registro_usuario = self.colecao.find_one({ "login": login })
        return  registro_usuario is not None and registro_usuario['senha'] == senha
    