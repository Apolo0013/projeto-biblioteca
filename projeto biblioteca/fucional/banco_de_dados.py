# importações
from random import randint
import sqlite3


# Funcoes
# Gerador de ID
def geradorID():
    """
    Descrição da função: Criar um ID de quatros digitos.

    Args:
    - Não receber parametro.

    Returns:
    - tipo de retorno: Descrição do que a função retorna.

    """
    Id_unicos = []  # guardar o ID já usados
    while True:
        Id = randint(1000,9999) # 1000 - 9999: numeros do ID
        if Id not in Id_unicos:
            Id_unicos.append(Id) # Guardar o ID.
            return Id


# banco de dados em apenas em uma funcao
def banco_de_dados(banco = 'livros'):
    cursor.execute(f'SELECT * FROM {banco}')
    banco_de_dados = cursor.fetchall()
    return banco_de_dados


# add informacoes de um livro no sqlite
def add_livros(autor , titulo , categoria , bancos , Id = True):
    if Id:
        Idd = geradorID()
    else:
        idd = Id
    cursor.execute(f'INSERT INTO {bancos} VALUES ("{autor}" , "{titulo}" , "{categoria}" , {idd})')
    cursor.execute('SELECT * FROM livros')
    dados = cursor.fetchall()
    banco.commit()
    return dados


def aluga_livro(usuario , autor , titulo , categoria ,  Id):
    cursor.execute(f'INSERT INTO emprestimosEdevolucao VALUES("{usuario}","{autor}","{titulo}","{categoria}","{Id}")')
    cursor.execute('SELECT * FROM emprestimosEdevolucao')
    dados = cursor.fetchall()
    banco.commit()
    return dados


def deleta_info(Id , bancos = 'livros'):
    cursor.execute(f'DELETE from {bancos} WHERE ID = {str(Id)}')
    banco.commit()


# Criando o banco de dados
banco = sqlite3.connect('dados_livros.db')

cursor = banco.cursor()
#cursor.execute('''CREATE TABLE livros (autor text,titulo text, categoria text, ID integer ''')

#cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimosEdevolucao (
#                    usuario text,
#                    autor text,
#                    titulo text,
#                    categoria text,
#                    ID integer
#                )''')

    