#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\33[34m', end='') #'\33[34m' Muda a cor para azul
        t += 1
    else:
        print('\33[m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {t} vezes.') #CONTRABARRA"N" (\n) QUEBRA A LINHA e '\33[M' Muda a cor para branco
if t == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')