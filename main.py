from fastapi import FastAPI
from Justific.src.endpoints import MembroEndpoints, OrganizacaoEndpoints, UsuarioEndpoints

app = FastAPI()

app.include_router(UsuarioEndpoints.router)
app.include_router(OrganizacaoEndpoints.router)
app.include_router(MembroEndpoints.router)

if __name__ == "__main__":
    print(OrganizacaoEndpoints.usuario_obter_por_id('65e79aadbec1cca43957a031'))
