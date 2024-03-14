from pymongo import MongoClient
from Justific.src.dominio.interfaces.repositorios.IRepositorioBase import IRepositorioBase
from Justific.src.data.config.database_mongodb import database_infos

class RepositorioBase(IRepositorioBase):
    '''
    Repositório padrão do sistema
    '''
    def __init__(self, nome_colecao: str):        
        client = MongoClient(database_infos['url_connection'])
        database = client[database_infos['database_name']]
        self.colecao = database.get_collection(nome_colecao)
        