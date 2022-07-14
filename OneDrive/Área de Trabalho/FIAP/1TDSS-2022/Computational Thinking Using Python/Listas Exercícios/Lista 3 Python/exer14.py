print("=====================<EXERCÍCIO 14>=====================")

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data inválida: ")
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and mês == 2 and dia == 29:
    print("Data válida")
elif mes == 2 and dia > 28:
    print("Data inválida")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida")
else:
    print("Data válida")