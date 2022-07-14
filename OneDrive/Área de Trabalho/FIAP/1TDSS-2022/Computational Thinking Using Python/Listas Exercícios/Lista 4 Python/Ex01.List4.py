n = int(input('digite a quantidade n: '))
i = 1
soma = 0
while i <= n:
    if i == n:
        num = 0
        break
    num = int(input(f'digite {i}º número: '))

    if num % 2 == 0:
        soma += num
        print(soma)
    
    i += 1 
