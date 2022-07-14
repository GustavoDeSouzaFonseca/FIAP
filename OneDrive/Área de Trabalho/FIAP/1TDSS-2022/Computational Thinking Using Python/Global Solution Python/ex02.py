melhorAval = 0
nmMelhorAval = ''
totAval = 0
empate = ''
algAval = 0
while True:
    nmProd = str(input('Digite o nome do produto: ')).strip().upper()
    aval = int(input('Digite a quantidade de estrelas que esse produto tem entre 1 e 5: '))
    totAval += 1
    while aval < 1 or aval > 5:
        aval = int(input('Digite a quantidade de estrelas que esse produto tem ENTRE 1 e 5: '))
    if nmProd == 'FINAL' and aval == 0:
        break
    if aval == 1:
        melhorAval = aval
        nmMelhorAval = nmProd
    if aval > melhorAval:
        melhorAval = aval
        nmMelhorAval = nmProd
    if aval == melhorAval:
        algAval += 1
        empate = nmProd + ' e ' + nmMelhorAval
if algAval > 0:
    print(f'Houve um empate entre {empate}')
else:
    print(f'O produto mais bem avaliado foi {nmMelhorAval}')