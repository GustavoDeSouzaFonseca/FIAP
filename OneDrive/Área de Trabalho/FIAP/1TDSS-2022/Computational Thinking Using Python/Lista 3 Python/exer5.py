print("=====================<EXERCÍCIO 5>=====================")
diaU = int(input("Digite a quantidade de dias úteis do mês: "))
hrTrab = int(input("Digite a quantidade de horas trabalhadas: "))
mph = int(input("Digite o seu valor-hora: "))

salFinal = hrTrab * mph
JornadaMensalExigida = diaU * 8

if hrTrab > JornadaMensalExigida:
    hrextra = (hrTrab - JornadaMensalExigida) * mph
    print("Seu valor de horas extra é", hrextra,"e o salário de ", salFinal)
elif hrTrab < JornadaMensalExigida:
    print("Você não completou suas horas. Seu salário é ", salFinal)
else:
    print("Seu salário foi de ", salFinal)