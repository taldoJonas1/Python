'''
2- Fazer uma função que retorne o maior elemento de um vetor.
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
3- Fazer uma função que retorne o menor elemento de um vetor.
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
4- Calcular a média dos valores das posições ímpares de um vetor. 
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
5- Fazer um programa que possui um menu com as seguintes opções 
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
    if n != 0:
        for i in range(10):
            result = 0
            result = n * (i + 1)
            print(f'{n} x {i+1} = {result}')
        print('\n')
    else:
        print('PROGRAMA CANCELADO\n')

def imc(p, h):
    if h > 3:
        h = h / 100
    result = p / (h**2)
    print(f'PESO: {p:.1f} kg\nALTURA: {h:.2f} m')
    print(f'Seu IMC: {result:.2f}\n')

def fatorial(n):
    nro = n
    fat = 1
    for n in range(n, 1, -1):
        fat *= n
    
    print(f'O fatorial de {nro} é {fat}\n')

opcao = int(input('MENU DE EXERCICIOS\n==================\n[1]TABUADA\n[2]IMC\n[3]FATORIAL\n[-1]ENCERRA PROGRAMA\nESCOLHA: '))
while opcao > -1:
    match opcao:
        case -1:
            print('PROGRAMA ENCERRADO')
        case 1:
            n1 = int(input('Digite um nro de 1 a 9 (0 cancela): '))
            while 0 > n1 or n1 > 9:
                n1 = int(input('ERRO\nInsira um nro entre 1 e 9 (0 cancela): ')) 
            resp = tabuada(n1)
        case 2:
            peso = float(input('Insira seu peso(kg): '))
            altura = float(input('Insira sua altura(m): '))
            resp = imc(peso, altura)
        case 3:
            nro = int(input('Digite um nro: '))
            while nro <= 0:
                nro = int(input('Digite um nro maior que 0: '))
            resp = fatorial(nro)
        case _:
            print('ESCOLHA UM NRO QUE ESTÁ NO MENU')
    opcao = int(input('MENU DE EXERCICIOS\n==================\n[1]TABUADA\n[2]IMC\n[3]FATORIAL\n[-1]ENCERRA PROGRAMA\nESCOLHA: '))  
'''
================================================================
6- Fazer uma função que calcule o quociente inteiro da divisão 
entre dois números, sem utilizar funções prontas.
'''
def quociente(dendo, sor):
    conta = dendo / sor
    return conta

dividendo = int(input('Insira o dividendo: '))
divisor = int(input('Insira o divisor: '))
resp = quociente(dividendo, divisor)
respInt = int(resp)
resto = dividendo - (respInt*divisor)
print(f'O quociente inteiro da divisão de {dividendo} por {divisor} é {respInt} com resto {resto}')
'''
================================================================
7- Fazer uma função que calcule o fatorial de um número.
'''
def fatorial(n):
    ni = n
    fat = 1
    for n in range(n, 1, -1):
        fat *= n
    
    print(f'O fatorial de {ni} é {fat}\n')

nro = int(input('Digite um nro inteiro positivo e seu fatorial será calculado: '))
while nro <= 0:
    nro = int(input('Digite um nro maior que 0: '))
resp = fatorial(nro)
'''
================================================================
8- Fazer uma função que receba o valor de N como parâmetro, 
calcular e retorne o valor do somatório S:
S = 1 + (2/4) + (3/9) + (4/16) + ... + (N/N²)
'''
def formula(n):
    s = 0
    for i in range(n):
        s += (i+1) / ((i+1)**2)
    
    print(f'O resultado da fórmula é {s}')

nro = int(input('\nEsta é a fórmula:\nS = 1 + (2/4) + (3/9) + (4/16) + ... + (N/N²)\nInsira o valor de N a ser calculado: '))
while nro <= 1:
    nro = int(input('Digite um nro maior que 1: '))
resp = formula(nro)
'''
================================================================
9- Fazer uma função que verifique se o número de um CPF é válido.
'''
def validacao(vetCPF):
    soma1 = soma2 = dig1 = dig2 = 0

    for i in range(9):
        soma1 += vetCPF[i] * (10 - i)
    
    div1 = soma1 // 11
    resto1 = soma1 - (div1 * 11)

    if resto1 >= 2:
        dig1 = 11 - resto1
    else:
        dig1 = 0
    
    for i in range(10):
        soma2 += vetCPF[i] * (11 - i)
    
    div2 = soma2 // 11
    resto2 = soma2 - (div2 * 11)

    if resto2 >= 2:
        dig2 = 11 - resto2
    else:
        dig2 = 0

    if vetCPF[9] == dig1 and vetCPF[10] == dig2:
        print('CPF VÁLIDO')
    else: 
        print('CPF INVÁLIDO')

print('\nPROGRAMA DE CONFIRMAÇÃO DE VALIDADE DE CPF\n==========================================')
nome = input('Nome completo: ')
cpf = input('Seu CPF: ')\
    .replace(' ','')\
    .replace('.','')\
    .replace('-','')

vetCPF = []
for i in range(len(cpf)):
    vetCPF.append(int(cpf[i]))
resp = validacao(vetCPF)
'''
================================================================
10- Fazer uma função que verifica se uma palavra, frase ou número 
é um palíndromo. Um palíndromo é qualquer sequência de caracteres 
que seja a mesma se lida da esquerda para a direita ou da direita
para a esquerda. Por exemplo, a palavra “osso” é um palíndromo, 
pois é idêntica não importa o sentido da leitura.
'''
def palindromo(t, p1, pal):
    p2 = []
    for i in range(t):
        p2.append(p1[t-(i+1)])
    if p1 == p2:
        print(f'A palavra {pal} é um palíndromo.')
    else:
        print(f'A palavra {pal} não é um palíndromo.')

print('VERIFICAÇÃO DE PALÍNDROMO\n=========================')
palavra = input('Digite uma palavra: ').lower()
tamanho = len(palavra)
vetPalavra = []
for i in range(tamanho):
    vetPalavra.append(palavra[i])
resp = palindromo(tamanho, vetPalavra, palavra)
'''
================================================================
11- A jornada de trabalho semanal de um funcionário é de 40 horas. 
O funcionário que trabalhar mais de 40 horas receberá hora extra, 
cujo cálculo é o valor da hora regular com um acréscimo de 50%.
Escreva uma função que receba o número de horas trabalhadas em uma
semana e o salário por hora, e retorne o salário do funcionário.
'''
def horasExtras(v, h):
    salarioFixo = v * 40
    hExtra = 0
    if h > 40:
        hExtra = h - 40
        hExtra *= 1.5
        acrescimo = hExtra * v
    else:
        acrescimo = 0
    print(f'O funcionário trabalhou {h+hExtra}, então seu salário é R${salarioFixo+acrescimo}')

horas = int(input('Insira a quantidade de horas trabalhadas pelo funcionário essa semana: '))
valor = float(input(f'Insira o valor da hora do funcioário: R$'))
valor = (f'{valor:.2f}')
resp = horasExtras(valor, horas)
