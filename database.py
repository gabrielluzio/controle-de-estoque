from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError


Banco_De_Dados = create_engine(
   "mysql+pymysql://root:Gabrielluzio1%40@localhost/estoque"
)

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
