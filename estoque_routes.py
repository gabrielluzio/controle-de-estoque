from fastapi import APIRouter, HTTPException
from database import sessao_executavel, Produto
from sqlalchemy.exc import SQLAlchemyError, IntegrityError




Router = APIRouter(prefix = "/produtos", tags = ["/produtos"])

#CREATE
@Router.post("/criar_produto")
async def criar_produto(novo_nome:str, novo_preco:float, nova_quantidade:int):
    sessao = sessao_executavel
    produto_criado = Produto(
        nome = novo_nome,
        preco = novo_preco,
        quantidade = nova_quantidade
    )
    try:
        sessao.add(produto_criado)
        sessao.commit()
        return{"mensagem": "PRODUTO CADASTRADO. "}

    except IntegrityError:
        sessao.rollback()

        raise HTTPException(
            status_code=409,
            detail="NÃO FOI POSSIVEL CADASTRAR PRODUTO. "
        )

    except SQLAlchemyError:
        sessao.rollback()
        print("ERRO NO BANCO DE DADOS. ")
        return produto_criado


#READ
@Router.get("/listar_produtos")
async def listar_produtos():
     sessao = sessao_executavel
     produto_listado = sessao.query.all()
     return produto_listado


#READ_ID
@Router.get("/ListarProduto_ID")
async def ListarProduto_ID(id: int):
    sessao = sessao_executavel
    produto_listado_id = sessao.query(Produto).filter(Produto.id == id).one_or_none()

    if not produto_listado_id:
        raise HTTPException(
            status_code=404,
            detail=" PRODUTO NÃO ENCONTRADO. "
        )
    return produto_listado_id


#UPDATE
@Router.put("/atualizar_produto")
async def atualizar_produto(id: int, preco_novo:float, quantidade_nova:int):
    sessao = sessao_executavel
    produto_atualizado = sessao.query(Produto).filter(Produto.id == id).first()

    if not produto_atualizado:
        raise HTTPException(
            status_code = 404,
            detail = " PRODUTO NÃO ENCONTRADO. "
        )
    produto_atualizado.preco = preco_novo
    produto_atualizado.quantidade = quantidade_nova

    try:
        sessao.commit()

    except  SQLAlchemyError:
        sessao.rollback()
        raise HTTPException(
            status_code=500,
            detail="ERRO NO BANCO DE DADOS. "
        )
    return {"mensagem": "PRODUTO ATUALIZADO. "}


#DELETE
@Router.delete("/deletar_produto")
async def deletar_produto(id: int):
    sessao = sessao_executavel
    produto_deletado = sessao.query(Produto).filter(Produto.id == id).first()

    if not produto_deletado:
        raise HTTPException(
            status_code = 404,
            detail = "PRODUTO NÃO ENCONTRADO. "
        )
    try:
        sessao.delete(produto_deletado)
        sessao.commit()
    except SQLAlchemyError:
        sessao.rollback()

        raise HTTPException(
            status_code=500,
            detail="ERRO NO BANCO DE DADOS. "
        )
    return{"mensagem": "PRODUTO DELETADO. "}