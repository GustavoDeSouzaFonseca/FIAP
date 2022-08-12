def imprime_result(campeao, lista):
    for pais in lista:
        if pais != campeao:
            print(campeao, "x" ,pais)

paises = ["Argentina", "Bélgica", "Brasil",
 "Colômbia", "Costa Rica", "França",
  "Holanda","Alemanha"]


for champion in paises:
    imprime_result(champion, paises)