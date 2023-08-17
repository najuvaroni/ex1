from pacotes.calculadora import *

op = int(input("Qual operação? 1- soma / 2- subtração / 3- divisão / 4- multiplicação:  "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if op == 1:
    soma = soma(n1, n2)
    print(soma)

elif op == 2:
    subtracao = subtracao(n1,n2)
    print(subtracao)

elif op == 3:
    div = divisao(n1,n2)
    print(div)

elif op == 4:
    mult = multiplicacao(n1,n2)
    print(mult)

else:
    print("Erro")


