from calculador import multiplicar, divisao, dividir, soma, subtracao, potencia


class TesteCalculador:
    def test_multiplica(self):
        n1 = 4
        n2 = 5
        resultado = 20
        result_obitido = multiplicar(n1, n2)
        assert resultado == result_obitido

    def test_divisao(self):
        n1 = 6
        n2 = 2
        esperado = 3
        obtido = divisao(n1, n2)
        assert esperado == obtido

    def test_dividir_negativo(self):
        n1 = 6
        n2 = 0
        esperado = 'Não dividiras por zero'
        obtido = dividir(n1, n2)
        assert esperado == obtido

    def test_soma(self):
        n1 = 45
        n2 = 5
        esperado = 50
        obtido = soma(n1, n2)
        assert esperado == obtido

    def test_subtracao(self):
        n1 = 45
        n2 = 5
        esperado = 40
        obtido = subtracao(n1, n2)
        assert esperado == obtido

    def test_potencia(self):
        n1 = 4
        n2 = 4
        esperado = 256
        obtido = potencia(n1, n2)
        assert esperado == obtido
        
        # comentario pelo git
