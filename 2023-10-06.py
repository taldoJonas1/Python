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

t = b = r = 0

print('ESTOQUE DE VINHOS, INSERIR A LETRA F ENCERRA.')
while tipo != 'F':
    tipo = input('INSIRA O TIPO DO VINHO [T]INTO, [B]RANCO OU [R]OSÊ: ')
    if tipo == 'T':
        t += 1
    elif tipo == 'B':
        b += 1
    elif tipo == 'R':
        r += 1
    else:
        print('LETRA INVÁLIDA')

total = t + b + r
pct_t = (t / total) * 100
pct_b = (r / total) * 100
pct_r = (t / total) * 100
print(f'SEU ESTOQUE:\nTINTO: {pct_t}% \nBRANCO: {pct_b}% \nROSÊ: {pct_r}%')

=======================================================================================================================
