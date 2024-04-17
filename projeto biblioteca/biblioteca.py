# importções
from fucional.funcao_livros import *



while True:
    print('\033[1;33m')
    titulo('MENU BIBLIOTECA')
    sleep(0.2)
    print('1 - Adicionar livro à biblioteca')
    sleep(0.2)
    print('2 - Remover livro da biblioteca')
    sleep(0.2)
    print('3 - Pesquisar livros por título, autor, categoria')
    sleep(0.2)
    print('4 - Mostrar lista de livros disponíveis')
    sleep(0.2)
    print('5 - Empréstimo e devolução de livros')
    sleep(0.2)
    print('6 - Cancelar o Programa')
    linha()
    while True:
        opcao = int(input('Escolha: \033[m'))
        sleep(0.2)
        if opcao in (1 , 2 ,3 , 4 , 5 , 6):
            break
        print('\033[1;31mERRO!!!: Apenas numeros  1 , 2 , 3 , 4 , 5 e 6\033[m')
    

    if opcao == 1:
        addLivro()

    elif opcao == 2:
        deletelivro()
    
    elif opcao == 3:
        PesquisaLivro()

    elif opcao ==  4:
        MostrarLivro()
    elif opcao == 5:
        Empréstimo_e_devolução()
    elif opcao == 6:
        print('Fim do Programa')
        break
