#for c in range
for c in range(0,7,2):
    print(c)
print('='*50)
print('{:^50}'.format('FIM'))
print('='*50)

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print (c)
print('='*50)
print('{:^50}'.format('FIM'))
print('='*50)

for c in range(6, 0, -1):
    print(c)
print('='*50)
print('{:^50}'.format('FIM'))
print('='*50)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): #range de (NUMERO DE INICIO/ FIM + 1 PARA CONTABILIZAR O ULTIMO/ DA FORMA DE PASSO EM PASSO 'P')
    print(c)
print('='*50)
print('{:^50}'.format('FIM'))
print('='*50)