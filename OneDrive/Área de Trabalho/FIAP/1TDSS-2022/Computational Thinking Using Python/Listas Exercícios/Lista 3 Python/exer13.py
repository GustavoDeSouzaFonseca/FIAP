print("=====================<EXERCÍCIO 13>=====================")
dia = int(input("Dia: "))
mes = int(input("Mês: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data inválida: ")
elif mes == 2 and dia > 28:
    print("Data inválida")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida")
else:
    print("Data válida")