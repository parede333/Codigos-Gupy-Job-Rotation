# -*- coding: utf-8 -*-
"""
Criado por Willian Wagner de Brito Coura

Resolução do problema para o test de Job Rotatio - São Paulo
------------------------------------------------------------------------------------------
Questão 2 
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
------------------------------------------------------------------------------------------
"""
def Fibonacci():
    """
    Função que retorna a sequência de fibonacci de acordo com o número que fora inserido.
    A função também verifica se o número inserido pertence ou não a sequência.

    -------

    """
    numero = int(input('Digite o número para calcular a sequencia de Fibonacci '))
    lista = []
    y = range(numero + 1)
    for i in y:
        if i < 2:
            lista.append(i)
        else: 
            y = (i - 1) + (i - 2)
            lista.append(y)
    print(30*"---")
    print('Essa é a sequencia obtido a partir do númerio inserido')
    print(lista)
    print(30*"---")
    if numero in lista:
        print(f'O número {numero} que foi inserido pertence a sequencia de Fibonacci')
    else:
        print(f'O número {numero} inserido não pertence a sequencia de Fibonacci')

if __name__ == '__main__':
    Fibonacci()