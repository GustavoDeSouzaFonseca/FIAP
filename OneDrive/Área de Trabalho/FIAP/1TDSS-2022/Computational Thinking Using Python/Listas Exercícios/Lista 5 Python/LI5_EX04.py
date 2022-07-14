def primo():
    totalDividido = 0
    n = 2
    for c in range(2,101):
        if n % c == 0:
            totalDividido += 1
            
            print(totalDividido)
            n += 1
primo()