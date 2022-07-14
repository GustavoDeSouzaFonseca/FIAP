#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Digite sua frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) - 1, -1 ,-1):
    inverso += juntar[letra]
print(juntar, inverso)
if juntar == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')