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
