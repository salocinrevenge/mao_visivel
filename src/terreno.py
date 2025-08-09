import pygame

class Terreno:
    def __init__(self, pos, tema, tipo, categoria = None, bioma = None, tabuleiro = None):
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
        self.carregar_imagem()

    def carregar_imagem(self):
        # Lógica para carregar a imagem do terreno com base no tipo e grupo
        # print(f"Carregando imagem: imgs/{self.tipo}_{self.grupo}.png")
        # self.imagem = pygame.image.load(f"imgs/{self.tipo}_{self.grupo}.png")

        self.imagem_ID = self.loaderImages.get_image_ID(f"imgs/bases/new_base.png")

    def tick(self):
        # Lógica para atualizar o estado do terreno, se necessário
        pass


    def render(self, screen, camera):
        # Lógica para renderizar o terreno na tela



        camera.render(screen, self, self.pos)