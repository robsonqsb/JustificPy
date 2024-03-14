from fastapi import FastAPI, Query
from Justific.src.data.repositorios.RepositorioUsuario import RepositorioUsuario

app = FastAPI()

@app.get('/api/usuario/efetuar_login')
def efetuar_login(login: str = Query(None), senha: str = Query(None)):
    '''
    Endpoint para autenticação no sistema
    '''
    repositorio_usuario = RepositorioUsuario()
    return repositorio_usuario.confirmar_autenticacao(login, senha)

if __name__ == "__main__":
    print(efetuar_login('admin', '12345'))
