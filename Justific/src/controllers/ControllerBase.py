from typing import List, Type
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase
from Justific.src.dominio.interfaces.controllers.IControllerBase import IControllerBase
from Justific.src.dominio.interfaces.repositorios.IRepositorioBase import IRepositorioBase

class ControllerBase(IControllerBase):
    '''
    Controller padrão de manipulação de entidades
    '''
    def __init__(self, repositorio: Type[IRepositorioBase]):
        self._repositorio = repositorio

    def obter_por_id(self, id: str) -> Type[EntidadeBase]:
        registro = self._repositorio.obter_por_id(id)
        return self.mapear_entidade(registro)

    def obter(self, filtro: dict = None) -> List[Type[EntidadeBase]]:
        registros = self._repositorio.obter(filtro)
        entidades = []
        for registro in registros:
            entidades.append(self.mapear_entidade(registro))
        return entidades

    def incluir(self, dados_inclusao: dict = None) -> str:
        entidade = self.mapear_entidade(dados_inclusao)
        return self._repositorio.incluir(entidade)

    def atualizar(self, entidade: EntidadeBase) -> bool:
        return self._repositorio.atualizar(entidade)
    