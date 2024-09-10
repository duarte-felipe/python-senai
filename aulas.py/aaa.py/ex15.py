# Solicito a entrada da altura e do sexo
altura = float(input("Digite a altura (em metros): "))
sexo = int(input("Digite o sexo (1 para feminino, 2 para masculino): "))
# Calcula o peso ideal com base no sexo
if sexo == 1:  
    peso_ideal = (62.1 * altura) - 44.7
elif sexo == 2:  
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = None
    print("Sexo inválido Use 1 para feminino e 2 para masculino.")
# Imprime o resultado se o sexo for válido
if peso_ideal is not None:
    print(f"O peso ideal é: {peso_ideal:.2f} kg")
