'''
Faça um programa que efetue a soma de todos os números ímpares que são
múltiplos de 3 e que se encontram no conjunto dos números de 1 até 500.
'''
soma = 0
for nro in range(0, 500, 1):
    if nro % 2 == 1 and nro % 3 == 0: 
        soma += nro

print(soma)

=======================================================================================================================
'''
Fazer um programa que simule uma contagem regressiva de 10 minutos, ou
seja, mostre: 10:00, 9:59, 9:58, 9:57, ..., 8:59, 8:58, até 0:00.
'''

print('10:00')
for m in range(9, -1, -1):
    for s in range(59, -1, -1):
        if s < 10:
            print(f'\n0{m}:0{s}')
        else:
            print(f'\n0{m}:{s}')
          
=======================================================================================================================
'''
Construa um programa que calcule a média aritmética de um conjunto de
números pares fornecidos pelo usuário. O usuário irá fornecer um total de 10
números. Observe que nada impede que o usuário forneça quantos números
ímpares quiser, com a ressalva de que eles não poderão ser acumulados.
'''

pares = 0
n = 0
for i in range(0, 10, 1):
    nro = int(input('Digite um nro inteiro: '))
    if nro % 2 == 0:
        pares += nro
        n += 1
media = pares / n
print(f'A média dos nros pares inseridos foi {media}')

=======================================================================================================================
'''
Construa um programa que calcule a média aritmética de um conjunto de
números pares que forem fornecidos pelo usuário. O valor de finalização 
será a entrada do número 0 (zero). Observe que nada impede que o
usuário forneça quantos números ímpares quiser, com a ressalva de que
eles não poderão ser acumulados.
'''

cont = soma = 0
while nro != 0:
    nro = int(input('DIGITE UM NRO INTEIRO |O NUMERO 0 ENCERRA|: '))
    if nro % 2 == 0:
        soma += nro
        cont += 1
media = soma / cont
print(f'A média dos nros pares inseridos foi {media}')      

=======================================================================================================================

'''
Imagine uma brincadeira entre dois colegas, na qual um pensa um número 
e o outro deve fazer chutes até acertar o número imaginado. Como dica, 
a cada tentativa é dito se o chute foi alto ou foi baixo. Elabore um 
programa dentro deste contexto, que leia o número imaginado e os chutes, 
ao final mostre quantas tentativas foram necessárias para descobrir o número.
'''

tent = 0
import random
n1 = random.randint(0,50)
n2 = int(input('Tente acertar o número: '))

while n2 != n1:
    if n2 > n1:
        n2 = int(input('Menos\n'))
        tent += 1
    elif n2 < n1:
        n2 = int(input('Mais\n'))
        tent += 1

if n2 == n1:
    print(f'ACERTOU!!!\n{tent + 1} tentativas.')

=======================================================================================================================

'''
Faça um programa que permita fazer um levantamento do estoque de vinhos de 
uma adega, tendo como dados de entrada tipos de vinho, sendo: 'T' para tinto, 
'B' para branco e 'R' para rosê. Especifique a porcentagem de cada tipo sobre 
o total geral de vinhos; a quantidade de vinhos é desconhecida, utilize para 
finalizador do algoritmo a opção 'F' de fim.
'''
