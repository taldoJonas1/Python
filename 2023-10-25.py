'''
Escreva uma função que receba dois parâmetros e imprima o
menor dos dois. Se eles forem iguais, imprima que eles são
iguais.
'''

def maior(n1, n2):
    if n1 > n2:
        print(f'{n2} é o menor.')
    elif n1 < n2:
        print(f'{n1} é o menor.')
    elif n1 == n2:
        print('São iguais.')

n1 = int(input('Digite o primeiro nro: '))
n2 = int(input('Digite o segundo nro: '))
maior(n1,n2)

============================================================

'''
Faça uma função que some os elementos de um vetor.
'''

def somaTotal(vet):
    soma = 0
    for i in range(r):
        soma += vet[i]
    return soma

r = int(input('Quantos numeros serão inseridos: '))
vet = []

for i in range(r):
    vet.append(int(input(f'Digite o {i+1}° nro: ')))

resp = somaTotal(vet)
print(f'Soma do vetor: {resp}')

============================================================

'''
Faça uma função que calcule a média dos elementos de um vetor,
a partir da função de soma.
'''

def somaTotal(vet):
    soma = 0
    for i in range(r):
        soma += vet[i]
    return soma

def mediaTotal(vet):
    soma = somaTotal(vet)

    media = soma / len(vet)
    return media


r = int(input('Quantos numeros serão inseridos: '))
vet = []

for i in range(r):
    vet.append(int(input(f'Digite o {i+1}° nro: ')))

somaTotal(vet)
resp = mediaTotal(vet)
print(f'Média do vetor: {resp}')
