'''
Fazer um algoritmo que leia a idade e o nome de 30 pessoas 
(o algoritmo não deve permitir valores inválidos). Os valores 
lidos devem ser armazenados em um vetor. Após a leitura de todos os valores, encontre: 

a) a média das idades; 
b) a quantidade de pessoas que possuem idade acima da média; 
c) o nome das pessoas que possuem idade abaixo da média; 
d) o nome da pessoa mais velha e da mais nova; 
e) para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.
'''

def exA(idade):
    soma = 0
    cont = 0
    for i in range(len(idade)):
        soma += idade[i]
        cont += 1
    media = soma / cont
    return media

def exB(media, idade):
    cont = 0
    for i in range(len(idade)):
        if idade[i] > media:
            cont += 1
    return cont

def exC(nome, idade, media):
    AdM = []
    for i in range(len(nome)):
        if idade[i] < media:
            AdM.append(nome[i])
    return AdM

def exD(n, idd):
    maior = idd[0]
    Imaior = 0
    menor = idd[0]
    Imenor = 0
    for i in range(len(idd)):
        if idd[i] > maior:
            maior = idd[i]
            Imaior = i
        elif idd[i] < menor:
            menor = idd[i]
            Imenor = i
    resp = (f'Mais velho(a): {n[Imaior]}\nMais novo(a): {n[Imenor]}')
    return resp

def exE(idd):
    fat = []
    for i in range(len(idd)):
        r = 1
        for j in range(idd[i], 1, -1):
            r *= j
        fat.append(r)
    print('IDADE                         FATORIAL')
    for i in range(len(idd)):
        print(f'{idd[i]}                         {fat[i]}')

nomes = []
idades = []
for i in range(30):
    nomes.append(input(f'Insira o nome da pessoa {i+1}'))
    idades.append(input(f'Insira a idade da pessoa {i+1}'))
    while idades[i] < 0:
        idades.append(input(f'IDADE INVÁLIDA\nInsira novamente a idade da pessoa {i+1}'))

a = exA(idades)
b = exB(a, idades)
c = exC(nomes, idades, a)
d = exD(nomes, idades)
e = exE(idades)
