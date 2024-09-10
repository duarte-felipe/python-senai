#Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta
#quantos destes valores são negativos, escrevendo esta informação.

a= []
for i in range(1, 5):
    num = int( input("Digite um numero: "))
    a.append(num)
    if(num>0):
        print("O numero {} e positivo! ".format(num))
        
    else:
        print("O numero {} e negativo! ".format(num))