from fastapi import FastAPI

from web_service.router import router

def app() -> FastAPI:
    """Cria e retorna a instância do FastAPI."""
    application = FastAPI(docs_url='/docs', debug=True)
    application.include_router(router)
    return application
       
if __name__ == "__main__":
    app()