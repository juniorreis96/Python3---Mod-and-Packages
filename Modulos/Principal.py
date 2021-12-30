"""(MODULOS-107) CRIAR UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES: AUMENTAR, DIMINUIR, DOBRO E METADE
IMPORTE ESSE MÓDULO E USE ESSAS FUNÇÕES."""

from UtilidadesCeV import moeda

n = int(input('Digite um número: '))

print(f'O número {n} com um acrescimo de 20% resulta em: {moeda.aumentar(n, 20, True)}')
print(f'O número {n} com uma diminuição de 20% resulta em: {moeda.diminuir(n, 20, True)}')
print(f'O número {n} tem como o dobro: {moeda.dobro(n, True)}')
print(f'O número {n} tem como metade: {moeda.metade(n, True)}')


"""(MODULOS-108) CRIAR UMA FUNÇÃO CHAMADA MOEDA() QUE CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIOS FORMATADO"""
from UtilidadesCeV import moeda


n = int(input('Digite um número: '))

print(f'O número {n} com um acrescimo de 20% resulta em: {moeda.moeda(moeda.aumentar(n, 20, True))}')
print(f'O número {n} com uma diminuição de 20% resulta em: {moeda.moeda(moeda.diminuir(n, 20, True))}')
print(f'O número {n} tem como o dobro: {moeda.moeda(moeda.dobro(n, True))}')
print(f'O número {n} tem como metade: {moeda.moeda(moeda.metade(n, True))}')


"""(MODULO-109) REPLICAR O EXERCICIO ANTERIOR COM UM PARÂMETRO OPCIONAL DE FORMATAR OU NÃO OS VALORES NÚMERICOS"""
from UtilidadesCeV import moeda
from time import sleep
n = int(input('Digite um número: '))
while True:
    qrmoeda = str(input('Deseja formatação? [S/N]: ')).upper().strip()
    if qrmoeda not in 'NS':
        print('Opção inválida!')
        print('-'*30)
        sleep(1.5)
    else:
        break

print(f'O acrescimo de 20% sobre o valor de {n} resulta em: {moeda.aumentar(n, 20, True if qrmoeda == "S" else False)}')
print(f'A diminuição de 20% sobre o valor {n} resulta em: {moeda.diminuir(n, 20, True if qrmoeda == "S" else False)}')
print(f'O dobro do valor {n} resulta em {moeda.dobro(n, True if qrmoeda == "S" else False)}')
print(f'A metade do valor {n} resulta em {moeda.metade(n, True if qrmoeda == "S" else False)}')

"""(MODULOS-110) ADICIONE AO MODULO MOEDA A FUNÇÃO RESUMO QUE TRÁS OS VALORES EM TABELAS ORGANIZADAS."""
from UtilidadesCeV import moeda
from time import sleep
n = float(input('Digite um valor: R$'))
valoracrescido = float(input('Qual o percentual a ser acrescido: '))
valordecrescido = float(input('Qual o percentual a ser decrescido: '))
while True:
    qrmoeda = str(input('Gostaria de conversão [S/N]: ')).upper().strip()
    if qrmoeda not in 'NS':
        print('-'*30)
        print('Você digitou uma opção inválida!')
        print('-'*30)
        sleep(1.5)
    else:
        break

moeda.resumo(n, valoracrescido, valordecrescido, True if qrmoeda == 'S' else False)


"""(MODULOS-111) CRIAR MODULOS INTERNOS CHAMADOS MOEDA E DADO. TRANSFERIR TODAS AS FUNÇÕES UTILIZADOS NOS DESAFIOS 
107, 108 E 109 PARA O PRIMEIRO PACOTE E MANTENHA TUDO FUNCIONANDO"""


"""(MODULOS-112) NO MODULO CHAMADO DADO. CRIAR UMA FUNÇÃO CHAMADA LeiaDinheiro() QUE SEJA CAPAZ DE FUNCIONAR COMO A
FUNÇÃO INPUT(), MAS COM UMA VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES MONETÁRIOS. E SE O VALOR FOR DIGITADO COM
VIRGULA ELE DEVE SER ACEITO DA MESMA FORMA."""
from UtilidadesCeV import moeda
from UtilidadesCeV import validadados


from time import sleep
n = validadados.lerdinheiro('Digite um valor: R$')

valoracrescido = float(input('Qual o percentual a ser acrescido: '))
valordecrescido = float(input('Qual o percentual a ser decrescido: '))

while True:
    qrmoeda = str(input('Gostaria de conversão [S/N]: ')).upper().strip()
    if qrmoeda not in 'NS':
        print('-'*30)
        print('Você digitou uma opção inválida!')
        print('-'*30)
        sleep(1.5)
    else:
        break

moeda.resumo(n, valoracrescido, valordecrescido, True if qrmoeda == 'S' else False)
