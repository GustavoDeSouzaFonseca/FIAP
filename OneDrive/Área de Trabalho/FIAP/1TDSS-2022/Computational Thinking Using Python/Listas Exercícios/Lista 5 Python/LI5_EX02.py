def primo():
    n = int(input('Digite um número para verificação primal: '))
    totalDividido = 0
    for c in range(1, n + 1, 1):
        if n % c == 0:
            print('\33[34m', end='')
            totalDividido += 1
        else:
            print('\33[m', end='')
        print(c, end=' ')
    if totalDividido == 2:
        print('\n\33[mO número É PRIMO')
    else:
        print('\n\33[mO número NÃO é primo')
        
primo()