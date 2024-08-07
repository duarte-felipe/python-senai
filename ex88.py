#8
cont = 0 
for i in range(5):
    valor = int(input("Digite um valor : "))
    if(valor<0):
        cont +=1 

print("A quantidade de numeros negativos e {}".format(cont))