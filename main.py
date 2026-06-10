from estoque import CRUD
def main():
    produtos = CRUD()
    produtos.conectar()
    while True:
        print('MENU\n'
              '1 - ADICIONAR PRODUTO\n'
              '2 - EXIBIR\n'
              '3 - BUSCAR_PRODUTO\n'
              '4 - ATUALIZAR_PREÇO\n'
              '5 - REMOVER PRODUTO\n'
              '6 - SAIR'
              '')

        usuario = int(input('ESCOLHA UMA OPÇÃO: '))

        if usuario == 1:
            try:
                nome = str(input('NOME DO PRODUTO: '))
                preco = float(input('PRECO DO PRODUTO: '))
                if preco <= 0:
                    print('VALOR INVALIDO. ')
                    continue
                quantidade= int(input('QUANTIDADE DO PRODUTO: '))
                if quantidade <= 0:
                    print('VALOR NEGATIVO INVALIDO')
                    continue
                produtos.criar_produto(nome,preco,quantidade)
            except ValueError:
                print('VALOR INVALIDO. ')



        elif usuario == 2:
            produtos.exibir_produtos()

        elif usuario == 3:
            nome = input('NOME PRODUTO: ')
            produtos.buscar_produtos(nome)

        elif usuario == 4:
            try:
                nome = input('NOME PRODUTO: ')
                preco = float(input('PREÇO PRODUTO: '))
                if preco <= 0:
                    print('VALOR NEGATIVO INVALIDO')
                    continue
                produtos.atualizar_preco(nome, preco)
            except ValueError:
                print('VALOR INVALIDO')

        elif usuario == 5:
            nome = input('NOME PRODUTO: ')
            produtos.remover_produto(nome)





if __name__ == "__main__":
    main()