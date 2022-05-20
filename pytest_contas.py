import pytest

import calculador


lista_para_multiplicar = [
    (3, 6, 18),
    (3, 3, 9),
    (5, 4, 20),
    (6, 2, 12),
    (7, 9, 63),
    (2, 5, 10),
    (2, 5000, 10000),
]
@pytest.mark.parametrize('n1, n2, esperado', lista_para_multiplicar)


def test_multiplicar(n1, n2, esperado):
    # as informaçoes vaoi vir da lista
    # configura

    # executa
    obtido = calculador.multiplicar(n1, n2)

    #valida
    assert  esperado == obtido


