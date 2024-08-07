qnt = int(input("Digite o número de maçãs: "))
preco = 0.30 if qnt< 12 else 0.25
total = qnt * preco
print(f"Valor total da compra: R$ {total:.2f}")
