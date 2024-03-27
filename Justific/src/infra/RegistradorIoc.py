from typing import Type
from Justific.src.controllers.ControllerUsuario import ControllerUsuario
from Justific.src.data.repositorios.RepositorioUsuario import RepositorioUsuario
from Justific.src.dominio.interfaces.controllers.IControllerUsuario import IControllerUsuario
from Justific.src.dominio.interfaces.repositorios.IRepositorioUsuario import IRepositorioUsuario

class RegistradorIoc():
    '''
    Registrador das interfaces e as respectivas classes concretas
    '''
    def __init__(self):
        self._repositorio_usuario = Type[IRepositorioUsuario]
        self.controller_usuario = Type[IControllerUsuario]

    def registrar(self):
        '''
        Registra de fato as interfaces com as respectivas classes concretas
        '''
        self._repositorio_usuario = RepositorioUsuario()
        self.controller_usuario = ControllerUsuario(self._repositorio_usuario)
