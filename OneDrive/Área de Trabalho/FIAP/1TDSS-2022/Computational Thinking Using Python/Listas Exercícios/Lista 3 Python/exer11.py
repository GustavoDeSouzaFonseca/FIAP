print("=====================<EXERCÍCIO 11>=====================")
preco = float(input("Informe o valor do produto: "))
escolha = int(input("Informe a forma de pagamento: "))

if escolha == 1:
    print("10% de desconto")
    print("valor: {:.2f}" .format(preco*0.9))
elif escolha == 2:
    print("5% de desconto")
    print("valor: {:.2f}" .format(preco * 0.95))
elif escolha == 3:
    print("2 vezes")
    print("valor: {:.2f}" .format(preco/2))
elif escolha == 4:
    print("4 vezes com juros de 7%")
    print("valor: {:.2f}" .format(preco * 1.07 / 4))
else:
    print("Você não escolheu uma forma de pagamento")