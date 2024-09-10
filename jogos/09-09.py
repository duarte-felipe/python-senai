import pygame
#Inicializando moulos pygame
pygame.init()
#Criando uma janela com o titulo "Ola Mundo"
janela = pygame.display.set_mode((400,300))
pygame.display.set_caption("Minha Tela")

deve_continuar = True
#loop do jogo
while deve_continuar:
# Checando eventos
    for event in pygame.event.get():
    #se for um evento QUIT 
        if event.type == pygame.QUIT:
            deve_continuar = False

#encerrando Pygame
pygame.quit() 

