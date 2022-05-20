import pytest


def multiplicar(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    if n1 != 0 and n2 != 0:
        return n1 / n2
    else:
        print(f'Numero nao pode ser zero')


def dividir(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 'Não dividiras por zero'


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def potencia(n1, n2):
    return n1 ** n2


if __name__ == '__main__':

    n1 = 4
    n2 = 5

    result = multiplicar(n1, n2)
    print(f'A Multiplicação é: {result}')

    n1 = 72
    n2 = 8

    result = divisao(n1, n2)
    print(f'O resultado a Divisão é: {result}')

    n1 = 18
    n2 = 3

    result = soma(n1, n2)
    print(f'O resultado a Soma é: {result}')

    n1 = 18
    n2 = 3

    result = subtracao(n1, n2)
    print(f'O resultado a Subtracao é: {result}')

    n1 = 2
    n2 = 5

    result = potencia(n1, n2)
    print(f'O resultado a Potencia é: {result}')

def test_multiplica():
    n1 = 4
    n2 = 5
    resultado = 20
    result_obitido = multiplicar(n1, n2)
    assert resultado == result_obitido


def test_divisao():
    n1 = 6
    n2 = 2
    esperado = 3
    obtido = divisao(n1, n2)
    assert esperado == obtido


def test_dividir_negativo():
    n1 = 6
    n2 = 0
    esperado = 'Não dividiras por zero'
    obtido = dividir(n1, n2)
    assert esperado == obtido


def test_soma():
    n1 = 45
    n2 = 5
    esperado = 50
    obtido = soma(n1, n2)
    assert esperado == obtido


def test_subtracao():
    n1 = 45
    n2 = 5
    esperado = 40
    obtido = subtracao(n1, n2)
    assert esperado == obtido


def test_potencia():
    n1 = 4
    n2 = 4
    esperado = 256
    obtido = potencia(n1, n2)
    assert esperado == obtido
