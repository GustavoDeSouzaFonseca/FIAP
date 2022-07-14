#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre
#quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de idade.
from datetime import date
atual = date.today().year
inicio = i = 1
totMaiorIdade = 0
totMenorIdade = 0
pessoa = 1
mort = 0
qnt = int(input('Digite a quantidade de pessoas que quer saber a maioridade ou menoridade. (+18//-18): '))

while qnt > 0 and i <= qnt:
    nasc = int(input(f'Digite a ano de nascimento da {pessoa}º pessoa: '))
    idade = atual - nasc
    pessoa += 1
    i += 1
    if idade >= 18 and idade <= 118: #if = se
        totMaiorIdade += 1
    elif idade >0 and idade <= 17: # se nao
        totMenorIdade += 1
    else: # resto
        mort += 1
while qnt <= 0:
    qnt = int(input('Você não digitou a quantidade necessária de pessoas! Digite novamente: '))
    while qnt > 0 and i <= qnt:
        nasc = int(input(f'Digite a ano de nascimento da {pessoa}º pessoa: '))
        idade = atual - nasc
        pessoa += 1
        i += 1
        if idade >= 18 and idade <= 118:
            totMaiorIdade += 1
        elif idade >0 and idade <= 17: 
            totMenorIdade += 1
        else:
            mort += 1
while qnt != int:
    qnt = int(input('Por favor insira os dados em números: '))
    while qnt > 0 and i <= qnt:
        nasc = int(input(f'Digite a ano de nascimento da {pessoa}º pessoa: '))
        idade = atual - nasc
        pessoa += 1
        i += 1
        if idade >= 18 and idade <= 118:
            totMaiorIdade += 1
        elif idade >0 and idade <= 17: 
            totMenorIdade += 1
        else:
            mort += 1
            
print(f'Existem {totMaiorIdade} maiores de idade') 
print(f'Existem {totMenorIdade} menores de idade.')
if mort != 0:
    print(f'Existem {mort} mortos!')