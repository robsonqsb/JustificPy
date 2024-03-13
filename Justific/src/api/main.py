from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

@app.get('/api/usuario/efetuar_login/')
def efetuar_login(login: str = Query(None), senha: str = Query(None)):
    '''
    Endpoint para autenticação no sistema
    '''
    if possui_informacoes_autenticacao_vazias(login, senha):
        return HTTPException(status_code = 401, detail = 'Login ou senha inválidos')
    return True

@property
def possui_informacoes_autenticacao_vazias(login: str = None, senha: str = None):
    '''
    Verifica se os parâmetros de login e senha possui valores definidos
    '''
    return login is None or login == '' or senha is None or senha == ''
