import pygame
from src.algebra_linear import calcular_posicao_absoluta

class Terreno:
    def __init__(self, tipo, grupo, bioma, numero, pos, tabueiro):
        self.tipo = tipo
        self.grupo = grupo
        self.bioma = bioma
        self.numero = numero
        self.pos = pos
        self.tabuleiro = tabueiro
        self.absolut_pos = calcular_posicao_absoluta(pos, tabueiro.dims, (540,800))
        self.carregar_imagem()

    def carregar_imagem(self):
        # Lógica para carregar a imagem do terreno com base no tipo e grupo
        self.imagem = pygame.image.load(f"imgs/{self.tipo}_{self.grupo}.png")


    def tick(self):
        # Lógica para atualizar o estado do terreno, se necessário
        pass


    def render(self, screen, camera):
        # Lógica para renderizar o terreno na tela



        camera.render(screen, self.imagem, self.absolut_pos)