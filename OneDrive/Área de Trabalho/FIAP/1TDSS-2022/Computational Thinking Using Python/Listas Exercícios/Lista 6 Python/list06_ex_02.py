frase = str(input('Digite uma frase: ')).strip()
frase2 = str(input('Digite o segundo número'))
for letra in range(len(frase)-1, len(frase), 1):
    print(frase[letra], end=' ')