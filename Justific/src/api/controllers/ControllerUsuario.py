from bson import ObjectId
from Justific.src.interfaces.controllers.IControllerUsuario import IControllerUsuario
from Justific.src.modelos.EntidadeBase import EntidadeBase

class ControllerUsuario(IControllerUsuario):
    '''
    Controller para controle de operações com usuário
    '''
    def obter_por_id(self, _id: ObjectId) -> type[EntidadeBase]:
        return super().obter_por_id(_id)

    def confirmar_autenticacao(self, login: str, senha: str) -> bool:
        return self._repositorio.confirmar_login(login, senha)
    