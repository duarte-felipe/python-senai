#Entrada de dados 
angulo1 = float(input("Digite o valor do primeiro ângulo (em graus): "))
angulo2 = float(input("Digite o valor do segundo ângulo (em graus): "))
angulo3 = float(input("Digite o valor do terceiro ângulo (em graus): "))
# Verificar o tipo do triângulo
if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Triângulo Retângulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Triângulo Obtusângulo")
else:
    print("Triângulo Acutângulo")
