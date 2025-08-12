from src.jogador import Jogador
from src.terreno import Terreno
from src.camera import Camera
from src.loader_images import loaderImages
import pygame

class Tabuleiro:
    def __init__(self):
        self.reset()

    def reset(self):
        
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(4)]  # Exemplo com 4 jogadores
        self.cartas = []
        self.terrenos = []
        self.vez = 0
        self.loaderImages = loaderImages(escala=1)

        self.window_dim = pygame.display.get_window_size()
        escala = 0.3
        self.tiles_size = 512
        self.camera = Camera([-self.window_dim[0],-self.window_dim[1]*(escala)], self.loaderImages, escala=escala, tabuleiro=self)

        self.criar_terrenos("mapas/minecraft1.txt")


    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def distribuir_cartas(self):
        # Lógica para distribuir cartas entre os jogadores
        pass

    def tick(self):
        # Atualizar o estado do tabuleiro
        self.camera.tick()

    def render(self, screen):
        # Renderizar o tabuleiro e os jogadores na tela

        # Renderizar terrenos seguindo a diagonal secundária (de cima para baixo)
        linhas = len(self.terrenos)
        colunas = len(self.terrenos[0])

        for coluna_atual in range(colunas - 1, -1, -1):
            i, j = 0, coluna_atual
            while i < linhas and j < colunas:
                self.terrenos[i][j].render(screen, self.camera)
                i += 1
                j += 1
        for linha_atual in range(1, linhas):
            i, j = linha_atual, 0
            while i < linhas and j < colunas:
                self.terrenos[i][j].render(screen, self.camera)
                i += 1
                j += 1

        for coluna_atual in range(colunas - 1, -1, -1):
            i, j = 0, coluna_atual
            while i < linhas and j < colunas:
                self.terrenos[i][j].renderGUI(screen, self.camera)
                i += 1
                j += 1
        for linha_atual in range(1, linhas):
            i, j = linha_atual, 0
            while i < linhas and j < colunas:
                self.terrenos[i][j].renderGUI(screen, self.camera)
                i += 1
                j += 1

        for jogador in self.jogadores:
            jogador.render(screen, self.camera)

    def criar_terrenos(self, path):
        # Lógica para criar terrenos a partir de um arquivo
        with open(path, "r") as file:
            estado = None
            possiveis_estados = set(["TEMA", "SIMBOLOS", "TERRENOS", "MAPA"])
            tema = None
            simbolos = dict()
            sequencia_terrenos = []
            i = -1
            for linha in file:
                adicionando = linha.strip()
                if adicionando:  # Ignorar linhas vazias
                    adicionando = adicionando.split(" ")
                    if len(adicionando) == 1 and adicionando[0] in possiveis_estados:
                        estado = adicionando[0]
                        continue
                    match estado:
                        case "TEMA":
                            tema = adicionando[0]
                        case "SIMBOLOS":
                            simbolos[adicionando[0]] = adicionando[1]
                        case "TERRENOS":
                            sequencia_terrenos.append([x.replace("_", " ") for x in adicionando])
                        case "MAPA":
                            i+=1
                            j=-1
                            self.terrenos.append([])
                            for letra in adicionando[0]:
                                j+=1
                                tipo = simbolos[letra]
                                if tipo == "TERRENO":
                                    terreno_atual = sequencia_terrenos.pop(0)
                                    self.terrenos[-1].append(Terreno(pos = [i,j], tema = tema, tipo = tipo, categoria = terreno_atual[0], bioma = terreno_atual[1], nome= terreno_atual[2], tabuleiro = self))
                                else:
                                    nome = tipo
                                    if tipo == "LIVRE":
                                        nome = None
                                    self.terrenos[-1].append(Terreno(pos = [i,j], tema = tema, tipo = tipo, tabuleiro = self, nome=nome))
                        case _:
                            pass

        

    def input(self, event):
        self.camera.input(event)