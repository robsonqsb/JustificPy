from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

@app.get('/api/usuario/efetuar_login/')    
def efetuar_login(login: str = Query(None), senha: str = Query(None)):
    '''
    Endpoint para autenticação no sistema
    '''
    if informacoes_autenticacao_vazias(login, senha):
        return HTTPException(status_code = 401, detail = 'Login ou senha inválidos')    
    return login == 'admin' and senha == '1234'

def informacoes_autenticacao_vazias(login, senha):
    return login is None or login == '' or senha is None or senha == ''