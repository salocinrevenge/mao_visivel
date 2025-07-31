import pygame
from src.algebra_linear import calcular_posicao_absoluta, obter_posicao_relativa_absoluta

class Terreno:
    def __init__(self, tipo, grupo, bioma, numero, pos, tabueiro):
        self.tipo = tipo
        self.grupo = grupo
        self.bioma = bioma
        self.numero = numero
        self.pos = pos
        self.tabuleiro = tabueiro
        self.escala = 0.22  # Escala para reduzir o tamanho da imagem
        self.pos_2d = obter_posicao_relativa_absoluta(pos, tabueiro.dims)
        self.rotacionar = True
        if self.pos_2d[1] == 0 or self.pos_2d[1] == tabueiro.dims[1]-1:
            self.rotacionar = False
        self.dim = (540*self.escala ,800*self.escala)
        self.carregar_imagem()
        self.absolut_pos = calcular_posicao_absoluta(self.pos_2d, self.dim)

    def carregar_imagem(self):
        # Lógica para carregar a imagem do terreno com base no tipo e grupo
        # print(f"Carregando imagem: imgs/{self.tipo}_{self.grupo}.png")
        # self.imagem = pygame.image.load(f"imgs/{self.tipo}_{self.grupo}.png")


        self.imagem = pygame.image.load(f"imgs/bases/base.png")
        original_size = self.imagem.get_size()
        print(f"Original size: {original_size}")
        self.dim = [original_size[0] * self.escala, original_size[1] * self.escala]
        print(f"Scaled size: {self.dim}")
        self.imagem = pygame.transform.scale(self.imagem, self.dim)
        self.dim[0] *=0.6
        self.dim[1] *=0.4
        if self.rotacionar:
            self.imagem = pygame.transform.rotate(self.imagem, 90)
            self.dim = (self.dim[1], self.dim[0])



    def tick(self):
        # Lógica para atualizar o estado do terreno, se necessário
        pass


    def render(self, screen, camera):
        # Lógica para renderizar o terreno na tela



        camera.render(screen, self.imagem, self.absolut_pos)