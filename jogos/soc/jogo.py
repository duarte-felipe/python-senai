#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pathlib import Path

# Diretório atual
DIRETORIO_ATUAL = str(Path(__file__).parent.absolute())

# Inicializar Pygame
pygame.init()

# Configurações da tela
tela = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Jogo com Sonic")

# Configurar o relógio
clock = pygame.time.Clock()

# Carregar imagens e música
sonic = pygame.image.load(Path(DIRETORIO_ATUAL) / 'imagens' / 'mario-f.png')
fundo = pygame.image.load(Path(DIRETORIO_ATUAL) / 'imagens' / 'green-hills.png')
pygame.mixer.init()
pygame.mixer.music.load(Path(DIRETORIO_ATUAL) / 'musicas' / 'musica1.wav')
pygame.mixer.music.play(-1)  # Reproduzir música em loop

# Configurações do personagem
sonic_x, sonic_y = 100, 350
sonic_speed = 5
jump_speed = -15  # Velocidade inicial do pulo
gravity = 1  # Força da gravidade
velocity_y = 0  # Velocidade vertical
is_jumping = False  # Estado de pulo

# Configurações da hit box
hitbox = pygame.Rect(sonic_x, sonic_y, sonic.get_width(), sonic.get_height())
hitbox_color = (0, 0, 0)

# Definir o retângulo do chão
chao_y = 500
chao = pygame.Rect(0, chao_y, 800, 100)  # (x, y, largura, altura)

def handle_movement(keys):
    global sonic_x, sonic_y, velocity_y, is_jumping, hitbox

    if keys[pygame.K_LEFT]:
        sonic_x -= sonic_speed
    if keys[pygame.K_RIGHT]:
        sonic_x += sonic_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = jump_speed
        is_jumping = True

    # Aplicar gravidade
    velocity_y += gravity
    sonic_y += velocity_y

    # Atualizar a hit box com a nova posição
    hitbox.topleft = (sonic_x, sonic_y)

    # Verificar colisão com o chão
    if hitbox.colliderect(chao) and hitbox.bottom > chao.top:
        sonic_y = chao.top - hitbox.height
        velocity_y = 0
        is_jumping = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    handle_movement(keys)

    # Desenhar o fundo
    tela.blit(fundo, (0, 0))

    # Desenhar o personagem
    tela.blit(sonic, (sonic_x, sonic_y))

    # Desenhar o chão para visualização (opcional)
    #pygame.draw.rect(tela, (0, 0, 0), chao)

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)
