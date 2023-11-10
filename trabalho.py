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
