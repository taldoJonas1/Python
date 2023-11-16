'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma
prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número
de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a
ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o
valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste
momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a
quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da
seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação, e quando houver
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
def valorPagamento(p, a):
    valorFinal = 0
    if a == 0:
        valorFinal = p
    else:
        valorFinal = p * 1.03
        for i in range(a):
            valorFinal *= 1.001
    print(f'{valorFinal:.2f}')
    return valorFinal

condicao= True
cont = 0
qtd = 0.0

while condicao:
    prest = float(input('Insira o valor da(s) prestação(ões): R$'))
    if prest == 0:
        print('=====PROGRAMA ENCERRADO=====\nRESULTADOS:')
        print(f'Quantidade de prestações pagas: {cont}')
        print(f'Valor total das prestações do dia: R${qtd:.2f}')
        condicao = False
    else:
        dias = int(input('Insira quantos dias houveram de atraso: '))
        x = valorPagamento(prest, dias)
        qtd += x
        cont += 1

'''
A MODA de um vetor de números é o número no vetor que é repetido com maior frequência.
Se mais de um número for repetido com frequência máxima igual, não existirá uma moda.
Escreva uma função que aceite um vetor de números e retorne a moda ou uma indicação de que
a moda não existe
'''

def modaVetor(vet):
    vet2 = []
    vet3 = []
    for i in range(len(vet)):
        if vet[i] not in vet2:
            vet2.append(vet[i])
    
    for i in range(len(vet2)):
        cont = 0
        for j in range(len(vet)):
            if vet2[i] == vet[j]:
                cont += 1
        vet3.append(cont)
    moda = 0
    for i in range(len(vet3)):
        if vet3[i] > moda:
            moda = vet3[i]
            posicao = i

    for i in range(len(vet3)):
        if i != posicao:
            if moda == vet3[i]:
                moda = 'A moda não existe'
                print('A moda não existe')
    
    if moda != 'A moda não existe':
        print(f'A moda do vetor é {vet2[posicao]}')


vet = []
tam = int(input('Insira quantos numeros serão inseridos no vetor: '))
while tam < 1:
    tam = int(input('Insira quantos numeros serão inseridos no vetor: '))

for i in range(tam):
    vet.append(int(input(f'Insira o {i+1}° numero: ')))

modaVetor(vet)

'''
Fazer um programa que desenvolva um jogo para adivinhar uma palavra oculta. Será um jogo
semelhante ao da forca, mas com algumas diferenças. Neste jogo, o jogador tenta adivinhar uma
palavra oculta, mediante uma quantidade de tentativas limitada. Para isso, o programa escolhe,
aleatoriamente, uma palavra de uma lista de palavras contidas em um arquivo e o jogador deve
adivinhar a palavra. Essa lista deve conter, no mínimo, 10 palavras. A quantidade de tentativas
também deve ser aleatória, em um intervalo de 6 a 11. Quando o jogador adivinha alguma letra,
as letras correspondentes na palavra são reveladas. Além disso, deve ser informado também a
quantidade de tentativas que ainda resta quando a letra for incorreta, mensagem caso já tenha
tentado a letra, e outras situações para tornar o jogo mais interessante. O jogo finaliza quando o
jogador adivinhar a palavra ou acabar as suas tentativas.
'''
import random

frutas = ['abacaxi', 'uva', 'morango', 'melancia', 'banana', 'pera', 'maca', 'manga', 'acai', 'mamao', 'melao',
          'kiwi', 'caju', 'acerola', 'jaca', 'pitanga', 'jabuticaba']
animais = ['leao', 'tigre', 'leopardo', 'onca', 'elefante', 'rinoceronte', 'crocodilo', 'golfinho', 'baleia', 
           'foca', 'orca', 'pinguim', 'gaviao', 'falcao', 'urubu', 'coruja']
tipo = int(input('===ASSUNTO DO JOGO===\n\n[1]FRUTAS\n[2]ANIMAIS\nESCOLHA O ASSUNTO: '))
while tipo != 1 and tipo != 2:
    tipo = int(input('===ASSUNTO DO JOGO===\n\n[1]FRUTAS\n[2]ANIMAIS\nESCOLHA O ASSUNTO: '))

if tipo == 1:
    opcao = frutas
elif tipo == 2:
    opcao = animais

palavra = random.choice(opcao)

dificuldade = int(input('\n===DIFICULDADE DO JOGO===\n\n[1]AMADOR(11 tentativas)\n[2]FACIL(10 tentativas)\
                        \n[3]INTERMEDIÁRIO(9 tentativas)\n[4]DIFÍCIL(8 tentativas)\
                        \n[5]IMPOSSÍVEL(7 tentativas)\n[6]HARDCORE(6 tentativas)\
                        \nESCOLHA A DIFICULDADE: '))
while dificuldade < 1 or dificuldade > 6:
    print('\nE R R O\nREINSIRA A DIFICULDADE!\n')
    dificuldade = int(input('\n===DIFICULDADE DO JOGO===\n\n[1]AMADOR(11 tentativas)\n[2]FACIL(10 tentativas)\
                        \n[3]INTERMEDIÁRIO(9 tentativas)\n[4]DIFÍCIL(8 tentativas)\
                        \n[5]IMPOSSÍVEL(7 tentativas)\n[6]HARDCORE(6 tentativas)\
                        \nESCOLHA A DIFICULDADE: '))
if dificuldade == 1:
    tent = 11
elif dificuldade == 2:
    tent = 10
elif dificuldade == 3:
    tent = 9
elif dificuldade == 4:
    tent = 8
elif dificuldade == 5:
    tent = 7
elif dificuldade == 6:
    tent = 6

palavra_oculta = '_'*len(palavra)

print('\n===JOGO INICIADO===\n')
max = tent
while tent > 0:
    print(f'Palavra: {palavra_oculta}\n')
    palpite = ''
    print(f'TENTATIVAS RESTANTES: {tent}')
    if tent == max:
        opcaoChute = 0
    else:
        opcaoChute = int(input('\n[0]DAR OUTRO PALPITE\n[1]TENTAR ACERTAR A PALAVRA (SE ERRAR É FIM DE JOGO)'))
        while opcaoChute != 0 and opcaoChute != 1:
            opcaoChute = int(input('\n\n==OPÇÃO INVÁLIDA==\n[0]DAR OUTRO PALPITE\n[1]TENTAR ACERTAR A PALAVRA (SE ERRAR É FIM DE JOGO)\nESCOLHA: '))

    if opcaoChute == 1:
        chute = input('PALPITE A PALAVRA, É AGORA OU NUNCA: ').lower()
        palavra_oculta = chute
        if palavra_oculta == palavra:
            print('PARABÉNS, VOCÊ ACERTOU!!!!')
            tent = 0
        else:
            print('GAME OVER! MELHORE')
            tent = 0

    elif opcaoChute == 0:
        palpite = input('DÊ UM PALPITE: ').lower()
        while len(palpite) > 1:
            palpite = input('===INSIRA APENAS UMA LETRA===\nDÊ UM PALPITE: ').lower()
        if palpite in palavra:
            nova = ''
            for i in range(len(palavra)):
                if palavra[i] == palpite:
                    nova += palpite
                elif palavra_oculta[i] != '_':
                    nova += palavra_oculta[i]
                else:
                    nova += '_'
            palavra_oculta = nova
                    
            print(f'A letra "{palpite}" está na palavra.')
        else:
            print(f'Infelizmente a palavra não contém a letra "{palpite}"')
        tent -= 1
        
        if palavra_oculta == palavra:
            print('PARABÉNS, VOCÊ ACERTOU!!!!')
            tent = 0
        elif palavra_oculta != palavra and tent == 0:
            print('GAME OVER! MELHORE')
