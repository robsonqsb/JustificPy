from fastapi import Body, FastAPI
from Justific.src.dominio.dtos.FiltroUsuarioDto import FiltroUsuarioDto
from Justific.src.dominio.dtos.UsuarioInclusaoDto import UsuarioDto
from Justific.src.infra.RegistradorIoc import RegistradorIoc

app = FastAPI()
registrador_ioc = RegistradorIoc()
registrador_ioc.registrar()

@app.post('/api/usuario/efetuar_login', description = 'Login através de usuário e senha')
def usuario_efetuar_login(usuario: UsuarioDto = Body(...)):
    '''
    Endpoint para autenticação no sistema
    '''
    return registrador_ioc.controller_usuario.confirmar_dados_login(usuario.login, usuario.senha)

@app.get('/api/usuario/obter_por_id/{id}', description = 'Obter usuário através do identificador')
def usuario_obter_por_id(id: str):
    '''
    Obter entidade por id correspondente
    '''
    return registrador_ioc.controller_usuario.obter_por_id(id)

@app.post('/api/usuario/listar', description = 'Listar usuários com a possibilidade de definição de filtro')
def usuario_listar(filtro: FiltroUsuarioDto = Body(None)):
    '''
    Obter os registros de usuários com a possibilidade de filtro
    '''
    return registrador_ioc.controller_usuario.obter(filtro.__dict__ if filtro is not None else None)

@app.post("/api/usuario/incluir", description = 'Inclusão de usuário')
def usuario_incluir(usuario: UsuarioDto = Body(...)):
    '''
    Incluir um novo usuário
    '''
    return registrador_ioc.controller_usuario.incluir(usuario.__dict__)

@app.put("/api/usuario/atualizar/{id}", description = 'Atualização de usuário')
def usuario_atualizar(id: str, usuario: UsuarioDto = Body(...)):
    '''
    Atualizar dados do usuário
    '''
    usuario_dic = usuario.__dict__
    usuario_dic["_id"] = id
    return registrador_ioc.controller_usuario.atualizar(usuario_dic)

@app.delete("/api/usuario/excluir/{id}")
def usuario_excluir(id: str):
    '''
    Excluir um usuário
    '''
    return registrador_ioc.controller_usuario.excluir(id)

if __name__ == "__main__":
    usuario_inclusao = UsuarioDto(login="usuario6",senha="44444")
    print(usuario_atualizar("6606bb9e8f58a5ee1173fb11", usuario_inclusao))
