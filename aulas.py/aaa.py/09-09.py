#ex 1
def verificar_numeros():
    num = input("Digite um número: ")
    
    # Verifica se a entrada é numérica
    if num.isnumeric():
        print("A entrada contém apenas números.")
    else:
        print("A entrada não contém apenas números.")

# Chamar a função
verificar_numeros()

#ex 2
def tudo_minuscula(var):
    if var.islower():
        return("A palavra esta em minuscula.")
    else:
        return("A palavra nao esta em minusucula.")
texto = input("Digite um texto: ")  
print(tudo_minuscula(texto))

#ex 3
def maiusucula(var):
    if var.isupper():
        return("A palavra esta em maiuscula.")
    else:
        return("A palavra nao esta em maiuscula.")
texto = input("Digite um texto: ")  
print(maiusucula(texto))

#ex 4
def letra(var):

    if var.startswhith(letraInicial):
        return("A sua palavra começa com a letra {}".format(var))
    else:
        return("A sua palavra nao começa com a letra {}".format(letraInicial))
verificaçao = input("Digite a letra: ")
palavra = input("Digite a palavra: ")

print(letra(palavra,verificaçao))

#ex5

def letraEspecifica(var):

    if var.endwith(letraInicial):
        return("A sua palavra começa com a letra {}".format(var))
    else:
        return("A sua palavra nao começa com a letra {}".format(letraInicial))
verificaçao = input("Digite a letra: ")
palavra = input("Digite a palavra: ")

print(letraEspecifica(palavra,verificaçao))

