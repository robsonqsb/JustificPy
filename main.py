from fastapi import FastAPI
from Justific.src.dominio.dtos.UsuarioInclusaoDto import UsuarioDto
from Justific.src.endpoints import usuario_endpoints

app = FastAPI()

app.include_router(usuario_endpoints.router)

if __name__ == "__main__":
    usuario_inclusao = UsuarioDto(login="usuario6",senha="44444")
    # print(usuario_atualizar("6606bb9e8f58a5ee1173fb11", usuario_inclusao))
