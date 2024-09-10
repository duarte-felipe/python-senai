#1 dicionario vazio 
vazio= {}
#print(vazio)

#2 verificar 3 valores
dicionario = {"Felipe", 22, "Segunda-feira"}
# print(dicionario)

#3 verificar um valor especifico
nomes = {"Nome": ["Felipe","Laura","Sara","Adam", "Felipe Jr"]}
true = input("Diga um nome: ")

if true in nomes ["Nome"]:
    print(f"O nome {true} esta no dicionario. ")
else:
   print(f"O nome {true} nao esta no dicionario ") 

#4 adicionar ao dicionario
informacao = {
    "Nome": "Felipe Duarte",
    "Ocupacao": "Jogar GTA"  # Corrigindo a acentuação
}

# Adicionando mais informações e exibindo o dicionário
print("Dicionário inicial:", informacao)

# Atualizando a informação
informacao["Ocupacao"] = "Programador"

# Exibindo o dicionário após a atualização
print("Dicionário após atualização:", informacao)



#5 deletar do dicionario
meu_dicionario = {
    'nome': 'Alice',
    'idade': 10,
    'cidade': 'Franca'
}

print("Dicionário antes de apagar o valor:", meu_dicionario)
# Apagando o valor associado à chave 'idade'
del meu_dicionario['idade']

print("Dicionário depois de apagar o valor:", meu_dicionario)

#6 
num = {"Datas": ['20-11', '03-05', '31-05']}
true = input("Diga uma data: ")

if true in num ["Datas"]:
    print(f"Essa data '{true}' esta no dicionario. ")
else:
   print(f"Essa data '{true}' nao esta no dicionario. ") 
