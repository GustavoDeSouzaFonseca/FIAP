import random
def randNum():
    i = 0
    listaNum = []
    n = int(input('Digite a quantidade de números aleatórios que quer imprimir: '))
    while i < n:
        listaNum.insert(i, random.randint(1, 1001))
        i += 1
    print(listaNum)
randNum()