from ast import List
from datetime import datetime
from typing import Type
from bson import ObjectId
from pymongo import MongoClient
from Justific.src.dominio.entidades.EntidadeBase import EntidadeBase
from Justific.src.dominio.interfaces.repositorios.IRepositorioBase import IRepositorioBase
from Justific.src.data.config.database_mongodb import database_infos

class RepositorioBase(IRepositorioBase):
    '''
    Repositório padrão do sistema
    '''
    def __init__(self, nome_colecao: str):
        client = MongoClient(database_infos['url_connection'])
        database = client[database_infos['database_name']]
        self._colecao = database.get_collection(nome_colecao)

    def obter_por_id(self, _id: str) -> dict:
        return self._colecao.find_one({ "_id": ObjectId(_id), "excluido": False })

    def obter(self, filtro: dict = None) -> List:
        filtro = filtro if filtro is not None else {}
        filtro["excluido"] = False
        return self._colecao.find(filtro)

    def incluir(self, entidade: type[EntidadeBase]) -> str:
        retorno = self._colecao.insert_one(self.converter_entidade_para_dicionario(entidade))
        return str(retorno.inserted_id)

    def atualizar(self, entidade: EntidadeBase) -> bool:
        id_atualizacao = entidade._id
        dados_alteracao = self.converter_entidade_para_dicionario(entidade)
        dados_alteracao['alterado_em'] = datetime.now()
        resultado = self._colecao.update_one({ "_id": ObjectId(id_atualizacao)}, { "$set": dados_alteracao })
        return resultado.modified_count > 0

    def excluir(self, id: str = None) -> bool:
        if id is None:
            return False
        resultado = self._colecao.update_one({ "_id": ObjectId(id) }, { "$set": { "excluido" : True, "alterado_em" : datetime.now() } })
        return resultado.modified_count > 0

    def converter_entidade_para_dicionario(self, entidade: Type[EntidadeBase]) -> dict:
        '''
        Método para converter uma entidade em dicionário
        '''
        entidade_retorno = entidade.__dict__
        del entidade_retorno['_id']
        return entidade_retorno
