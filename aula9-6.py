def par(n): 
    if n%2==0:
        par= "e par!"
        return par
    else: 
        par= "infelizmente nao e par"
        return par
n= int(input("Digite um numero para verificarmos se ele e par! "))
print("O numero {} {}".format(n,par(n)))