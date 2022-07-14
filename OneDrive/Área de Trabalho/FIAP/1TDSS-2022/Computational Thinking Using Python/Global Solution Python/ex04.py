def qntDigiCODEbar():
    codeBar = str(input('Digite o código: ')).upper().strip()
    while len(codeBar) != 15:
        codeBar = str(input('Digite o código: ')).upper().strip()
    codeBar.count('1')
    codeBar.count('2')
    codeBar.count('3')
    codeBar.count('4')
    codeBar.count('5')
    codeBar.count('6')
    codeBar.count('7')
    codeBar.count('8')
    codeBar.count('9')
    codeBar.count('0')
    totNum = codeBar.count('1') + codeBar.count('2') + codeBar.count('3') + codeBar.count('4') + codeBar.count('5') + codeBar.count('6') + codeBar.count('7') + codeBar.count('8') + codeBar.count('9') + codeBar.count('0')
    if totNum != 8:
        print(f'O {codeBar} não é um código válido por NÃO conter 8 dígitos')
    else:
        print(f'o {codeBar} é um código de barras válido por conter {totNum} dígitos e 7 caracteres!')
qntDigiCODEbar()

