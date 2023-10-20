'''
Fazer um programa que leia um vetor de 20 números inteiros e 
determine qual o maior e o menor número do vetor e imprima os 
dois valores.
'''
r = range(20)
vet = []


for i in r:
    vet.append(int(input('Insira um nro: ')))

maior = menor = vet[0]
for i in r:
    if vet[i] > maior:
        maior = vet[i]
    elif vet[i] < menor:
        menor = vet[i]

print(f'Maior numero do vetor: {maior}')
print(f'Menor numero do vetor: {menor}')

==========================================================================
'''
Crie um programa que leia um vetor de 30 números inteiros e gere 
um segundo vetor cujas posições pares são o dobro do vetor original 
e as ímpares são o triplo.
'''

vet1 = []
vet2 = []
r = range(30)

for i in r:
    vet1.append(int(input('Insira um nro: ')))

print(vet1)

print('\n=====VETOR MODIFICADO=====\n')

for i in r:
    if i == 0:
        vet2.append(vet1[i])
    elif i % 2 == 0:
        vet2.append(vet1[i] * 2)
    elif i % 2 == 1:
        vet2.append(vet1[i] * 3)

print(vet2)

==========================================================================

'''
Crie um programa que permita a leitura de um vetor de 30 números 
inteiros e gere um segundo vetor com os mesmos dados, só que de 
maneira invertida, ou seja, o primeiro elemento do vetor original 
ficará na última posição do novo vetor, o segundo na penúltima 
posição e assim por diante.
'''

vet1 = []
vet2 = []
r = range(30)

for i in r:
    vet1.append(int(input('Insira um nro: ')))

print(vet1)

print('\n=====VETOR INVERTIDO=====\n')

for i in r:
    vet2.append(vet1[29-i])

print(vet2)

==========================================================================
'''
Crie um programa que leia um vetor de 20 números inteiros e em
seguida divida estes números em outros 2 novos vetores, separando
os números pares dos números ímpares.
'''
vet = []
pares = []
impares = []
r = range(20)

for i in r:
    vet.append(int(input('Insira um nro: ')))

print(f'\n{vet}')

print('\n=====VETORES DIVIDIDOS=====\n')

for i in r:
    if vet[i] % 2 == 0:
        pares.append(vet[i])
    else:
        impares.append(vet[i])

print(f'\nPARES{pares}')
print(f'\nIMPARES{impares}')

==========================================================================

'''
Crie um programa que leia uma série de 50 notas e calcule quantas 
são 10% acima da média e quantas são 10% abaixo da média.
'''
notas = []
r = range(5)
soma = cont = cont1 = 0

for i in r:
    notas.append(float(input(f'Insira a {i+1}° nota: ')))
    soma += notas[i]

print(f'NOTAS{notas}')

media = soma / 5

for i in r:
    if notas[i] >= (media + (0.1*media)):
        cont += 1
    elif notas[i] <= (media - (0.1*media)):
        cont1 += 1

print(f'10% ACIMA DA MÉDIA: {cont}')
print(f'10% ABAIXO DA MÉDIA: {cont1}')
