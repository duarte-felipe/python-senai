#1 
#como toda a aula esta aqui, importar math inteira é mais viavel 
import math

numero = float(input("Digite um número para calcular a raiz quadrada: "))

# calculando a raiz quadrada do número
raiz_quadrada = math.sqrt(numero)

# Exibe o resultado
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")

#2
numero = float(input("Digite um número: "))
raiz_quadrada = math.sqrt(numero)
raiz_quadrada_ceil = math.ceil(raiz_quadrada)
print(f"A raiz quadrada arredondada para cima é {raiz_quadrada_ceil}")

#3 
numero = float(input("Digite um número: "))
raiz_quadrada = math.sqrt(numero)
raiz_quadrada_floor = math.floor(raiz_quadrada)
print(f"A raiz quadrada arredondada para baixo é {raiz_quadrada_floor}")

#4 
numero = float(input("Digite um número real: "))
porcao_inteira = math.trunc(numero)
print(f"A porção inteira de {numero} é {porcao_inteira}")

#5
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")

#6
angulo = float(input("Digite um ângulo em graus: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")

#7
alunos = [input(f"Nome do aluno {i+1}: ") for i in range(4)]
escolhido = random.choice(alunos)
print(f"O aluno escolhido é {escolhido}")

#8
alunos = [input(f"Nome do aluno {i+1}: ") for i in range(4)]
random.shuffle(alunos)
print("Ordem de apresentação:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i}. {aluno}")
