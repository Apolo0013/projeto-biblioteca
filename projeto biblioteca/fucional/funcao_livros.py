from time import sleep
from .banco_de_dados import *


def titulo(nome):
    print('_' * 50)
    print(f'{nome}'.center(40))
    print('_' * 50)


def linha():
    print('_' * 50)





# Adicionar livro à biblioteca
#auto título, categoria
def addLivro():
    autor = str(input('Autor: ')).strip()
    titulos = str(input('Titulo: ')).strip()
    categoria = str(input('Categoria: ')).strip()
    banco = add_livros(autor = autor  , titulo = titulos , categoria = categoria)
    return  banco # retona o banco de dados ja com as informacoes do livro.


# Mostrar lista de livros disponíveis
def MostrarLivro(bancos = 'livros'):
    """
    Descrição da função: Mostrar atual lista.

    Parametro:
    - bancos_de_dados: a lista que esta as informacoes do livro.

    Returns:
    - sem retorno

    """
    nomes = ['Autor','Titulo','Categoria','ID']
    banco = banco_de_dados(bancos)
    
    if len(banco) != 0:
        titulo('Lista Atual de Livros')
        for v in range(0, len(banco)):
            index = 0
            print(f'ID: {banco[v][3]} do livro') # Mostrar o ID do livro
            sleep(0.1)
            linha()
            for p ,  valor in enumerate(banco[v]):
                sleep(0.2)
                if p > 0:
                    print(f'{nomes[index]} - {valor:>5}') # O modelo de exbição
                    index += 1
            sleep(1)
            linha()
        sleep(4)
    else:
        linha()
        print('\033[1;31mNão existe nenhum Livro registrado\033[m')
        linha()

# Remover livro da biblioteca
def deletelivro():
    """
    Descrição da função: Deleta todas as informações de um livro.

    Parametro:
    - bancos_de_dados: a lista com todas informacoes dos livros

    Returns:
    - retorna: sem retorno

    """
    banco = banco_de_dados()
    if len(banco) != 0:
        titulo('Removendo Livro')
        sleep(1)
        MostrarLivro()
        linha()
        excluir = int(input('digite o ID: ')) # pedir a qual livro sera apagado
        deleta_info(excluir) # uma funcao em outro modulo relacionado a banco de dados
        print(f'\033[1;31mLivro ID: {excluir} foi removido!!!\033[m')
    else:
        linha()
        print('\033[m\033[1;31mNão existe nenhum Livro registrado!!!\033[m')
        linha()
    linha()
    MostrarLivro()
    sleep(4)


# Pesquisar livros poro, aut títulor, categoria, etc.
def PesquisaLivro(): 
    """
    Descrição da função: Pesquisa o livro com as seguintes filtro.
    - Autor
    - Titulo
    - Categoria
    - ID

    Parametro:
    - banco_de_dados: a lista com todas informacoes dos livros

    Returns:
    - retorna: nada

    """
    titulo('Pesquisando Livro')
    print(' - Autor')
    print(' - Titulo')
    print(' - Categoria')
    print(' - ID')
    print('*Escreva o filtro ex: Autor')
    linha()
    while True:
        filtro = str(input('Digite a filtração: ')).upper().strip()[0] # Pedir qual tipo de filtro.
        if filtro in 'ATCI':
            break
        print(f'\033[1;31mNão existe esse filtro!!!\033[m')
    linha()
    #Texto de orientação
    print('Existem alguns cuidados na hora de pesquisa:')
    print('As informações do livros deve se inserido corretamente ex:')
    print('J.R.R. Tolkien, deve se escrito assim, sem nenhuma alteração.')

    nomes = ['autor' , 'titulo' , 'categoria' , 'ID']
    banco = banco_de_dados()
    if filtro in 'A':
        '''
        Aqui esse pequeno sistema pegar so o autor e ver se
        no dicionario tem esse nomes na variavel a baixo,
        chamado pesquisa isso vai se repetir com os mesmo sistema
        de filtração.
        '''
        pesquisa = str(input('Pesquisa: ')).strip()
        titulo(f'Resultado da Pesquisa: {pesquisa}')
        sleep(1)
        for livros in range(0 , len(banco)):
            cont = index = 0
            
            for valor in banco[livros]:
                if cont == 0:
                    for valor in banco[livros]:
                        sleep(0.8)
                        print(f'{nomes[index]} - {valor :>7}')
                        index += 1          
                    linha()
                    sleep(2)
                cont+=1


    elif filtro in 'T':
        pesquisa = str(input('Pesquisa: ')).strip()
        titulo(f'Resultado da Pesquisa: {pesquisa}')
        sleep(1)
        for livros in range(0, len(banco)):
            index= cont = 0
            
            for valor in banco[livros]:
                if cont == 1:
                    for valor in banco[livros]:
                        sleep(0.8)
                        print(f'{nomes[index]} - {valor :>7}')
                        index += 1
                    linha()
                    sleep(2)
                cont += 1


    elif filtro in 'C':
        pesquisa = str(input('Categoria: ')).strip()
        titulo(f'Resultado da Pesquisa: {pesquisa}')
        sleep(1)
        for livros in range(0 , len(banco)):
            index = cont = 0
            for valor  in banco[livros]:
                if cont == 2:
                    for valor in banco[livros]:
                        sleep(0.8)
                        print(f'{nomes[index]} - {valor :>7}')
                        index += 1
                    linha()
                    sleep(2)
                cont += 1

    elif filtro in 'I':
        pesquisa = int(input('ID: '))
        titulo(f'Resultado da Pesquisa: {pesquisa}')
        sleep(1)
        for livros in range(0 , len(banco)):
            index = cont = 0 
            for valor in banco[livros]:
                if cont == 3:
                    titulo(f'{banco[livros][1]}')
                    for valor in banco[livros]:
                        sleep(0.8)
                        print(f'{nomes[index]} - {valor :>7}')
                        index += 1
                    linha()
                    sleep(2)
                cont += 1
    sleep(3)


# Empréstimo e devolução de livros
def Empréstimo_e_devolução():
    titulo('Devolução e Empretismo')
    print('1 - Alugar um Livro')
    print('2 - Devolução do Material')
    print('3 - Ver livros emprestado')
    linha()
    while True:
        escolher = int(input('Escolher: '))
        linha()
        if escolher in (1,2,3):
            break
        print('\033[mApenas 1,2 e 3!!!\033[m')
    banco = banco_de_dados()
    nomes = ['autor' , 'titulo' , 'categoria' , 'ID']

    if escolher == 1:
        MostrarLivro()
        print('Digite o id do livro desejado!!!')
        livroID = int(input('ID: '))
        for livro in range(0 , len(banco)):
            cont = index = 0
            for valor in banco[livro]:
                if cont == 3:
                    if livroID == valor:
                        for p , valor in enumerate(banco[livro]):
                            sleep(0.3)
                            print(f'{nomes[index]} - {valor :7>}')
                            if p == 0:
                                autor = valor
                            if p == 1:
                                titulos = valor
                            if p == 2:
                                categoria = valor
                            if p == 3:
                                Id = valor
                            index += 1
                        linha()
                        Sn = str(input('Quer mesmo alugar o livro?: ')).strip()[0]
                        if Sn in 'Ss':
                            nome = str(input('Seu nome?: '))
                            deleta_info(livroID)
                            print(f'''{aluga_livro(usuario = nome ,
                                    autor = autor ,
                                    titulo = titulos ,
                                    categoria = categoria,
                                    Id = Id)}''')
                        else:
                            print('\033[1;31mVocê optou a não alugar o livro\033[m')
                else:
                    cont += 1

    elif escolher ==  2:
        titulo('Devolução Do livro :)') 
        print('Digite o ID do livro que iremos verificar no nosso banco de dados')
        livroID = int(input('ID: '))
        banco = banco_de_dados(banco = 'emprestimosEdevolucao')
        nomes = ['autor' , 'titulo' , 'categoria' , 'ID']

        for livro in range(0 ,  len(banco)):
            cont = index = 0
            for valor in banco[livro]:
                if cont == 3:
                    if livroID == valor:
                        idexbição = valor
                        for p , valor in enumerate(banco[livro]):
                            sleep(0.3)
                            print(f'{nomes[index]} - {valor :7>}')
                            if 0 < p <= 3:
                                index += 1
                            if p == 1:
                                autor = valor
                            if p == 2:
                                titulos = valor
                            if p == 3:
                                categoria = valor
                            if p == 4:
                                Id = valor
            
                        linha()
                        print('Aguarde...')
                        linha()
                        sleep(4)
                        print(f'Livro ID: {idexbição} em processo de devolução...')
                        sleep(1)
                        add_livros(autor = autor , titulo = titulos , categoria = categoria , Id = False )
                        deleta_info(Id = livroID, bancos = 'emprestimosEdevolucao')
                        print('Pronto!!!')
                        MostrarLivro()
                else:
                    cont += 1

    elif escolher == 3:
        MostrarLivro(bancos = 'emprestimosEdevolucao')