'''
Fazer um programa que calcule a soma dos elementos de um vetor
'''
fim = int(input('Digite quantos nros serão inseridos: '))
while fim < 2:
    fim = int(input('Digite um nro maior que 2: '))
vet = []
soma = 0

for i in range(fim):
    vet.append(int(input('Digite um nro: ')))

for i in range(fim):
    soma += vet[i]

print(f'Soma: {soma}')

===================================================================================
'''
Fazer um programa que calcule a média dos números pares de um vetor.
'''
fim = int(input('Digite quantos nros serão inseridos: '))
while fim < 2:
    fim = int(input('Digite um nro maior que 2: '))
vet = []
cont = soma = 0

for i in range(fim):
    vet.append(int(input('Digite um nro: ')))

for i in range(fim):
    if vet[i] % 2 == 0:
        soma += vet[i]
        cont += 1

print(f'Média dos nros pares: {soma / cont}')

===================================================================================
'''
Considere um programa que calcule a média aritmética geral de uma classe 
de alunos e imprima a quantidade de notas que estão acima da média calculada. O 
usuário deve entrar com a quantidade de alunos.
'''
fim = int(input('Digite o nro de alunos: '))
while fim < 2:
    fim = int(input('Digite um nro maior que 2: '))
vet = []
cont = 0

for i in range(fim):
    vet.append(float(input(f'Digite uma nota: ')))

for i in range(fim):
    if vet[i] >= 6:
        cont += 1

print(f'Quantidade de alunos acima da média: {cont}')
