import random

def embaralhar(deck):
    qtd = random.randint(200, 1000)
    while qtd > 0:
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        #trocando as cartas
        aux = deck[i]
        deck[i] = deck[j]
        deck[j] = aux
        qtd = qtd - 1   

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

def soma_pontos(mao):
    soma = 0
    for c in mao:
        if c[0] > 10:
            soma = soma + 10
        else:
            soma = soma + c[0]
    return soma

baralho = cria_baralho()
embaralhar(baralho)

humano = distribui(2, baralho)
cpu = distribui(2, baralho)

print('='*30)
print('{:^30}'.format('SUA VEZ'))
print('='*30)
print('')
print(humano)
resp = input('Quer mais cartas (S/N) ???').upper()
while resp == 'S':
    c = comprar(baralho)
    humano.append(c)
    print(humano)
    resp = input('Quer mais cartas (S/N) ???').upper()


if resp == 'N':
    print('_'*30)
    print('{:^30}'.format('SOMA TOTAL: ', soma_pontos(humano)))

while soma_pontos(cpu) < 17:
    cpu.append(comprar(baralho))

print('='*30)
print('{:^30}'.format('VEZ DO COMPUTADOR'))
print('='*30)
print('')
print(cpu)

