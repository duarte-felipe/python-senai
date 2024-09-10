#1. Escreva um programa que pergunte a velocidade de um carro. Caso 
#ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi muktado

#variavel pra velocidade do carro 
vel = float(input("Digite a velocidade: "))

#if e else falando sobre 80>
if vel >80:
    print("Voce foi multado! ")
    
else:
    print("Voce nao foi multado! ")
    

#2. Faça um programa que leia o ano de nascimento de uma pessoa,
#calcule a idade dela e depois mostre se ela pode ou não votar.

#variavel pra solicitar data de nascimento 
ano= int(input("Digite seu ano de nascimento: "))
#if e else fazendo as contas do ano 
if ano >= 16: 
    print("Voce pode votar! ")
    
else:
    print("Voce nao pode votar! ")
    
    
#3. Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule
#a sua média e mostre na tela. No final, analise a média e mostre se o aluno 
#teve ou não um bom aproveitamento (se ficou acima da média 7.0).

#variavel pras notas e nome do aluno
nome= input("Digite o nome do aluno: ")
nota1 = float(input("DIgite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#variavel para media 
media= (nota1+nota2) /2

#print e conclusao do ex parcialmente 
print(f"A media do aluno/a {nome} e de {media}")

#aproveitamento do aluno e agora sim conclusao total do ex
if media >= 7.0:
    print("Ele/a teve um bom aproveitamento! ")
else:
    print("Ele/a nao teve um bom apoveitamento! ")


#4. Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

#variavel para o usuario falar o numero
num= int(input("Digite um numero: "))

#if e else com % pra descobrir se o numero e divisivel ou nao por 2 (o numero par)
if num % 2== 0:
    print("O numero e e par. ")
else: 
    print("O numero impar. ")
    
#5. Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar
#descontos para todos, mas especialmente para mulheres. Faça um
#programa que leia nome, sexo e o valor das compras do cliente 
#e calcule o preço com desconto. Sabendo que:  
            #Homens ganham 5% de desconto
            #Mulheres ganham 13% de desconto

#variaveis ja nomeadas com str e float para nao ter erro com o python
nome = str(input("Nome: "))
sexo = str(input("DIgite seu sexo: Digite F ou M "))
valor = float(input("Valor das compras: "))


#if e else somando os descontos dos sexos 
if sexo.upper() == "M": 
    valor_desconto= valor-(valor*0.05)
elif sexo.upper() == "F": 
    valor_desconto = valor-(valor*0.13)
#else para nao ter erro com caracter
else:
    print("Caracter invalido.")

print("O/a {nome} teve o valor final com desconto de: {valor_desconto} ".format(nome) .format( valor_desconto))


#6. Faça um algoritmo que pergunte a distância que um passageiro deseja
#percorrer em Km, calcule o preço da passagem cobrando:
        #R$0.50 por Km para viagens até 200Km e
        #R$0.45 para viagens mais longas.

#leitura da distância solicitada
distancia = float(input("Digite a distância em Km: "))

#if e else com o Cálculo do preço da passagem
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

#print com o valor final
print(f"O preço da passagem é: R$ {preco:.2f}")



#7. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200

for num in range(100, 1, -1):
    if num % 2 != 0:
        print(num)


#8. Números ímpares até 20: Escreva um programa que imprima todos os
#números ímpares de 1 até 20 usando um loop while.

#inicia o número
numero = 1
#loop para imprimir números ímpares de 1 até 20
while numero <= 20:
    if numero % 2 != 0:
        print(numero)
    numero += 1


#9. Calcular Área de um Retângulo: Crie uma função que recebe a largura e a
#altura de um retângulo e retorna a sua área.
                #A= largura X altura

def calculo(largura, altura):
    area = (largura*altura)
    return area 


altura = float(input("Digite a altura: "))
largura= float(input("Digite a largura: "))
print("A altura do calculo foi {altura}, a largura do calculo foi {largura} e o resultaado de sua area e de: {}".format(altura*largura))




