class Camera():
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def render(self, screen, image, pos):
        # Ajustar a posição da câmera na tela
        adjusted_pos = (pos[0] - self.x, pos[1] - self.y)
        screen.blit(image, adjusted_pos)