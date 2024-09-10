#penultima avaliaçao                                       TUPLA

#1. Crie uma tupla com 5 números inteiros.          #usei essa tupla pra outros ex
num = (10, 20, 30, 40, 50 )

#2. Acesse o primeiro elemento de uma tupla.
primeiro_num = num [0] 
#print(primeiro_num)  
print(num[0])  #ou assim tb 

#3. Acesse o último elemento de uma tupla.
print(num[4])  #tupla do ex 1 

#4. Acesse o terceiro elemento de uma tupla.
terceio_num = num [2] #tupla do x 1
print(terceio_num)

#5. Verifique o comprimento de uma tupla.
print(len(num)) #tupla do ex 1 

#6. Concatene duas tuplas. 
#duas tuplas
num1 = (100,200,300,400)
num2 = (500,600,700,800)
#concatenando duas tuplas
soma = num1+num2
#print da concatenaçao
print(soma)

#7. Repita uma tupla 3 vezes.
#upla
numeros = (10, 20, 30, 40, 50)
result = ()
#for para repetir a tupla
for _ in range(3):
    result += numeros
print(result)

#8. Conte quantas vezes um elemento aparece na tupla.
num0 = (10, 20, 30, 20, 50, 20)
valor = num0.count(20)
print(valor)

#9. Encontre o índice de um elemento específico na tupla.
elemento= 50
try: 
    indice = num0.index(elemento)
    print("o indice {} do elemento {}".format(indice, elemento))
except ValueError:
    print("Valor nao encontrado")

#10.Verifique se uma tupla está vazia.
tupla = () #tupla vazia 
#if para verificar se esta ou nao vazia 
if tupla:
    print("A tupla não está vazia." )
else:
    print("A tupla está vazia.")


 #                                                       LISTA 
#1. Crie uma lista com 5 números inteiros
listaa=[1,2,3,4,5]
print(listaa)

#2. Multiplique todos os elementos de uma lista de números.
print("Multiplique todos os elementos de uma lista de números")
from functools import reduce
import operator
# Usando reduce com uma função lambda q o jean ensinou 
resultado = reduce(lambda x, y: x * y, listaa) #print basico
print("A multiplicação dos elementos da lista 1 é: {}".format(resultado))

#3. Encontre o maior número em uma lista de números.
print("O maior numero da lista 1 é: {}".format(max(listaa)))

#4. Encontre o menor número em uma lista de números.
print("O maior numero da lista 1 é: {}".format(min(listaa)))

#5. Ordene uma lista de números em ordem crescente.
print("Ordene uma lista de números em ordem crescente")

lista_aleatoria=[1,69,400,90,-80,200,570,960,2,4,6,-2,-3]

print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada: {}".format(sorted(lista_aleatoria)))

#6. Ordene uma lista de números em ordem decrescente.
print("Lista : {}".format(lista_aleatoria))

print("Lista ordenada decrescente: {}".format(sorted(lista_aleatoria,reverse=True)))

#7. Inverta a ordem dos elementos em uma lista.
print("lista: {}".format(listaa))

# ira inverter a lista
listaa.reverse()

# Imprime a lista invertida
print("Lista invertida: {}".format(listaa))

#8. Crie uma cópia de uma lista.
copia= listaa.copy()

print("lista: {}".format(listaa))

print("Cópia da lista : {}".format(copia))

#9. Limpe todos os elementos de uma lista.
listaa.clear()
print("Lista vazia: {}".format(listaa))

                                                                   #DICIONARIO
#1. Crie um dicionário com 3 pares chave-valor de strings.
dicionario={"Nome":"Felipe","Cidade":"franca","Sexo":"masculino"}
print(dicionario)

#2. Acesse o valor de uma chave específica em um dicionário.
print("O Nome no dicio1: {}".format(dicionario["Nome"]))

#3. Adicione um novo par chave-valor a um dicionário.
dicionario["idade"]= 18

print(dicionario)

#4. Remova um par chave-valor de um dicionário usando a função pop.
removido=dicionario.pop("Cidade")

print("O valor de {} foi removido do dicionario {}".format(removido,dicionario))

#5. Verifique se uma chave específica está presente em um dicionário.
print("O chave nome está no diconario? {}".format("Nome"in dicionario))

print("O elemento cidade está no dicionario? {}".format('Cidade' in dicionario))

#6. Verifique se um valor específico está presente em um dicionário.
print("O nome Felipe está no dicionario? ")

print("Felipe" in dicionario.values())

#7. Conte quantos pares chave-valor um dicionário possui.
print("A quantidade de pares de chaves no dicionario é: {}".format(len(dicionario)))

#8. Copie um dicionário para outro.
print(dicionario)

print("Vou copiar o diconario! ")

dicio2= dicionario.copy()
print("O dicionario 2 é: {}".format(dicio2))