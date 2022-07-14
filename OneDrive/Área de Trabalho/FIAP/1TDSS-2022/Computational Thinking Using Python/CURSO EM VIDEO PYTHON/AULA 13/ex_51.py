#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
#mostre os 10 primeiros termos dessa progressão.
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a = 0
for c in range(1, 11):
    a = n + (c-1) * r
    print(a)
