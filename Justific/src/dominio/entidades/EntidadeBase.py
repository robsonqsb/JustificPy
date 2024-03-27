from datetime import datetime

class EntidadeBase():
    '''
    Entidade padrão do sistema
    '''
    def __init__(self, _id: str = None, data_criacao: datetime = None):
        self._id = _id if _id is not None else None
        self.data_criacao = data_criacao if data_criacao is not None else datetime.now()
        if _id is None:
            self.excluido = False
        