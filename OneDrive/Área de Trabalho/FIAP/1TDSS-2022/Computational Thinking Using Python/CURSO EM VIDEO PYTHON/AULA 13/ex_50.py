#Desenvolva um programa que leia seis números inteiros e mostre a soma 
#apenas daqueles que forem pares. Se o valor digitado for impar desoconsidere-o.
s = 0
for c in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n%2 == 0:
        s += n
print(f'A soma entre os números pares digitados foi de {s}')
    