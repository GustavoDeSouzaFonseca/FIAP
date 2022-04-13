print("=====================<EXERCÍCIO 2>=====================")
team1 = str(input("Digite o nome do primeiro time: "))
g1 = int(input(f"Digite a quantidade de gols que {team1} marcou: "))
team2 = str(input("Digite o nome do segundo time: "))
g2 = int(input(f"Digite a quantidade de gols que {team2} marcou: "))

if g1 > g2:
    print(team1 ,"é o time vencedor!")
elif g1 < g2:
    print(team2 ,"é o time vencedor!")
else:
    print("EMPATE")