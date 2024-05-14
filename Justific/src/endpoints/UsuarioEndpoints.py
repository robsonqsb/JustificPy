from fastapi import APIRouter, Body
from Justific.src.dominio.dtos.FiltroUsuarioDto import FiltroUsuarioDto
from Justific.src.dominio.dtos.UsuarioDto import UsuarioDto
from Justific.src.infra.RegistradorIoc import RegistradorIoc

router = APIRouter(tags = ['usuario'])
controller_usuario = RegistradorIoc().registrar_controller_usuario()

@router.post('/api/usuario/efetuar_login', description = 'Login através de usuário e senha')
def efetuar_login(usuario: UsuarioDto = Body(...)):
    '''
    Endpoint para autenticação no sistema
    '''
    return controller_usuario.confirmar_dados_login(usuario.login, usuario.senha)

@router.get('/api/usuario/obter_por_id/{id}', description = 'Obter usuário através do identificador')
def obter_por_id(id: str):
    '''
    Obter entidade por id correspondente
    '''
    return controller_usuario.obter_por_id(id)

@router.post('/api/usuario/listar', description = 'Listar usuários com a possibilidade de definição de filtro')
def listar(filtro: FiltroUsuarioDto = Body(None)):
    '''
    Obter os registros de usuários com a possibilidade de filtro
    '''
    return controller_usuario.obter(filtro.__dict__ if filtro is not None else None)

@router.post("/api/usuario/incluir", description = 'Inclusão de usuário')
def incluir(usuario: UsuarioDto = Body(...)):
    '''
    Incluir um novo usuário
    '''
    return controller_usuario.incluir(usuario.__dict__)

@router.put("/api/usuario/atualizar/{id}", description = 'Atualização de usuário')
def atualizar(id: str, usuario: UsuarioDto = Body(...)):
    '''
    Atualizar dados do usuário
    '''
    usuario_dic = usuario.__dict__
    usuario_dic["_id"] = id
    return controller_usuario.atualizar(usuario_dic)

@router.delete("/api/usuario/excluir/{id}")
def excluir(id: str):
    '''
    Excluir um usuário
    '''
    return controller_usuario.excluir(id)
