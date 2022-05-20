# importando a biblioteca de teste
import pytest
# nome da função obs quando colocar entre aspas é exatamente o que esta escrito
# quando entre parentes sem aspas é uma variavel
# os dois pontos indica que comecou


def imprimir_oi(name):
    print(f'Oi, {name}')

def somar(numero_a, numero_b):
    return numero_a + numero_b

def subtrair(numero_a, numero_b): #nome metodo ou funcao (nome usando um verbo){(parametro-ingredientes)}
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b

def dividir(numero_a, numero_b):
    return numero_a / numero_b


if __name__ == '__main__':
    imprimir_oi('Jeferson-Helia-Noah')

    # Chamar da definição somar e mostrar o resultado
    resultado = somar(7, -6)
    print(f'a soma: {resultado}')

    # Chamar a definição subtrair e mostrar o resultado
    resultado = subtrair(100, 59)
    print(f'A subtração: {resultado}')

    # Chamar a definição Multiplicar e mostrar o resultado
    resultado = multiplicar(3, 5)
    print(f'A Multiplicação: {resultado}')


    # Chamar a definição Multiplicar e mostrar o resultado
    resultado = dividir(16, 4)
    print(f'A Divisao: {resultado}')

# primeiro teste unitario



