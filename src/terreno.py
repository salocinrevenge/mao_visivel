import pygame
from src.algebra_linear import obter_posicao_relativa_absoluta

class Terreno:
    def __init__(self, tipo, grupo, bioma, numero, pos, tabueiro, escala):
        self.tipo = tipo
        self.grupo = grupo
        self.bioma = bioma
        self.numero = numero
        self.pos = pos
        self.tabuleiro = tabueiro
        self.escala = escala  # Escala para reduzir o tamanho da imagem
        self.pos_2d = obter_posicao_relativa_absoluta(pos, tabueiro.dims)
        self.espelhar = True
        if self.pos_2d[1] == 0 or self.pos_2d[1] == tabueiro.dims[1]-1:
            self.espelhar = False
        self.carregar_imagem()

    def carregar_imagem(self):
        # Lógica para carregar a imagem do terreno com base no tipo e grupo
        # print(f"Carregando imagem: imgs/{self.tipo}_{self.grupo}.png")
        # self.imagem = pygame.image.load(f"imgs/{self.tipo}_{self.grupo}.png")


        self.imagem = pygame.image.load(f"imgs/bases/new_base.png")
        original_size = self.imagem.get_size()
        self.dim = [original_size[0] * self.escala, original_size[1] * self.escala]

        self.imagem = pygame.transform.scale(self.imagem, self.dim)
        if self.espelhar:
            self.imagem = pygame.transform.flip(self.imagem, True, False)



    def tick(self):
        # Lógica para atualizar o estado do terreno, se necessário
        pass


    def render(self, screen, camera):
        # Lógica para renderizar o terreno na tela



        camera.render(screen, self.imagem, self.pos_2d)