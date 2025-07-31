from src.tabuleiro import Tabuleiro
from src.camera import Camera

class Jogo:
    def __init__(self):
        self.cenas = []
        self.cena_atual = None
        self.adicionar_cena(Tabuleiro())
        self.camera = Camera()

    def adicionar_cena(self, cena):
        self.cenas.append(cena)
        if not self.cena_atual:
            self.cena_atual = cena

    def tick(self):
        if self.cena_atual:
            self.cena_atual.tick()

    def render(self, screen):
        if self.cena_atual:
            self.cena_atual.render(screen, self.camera)

    def input(self, event):
        if self.cena_atual:
            self.cena_atual.input(event)