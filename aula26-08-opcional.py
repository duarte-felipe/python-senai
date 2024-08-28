# aprendendo dicionario       fazendo print pra abrir o dicionario 

#dicionario com ID
pessoa = {"NOME": "Felipe", "IDADE": 22, "FILHOS": ["Sara, Felipe jr, Adam"]}
#dicionario com marca de carro 
carro = {"MARCA": "Chevrolet", ", MODELO": "Tracker", "ANO": 2023}

#meu primeoro dicionario
meu_carro = {"MARCA": "Honda", ", MODELO": "Civic", "ANO": 2020}
print(meu_carro)

#podutos para Ecomerce
produtos = [
    {'id':'0305', 'tipo': 'forno', 'ano': 2020 },
     {'id':'2011', 'tipo': 'celular', 'ano': 2024 },
      {'id':'0320', 'tipo': 'geladeira', 'ano': 2022 },
#precisa de print para abrir o dicionario (duvida desse)
]
print(produtos)

#dicionario vazio
listaTelefonica = {"Franca": 16, "Batatais": 20}

print(listaTelefonica)

vazio = {}

print(vazio)


#dicionario vazio pra colocar novas informaçoes
#a variavel começa com o dicionario vazio
informaçao = {} #dicionario vazio

#chamando a variavel do dicionario e colocando [bla bla]=  e a informaçao fora "meu nome"
informaçao["Nome"] = "Felipe Duarte"

informaçao["Ocupaçao"] = "Jogar GTA "
#mais informaçao e  print pa funcionar
print(informaçao)
#ele troca as informaçoes do mesmo chamando dnv
informaçao["Ocupaçao"] = "Programador"
print(informaçao)


#dicionario pra identificar se tem ou nao um pais dentro  do codigo
#diferente do que foi pedido mas mais complexo
capitais = {"BRASIL": 'Brasilia', "JAPAO": 'Toquio', #vaiavel pra paises e capitais
    "ALEMANHA": 'Berlim', "ESTADOS UNIDOS": 'Washington, D.C.',  "FRANÇA": 'Paris', "REINO UNIDO": 'Londres',
    "CANADA": 'Ottawa', "AUSTRALIA": 'Camberra',  "ITALIA": 'Roma', "ESPANHA": 'Madri',   "CHINA": 'Pequim', "INDIA": 'Nova Délhi',  "RUSSIA": 'Moscovo',
    "AFRICA DO SUL": 'Pretória', "MEXICO": 'Cidade do México',  "ARGENTINA": 'Buenos Aires',  "CHILE": 'Santiago', "COLÔMBIA": 'Bogotá',  "PERU": 'Lima',
    "VENEZUELA": 'Caracas', "PAQUISTÃO": 'Islamabad', "INDONÉSIA": 'Jacarta', "TAILÂNDIA": 'Bangkok', "NIGÉRIA": 'Abuja',  "ETIÓPIA": 'Addis Abeba'
}
pais = input("Qual pais voce deseja saber? ") #input pro usuario solicitar um pai

if pais.upper() in capitais:    #if e else basico 
    capital = capitais[pais.upper()]
    print(f"A capital de {pais} é {capital}.")
else:
    print("A esse pais nao foi encontrado no dicionario".format(pais)) 

                #para apagar algo dentro do dicionario como Brasil é 
               #del capitais[BRASIL]

#exercicos de teste

# from sys import exit 
