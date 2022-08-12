from http.cookies import BaseCookie
from random import random


def cria_baralho():
    bar = []
    for naipe in ('♢', '♠', '♡', '♣'):
        for valor in range(1,14):
            c = (valor, naipe)
            bar.append(c)
    return bar

def comprar(deck):
    return deck.pop()

def distribui(qnt, deck):
    mao = []
    while qnt > 0:
        mao.append(comprar(deck))
        qnt = qnt - 1
    return mao

def embaralhar(deck):
    qnt = random.radiant(200, 1000)

    while qnt > 0:
        i = random.radiant(0,51)
        j = random.radiant(0,51)
        #trocando as cartas
        aux = deck[i]
        deck[i] = deck[j]
        deck[j] = aux
        qnt = qnt - 1

def soma_pontos(mao):
    soma = 0
    for c in mao:
        if c[0] > 10:
            soma = soma + 10
        else:
            soma = soma + c[0]
    return soma

    
    

baralho = cria_baralho()


humano = distribui(2, baralho)
cpu = distribui(2, baralho)

print(humano)

resp = input('Quer mais cartas (S/N) ???').upper
while resp == 'S':
    c = comprar(baralho)
    humano.append(c)
    print(humano)
    resp = input('Quer mais cartas (S/N) ???')

while soma_pontos(cpu) < 17:
    cpu.append(comprar(baralho))

print(cpu)

