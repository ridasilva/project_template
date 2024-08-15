# Código para saudar visitante
# Autor: Ricardo
# Data: 15/08/24
# python hello.py <nome do visitante>
import sys


def hello(nome_visitante):
    '''
    Função que imprimi uma mensagem de boas vindas
    '''
    print(f'Olá {nome_visitante}, seja bem-vindo!')


if __name__=='__main__':
    hello(sys.argv[1])
