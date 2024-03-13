from bson import ObjectId
from Justific.src.interfaces.repositorios.IRepositorioBase import IRepositorioBase
from Justific.src.modelos.EntidadeBase import EntidadeBase
from Justific.src.data.config import database_infos
from pymongo import MongoClient

class RepositorioBase(IRepositorioBase):
    '''
    Repositório padrão do sistema
    '''
    def __init__(self, collection_name: str):
        client = MongoClient(database_infos['url_connection'])
        self.database = client[database_infos['database_name']]
        self.collection = self.database.get_collection(collection_name)

    def obter_por_id(self, _id: ObjectId) -> EntidadeBase:
        return self.collection.find({ "_id": _id })
    