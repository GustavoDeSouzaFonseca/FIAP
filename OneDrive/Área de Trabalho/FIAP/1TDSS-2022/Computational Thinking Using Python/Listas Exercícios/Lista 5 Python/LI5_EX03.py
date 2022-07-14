def primo():
    n = int(input('Digite um número para verificação primal: '))
    totalDividido = 0
    nPrimo = bool()
    for c in range(1, n + 1, 1):
        if n % c == 0:
            totalDividido += 1
    if totalDividido == 2:
        print(bool(True))
    else:
        print(bool(False))
        
primo()