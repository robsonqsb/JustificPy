from typing import Type
from Justific.src.controllers.ControllerMembro import ControllerMembro
from Justific.src.controllers.ControllerOrganizacao import ControllerOrganizacao
from Justific.src.controllers.ControllerUsuario import ControllerUsuario
from Justific.src.data.repositorios.RepositorioMembro import RepositorioMembro
from Justific.src.data.repositorios.RepositorioOrganizacao import RepositorioOrganizacao
from Justific.src.data.repositorios.RepositorioUsuario import RepositorioUsuario
from Justific.src.dominio.interfaces.controllers.IControllerMembro import IControllerMembro
from Justific.src.dominio.interfaces.controllers.IControllerOrganizacao import IControllerOrganizacao
from Justific.src.dominio.interfaces.controllers.IControllerUsuario import IControllerUsuario
from Justific.src.dominio.interfaces.repositorios.IRepositorioMembro import IRepositorioMembro
from Justific.src.dominio.interfaces.repositorios.IRepositorioOrganizacao import IRepositorioOrganizacao
from Justific.src.dominio.interfaces.repositorios.IRepositorioUsuario import IRepositorioUsuario

class RegistradorIoc():
    '''
    Registrador das interfaces e as respectivas classes concretas
    '''
    def __init__(self):
        self._repositorio_usuario = Type[IRepositorioUsuario]
        self._repositorio_organizacao = Type[IRepositorioOrganizacao]
        self._repositorio_membro = Type[IRepositorioMembro]

    def registrar_controller_usuario(self) -> Type[IControllerUsuario]:
        '''
        Registra a classe concreta de controller de usuário
        '''
        self._repositorio_usuario = RepositorioUsuario()
        return ControllerUsuario(self._repositorio_usuario)

    def registar_controller_organizacao(self) -> Type[IControllerOrganizacao]:
        '''
        Registra a classe concreta de controller de usuário
        '''
        self._repositorio_organizacao = RepositorioOrganizacao()
        return ControllerOrganizacao(self._repositorio_organizacao)

    def registrar_controller_membro(self) -> Type[IControllerMembro]:
        '''
        Registra a classe concreta de controller de membro
        '''
        self._repositorio_membro = RepositorioMembro()
        return ControllerMembro(self._repositorio_membro)
    