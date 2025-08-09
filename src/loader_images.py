import pygame

class loaderImages:
    def __init__(self, escala=1):
        self.escala = escala
        self.path_to_id = {}
        self.images = {}
        self.id = 0

    def get_image_ID(self, path):
        if path not in self.path_to_id:
            image = pygame.image.load(path)
            id = self._get_id()
            self.path_to_id[path] = id
            self.images[id] = {"id": id, "image": {1: image}} # 1 é a escala padrão
        else:
            id = self.path_to_id[path]
        return id

    def get_image(self, image_ID):
        if image_ID not in self.images:
            raise ValueError(f"Image ID {image_ID} not found.")
        if self.escala not in self.images[image_ID]["image"]:
            self._compute_scale(image_ID, self.escala)
        return self.images[image_ID]["image"][self.escala]
    
    def _compute_scale(self, image_ID, escala):
        if image_ID not in self.images:
            raise ValueError(f"Image ID {image_ID} not found.")
        original_image = self.images[image_ID]["image"][1]
        scaled_image = pygame.transform.scale(original_image, (int(original_image.get_width() * escala), int(original_image.get_height() * escala)))
        self.images[image_ID]["image"][escala] = scaled_image
        return scaled_image

    def update_scale(self, escala):
        self.escala = escala

    def _get_id(self):
        id = self.id
        self.id += 1
        return id