print('=' * 100)
print('{:^100}'.format('CURSO PYTHON AULA 6'))
print('=' * 100)

dia = int(input('Digite por quantos dias alugou seu carro: '))
km = float(input('Quantos km você percorreu? '))

vdia = dia * 60
vkm = km * 0.15
vtotal = vdia + vkm

print('O valor total é de', vtotal)

print('=' * 100)
print('{:^100}'.format('Volte Sempre'))