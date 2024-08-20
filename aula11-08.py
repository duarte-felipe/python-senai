#1

# Cria um arquivo vazio chamado 'exercicio1.txt'
with open('exercicio1.txt', 'w') as file:
    pass

#2 

# Define a mensagem a ser escrita
mensagem = "Estou aprendendo Python!"
# abre (ou cria) o arquivo 'mensagem.txt' e escreve a mensagem nele
with open('mensagem.txt', 'w') as file:
    file.write(mensagem)

#3 

# Define as linhas de texto
linhas = [
    "Primeira linha de texto.",
    "Segunda linha de texto.",
    "Terceira linha de texto."
]
# Abre (ou cria) o arquivo 'notas.txt' e escreve as linhas nele
with open('notas.txt', 'w') as file:
    for linha in linhas:
        file.write(linha + '\n')

#4 

# Abre (ou cria) o arquivo 'numeros.txt' em modo de escrita
with open('numeros.txt', 'w') as file:
    # Escreve os números de 1 a 10, um por linha
    for numero in range(1, 11):
        file.write(f"{numero}\n")

#5 

# Abre o arquivo 'exercicio1.txt' em modo de leitura
with open('exercicio1.txt', 'r') as file:
    # Lê e exibe o conteúdo do arquivo
    conteudo = file.read()
    print(conteudo)

#aiaiaiai