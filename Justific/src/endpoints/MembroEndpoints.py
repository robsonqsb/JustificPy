from fastapi import APIRouter, Body
from Justific.src.dominio.dtos.FiltroMembroDto import FiltroMembroDto
from Justific.src.dominio.dtos.MembroDto import MembroDto
from Justific.src.infra.RegistradorIoc import RegistradorIoc

router = APIRouter(tags = ['membro'])
controller_membro = RegistradorIoc().registrar_controller_membro()

@router.get('/api/membro/obter_por_id/{id}', description = 'Obter membro através do identificador')
def obter_por_id(id: str):
    '''
    Obter entidade por id correspondente
    '''
    return controller_membro.obter_por_id(id)

@router.post('/api/membro/listar', description = 'Listar membros com a possibilidade de definição de filtro')
def listar(filtro: FiltroMembroDto = Body(None)):
    '''
    Obter os registros de membros com a possibilidade de filtro
    '''
    return controller_membro.obter(filtro.__dict__ if filtro is not None else None)

@router.post("/api/membro/incluir", description = 'Inclusão de membro')
def incluir(membro: MembroDto = Body(...)):
    '''
    Incluir um novo membro
    '''
    return controller_membro.incluir(membro.__dict__)

@router.put("/api/membro/atualizar/{id}", description = 'Atualização de membro')
def atualizar(id: str, membro: MembroDto = Body(...)):
    '''
    Atualizar dados do membro
    '''
    membro_dic = membro.__dict__
    membro_dic["_id"] = id
    return controller_membro.atualizar(membro_dic)

@router.delete("/api/membro/excluir/{id}")
def excluir(id: str):
    '''
    Excluir um membro
    '''
    return controller_membro.excluir(id)
