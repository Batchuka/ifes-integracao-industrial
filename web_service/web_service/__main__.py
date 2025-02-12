from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from slowapi import Limiter
# from slowapi.util import get_remote_address
# from slowapi.middleware import SlowAPIMiddleware
from web_service.router import router

# limiter = Limiter(key_func=get_remote_address)

def app() -> FastAPI:
    application = FastAPI(docs_url='/docs', debug=True)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.state.limiter = limiter
    # application.add_middleware(SlowAPIMiddleware)
    application.include_router(router)
    return application

if __name__ == "__main__":
    app()