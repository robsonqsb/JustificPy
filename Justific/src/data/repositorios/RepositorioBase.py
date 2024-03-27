from ast import List
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
        filtro["excluido"] = False
        return self._colecao.find(filtro)

    def incluir(self, entidade: type[EntidadeBase]) -> str:
        entidade_inclusao = entidade.__dict__
        del entidade_inclusao['_id']
        retorno = self._colecao.insert_one(entidade_inclusao)
        return str(retorno.inserted_id)

    def atualizar(self, entidade: EntidadeBase) -> bool:
        return self._colecao.update_one({ "_id": ObjectId(entidade.id)}, entidade.__dict__)
    