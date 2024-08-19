lista= [10,20,30,40]

valor = int(input("Digite oque procura aqui: "))

res = valor in lista 

if res== True: 
    print("O que voce procura   {}  esta na lista {}".format(valor, lista))
else:
    print("O que voce procura   {}  nao esta na lista{}".format(valor, lista))