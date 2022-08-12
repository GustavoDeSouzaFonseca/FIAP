def insere_ordenado(x, lista):
    i=0
    while i < len(lista) and lista[i] < x:
        i += 1

    lista.insert(i,x)

colecao = [4, 7, 10, 23, 45, 56, 56, 89, 90]
insere_ordenado(895, colecao)
print(colecao)