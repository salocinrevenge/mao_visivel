from src.algebra_linear import toIsometric
import pygame

class Camera():
    def __init__(self, pos, loaderImages, escala) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.target = None
        self.escala = escala
        self.desloc_figs_padrao = [0,38]
        self.loaderImages = loaderImages
        self.window_dim = pygame.display.get_window_size()
        self.window_dim = [self.window_dim[0] // 2, self.window_dim[1] // 2]

    def tick(self):
        if self.loaderImages.escala != self.escala:
            self.loaderImages.update_scale(self.escala)
    
    def render(self, screen, obj, pos):
        imagem = self.loaderImages.get_image(obj.imagem_ID)
        x,y = toIsometric(pos[0], pos[1])
        pos_final_x = x * (256+self.desloc_figs_padrao[0]) * self.escala + self.x* self.escala+ self.window_dim[0]
        pos_final_y = y * (256+self.desloc_figs_padrao[1])*self.escala + self.y* self.escala+ self.window_dim[1]
        
        # Calcula o tamanho da imagem considerando a escala
        img_width = imagem.get_width()
        img_height = imagem.get_height()

        # Verifica se a imagem está completamente fora da tela
        screen_rect = screen.get_rect()
        img_rect = pygame.Rect(pos_final_x, pos_final_y, img_width, img_height)
        if not screen_rect.colliderect(img_rect):
            return
        
        screen.blit(imagem, (pos_final_x, pos_final_y))


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