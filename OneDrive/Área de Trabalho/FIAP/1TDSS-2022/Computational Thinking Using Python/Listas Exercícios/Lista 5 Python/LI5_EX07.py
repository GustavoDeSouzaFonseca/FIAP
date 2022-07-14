def validSameN():
    n1 = str(input('Digite um número inteiro: '))
    n2 = str(input('Digite o segundo número inteiro: '))
    print(n1[-2], n2[-2], n1[-1], n2[-1])
    if n1[-2] == n2[-2] and n1[-1] == n2[-1]:
    	print("Encaixa")
    else: 
        print('NÃO encaixa!')


def validSameNumber():
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite o segundo número inteiro: '))
    uN1 = n1 / 1 % 10
    dN1 = n1 / 10 % 10
    uN2 = n2 / 1 % 10
    dN2 = n2 / 10 % 10
    if uN1 == uN2 and dN1 == dN2:
        print("Encaixa")
    else: 
        print('NÃO encaixa!')
validSameNumber()