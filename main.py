from fastapi import Body, FastAPI, Query
from Justific.src.dominio.dtos.FiltroUsuarioDto import FiltroUsuarioDto
from Justific.src.dominio.dtos.UsuarioInclusaoDto import UsuarioInclusaoDto
from Justific.src.infra.RegistradorIoc import RegistradorIoc

app = FastAPI()
registrador_ioc = RegistradorIoc()
registrador_ioc.registrar()

@app.get('/api/usuario/efetuar_login', description = 'Login através de usuário e senha')
def usuario_efetuar_login(login: str = Query(None), senha: str = Query(None)):
    '''
    Endpoint para autenticação no sistema
    '''
    return registrador_ioc.controller_usuario.confirmar_dados_login(login, senha)

@app.get('/api/usuario/obter_por_id')
def usuario_obter_por_id(id: str = Query(None)):
    '''
    Obter entidade por id correspondente
    '''
    return registrador_ioc.controller_usuario.obter_por_id(id)

@app.post('/api/usuario/listar')
def usuario_listar(filtro: FiltroUsuarioDto = Body(None)):
    '''
    Obter os registros de usuários com a possibilidade de filtro
    '''
    return registrador_ioc.controller_usuario.obter(filtro.__dict__ if filtro is not None else None)

@app.post("/api/usuario/incluir")
def usuario_incluir(usuario: UsuarioInclusaoDto = Body(...)):
    '''
    Incluir um novo usuário
    '''
    return registrador_ioc.controller_usuario.incluir(usuario.__dict__)

if __name__ == "__main__":
    usuario_inclusao = UsuarioInclusaoDto(login="usuario5",senha="33333")
    print(usuario_incluir(usuario_inclusao))
