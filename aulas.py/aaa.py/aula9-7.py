def impar(n): 
    if n%3==0:
        impar= "e impar!"
        return impar
    else: 
        impar= "infelizmente nao e impar"
        return impar
n= int(input("Digite um numero para verificarmos se ele e impar! "))
print("O numero {} {}".format(n,impar(n)))