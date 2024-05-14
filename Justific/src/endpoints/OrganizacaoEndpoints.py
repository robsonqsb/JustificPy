from fastapi import APIRouter, Body
from Justific.src.dominio.dtos.FiltroOrganizacaoDto import FiltroOrganizacaoDto
from Justific.src.dominio.dtos.OrganizacaoDto import OrganizacaoDto
from Justific.src.infra.RegistradorIoc import RegistradorIoc

router = APIRouter(tags = ['organizacao'])
controller_organizacao = RegistradorIoc().registar_controller_organizacao()

@router.get('/api/organizacao/obter_por_id/{id}', description = 'Obter organização através do identificador')
def obter_por_id(id: str):
    '''
    Obter entidade por id correspondente
    '''
    return controller_organizacao.obter_por_id(id)

@router.post('/api/organizacao/listar', description = 'Listar organizações com a possibilidade de definição de filtro')
def listar(filtro: FiltroOrganizacaoDto = Body(None)):
    '''
    Obter os registros de organizações com a possibilidade de filtro
    '''
    return controller_organizacao.obter(filtro.__dict__ if filtro is not None else None)

@router.post("/api/organizacao/incluir", description = 'Inclusão de organização')
def incluir(organizacao: OrganizacaoDto = Body(...)):
    '''
    Incluir um novo usuário
    '''
    return controller_organizacao.incluir(organizacao.__dict__)

@router.put("/api/organizacao/atualizar/{id}", description = 'Atualização de organização')
def atualizar(id: str, organizacao: OrganizacaoDto = Body(...)):
    '''
    Atualizar dados da organização
    '''
    organizacao_dic = organizacao.__dict__
    organizacao_dic["_id"] = id
    return controller_organizacao.atualizar(organizacao_dic)

@router.delete("/api/organizacao/excluir/{id}")
def excluir(id: str):
    '''
    Excluir uma organização
    '''
    return controller_organizacao.excluir(id)
