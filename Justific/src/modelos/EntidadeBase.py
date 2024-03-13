from bson import ObjectId

class EntidadeBase():
    '''
    Entidade padrão
    '''
    def __init__(self):
        self._id = ObjectId()
