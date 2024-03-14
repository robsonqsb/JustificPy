from datetime import datetime
from bson import ObjectId

class EntidadeBase():
    '''
    Entidade padrão do sistema
    '''
    def __init__(self):
        self._id = ObjectId()
        self.data_criacao = datetime.now()
        self.excluido = False
