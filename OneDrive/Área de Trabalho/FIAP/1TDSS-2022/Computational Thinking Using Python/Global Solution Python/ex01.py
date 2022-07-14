qntMeses = int(input('Digite a quantidade de meses: '))
i = 1
totMes = 1
ftTotal = 0
while i <= qntMeses:
    ftMensal = float(input(f'Digite a fatura mensal do {totMes}º mês: '))
    ftTotal += ftMensal
    totMes += 1
    i += 1
medFat = ftTotal/qntMeses
print(medFat)
