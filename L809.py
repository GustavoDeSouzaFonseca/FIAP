def interseccao(listaA, listaB):
    lista_resp = []

    for x in listaA:
        if x in listaB:
            lista_resp.append(x)

    return lista_resp

