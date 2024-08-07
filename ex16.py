import math

lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm): "))

if lados == 3:
    area = (math.sqrt(3) / 4) * (medida_lado ** 2)
    print(f"TRIÂNGULO")
    print(f"Área: {area:.2f} cm²")
elif lados == 4:
    area = medida_lado ** 2
    print(f"QUADRADO")
    print(f"Área: {area:.2f} cm²")
elif lados == 5:
    print(f"PENTÁGONO")
else:
    print("Número de lados não suportado para os cálculos.")
