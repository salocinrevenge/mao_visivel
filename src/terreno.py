import pygame
import math

class Terreno:
    def __init__(self, pos, tema, tipo, categoria = None, bioma = None, nome = None, tabuleiro = None):
        self.pos = pos
        self.tipo = tipo
        self.tema = tema
        self.bioma = bioma
        self.categoria = categoria
        if tabuleiro is None:
            assert Exception("Tabuleiro deve ser passado para terreno")
        self.loaderImages = tabuleiro.loaderImages 
        self.tabuleiro = tabuleiro
        self.escala = 1
        self.nome = nome
        self.carregar_imagem()
        self.animacao_descricao = 0

    def carregar_imagem(self):
        # Lógica para carregar a imagem do terreno com base no tipo e grupo
        # print(f"Carregando imagem: imgs/{self.tipo}_{self.grupo}.png")
        # self.imagem = pygame.image.load(f"imgs/{self.tipo}_{self.grupo}.png")
        if self.tipo == "TERRENO" and self.categoria == "COMUM":
            self.imagem_ID = self.loaderImages.get_image_ID(f"imgs/{self.tema}/{self.bioma}.png")
        else:
            self.imagem_ID = self.loaderImages.get_image_ID(f"imgs/bases/new_base.png")


    def tick(self):
        # Lógica para atualizar o estado do terreno, se necessário
        pass


    def render(self, screen, camera):
        # Lógica para renderizar o terreno na tela
        camera.render(screen, self, self.pos)


    def renderGUI(self, screen, camera):
        if self.nome:
            mouse_pos = pygame.mouse.get_pos()
            mouse_tile_pos = camera.screen_to_world(mouse_pos)
            if math.ceil(mouse_tile_pos[0]) - 2 == self.pos[0] and math.ceil(mouse_tile_pos[1]) == self.pos[1]:
                if self.animacao_descricao < 100:
                    self.animacao_descricao += 20
                camera.render_terrain_name(screen, self, self.pos, anim = self.animacao_descricao)
            else:
                if self.animacao_descricao > 0:
                    camera.render_terrain_name(screen, self, self.pos, anim = self.animacao_descricao)
                    self.animacao_descricao -= 20