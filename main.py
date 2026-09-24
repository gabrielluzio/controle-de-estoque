from fastapi import FastAPI
from estoque_routes import Router


app = FastAPI(
    title="API de Controle de Estoque",
    description="API REST para gerenciamento de produtos e estoque.",
    version="1.0.0"
)

app.include_router(Router)


