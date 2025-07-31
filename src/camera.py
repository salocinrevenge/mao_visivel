from src.algebra_linear import toIsometric
import pygame

class Camera():
    def __init__(self, pos, escala) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.target = None
        self.escala = (1/escala)

    def tick(self):
        pass
    
    def render(self, screen, imagem, pos):
        x,y = toIsometric(pos[0], pos[1])
        screen.blit(imagem, (x * 16 * self.escala + self.x, y * 16 * self.escala + self.y))


    def input(self, evento):
        pass