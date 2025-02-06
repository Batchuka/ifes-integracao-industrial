from pathlib import Path

import uvicorn
from fastapi import FastAPI

from web_service.router import router

def app() -> FastAPI:
    """Cria e retorna a instância do FastAPI."""
    application = FastAPI(docs_url='/docs', debug=True) # TODO: não faz sentido passar debug em produção. Esse argumento só é necessário em Desenvolvimento.
    application.include_router(router)
    return application


def main():
    try:
        reload_dir = str(Path(__file__).resolve().parent)
        uvicorn_args = {
            "app": "__main__:app",
            "host": config('host'),
            "port": int(config('port')),
            "factory": True
        }

        if env() == "dev":
            uvicorn_args.update({
                "reload": True,
                "reload_dirs": [reload_dir]
            })

        uvicorn.run(**uvicorn_args)

    except SystemExit as e:
        if e.code != 0:  # Ignorar saídas de reload bem-sucedidos
            print(f"Servidor Uvicorn terminou com SystemExit({e.code})")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        

if __name__ == "__main__":
    app()