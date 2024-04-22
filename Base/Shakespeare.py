# pip install pygame
import pygame
import sys
from cobrinha import Cobra
from comida import Comida
import time

# iniciar fonte
pygame.font.init()
minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)

# inicializar o pygame
pygame.init()
TAM_TELA = (300,400)
tela = pygame.display.set_mode(TAM_TELA)

# cronômetro | tempo
tempo = pygame.time.Clock()

pontuacao = 0

cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao

# inicia o loop do jogo
while True:

    tela.fill((7,0,35)) # RGB - Red, Green, Blue - (255,255,255)

    for event in pygame.event.get():
        # listener - mouse ou teclado
        if event.type == pygame.QUIT:
            # interrompe pygame
            pygame.quit()
            # fechar script (janela)
            sys.exit()
   #texto da pontuacao
    pontos = minha_fonte.render(f'Pontuação:{pontuacao}',True (255,255,255))
    tela.blit(pontos, (10,10))
    # desenha cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255,204,0),
                               # esquerda, cima, largura, altura
                               pygame.Rect(pos[0], pos[1], 10, 10))

    # desenha comida
    pygame.draw.rect(tela, pygame.Color(255,0,0),
                     pygame.Rect(posicao_comida[0],posicao_comida[1],10,10))

    # atualiza a tela a cada frame
    pygame.display.update()

    # FPS - Frames por Segundo
    tempo.tick(20)

# class comida

import random

class Comida:
    def __init__(self, tam_tela=(300,400)):
        self.tam_tela = tam_tela
        self.posicao = [random.randrange(10,self.tam_tela[0],10),
                       random.randrange(10,self.tam_tela[1],10)]
        self.devorada = False

    def gera_nova_comida(self):
        if self.devorada:
            self.posicao = [random.randrange(10,self.tam_tela[0],10),
                           random.randrange(10,self.tam_tela[1],10)]
            self.devorada = False
        return self.posicao


# class Cobra



class Cobra:
    def __init__(self, tam_tela=(300,400),
                        posicao=[80,50],# [esquerda, cima]
                        corpo=[[80,50],[70,50],[60,50]],
                        direcao = 'DIREITA'):
        self.tam_tela = tam_tela
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = direcao

    def muda_direcao(self, nova_direcao):
        if nova_direcao == 'DIREITA' and not self.direcao == 'ESQUERDA':
            self.direcao = 'DIREITA'
        if nova_direcao == 'ESQUERDA' and not self.direcao == 'DIREITA':
            self.direcao = 'ESQUERDA'
        if nova_direcao == 'CIMA' and not self.direcao == 'BAIXO':
            self.direcao = 'CIMA'
        if nova_direcao == 'BAIXO' and not self.direcao == 'CIMA':
            self.direcao = 'BAIXO'

    def move(self, posicao_comida):
        if self.direcao == 'DIREITA':
            self.posicao[0] += 10
        if self.direcao == 'ESQUERDA':
            self.posicao[0] -= 10
        if self.direcao == 'CIMA':
            self.posicao[1] -= 10
        if self.direcao == 'BAIXO':
            self.posicao[1] += 10

        # adiciona pedaço do corpo da cobra na frente da cabeça
        self.corpo.insert(0, list(self.posicao))
        # confere se comeu comida
        if self.posicao == posicao_comida:
            return True
        # remove pedaço da cauda
        self.corpo.pop()
        return False

    def verifica_colisao(self):
        # posicao => [esquerda, cima]
        # tam_tela => [largura, altura]

        # se dist_esquerda > tam_tela_horizontal ou se a dist_esquerda < 0
        if self.posicao[0] > (self.tam_tela[0]-10) or self.posicao[0] < 0:
            return True 