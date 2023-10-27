'''
Fazer uma função que retorne o maior elemento de um vetor.
'''
def maior(vet):
    maiorN = vet[0]
    for i in range(r):
        if vet[i] > maiorN:
            maiorN = vet[i]
    
    return maiorN

r = int(input('Quantos numeros serão inseridos: '))
while r <= 0:
    r = int(input('Insira um nro maior que 0'))
vet = []

for i in range(r):
    vet.append(int(input(f'Digite o {i+1}° nro: ')))

resp = maior(vet)
print(f'Maior do vetor: {resp}')
'''
================================================================
'''
'''
Fazer uma função que retorne o menor elemento de um vetor.
'''
def menor(vet):
    menorN = vet[0]
    for i in range(r):
        if vet[i] < menorN:
            menorN = vet[i]
    
    return menorN

r = int(input('Quantos numeros serão inseridos: '))
while r <= 0:
    r = int(input('Insira um nro maior que 0'))
vet = []

for i in range(r):
    vet.append(int(input(f'Digite o {i+1}° nro: ')))

resp = menor(vet)
print(f'Menor do vetor: {resp}')
'''
================================================================
'''
