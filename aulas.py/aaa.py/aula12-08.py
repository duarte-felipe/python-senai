#opcional 1 
frutas = ("Banana", "Maça")
print(frutas)

carne = ("Peixe", "Alcatra")
print(carne)



comidas = frutas+ carne
print(comidas)

vegetais = ("Abobrinha", "Pepino")
print(vegetais)

#opcional 2 

lanche = ('Thomas', 'Pao','alface')

print(lanche)
print(lanche [1])
print(lanche [2])
print(lanche [-2])

#ignora o ultimo elemeno (fatiamento)
print(lanche[:2])

lanche= ('Tomate', 'Pao', 'Alface')

for i in lanche:
    print(f"Eu comi {i}")
    
print(len(lanche))

#opcional 3 

pessoa = ("Laura", 33 , 'M', 80)

del(pessoa)

#1 

tuplaVazia = ()
print(tuplaVazia)

#2

numeros = (1, 2, 3, 4, 5)
print(numeros)

#3

tuplaStrings = ("maçã", "banana", "cereja")

#4

tuplaMista = (42, "Python", 3.14, "aloooo")

#5

tupla = ("a", "b", "c")
prim_elemento = tupla [0]
print(prim_elemento)  # Isso irá imprimir: 'a'

#6

tupla_exemplo = (10, 20, 30)
ultimo_elemento = tupla_exemplo[-1]
print(ultimo_elemento)  # Isso irá imprimir: 30

#7

tupla_exemplo = ("a", "b", "c", "d")
terceiro_elemento = tupla_exemplo[2]
print(terceiro_elemento)  # Isso irá imprimir: 'c'

#8

tupla_exemplo = (1, 2, 3, 4)
comprimento = len(tupla_exemplo)
print(comprimento)  # Isso irá imprimir: 4


#9

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Isso irá imprimir: (1, 2, 3, 4, 5, 6)

#10

tupla_exemplo = ("a", "b")
tupla_repetida = tupla_exemplo * 3
print(tupla_repetida)  # Isso irá imprimir: ('a', 'b', 'a', 'b', 'a', 'b')

#11

# criando a tupla
minha_tupla = (1, 2, 3, 4, 5)

# Verificando se o elemento 3 está na tupla
elemento = 3
presente = elemento in minha_tupla

print(presente)  # Saída

#12

# Definindo uma tupla
minha_tupla = (1, 2, 3, 4, 2, 2, 5, 6)

# Elemento que queremos contar
elemento = 2

# Contando o número de vezes que o elemento aparece na tupla
quantidade = minha_tupla.count(elemento)

print(f"O elemento {elemento} aparece {quantidade} vezes na tupla.")

#13

# Definindo uma tupla
minha_tupla = (10, 20, 30, 40, 50)

# Elemento que queremos encontrar
elemento = 30

# Encontrando o índice do elemento
indice = minha_tupla.index(elemento)

print(f"O elemento {elemento} está no índice {indice}.")

#14

# Definindo uma tupla
minha_tupla = ()

# Verificando se a tupla está vazia
if not minha_tupla:
    print("A tupla está vazia.")
else:
    print("A tupla não está vazia.")

