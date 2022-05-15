cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;30;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;30m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'
         }

nome = 9

print('{}'.format(cores['ciano'], nome , cores['amarelo em negrito']))
print('='*100)
print('{}'.format(cores['roxo em negrito'], nome , cores['amarelo em negrito']))
print('{:^100}'.format("Exercício de Cores"))
print('{}'.format(cores['ciano'], nome , cores['amarelo em negrito']))
print('='*100)

print('{}'.format(cores['roxo em negrito'], nome , cores['amarelo em negrito']))
print('Boa Noite! digite uma cor para utilizar.')
cor = input('Dentre elas: Vermelho, Azul, Amarelo, Branco, Roxo, Verde, Ciano, Preto e Branco : ')
if cor == "Vermelho" or cor == "vermelho":
    print('{}'.format(cores['vermelho'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para vermelho!')
elif cor == "Azul" or cor == "azul":
    print('{}'.format(cores['azul'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para azul!')
elif cor == "Amarelo" or cor == "amarelo":
    print('{}'.format(cores['amarelo'], nome , cores['limpa']))
    print('Você mudou sua cor para amarelo!')
elif cor == "Branco" or cor == "branco":
    print('{}'.format(cores['branco'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para Branco!')
elif cor == "Roxo" or cor == "roxo":
    print('{}'.format(cores['roxo'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para roxo!')
elif cor == "Verde" or cor == "verde":
    print('{}'.format(cores['verde'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para Verde!')
elif cor == "Ciano" or cor == "ciano":
    print('{}'.format(cores['ciano'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para Ciano!')
elif cor == "Preto e Branco" or cor == "preto e branco":
    print('{}'.format(cores['preto e branco'], nome , cores['amarelo em negrito']))
    print('Você mudou sua cor para Preto e Branco!')
else:
    print('Não selecionou uma cor válida!')

print('='*100)
print('{:^100}'.format('Descobrir MMC de dois números'))
print('='*100)

def divisao(a, b):
    return a // b, a % b

def mmc(a, b):
    multiplo = a
    while multiplo % a != 0 or multiplo % b != 0:
        multiplo = multiplo + 1

    return multiplo

print(mmc(28, 16))