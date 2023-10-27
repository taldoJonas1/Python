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
Calcular a média dos valores das posições ímpares de um vetor. 
Passar o vetor como parâmetro e retornar a média.
'''
import random

def mediaPosicoesImpares(vet):
    media  = soma = qtd = 0
    print(vet)

    for i in range(r):
        if i % 2 != 0:
            qtd += 1
            soma += vet[i]
    
    media = (soma / qtd)
    return media

r = int(input('Quantos numeros serão inseridos: '))
while r <= 0:
    r = int(input('Insira um nro maior que 0'))
vet = []

for i in range(r):
    vet.append(random.randint(1, 100))
    # vet.append(int(input(f'Insira o nro na posição {i} do vetor: ')))

resp = mediaPosicoesImpares(vet)
print(f'A média dos nros nas posições impares do vetor é: {resp}')
'''
================================================================
Fazer um programa que possui um menu com as seguintes opções 
para executar diferentes funções, até que o usuário digite -1 
e termine o programa:
◦ Escrever a tabuada de um número ou uma mensagemde erro caso 
o número não esteja entre 1 e 9. O número deve ser passado 
como parâmetro e a validação feita na função.
◦ Calcular o Índice de Massa Corporal (IMC): a fórmula é 
IMC = peso / altura2
◦ Passar o peso e altura como parâmetros e retornar o IMC.
◦ Calcular o fatorial de um número. O número deve ser
passado como parâmetro e retornar o resultado.
'''
def tabuada(n):
    for i in range(10):
        result = 0
        result = n * i
        print(f'{n} x {i} = {result}')

def imc(p, h):
    result = p / (h**2)
    print(f'Seu IMC: {result}')

def fatorial(n):
    nro = n
    fat = 1
    for n in range(n, 1, -1):
        fat *= n
    
    print(f'O fatorial de {nro} é {fat}')

opcao = int(input('MENU DE EXERCICIOS\n==================\n[1]TABUADA\n[2]IMC\n[3]FATORIAL\n[-1]ENCERRA PROGRAMA\nESCOLHA: '))
match opcao:
    case -1:
        print('PROGRAMA ENCERRADO')
    case 1:
        n1 = int(input('Digite um nro de 1 a 9: '))
        while 1 > n1 > 9:
            n1 = int(input('ERRO\nInsira um nro entre 1 e 9: ')) 
        resp = tabuada(n1)
    case 2:
        peso = float(input('Insira seu peso (kg): '))
        altura = float(input('Insira seu peso (m): '))
        resp = imc(peso, altura)
    case 3:
        nro = int(input('Digite um nro: '))
        while nro <= 0:
            nro = int(input('Digite um nro maior que 0: '))
        resp = fatorial(nro)
    case _:
        print('ESCOLHA UM NRO QUE ESTÁ NO MENU')
