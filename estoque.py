import mysql.connector

class ConectarBanco:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    # funçao para conexao do banco de dados.
    # com tratamento de erro para possiveis erros na conexao com o banco.
    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='SENHA',
                database='estoque'
            )
            self.cursor = self.conexao.cursor()
            print('BANCO CONECTADO')

        except mysql.connector.Error as erro:
            print('ERRO AO CONECTAR BANCO DE DADOS  ')
            print(erro)
            exit()

    # funçao para fechamento de conexao e fechamneto do cursor
    def fecharconexao(self):
        if self.cursor:
            self.cursor.close()

        if self.conexao:
            self.conexao.close()

class CRUD(ConectarBanco):

    # funçao para criar um produto com tratamento de erro para produtos duplicados
    def criar_produto(self,nome,preco,quantidade):
        try:
            comando = f'insert into dados (nome, preco, quantidade) values (%s, %s, %s)'
            self.cursor.execute(comando, (nome, preco, quantidade))
            self.conexao.commit()

        except mysql.connector.IntegrityError:
            print('Erro: PRODUTO JA CADASTRADO!')

    # funçao para exibir os produtos do bancos de dados
    def exibir_produtos(self):
        comando = f'select * from dados'
        self.cursor.execute(comando)

        produtos = self.cursor.fetchall()

        for produto in produtos:
            print(produto)

    # funçao para buscar um produto especifico dentro do banco de dados
    def buscar_produtos(self,nome):
        comando = f'select * from dados where nome = %s'
        self.cursor.execute(comando, (nome,))
        produto = self.cursor.fetchone()
        if produto:
            print(produto)
        else:
            print('PRODUTO NÃO ENCONTRADO!')

    # funçao para atualizar preço de um produto
    def atualizar_preco(self,nome,preco):
        comando = f'update dados set preco = %s where nome = %s'
        self.cursor.execute(comando, (preco,nome))
        self.conexao.commit()
        produtos = self.cursor.rowcount
        if produtos == 0:
            print('PRODUTO NÃO ENCONTRADO!')
        else:
            print('PREÇO ATUALIZADO')

    # funçao para deletar um produto
    def remover_produto(self, nome):
        comando = f'delete from dados where nome = %s'
        self.cursor.execute(comando, (nome,))
        self.conexao.commit()
        produtos = self.cursor.rowcount
        if produtos == 0:
            print('PRODUTO NÃO ENCONTRADO!')
        else:
            print('PRODUTO REMOVIDO COM SUCESSO')



