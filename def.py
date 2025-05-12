produto = [20, 15, 10, 30, 5]


def atualizar():
    produtoIndice = int(input('digite o indice do produto(0,1,2,3 ou 4)'))
    produtoQuantidade = int(input('digite a quantidade vendida do produto'))
    produto[produtoIndice] = produto[produtoIndice] - produtoQuantidade


atualizar()
print(produto)


def adicionar():
    produtoIndice = int(input('Digite o índice do produto (0,1,2,3 ou 4): '))
    produtoQuantidade = int(
        input('Digite a quantidade a adicionar ao estoque: '))
    produto[produtoIndice] = produto[produtoIndice] + produtoQuantidade
    print("Quantidade atualizada em estoque após adição:", produto)


adicionar()
print(produto)


def exibir():
    print("Quantidade atual de cada produto:", produto)
