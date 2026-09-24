from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
URL_BANCO = os.getenv("DATABASE_URL")

Banco_De_Dados = create_engine(URL_BANCO)

sessao = sessionmaker(bind=Banco_De_Dados)
sessao_executavel = sessao()

Base = declarative_base()


class Produto(Base):
    __tablename__ = "produtos" #funçao do sqlalchemy para encontrar a tabela "produtos" no mysql

    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(20), nullable=False, unique=True)
    preco = Column("preco", Numeric(10, 2))
    quantidade = Column("quantidade", Integer)


Base.metadata.create_all(bind=Banco_De_Dados)
