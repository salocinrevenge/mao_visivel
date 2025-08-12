from src.algebra_linear import toIsometric
import pygame
from src.algebra_linear import fromIsometric

class Camera():
    def __init__(self, pos, loaderImages, escala, tabuleiro) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.target = None
        self.escala = escala
        self.desloc_figs_padrao = [0,38]
        self.loaderImages = loaderImages
        self.window_dim = pygame.display.get_window_size()
        self.window_dim = [self.window_dim[0] // 2, self.window_dim[1] // 2]
        self.tabuleiro = tabuleiro
        self.tiles_size = tabuleiro.tiles_size

    def tick(self):
        if self.loaderImages.escala != self.escala:
            self.loaderImages.update_scale(self.escala)
    
    def render(self, screen, obj, pos):
        imagem = self.loaderImages.get_image(obj.imagem_ID)
        x,y = toIsometric(pos[0], pos[1])
        pos_final_x = x * ((self.tiles_size//2)+self.desloc_figs_padrao[0]) * self.escala + self.x* self.escala+ self.window_dim[0]
        pos_final_y = y * ((self.tiles_size//2)+self.desloc_figs_padrao[1])*self.escala + self.y* self.escala+ self.window_dim[1]
        
        # Calcula o tamanho da imagem considerando a escala
        img_width = imagem.get_width()
        img_height = imagem.get_height()

        # Verifica se a imagem está completamente fora da tela
        screen_rect = screen.get_rect()
        img_rect = pygame.Rect(pos_final_x, pos_final_y, img_width, img_height)
        if not screen_rect.colliderect(img_rect):
            return
        
        screen.blit(imagem, (pos_final_x, pos_final_y))

    def render_terrain_name(self, screen, obj, pos, anim = None):
        # anim é None se não houver animação, ou um valor entre 0 e 100 para a animação
        opacity = 1
        size = 24
        if anim is not None:
            opacity = int(255 * (anim / 100))
            size = int(24 * (anim / 100))

        font = pygame.font.Font(None, size)
        text = font.render(obj.nome, True, (255, 255, 255, opacity))
        # Renderiza o texto para a borda preta
        border_text = font.render(obj.nome, True, (0, 0, 0, opacity))
        x, y = toIsometric(pos[0], pos[1])
        pos_final_x = x * ((self.tiles_size//2) + self.desloc_figs_padrao[0]) * self.escala + self.x * self.escala + self.window_dim[0]
        pos_final_y = y * ((self.tiles_size//2) + self.desloc_figs_padrao[1]) * self.escala + self.y * self.escala + self.window_dim[1]
        # Centraliza o texto no centro do terreno
        text_rect = text.get_rect(center=(pos_final_x + ((self.tiles_size) * self.escala) / 2, pos_final_y + ((self.tiles_size) * self.escala) * 0.75))
        border_rect = border_text.get_rect(center=text_rect.center)

        if anim is not None:
            # Calcula o tamanho do retângulo com base na animação (de 0% a 100%)
            grow = anim / 100
            min_width = max(150, text_rect.width)
            min_height = 200
            rect_width = int(min_width * grow)
            rect_height = int(min_height * grow)
            rect_x = text_rect.centerx - rect_width // 2
            rect_y = text_rect.centery - rect_height + size
            # rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
            s = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
            s.fill((255, 255, 255, int(opacity*0.7)))
            screen.blit(s, (rect_x, rect_y))
            
        # Desenha a borda preta ao redor do texto branco
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    offset_rect = border_rect.copy()
                    offset_rect.x += dx
                    offset_rect.y += dy
                    screen.blit(border_text, offset_rect)
        # Desenha o texto branco por cima
        screen.blit(text, text_rect)


    def input(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 4:  # Scroll up
                self.escala = min(1.5, round(self.escala + 0.1, 1))
            elif evento.button == 5:  # Scroll down
                self.escala = max(0.1, round(self.escala - 0.1, 1))
        elif evento.type == pygame.MOUSEMOTION:
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_SPACE] and pygame.mouse.get_pressed()[0]) or pygame.mouse.get_pressed()[2]:  # Espaço pressionado
                rel = evento.rel
                self.x += rel[0]
                self.y += rel[1]


    def screen_to_world(self, pos):
        x = (pos[0] - self.x * self.escala - self.window_dim[0]) / ((self.tiles_size // 2) + self.desloc_figs_padrao[0]) / self.escala
        y = (pos[1] - self.y * self.escala - self.window_dim[1]) / ((self.tiles_size // 2) + self.desloc_figs_padrao[1]) / self.escala
        return fromIsometric(x, y)